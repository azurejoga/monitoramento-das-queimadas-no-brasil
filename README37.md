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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fc5f7a3-7ce7-3aed-ba47-96a98afe5331 | -22.80114 | -47.79901 | 2025-09-15 04:23:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5187c80f-e488-35df-91f6-605bd00c02f5 | -20.52946 | -46.86674 | 2025-09-15 04:23:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 042f9ea3-ec97-369c-bfed-0ce995b16b47 | -20.08576 | -46.88804 | 2025-09-15 04:23:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cb76a64-c7a1-322e-ba66-f39c2028fd40 | -23.00867 | -47.54984 | 2025-09-15 04:23:00 | NOAA-21 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d57997ec-253f-3598-bdb3-fb5271181d34 | -19.70073 | -47.6503 | 2025-09-15 04:23:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2f22604-a499-31ae-9f9d-5901f1cb3fda | -19.72033 | -45.44601 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f81b286-c792-33a7-9785-af636b4e7d80 | -22.29186 | -47.95462 | 2025-09-15 04:23:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a734416c-811f-3321-a557-1818a63da9e1 | -20.52674 | -47.47427 | 2025-09-15 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 905fa718-e4fa-32fc-9ae9-7321ebe2e94d | -18.15875 | -49.20333 | 2025-09-15 04:23:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 85005f59-e57a-3adc-88e7-722c5e28a0c1 | -19.19214 | -47.20068 | 2025-09-15 04:23:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5db124e-17a3-3722-ba94-de7a1b08ecc7 | -18.13974 | -49.19217 | 2025-09-15 04:23:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2412f642-d6b7-3876-8371-5ed67ea85daf | -20.83404 | -46.4826 | 2025-09-15 04:23:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 12ceafc7-69d4-32a4-832d-57ae4182b9f3 | -16.67122 | -49.77325 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| def0fb7c-d627-394f-9d7f-6982ed128012 | -22.17599 | -49.61209 | 2025-09-15 04:23:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fc252d38-e378-32cb-bba5-25f47389bf2b | -20.74026 | -56.74388 | 2025-09-15 04:23:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcc56b1a-c82d-3d0d-ad02-6c3d64a055ee | -18.58484 | -48.14879 | 2025-09-15 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37dd5f6d-1011-32b4-8393-66682daf2da9 | -17.31195 | -46.11079 | 2025-09-15 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddc43242-7975-339b-a95b-94f136b87ece | -21.11191 | -46.13324 | 2025-09-15 04:23:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ccbf206-08ff-3ab3-820e-731656413335 | -20.09921 | -43.19656 | 2025-09-15 04:23:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3012116a-2450-3348-b45f-766456cabe05 | -22.20294 | -48.35522 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ccad52e-bd1c-3597-bb84-1c0178073282 | -17.73172 | -47.94904 | 2025-09-15 04:23:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62c57927-50f0-3ac5-b2c5-29968b9b4867 | -21.06275 | -47.14029 | 2025-09-15 04:23:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| efa5099a-49f3-3ef6-83f4-c8d9c9c9041d | -18.02338 | -46.9539 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f607f6f-ea00-3928-a05b-9c7590d0eabd | -22.99515 | -49.93557 | 2025-09-15 04:25:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 53a224e9-608b-3450-90e4-c3bb0441a02b | -22.67092 | -53.12187 | 2025-09-15 04:25:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 301fe4a1-6108-30b0-9c43-ebaa33f5a602 | -23.46823 | -47.52048 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 318c23db-b912-3876-8b98-0a84282b454e | -28.62685 | -51.00744 | 2025-09-15 04:25:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 78371703-16dd-351d-8c39-a8f76829b9cb | -23.48132 | -47.29205 | 2025-09-15 04:25:00 | NOAA-21 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 30a26e5c-36b3-362b-bbef-4bc10c2a094c | -23.1427 | -49.63824 | 2025-09-15 04:25:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ed5117a8-6742-3558-a416-a344edb2c2b3 | -28.92889 | -50.84785 | 2025-09-15 04:25:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1554654-54d1-3af1-952f-25be72012270 | -23.47659 | -47.37104 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 28ec70e5-cc73-3c86-8edc-78e46aa93667 | -23.4811 | -47.36388 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5c8be850-d59a-3d87-bb08-6cf636437a97 | -24.58223 | -50.98867 | 2025-09-15 04:25:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ae4f1497-4036-39c3-ac92-52469071e986 | -25.17724 | -50.07402 | 2025-09-15 04:25:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3d15be59-2413-3f85-a058-93407f154517 | -23.47774 | -47.36328 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ac4606ad-baf0-36e5-9a5f-61e2bd9d6b85 | -23.47795 | -47.29145 | 2025-09-15 04:25:00 | NOAA-21 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c7ed3dfe-c205-357e-a918-fb01e28dd2cf | -22.99787 | -49.94 | 2025-09-15 04:25:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fcbf4f81-0481-321e-8523-9ca0e8c9c483 | -22.65766 | -53.10863 | 2025-09-15 04:25:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ccad7792-fe35-3898-bbd2-c21b00870a10 | -24.21921 | -48.61935 | 2025-09-15 04:25:00 | NOAA-21 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c0e6ef62-f468-3c71-9c68-bcacf2580750 | -22.04912 | -56.08796 | 2025-09-15 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ee9c2a5-63d5-34ed-8bdc-c2c47066c5fd | -24.84213 | -50.35524 | 2025-09-15 04:25:00 | NOAA-21 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c6ed85b6-4dff-31ec-8d4c-7ec3037ca743 | -28.62354 | -51.00676 | 2025-09-15 04:25:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5ecce45a-1c4f-3d63-bcef-59f477ca199a | -28.23637 | -49.92973 | 2025-09-15 04:25:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b75b6828-c5aa-3966-bd5d-f1da23aaf42e | -23.14391 | -49.63078 | 2025-09-15 04:25:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e3891061-09b1-3d96-ac9e-b9c4175e6b3f | -22.66335 | -53.12026 | 2025-09-15 04:25:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3728f02a-435e-358a-8fb1-aebb1dfb278a | -23.24983 | -47.10608 | 2025-09-15 04:25:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e6644403-39bc-305c-88e1-bd81c0e7f668 | -24.84276 | -50.35139 | 2025-09-15 04:25:00 | NOAA-21 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 314011c7-4148-3a7d-ba38-9ca6c236b2b1 | -23.4839 | -47.36833 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ecf34ec9-73d4-32c1-9d59-25d138c13f2d | -22.6605 | -53.11445 | 2025-09-15 04:25:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 44e05382-d42b-3c30-a665-22534aaeb07a | -23.60157 | -47.38774 | 2025-09-15 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fe173c72-822c-3a08-afc9-11c9555678b1 | -22.50628 | -52.97794 | 2025-09-15 04:25:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a6fc5cff-01e5-325c-9e0d-48e4974b2fd0 | -23.4738 | -47.36657 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 2aa7b24d-ce07-3314-acdb-a3927da638c6 | -23.60944 | -47.38106 | 2025-09-15 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 916906dc-3a9c-3b14-bd6a-d0c43a4555bf | -22.99389 | -49.94321 | 2025-09-15 04:25:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c2031bcb-0a6b-3862-a00d-1784d4aa2192 | -23.21799 | -48.45374 | 2025-09-15 04:25:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d908ef5e-1877-3434-a929-01a867548fc7 | -23.7879 | -51.64705 | 2025-09-15 04:25:00 | NOAA-21 | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b982da46-ee44-3814-b2b6-ec2f1d0a39ac | -23.48053 | -47.36774 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8b8a0777-9ad1-37d0-adbf-9003c9a3669e | -23.60663 | -47.37662 | 2025-09-15 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6ef792fd-096c-32ba-b191-9a15e2345cac | -23.25157 | -49.51469 | 2025-09-15 04:25:00 | NOAA-21 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c9d14a46-cc00-3a59-93f6-e15530a5b4dc | -23.47996 | -47.37162 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ee1e8bde-9b4c-3f03-9e66-4a367f3b5780 | -22.99452 | -49.93938 | 2025-09-15 04:25:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9852d0ba-7f90-335c-8c2d-47ba0fd1692c | -23.47266 | -47.37433 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 90f2f9e5-e5fc-3b7f-a10f-813cc7fd80a9 | -24.41808 | -50.07161 | 2025-09-15 04:25:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e45162f3-3db6-3678-af3c-1c9ab46071cc | -23.14044 | -49.63404 | 2025-09-15 04:25:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1c8cc09-a384-3c12-9641-3afb0349189c | -23.47323 | -47.37045 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| b474d0d5-968f-3fb6-893e-70e371654ca0 | -23.45857 | -50.80261 | 2025-09-15 04:25:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a37de380-6da1-3623-9f94-6a5e0a30195f | -24.4345 | -50.05502 | 2025-09-15 04:25:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eb1681b-a7dc-3080-957b-c816bab518d1 | -29.04681 | -50.87495 | 2025-09-15 04:25:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 87ab48b8-f074-39e9-b762-5dba34439b44 | -23.24645 | -47.10551 | 2025-09-15 04:25:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f56f652b-2d7a-36b6-aef1-d96f245f9739 | -23.7257 | -47.3521 | 2025-09-15 04:25:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f4ebf32a-b769-30c4-8916-2661b319812d | -23.23778 | -51.00547 | 2025-09-15 04:25:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99b85f93-d5eb-34ff-97a8-c01f7842b41d | -22.91369 | -51.14533 | 2025-09-15 04:25:00 | NOAA-21 | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a02ae324-c7a1-385d-9c32-9a932e9c902b | -22.99054 | -49.94262 | 2025-09-15 04:25:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9983948c-1586-3a96-b98a-f8abed5ffad5 | -23.14331 | -49.63449 | 2025-09-15 04:25:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e9ec1d81-fb85-3d77-b391-75c5f40ba529 | -23.47717 | -47.36716 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| ce60889f-1992-3528-bddf-44803f920a95 | -22.99724 | -49.94383 | 2025-09-15 04:25:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 557a2b7d-0b1e-328e-bcb3-66c8153a9fbc | -23.24588 | -47.10946 | 2025-09-15 04:25:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 289e0aff-c853-327a-973e-559cd7354d29 | -26.0801 | -52.17767 | 2025-09-15 04:25:00 | NOAA-21 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f459d88d-fbba-36ba-94f7-b5557cf694a1 | -23.47602 | -47.37491 | 2025-09-15 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 110cdcc1-ef6c-3acf-bc15-25505631d4f2 | -22.66713 | -53.12106 | 2025-09-15 04:25:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ca67d99d-3b69-3d78-9b9b-cc090632ce0e | -23.5982 | -47.38719 | 2025-09-15 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 410899a1-9ec4-3a9a-b284-673217ce917f | -23.45925 | -50.7986 | 2025-09-15 04:25:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6cee5a54-8511-3540-b1ff-76e3fb9721b5 | -23.78674 | -51.64816 | 2025-09-15 04:25:00 | NOAA-21 | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dc2ea88e-c6ba-3328-be84-bb73474fe77b | -23.20099 | -49.63757 | 2025-09-15 04:25:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 56823d89-735a-3ee1-801c-b2de4323c89f | -3.81768 | -48.89449 | 2025-09-15 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40a2cffb-8ded-3c67-8a2b-60c28063c09b | -3.67138 | -50.6838 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f716f782-794a-3eb3-9ddc-73cafc7b62ad | -3.22556 | -47.62982 | 2025-09-15 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 447f0e06-a081-3de2-9060-5be16cc61b49 | -3.66556 | -50.95286 | 2025-09-15 04:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0fe8239-81f1-3c39-b526-73f4c2e46bd1 | -3.59661 | -47.51593 | 2025-09-15 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00dd588b-27f6-31ed-a6d1-fd9bd96ff149 | -4.17744 | -48.57698 | 2025-09-15 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 66d7e59a-5bed-31af-a0ea-bfd4e98a34ff | -3.59598 | -47.51997 | 2025-09-15 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01106fb6-4785-39f5-b35e-76bb812b594e | -3.55329 | -49.04615 | 2025-09-15 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6677aa4-5b84-3c5c-9bc1-53479dc9c67e | -4.17802 | -48.57326 | 2025-09-15 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9339be8b-bb88-325a-bf51-906e79f4deba | 4.30864 | -60.97177 | 2025-09-15 04:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1104a283-e4bc-3c7f-bb6c-d4dc72a5c70c | -3.24796 | -50.8125 | 2025-09-15 04:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d6e9f91f-d707-3932-8072-989b6dbb371e | -2.29286 | -48.57227 | 2025-09-15 04:46:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42bcf4b4-8f87-32a1-b5c0-3c02d8641cad | -4.17458 | -48.5727 | 2025-09-15 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 918152c8-8ae8-368f-902b-fc807547463e | -2.95323 | -51.28296 | 2025-09-15 04:46:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6487121-093c-3ba8-bf78-9b6e2b284f04 | -3.60018 | -47.51649 | 2025-09-15 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dee45415-0ef3-32c3-a4a3-2d1a347516f0 | -2.26226 | -47.84637 | 2025-09-15 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README38.md)
