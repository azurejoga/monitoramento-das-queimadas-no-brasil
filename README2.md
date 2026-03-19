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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0934282-6d15-3fd8-939e-9c9d67fe78ee | 0.775 | -59.8782 | 2026-03-19 03:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| fe2bb5d1-0cd1-3820-ad32-d7ccc336eda0 | 0.7751 | -59.8592 | 2026-03-19 03:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 0f53b28a-8f9a-3c58-80be-69a503f2a121 | 0.775 | -59.8782 | 2026-03-19 03:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 14c16f4d-315f-3ee7-9313-ad4a453eb4e9 | -9.61621 | -36.97107 | 2026-03-19 03:13:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2adfa02b-2fc2-310a-a2c5-f8d9d0893185 | -9.61739 | -36.96887 | 2026-03-19 03:13:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| acbefe99-5190-3b2e-bf72-0adc09f0d489 | -8.78049 | -38.9125 | 2026-03-19 03:13:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| bcd8a74e-4c5b-3099-9624-053498d29c1f | -9.21017 | -36.70346 | 2026-03-19 03:13:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 08e2943d-da4b-38d9-abb8-f659e1c2bd59 | -9.20962 | -36.70653 | 2026-03-19 03:13:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 56307e33-20d3-3cec-8e92-a3522727cd7b | -15.83881 | -39.18321 | 2026-03-19 03:15:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 686b9226-2ee6-3d72-bc0e-59b682f8bb90 | -11.54256 | -38.26073 | 2026-03-19 03:15:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 05e72642-9752-3e6c-9709-9c017b0aaf1a | -12.15794 | -38.08976 | 2026-03-19 03:15:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b226f8c1-67ca-3fd4-b718-b80ee396f55f | -11.5421 | -38.26613 | 2026-03-19 03:15:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 942a6492-f258-3515-aaea-9570c99e1717 | -11.54187 | -38.26438 | 2026-03-19 03:15:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 90d5275c-1d3b-30de-a935-25eb2cba9801 | -11.54283 | -38.26241 | 2026-03-19 03:15:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 423eba67-c2fa-3ffa-b3fa-4f7cb697580e | -16.40762 | -39.75388 | 2026-03-19 03:15:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f717d79e-ff5e-3c98-9e66-d2171484a3d1 | -20.03329 | -41.65531 | 2026-03-19 03:17:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 274fde3c-f134-3c6f-b685-1b8ee3939fd5 | -20.03218 | -41.66034 | 2026-03-19 03:17:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1be0de3a-e146-3e6c-a5f1-bd18dda2b3d5 | 0.7751 | -59.8592 | 2026-03-19 03:20:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 24e15e29-48b8-3eca-8a72-35bd20164dc8 | 0.7751 | -59.8592 | 2026-03-19 03:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6a8a782d-1db0-3ae4-ae60-66a29fa220b3 | 0.775 | -59.8782 | 2026-03-19 03:30:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0abeab8a-642b-3114-81cc-7835f67a17e5 | 0.775 | -59.8782 | 2026-03-19 03:40:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 964ad150-71f9-3b63-b463-698067ea640b | 0.7751 | -59.8592 | 2026-03-19 03:40:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6f51c172-cc8c-31f0-bff0-14c84fb11d89 | -8.781 | -38.90961 | 2026-03-19 03:42:00 | NPP-375D | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 28c1f709-4734-3601-89e2-fbbb553faad6 | -9.50746 | -37.08918 | 2026-03-19 03:42:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ff9fc255-e251-3dd9-8af4-354983bf8cbf | -8.77615 | -38.91408 | 2026-03-19 03:42:00 | NPP-375D | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 975aad76-4c57-3060-8bd7-b29d42b0c2bd | -8.77702 | -38.90891 | 2026-03-19 03:42:00 | NPP-375D | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f1366276-973f-32a7-b079-f908510f8633 | -9.62074 | -36.97086 | 2026-03-19 03:42:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d3b3c87d-8cb1-3691-a57b-da1438d323e5 | -9.6172 | -36.97027 | 2026-03-19 03:42:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2746bf48-4d4e-38ec-83dd-5a70e14850c0 | -9.20724 | -36.70316 | 2026-03-19 03:42:00 | NPP-375D | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 865e591d-2f63-3c77-8901-6e2ba1db995b | -9.20659 | -36.70708 | 2026-03-19 03:42:00 | NPP-375D | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4144d558-a059-3eed-86ba-8ca7be36a5e1 | -8.78013 | -38.91478 | 2026-03-19 03:42:00 | NPP-375D | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9175abbc-2bab-3897-9665-12c0e69c527e | -10.07432 | -36.25279 | 2026-03-19 03:45:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bd774e7d-b243-3f9f-9ffa-5fdbd4e7ac73 | -15.84537 | -40.14695 | 2026-03-19 03:45:00 | NPP-375D | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7302659e-f6bf-3798-adc7-576df7b14c16 | -16.41031 | -39.75178 | 2026-03-19 03:45:00 | NPP-375D | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2690a7c3-b4e9-33b3-b445-75fcac6cbb52 | -11.54086 | -38.26255 | 2026-03-19 03:45:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a32e9798-b289-3bdc-b9a1-002f8acef2a0 | -11.80056 | -47.09332 | 2026-03-19 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bb74e83-a169-3818-b6ec-e699f8c02063 | -11.79948 | -47.09864 | 2026-03-19 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 50a5f3e7-076d-30e1-836b-b251908ad8d5 | -15.36203 | -39.47621 | 2026-03-19 03:45:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5913cffd-7365-37f9-91e3-fe1a5d76e6d2 | -12.91908 | -43.02195 | 2026-03-19 03:45:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a61bd98b-d8c8-371d-8e18-6bb730a38e6a | -11.80586 | -47.10017 | 2026-03-19 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fac64d6-db64-3ac2-a676-ecc851adf0f5 | -13.37972 | -40.04829 | 2026-03-19 03:45:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e5cdb002-566c-3cc4-94c8-ff9456b9b74b | -11.54379 | -38.26764 | 2026-03-19 03:45:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 027255e8-e72a-3590-ac2d-f128c9125ba7 | -11.79905 | -47.10149 | 2026-03-19 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d45b3371-59ff-3698-ac5d-ddf1d3d2be54 | -14.77462 | -43.95667 | 2026-03-19 03:45:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fb0d4a5d-8c82-3361-b829-cd67d9e5a00c | -15.83964 | -39.18523 | 2026-03-19 03:45:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 104ccc03-23a5-353a-96e8-ec7f212479f5 | -12.91677 | -43.01693 | 2026-03-19 03:45:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5e32372c-3450-3672-9981-d7cc7b28493a | -14.77962 | -43.95771 | 2026-03-19 03:45:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b05933dc-fd86-3a4e-a141-fea91a04985a | -10.02139 | -38.1308 | 2026-03-19 03:45:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 491ab414-3231-3360-8cc5-f8fdc69beac6 | -12.15716 | -38.09092 | 2026-03-19 03:45:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38e26c94-06d3-305a-a539-8fed5a8b07cb | -11.79378 | -47.09468 | 2026-03-19 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c350a57-7226-3f7a-96eb-d11354c00e83 | -15.53079 | -40.83918 | 2026-03-19 03:45:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7073b417-652f-358c-8f52-b0bbe5d4c29c | -12.91567 | -43.02259 | 2026-03-19 03:45:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a85d8bdf-5971-3e95-9c1b-d75b2bf1a1ff | -11.54455 | -38.26319 | 2026-03-19 03:45:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7acc84f-8000-3cbd-9acb-e05d33de42f4 | -14.78076 | -43.95186 | 2026-03-19 03:45:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 359b9611-6783-36ee-8e1b-c6c4241a0998 | -11.80017 | -47.09612 | 2026-03-19 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4246845b-75bb-3ad6-bef4-e941b9960118 | -12.28923 | -38.03939 | 2026-03-19 03:45:00 | NPP-375D | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7d60c5f8-420c-36b0-9ba3-6fc3a3f0c4e1 | -12.36131 | -37.94655 | 2026-03-19 03:45:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a4ce9f35-0f17-3475-a02b-599135af18f0 | -14.77577 | -43.9508 | 2026-03-19 03:45:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3ab74700-e4d2-38a6-adf3-db89dfa1b589 | -20.03058 | -41.65619 | 2026-03-19 03:47:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 289f920b-b4c4-3ea5-887c-c940b157dc08 | -20.03106 | -41.66038 | 2026-03-19 03:47:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4556cd2f-14ad-39af-b026-d2e850c43f09 | -20.03208 | -41.65475 | 2026-03-19 03:47:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 57611e27-9dc4-3248-9401-079d50664d47 | 0.775 | -59.8782 | 2026-03-19 03:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d5256142-9efc-3e8a-9db9-6541cdb86ff7 | 0.7751 | -59.8592 | 2026-03-19 03:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| cb084e11-e5c8-3804-9c34-d81faedcebb4 | 0.775 | -59.8782 | 2026-03-19 04:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 36833864-b991-3bd1-a47f-8620d04b9765 | -11.79587 | -47.09482 | 2026-03-19 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 651e9b69-a999-3f26-8a07-82c90a4984e7 | -9.20626 | -36.70459 | 2026-03-19 04:04:00 | NOAA-20 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 44810efc-3a9f-31a7-8054-4c5454e80470 | -9.50458 | -37.09129 | 2026-03-19 04:04:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ebf373a8-3dc8-3694-8c1d-fdd0d370a226 | -12.15741 | -38.09153 | 2026-03-19 04:04:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c8eee45-2b5c-3cce-868b-be3c250e87bb | -10.66031 | -40.29915 | 2026-03-19 04:04:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7ee11da-4c57-3eb1-85a6-5116738ee5aa | -10.45351 | -38.40274 | 2026-03-19 04:04:00 | NOAA-20 | ANTAS | BAHIA | Brasil | 2901601 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 05f6bfda-94b6-37a9-a335-fa61bd2891f7 | -13.38031 | -40.04507 | 2026-03-19 04:04:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 53ac146c-2399-3253-986e-82631bc08639 | -8.77718 | -38.9125 | 2026-03-19 04:04:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2c506aee-a885-366c-9a95-240169da646a | -12.40496 | -40.40753 | 2026-03-19 04:04:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4f0427c3-423d-3f22-9987-3ff8a9a97493 | -11.10423 | -38.13626 | 2026-03-19 04:04:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 19541d8f-2857-3bb5-8bf6-dcb3c41ca5a3 | -11.79517 | -47.09877 | 2026-03-19 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9740d3a-54fd-3d4f-bbe1-c4181468e077 | -9.42719 | -40.71143 | 2026-03-19 04:04:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd0333d4-66d0-3070-a1d4-7a7bd5aec8cc | -8.78057 | -38.91302 | 2026-03-19 04:04:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1e56fbfe-43d1-3448-b027-64a55b2c2521 | -11.80356 | -47.10038 | 2026-03-19 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b8113eb-6aa0-376a-8952-7e46c1b5f310 | -12.91772 | -43.02008 | 2026-03-19 04:04:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| eb6d32b8-a3bd-30c2-b3d8-681b5507fb65 | -12.49426 | -43.65166 | 2026-03-19 04:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e13ea31-f9ed-3ded-8013-6bb3ab339c5f | -9.50525 | -37.08683 | 2026-03-19 04:04:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 737cc30f-8fba-3ae1-b039-ec38aa7ee2b0 | -12.36148 | -37.94611 | 2026-03-19 04:04:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ae58ea7b-6b12-360d-9048-229eedb2e0bc | -8.78114 | -38.90936 | 2026-03-19 04:04:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| edafd797-d536-3a36-b3d4-f8ba8f851b22 | -11.79936 | -47.09958 | 2026-03-19 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2289c7e1-d316-3be7-8e67-e08c2c9f386d | -10.02092 | -38.12966 | 2026-03-19 04:04:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 506bbcec-a17d-3c6e-ab90-b53af91f0b70 | -11.80006 | -47.09563 | 2026-03-19 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93009f6d-39d8-396d-acdd-d269746d5f0f | -11.54302 | -38.26343 | 2026-03-19 04:04:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c087deb8-22d1-398e-ab43-a5d4ce2729d6 | -8.77775 | -38.90883 | 2026-03-19 04:04:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a09de888-053a-30e4-8f0a-872c168f80cf | -9.61947 | -36.96906 | 2026-03-19 04:04:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49735ccc-9df1-3365-9648-0d6868928af4 | -11.53945 | -38.26287 | 2026-03-19 04:04:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe8dc376-ffa7-359b-9fc8-330b0fe4a90b | -14.77838 | -43.95649 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 43fa3099-8f85-3d8c-b016-bd79af34b75a | -19.49394 | -40.32911 | 2026-03-19 04:06:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d5a081e2-9308-3ff5-b45d-3ec52dae8707 | -14.77966 | -43.94889 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a21e2716-d145-3799-89e1-5a0e078e9e42 | -14.78179 | -43.9571 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e600b499-cd39-3ead-85c9-e81a50231a15 | -14.78307 | -43.94949 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 579c94be-edda-34be-924d-6d37e064152b | -14.77774 | -43.96031 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21c1f406-b51f-3083-bbe5-38b893da7edd | -15.52795 | -40.84119 | 2026-03-19 04:06:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0bab620a-2738-31ba-b21f-4d44023c7158 | -16.40967 | -39.74962 | 2026-03-19 04:06:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9e409c87-1d79-3338-bc3c-9906a78ff15b | -14.77496 | -43.95589 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0878130c-3689-36a3-be0a-f339eb2c01c3 | -14.77432 | -43.95971 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
