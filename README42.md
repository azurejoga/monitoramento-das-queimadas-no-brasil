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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 335c2208-51c8-3849-bf84-8e7686a69bba | -11.25855 | -50.47684 | 2025-08-16 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b308bd9c-b022-37be-a35c-f08140526836 | -12.59003 | -46.93913 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80d6060b-2328-3fcb-adb7-a6fcd619ffae | -12.54101 | -46.94826 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b7b21932-4745-3fa3-82ff-50ef64e5ba70 | -8.99027 | -60.51173 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 686caf8d-5d83-32b8-a4e1-8644d88a6d52 | -12.60399 | -46.94117 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 34d6014b-74f8-3256-9d2b-56d69c8c4940 | -12.5526 | -46.96607 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4fe89b7-94cf-3cbd-9a66-a5028a95daa8 | -12.48952 | -47.50098 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef08c7f1-8451-3a30-869b-791426f3db30 | -11.34873 | -55.43599 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f589eb4-54e3-3038-8b91-52df186c8919 | -14.93596 | -54.70501 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9769b918-a11c-390a-b65c-9a340bfd2707 | -14.51956 | -49.38692 | 2025-08-16 04:34:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8172d31-5059-3a4d-a56e-d674417ddf3a | -11.34951 | -55.43161 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4496a37f-4903-3b96-803f-5a71ba007a5c | -11.91209 | -52.53048 | 2025-08-16 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0214e73b-cfaf-3be0-b762-38f725e6011a | -14.93692 | -54.69966 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 1a6bc2ef-8259-33fc-ba95-167d063834bd | -12.23295 | -41.38445 | 2025-08-16 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c1b04a32-8bca-3b8c-b422-55f7c333bbd0 | -14.58393 | -47.92683 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b25f0139-e6df-3b45-ab44-33afd34e2a82 | -12.83311 | -46.02924 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a00b1c0-9883-3180-87d0-75b63785e4a1 | -9.49957 | -60.53765 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fd3c6cc-8e41-36d2-bce7-cd5c2e3f6227 | -17.36734 | -48.81829 | 2025-08-16 04:34:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03b04604-5199-3546-99f1-d3428156931b | -8.97837 | -61.70839 | 2025-08-16 04:34:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 583402eb-63ef-3527-9756-3cd6f3802af3 | -9.16902 | -59.64415 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1eeb4b2-066c-3b27-976b-bd4cf4476f9b | -9.91935 | -60.48706 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a21ef6da-4f25-3fcd-bceb-4a27014d4d23 | -16.28003 | -58.69967 | 2025-08-16 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 21f53032-f6ce-3249-9867-e4e5bdeee52f | -8.97898 | -60.53619 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8bc5da3b-36ba-3f60-b94a-a8a0904995ef | -12.82889 | -46.0064 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 943cf12b-1454-3fb1-b6e1-de45ad69bf3a | -13.60727 | -46.91858 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc6fe0bd-8c12-3a3c-9a9e-ac4bb541b125 | -12.59883 | -46.97626 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fcb7b0c-7b16-3c36-9eef-46fc3704a2e7 | -12.47204 | -46.98147 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaea4a40-3d09-3774-9454-f14be6bb68dd | -13.33243 | -45.22188 | 2025-08-16 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27d091ec-ad09-373e-b30d-14eaf515754d | -13.58543 | -46.96959 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3459ac7d-4669-35c3-96eb-c9032e8597e3 | -9.16985 | -59.63976 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e2c6852-ed99-34dd-8ded-c8121a6e26ae | -12.55608 | -46.96662 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 580ff616-1252-3b9b-a543-a9f5bb768310 | -9.50432 | -60.53125 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a20820c1-ed90-37ac-85ee-4a6edbb9f4e8 | -12.5821 | -47.04168 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fbdef9d-0d00-3a52-bd1b-bde6bf22b23d | -12.52766 | -46.96617 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02b3122b-d24b-3a60-aa87-cc5986df9a44 | -9.15963 | -59.62847 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0eb56f05-d67c-3b0f-bdf7-5334228e3102 | -14.94485 | -54.70065 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4b36e18d-034f-3a66-bc31-3a3da3e6ac84 | -8.98832 | -60.52183 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2ca0bd93-f360-3d1d-9a19-961178d11b23 | -13.12852 | -57.16719 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e4ed919-a98d-3a81-b4a8-aa270006a7f0 | -14.59303 | -47.93605 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7e0242d-00b0-3c13-a68d-74bdee9261fe | -14.15948 | -54.05048 | 2025-08-16 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 026f6390-660a-32e9-b6e9-27f927aaa444 | -12.60875 | -45.23436 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6a28fe3-d9c8-3d7f-b5a6-c1f3b0111bab | -12.83552 | -46.03847 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73d737e7-a1e4-353d-ae78-64b11f038975 | -16.23166 | -51.11977 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32cdb710-83b0-37e1-9963-ffbfc3570820 | -13.57665 | -46.98059 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4b6e58c-8615-3096-946d-8ae0ed6626ae | -12.56014 | -46.96329 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| c20adaec-02ef-3397-890e-4143678f324a | -10.04666 | -59.11958 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54c7e390-63fb-3d9c-ae0e-cc906f5a9bd9 | -10.00905 | -59.22453 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58e4054c-37e5-3c96-ae34-6d0c3a0887ed | -12.55898 | -46.97104 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0e14550a-3b28-3c42-8056-8267395ad761 | -16.24107 | -51.12508 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90301704-1f14-3749-8801-85884b7acead | -16.24048 | -51.12877 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e9ef4ca-89c6-34e9-a0b5-7c7524da2c19 | -9.49666 | -60.55306 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9d0a222-9f8a-3c8c-90d4-b2c11411052b | -9.16142 | -59.68417 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90c403fc-33b2-33c6-b0de-c38addd2395d | -11.27179 | -50.4903 | 2025-08-16 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d75c4d6-cab8-3443-b653-b27dd69eb855 | -13.62244 | -46.91337 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 960c96e2-c8b6-34a2-af3f-2281849c41dc | -12.80854 | -45.99146 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b20c87e0-60e9-3341-bb3f-3d44824929ef | -9.1614 | -59.65165 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa1d0faa-8a31-3c72-b61c-8b57e21a6c9a | -12.59874 | -46.92837 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 31d5209b-9dab-324c-b41b-0825858adab0 | -8.99062 | -60.54386 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| cad23af6-dbfd-3b3f-ad7e-bf7eb6bb233f | -13.49757 | -43.61271 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 70b58474-df01-308f-9c78-10ca71944f76 | -8.99465 | -60.52297 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6a927f53-6a57-30e2-9f41-01c47d3d9a6e | -11.34466 | -55.40853 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44659cc3-cb25-3d95-aebd-41471d0aa62a | -14.53249 | -48.59541 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39394534-5b04-3599-80f1-90200ffa5872 | -12.60229 | -46.95275 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c570faed-8f2f-338a-bdef-b839385540eb | -13.10764 | -46.85288 | 2025-08-16 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c154c3f0-ce55-3c72-91a4-74c7a74d2183 | -11.93111 | -44.11775 | 2025-08-16 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dffc5d02-2398-3af9-a1d2-fa8d47026f71 | -8.97716 | -61.71456 | 2025-08-16 04:34:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 44541810-d3f0-3c80-b071-e8e90fa33597 | -8.98199 | -60.52065 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7b1f7f86-8b54-37bb-aa28-8f0685878f8c | -11.66265 | -51.62802 | 2025-08-16 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 782ea036-ae11-3065-91b1-f9a0313cb98c | -13.44545 | -56.67856 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 639c2bf6-1b50-39dc-9d97-7c5913ac2c2e | -17.21633 | -49.58887 | 2025-08-16 04:34:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ede2a121-81a7-3e99-a696-90f650c88ca7 | -13.00083 | -56.87993 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fecfdd9e-8f99-39ee-895b-42f69deecbab | -14.94231 | -54.76001 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8079bb6-ad25-395e-93ba-7fc193859fdf | -12.53985 | -46.95609 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35197c1e-2ac3-33f9-afd6-8f02560f82f0 | -11.34978 | -55.40505 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bdf1571-79c4-3bfe-a22a-c2847854e992 | -12.60593 | -45.23172 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef1aa75-3846-3e70-90ac-d161a839234c | -12.59645 | -46.91965 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 297db6d3-2e4c-3e3b-b672-08ca376f9553 | -14.52633 | -48.59066 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9862f92f-e749-3c09-8797-f6fe060cba1b | -12.83676 | -46.02975 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e36e556-bf13-3e25-a3ec-984ba08a125d | -14.60272 | -47.94135 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94fd0201-8895-333b-9c11-3cd780207ba5 | -12.61421 | -45.22811 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1750ccc0-5f59-3f91-bcb1-f7fe6f5bc256 | -12.53114 | -46.96671 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db247b23-b9d2-3c2f-8f2f-78c3e6c5ceb6 | -14.94604 | -54.73918 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| cce8c560-4c76-361d-9145-5e8b70b511f5 | -14.86932 | -60.08464 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e9af59bd-e086-34a2-8179-759d307df2ae | -14.6073 | -47.93368 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c584609c-31af-33e3-883f-4c700a8e4800 | -14.58734 | -47.9274 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf86a943-196a-34f5-9373-789379bdcd08 | -15.8801 | -52.33479 | 2025-08-16 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89cece8a-740a-35b9-8a14-e5c364570739 | -11.50636 | -47.24561 | 2025-08-16 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cca0b84-5fdf-340b-9a07-5919297c645b | -12.46208 | -46.98846 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9705698-e7c1-3d8e-ab04-c216ec7b8e5f | -16.23988 | -51.13245 | 2025-08-16 04:34:00 | NOAA-20 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3bf3dd70-8a88-3616-b576-350b8b23db40 | -12.60286 | -46.94886 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4145f812-1383-3f50-a445-09dbeb7bfc50 | -8.99658 | -60.5129 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d6eacadf-d8b6-3478-9fa3-fd2dd8a43aec | -13.60841 | -46.91076 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96130051-3e45-3759-912a-65627f34df1a | -13.44721 | -56.66898 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c618cdd-a801-30fa-bed2-2e9de6c6f832 | -13.86863 | -45.54848 | 2025-08-16 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77f094cb-c572-39de-8de2-10fb17d299b7 | -12.55487 | -46.95087 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 43bf96cc-518e-3885-b0b3-e82b33375b0b | -12.61041 | -46.94599 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96fbf03a-966d-38e8-a109-76550065dafe | -9.16225 | -59.64721 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d363515-0e3a-3d38-b984-de2017fc5027 | -12.60338 | -46.92101 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a1bd4297-64a9-307f-87f8-86a7ae33fb1e | -12.54217 | -46.96442 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 843ccc05-6e08-3664-b3f7-fdd4ce42cad3 | -14.61637 | -47.91958 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README43.md)
