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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3d3e8e2-bbee-38a5-b750-d189c334dcc0 | -1.82592 | -54.50428 | 2026-08-12 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc66649b-9c14-303e-a513-db55ec867b34 | -4.11123 | -50.4495 | 2026-08-12 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ec59f4-295f-392a-9f47-971c573b2c7f | -2.80664 | -48.59322 | 2026-08-12 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4d6a206-a83c-3bdf-92db-fa6fcfb4161f | -2.4172 | -48.63392 | 2026-08-12 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e23feee7-aa29-347a-ad11-8b90784a0b6e | -1.82923 | -54.5048 | 2026-08-12 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2f4e09a-7979-3ddb-8ac6-bbb034786880 | -3.23701 | -49.46172 | 2026-08-12 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e047ea63-b717-3497-9226-64ba9a1d293f | -4.35678 | -48.14855 | 2026-08-12 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f826c6b2-3506-39b1-90b4-f8eda854a465 | -1.82538 | -54.50773 | 2026-08-12 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ed976bc-f5ad-36ee-8b0e-b6cb7176fd98 | 0.18919 | -60.49376 | 2026-08-12 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fba0a297-8f1c-3f8b-a14e-ad6753ec2b8a | -1.42798 | -55.25797 | 2026-08-12 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49d126fc-eafc-3cd7-9cba-fbff31741150 | -3.70289 | -54.25588 | 2026-08-12 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1f16556-60c7-3bf5-8a77-438e382333e5 | -3.85617 | -54.07991 | 2026-08-12 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 367b2963-c785-37ab-98c3-b04fca95c5c6 | -2.74307 | -54.59148 | 2026-08-12 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6c7e8e9-6e67-30ff-95fa-7282b434879a | -2.68921 | -48.20388 | 2026-08-12 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55bc4c71-cc40-3386-9b19-29c8e9e79968 | -3.02868 | -54.52627 | 2026-08-12 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad166cac-9009-3bc8-a9dc-02a8aa8d33eb | -2.68849 | -48.2086 | 2026-08-12 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebf81167-b7fa-3fc5-932a-75221c4ee211 | -3.4813 | -47.68693 | 2026-08-12 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ba56cea-1df3-31b7-a084-1aca64b67cd3 | -2.74253 | -54.59493 | 2026-08-12 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a05e77e6-56dc-3192-894a-e15785daa66a | -3.4369 | -49.48234 | 2026-08-12 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9d2b4b8-270f-3a69-90aa-d29ccdcfce3f | -3.15192 | -54.6059 | 2026-08-12 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2c39fbd-2d3e-33e5-8120-058fb2ff4118 | -4.1072 | -50.44891 | 2026-08-12 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca8162f6-d679-3d1a-9146-335196fcb9ee | -3.22437 | -49.99114 | 2026-08-12 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56b2ef88-10b6-35eb-b5e1-0f1b4d50f950 | 1.1019 | -60.51337 | 2026-08-12 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 505a6b90-f344-3f26-86bf-8d219dccbb3c | -3.43265 | -49.48169 | 2026-08-12 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8752675-3cc7-3e1b-b7c9-7e00fc5c8d13 | -2.80456 | -48.59483 | 2026-08-12 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e01bb231-58c4-373f-abbb-97e1931d821a | -3.84464 | -49.03753 | 2026-08-12 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01dddc80-5612-37fc-be30-51050b949876 | -1.83417 | -54.49498 | 2026-08-12 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 915fbeca-072d-3ce8-974b-203036ca02e3 | -2.96086 | -49.26044 | 2026-08-12 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ed9634a-05eb-3858-b9db-a9ba95d202e9 | 1.68909 | -61.08067 | 2026-08-12 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22beba2d-5d39-3bdf-8cfb-a52a4e7f0ec7 | -2.42164 | -48.63459 | 2026-08-12 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0f2fedc-fe17-3828-87d7-b33753cccb1b | -3.429 | -49.48222 | 2026-08-12 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b30d1e4-068a-3785-a0af-58813fde72d0 | -2.80217 | -48.59251 | 2026-08-12 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66454289-06ab-3959-a4a4-0803a4270d84 | -2.84173 | -54.67752 | 2026-08-12 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b3749fd-f577-320e-8e1e-d066bd9fa36a | -2.84119 | -54.68096 | 2026-08-12 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e600a1f6-0f32-3736-9508-97139f1031f2 | 4.18588 | -60.02465 | 2026-08-12 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 392eeb91-e0c0-3148-b310-cee55f5baea6 | -2.41691 | -51.83471 | 2026-08-12 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bc271d4-477e-362d-9628-8c1a958d7f91 | 2.64808 | -60.08923 | 2026-08-12 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cb6bc51-dfd0-34c6-a528-387784364624 | -2.96025 | -49.26448 | 2026-08-12 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d532e7c-28f4-3ee3-9983-fa5ba708a3d6 | -3.26563 | -49.53023 | 2026-08-12 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c651fc9-a326-3f2a-86ea-b5ba5ba5726d | 0.18855 | -60.48964 | 2026-08-12 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b089d001-5787-39a5-9442-70e355a7b623 | -4.4718 | -45.89983 | 2026-08-12 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84a95c55-c37d-3a7f-9fb0-64453d32ba6d | -4.46631 | -45.89879 | 2026-08-12 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64f50008-5713-3426-a9bf-ee5184c7ef2c | -3.14861 | -54.60538 | 2026-08-12 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc0d1734-78ce-3de8-a64d-330ca21f5ebc | -3.2376 | -49.45773 | 2026-08-12 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 441f1341-bcd0-335d-98d1-d0597e850ccc | -3.43325 | -49.48286 | 2026-08-12 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb9fcf79-d97d-31a5-9f4b-653ad291e872 | 2.64873 | -60.09338 | 2026-08-12 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf0363a4-0576-3d42-8e29-89049f42fbd9 | -2.80522 | -48.59039 | 2026-08-12 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d36a1464-be6d-3271-9f52-ec03741ec90a | -2.4195 | -51.83654 | 2026-08-12 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1c6add4-965d-327e-a425-5eb2d4860cd6 | -4.46577 | -45.90242 | 2026-08-12 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cff3b3ff-c001-3edd-8bb5-e0540f588875 | -0.89257 | -50.47298 | 2026-08-12 05:08:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc009e50-4530-3253-8029-b58230d76f85 | -11.9535 | -46.3444 | 2026-08-12 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 487dacf7-a362-3176-ab5e-ef08ac46d9e3 | -11.9539 | -46.3217 | 2026-08-12 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a49c9627-f005-3814-8ca7-e5585c2d62da | -8.95646 | -60.53784 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6600f1de-c75c-3923-bb61-dbf33bb3152c | -10.63603 | -47.4866 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6adc8d2b-1575-3ed5-ab25-57170ee1fe1f | -6.54688 | -43.12974 | 2026-08-12 05:10:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d0f76ab4-c77e-32dd-9a68-b63b63fe1669 | -11.47161 | -44.55991 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62911172-f2d1-346a-95ee-9205e1940697 | -8.95504 | -60.49977 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dabe776-da08-3249-bea8-4f18e807948d | -8.95116 | -60.54644 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1f449b3d-665f-3a1d-b3a8-167cc42d51be | -9.34377 | -47.49022 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57900b39-eac9-3de2-8fa3-3c4736d68a23 | -6.59146 | -59.00922 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 40750d24-101f-35b9-bd62-f39cba9cd11b | -9.47469 | -60.52731 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cefaa347-04e1-3cd4-a062-fb9383fcbb53 | -11.95477 | -46.38685 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0e3444ff-8c6c-3168-a0a0-12be5248d424 | -11.49646 | -54.60529 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bf8e1cb-a250-33f5-82ef-f76843cfc5df | -8.95128 | -60.49913 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e037c272-f5d3-3a6b-9aa7-4fd2d1ebb99b | -8.89515 | -60.57961 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8389c955-8d22-3ed7-9245-a95096fb8f04 | -12.16241 | -50.13043 | 2026-08-12 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df202f2e-64f0-3fc8-a0df-3b5b0c87232b | -11.98414 | -46.37098 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81cbfafe-4ce7-3d95-ac78-fe47eea2564e | -11.81951 | -51.83339 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9f95e35-1e30-3988-910f-84b0d0a20df6 | -7.4578 | -46.1453 | 2026-08-12 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91339f60-0cfd-3292-993a-40c3639daa70 | -8.95414 | -60.5308 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4a68f1df-362f-3f56-a7b3-d202100132b7 | -8.98612 | -60.59318 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed72ed4d-7322-3cd2-abe2-5d7ac6df105e | -10.63556 | -47.49022 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a94fd9af-4856-39dc-b5d3-696843e58223 | -8.95565 | -60.56614 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b46f8f30-d679-3320-9d30-75421363235b | -9.34998 | -47.48425 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c05a6fb-bd6b-3241-8a55-5a7aed986a14 | -9.34201 | -47.50354 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4a80991-d074-3d3a-9a82-9f63720f24cf | -8.94676 | -60.50307 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84b98268-d8bf-3327-9ca1-5837541b853e | -8.95095 | -60.54922 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30c01004-1fa2-3fdc-ad20-583f3bb9b40c | -9.3323 | -47.53622 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afbf60d0-d173-3688-8337-d647e00968e0 | -11.83718 | -51.88058 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fae331ee-4afb-3108-ba64-a80dba530145 | -6.99882 | -42.63794 | 2026-08-12 05:10:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f23fc51-44bd-3c36-b103-dfc12d37c519 | -11.94985 | -46.37765 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60d14cc5-07b2-3480-b2eb-a81f4f667b36 | -8.35765 | -45.98032 | 2026-08-12 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 80ad1c12-356b-37e4-bae0-c52d54ff16a7 | -6.85079 | -46.00897 | 2026-08-12 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 652fd31e-448c-3f28-80e4-7c3e632810d2 | -11.98213 | -46.36019 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99b1ebf1-505d-365c-8d07-b1059d6a8f9c | -10.83904 | -50.34873 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1158a18e-276c-3b25-9477-a142e43b5d82 | -6.85136 | -46.00474 | 2026-08-12 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14541aaa-a2d4-3c4a-b648-441bd7eec739 | -11.46958 | -46.68991 | 2026-08-12 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 339619e7-a5fb-31d1-9a59-15d3b617b0dd | -11.65255 | -50.14407 | 2026-08-12 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 372a5460-d50b-315a-a57c-8baee593e298 | -9.47323 | -60.51307 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b00cb78-b6e2-3655-8cf0-d4e4effc9822 | -11.78299 | -51.85485 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ba001c7-3a45-3fca-87e5-30bd82e818cd | -9.58218 | -48.42139 | 2026-08-12 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50d42db3-7636-34d3-8e8a-cdcb31552a44 | -7.0112 | -44.62883 | 2026-08-12 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40876143-5ae8-3c0a-814e-53098267732f | -11.48171 | -44.575 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1527bb8c-94ed-3d76-a0e6-553ac24e294b | -9.13138 | -46.38556 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e2b7a09-22c0-3c06-8f7c-ecb97e5c8045 | -6.54934 | -43.11151 | 2026-08-12 05:10:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 20247f5c-0162-3ef2-99b5-308724760dac | -6.61735 | -58.99997 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62ea68e8-588b-331f-b9fa-3989e7fbdce8 | -8.94811 | -60.56482 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6cf93070-6d00-3c22-b7dd-cfa376a7dcca | -8.95346 | -60.53257 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| eef405c6-1789-3338-aabe-af2a419eef1e | -8.95788 | -60.57611 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af760c18-64d5-3e8c-a27f-716b8e87305b | -11.82718 | -51.83843 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README26.md)
