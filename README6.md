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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e0b7afe-3ac1-3609-b1c8-08731328dd0a | -3.2314 | -46.9376 | 2026-09-25 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 206.6 |
| 9ce18db8-0205-3f80-8dc6-9b9d52b39ddd | -7.3853 | -64.3849 | 2026-09-25 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 1790bdf5-4b65-357d-8617-89b33c7762f7 | -8.6077 | -48.3764 | 2026-09-25 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 224.3 |
| 80a4e9da-1abf-33b7-adf1-2a6a5412c457 | -5.8047 | -43.9132 | 2026-09-25 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b3dbe366-a8bd-390d-add2-1486b4e369f7 | -8.6265 | -48.3747 | 2026-09-25 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 67e070ae-291d-3088-bb2b-1f2816910d8c | -8.5889 | -48.3781 | 2026-09-25 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 191.3 |
| b53c7759-ea26-3c0a-b5a4-9e3b85e96621 | -12.0605 | -50.2989 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| bb47254f-c7e8-367c-9d21-e8f276ab818c | -9.1812 | -60.7939 | 2026-09-25 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4dcfadab-9739-327f-b3c8-5f2a15588ec7 | -8.5891 | -48.3564 | 2026-09-25 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| ee331996-4eeb-3604-9eb2-44428af2949e | -6.8817 | -55.5592 | 2026-09-25 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 25b3d38a-a3c2-37ed-859b-87e390cff748 | -8.9663 | -72.8525 | 2026-09-25 01:00:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 65.5 |
| dbad1618-6fa7-34a8-8f77-4ddd2793e538 | -8.34 | -44.1427 | 2026-09-25 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 2f734899-a349-3720-a39e-a8d9ef34323e | -1.1462 | -54.0796 | 2026-09-25 01:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 39332f6d-1c88-37dd-bfb9-816332189f0f | -8.34 | -44.1427 | 2026-09-25 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2c9a59d5-69b9-3476-bc64-b1e3e1cb78be | -11.9774 | -50.7585 | 2026-09-25 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 67add9ac-ea27-3158-a478-e5a7a387cb7c | -7.4793 | -54.9664 | 2026-09-25 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9b7b4bc9-9a18-33cc-89af-8614d0d9e346 | -5.7754 | -45.1053 | 2026-09-25 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| da2068b0-f446-359e-a347-1cf7960ba194 | -3.2314 | -46.9376 | 2026-09-25 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 178.8 |
| 441f9819-16f2-3270-90eb-bc8abdabd6aa | -7.3853 | -64.3849 | 2026-09-25 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5b0f30ff-ec18-345d-b369-50dc4af0e45d | -7.4039 | -64.3469 | 2026-09-25 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3d297be8-f89b-3dbb-b880-9a49585773c3 | -7.3854 | -64.3475 | 2026-09-25 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 1a1056c7-d6c1-3f6d-834f-f72c57ebc76e | -11.6754 | -50.601 | 2026-09-25 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 7e892e2b-f8c0-335f-8f5c-85a1f3303e2f | -7.4037 | -64.3843 | 2026-09-25 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d4ee288e-8d28-38fa-a050-78aa5dfb39aa | -11.2859 | -51.3031 | 2026-09-25 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4df7a462-ffb0-3bb0-ad73-df13b777c7a4 | -12.0609 | -50.2773 | 2026-09-25 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 0121d4d1-4128-3b84-8121-1fc80244f079 | -11.959 | -50.7179 | 2026-09-25 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 45c04287-593a-3737-8a58-87187448dd2c | -1.1461 | -54.0996 | 2026-09-25 01:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| a1cfadf1-7c9d-384c-a558-4753fc09ab19 | -3.2501 | -46.9149 | 2026-09-25 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 579371f5-a113-38ef-b6e4-7fef629c1d2c | -12.0799 | -50.275 | 2026-09-25 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 4ab0bb58-2bae-3c22-a379-d28193799c4f | -11.9586 | -50.7393 | 2026-09-25 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| af30260d-525c-3b49-bd09-b89b462c14c6 | -4.1012 | -54.6185 | 2026-09-25 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4cab1db1-ff96-355f-a03a-a633f1dc2e9f | -3.25 | -46.9369 | 2026-09-25 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 170.7 |
| 7c032701-c301-39b6-bc8c-01e3a082ef5d | -8.9663 | -72.8525 | 2026-09-25 01:10:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 18e7238f-3fef-360f-9e87-da027b2a8b92 | -7.4791 | -54.9865 | 2026-09-25 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 70610062-9a94-3887-93d2-4bbc28e9d25b | -7.3854 | -64.3662 | 2026-09-25 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| b621be8a-2bb0-3f12-ab5f-9345207f2c78 | -12.0612 | -50.2558 | 2026-09-25 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 7195001c-8b2d-3546-ad1d-9e88820b5e3c | -12.0803 | -50.2535 | 2026-09-25 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f58467c8-8452-3a23-a812-cb7eb5635d35 | -9.1536 | -59.464 | 2026-09-25 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d4ff8717-e722-3e98-a1a3-eb3c8a3ddfac | -11.3048 | -51.3011 | 2026-09-25 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d92ae2b4-e13a-39de-b209-053f554766fd | -11.9399 | -50.7201 | 2026-09-25 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 141.0 |
| e0f52b35-2128-3d5e-81f8-97e5a8c017b4 | -7.4038 | -64.3656 | 2026-09-25 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 811c7c67-550d-3a55-afd5-c15f04747d6d | -9.1535 | -59.4834 | 2026-09-25 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3e1e1252-5874-3539-8e34-5ceec3c9cb27 | -3.2315 | -46.9156 | 2026-09-25 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 97dce0de-657d-3818-a77a-bf78213fabb3 | -3.23 | -46.93 | 2026-09-25 01:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91659bd9-c563-3e2a-b21f-4d6ba1b28e73 | -10.44349 | -64.49026 | 2026-09-25 01:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1cf254d0-f4a3-32bc-b1be-722c8a0d9696 | -10.44539 | -64.50304 | 2026-09-25 01:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| cf48ae98-bf05-3dbe-b392-f59c51aec231 | -1.1462 | -54.0796 | 2026-09-25 01:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| da21913e-3f7b-3f70-a946-83f14701714d | -7.3854 | -64.3662 | 2026-09-25 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| aa6d5534-839d-3eaf-bbb1-822cfe02e78d | -11.6757 | -50.5796 | 2026-09-25 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 69dffec1-704e-35d9-ab10-811cc9232a69 | -11.6754 | -50.601 | 2026-09-25 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f39893ba-8986-3488-8611-ca38170ca784 | -5.7754 | -45.1053 | 2026-09-25 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 5f6de081-de2b-3451-9962-608d7a4c3b11 | -8.9663 | -72.8525 | 2026-09-25 01:20:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b766d674-219e-3d7a-a2c3-32718a6b1bc5 | -6.9862 | -63.0096 | 2026-09-25 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a96da2db-dfcc-3829-93e9-5f1c51221303 | -6.9863 | -62.9908 | 2026-09-25 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9ebc0e7a-4331-36fa-9a02-099a20d63374 | -11.3048 | -51.3011 | 2026-09-25 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| fd0cb460-0584-3093-9a1e-3331a85ea774 | -7.4038 | -64.3656 | 2026-09-25 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 31c61f55-b40d-3df9-803c-515b6076ac10 | -1.1461 | -54.0996 | 2026-09-25 01:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 2a80f1ab-57ac-3063-a94a-d70257a70e13 | -11.6564 | -50.6031 | 2026-09-25 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 2374dc76-1142-366e-81a7-6df454c8b778 | -7.4037 | -64.3843 | 2026-09-25 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2fae54b9-37c9-3ece-b31c-be5348c0cb1c | -3.2314 | -46.9376 | 2026-09-25 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 37739ea4-995b-3cbd-80ca-e4c437ab0b60 | -7.3853 | -64.3849 | 2026-09-25 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| edf04590-1a06-3e66-a7ed-159c5fb0da48 | -11.9399 | -50.7201 | 2026-09-25 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| cf479f64-79bf-3e59-84b8-435ad13aa3d9 | -11.959 | -50.7179 | 2026-09-25 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 92ff5cbd-0ee0-3c3f-a568-1a3927e93f16 | -3.2315 | -46.9156 | 2026-09-25 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7aa2a62e-76f2-3c1e-9780-fb4c21255e4a | -3.25 | -46.9369 | 2026-09-25 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| df7beb01-b3df-3fe8-9c3c-f3b264335455 | -9.1722 | -59.4629 | 2026-09-25 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 007d9601-555a-39a4-a368-4ae30345bd22 | -3.2501 | -46.9149 | 2026-09-25 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 1e9473cf-f83b-3754-8cf2-db5b9646becb | -9.1536 | -59.464 | 2026-09-25 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a3ad3ee6-bbbb-361a-b89a-ec33511fd158 | -11.2859 | -51.3031 | 2026-09-25 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 097f75a7-61ad-3d9d-976e-d02dfb4ed8f0 | -14.7344 | -46.2219 | 2026-09-25 01:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2cbefcea-fdd7-31bb-9b24-46b2890345ea | -9.1535 | -59.4834 | 2026-09-25 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1fe9166c-3b55-3fb8-85a1-dc268ad8700a | -12.0609 | -50.2773 | 2026-09-25 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d0ce15ff-32d7-3bb2-b0e0-4d616d19919f | -12.0727 | -50.7474 | 2026-09-25 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d688bf70-8f70-3901-8b15-a88bd28c93aa | -9.06547 | -65.70863 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ccca5927-02bc-39f0-88f9-5828d20350de | -9.16412 | -60.77401 | 2026-09-25 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| ddb282cf-e1e9-3c57-9e8c-fbabc5892338 | -9.54747 | -65.99309 | 2026-09-25 01:20:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7626707a-9e29-3784-b45f-8f4858373bfa | -9.01962 | -60.53217 | 2026-09-25 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| d2202389-f0e5-38fb-acb6-cbb36369ed01 | -9.55703 | -65.99162 | 2026-09-25 01:20:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99d5780e-aafb-3739-ab5e-af06b80e1a11 | -8.63894 | -66.8603 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| d7b2d7e8-0128-3b06-afe5-0ad0735174e9 | -7.86943 | -72.98071 | 2026-09-25 01:20:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 39f9ea2d-5665-3ecb-8332-c19c39bfb255 | -9.02457 | -60.55367 | 2026-09-25 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0b895131-3b2b-3ac5-9905-7ad7a530ad30 | -6.94874 | -71.79113 | 2026-09-25 01:20:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d3f0aef8-0e49-3e6a-a39c-0b869164cac3 | -6.98669 | -63.00354 | 2026-09-25 01:20:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 62e95eca-0e01-3d70-af36-5dc667e872d3 | -8.65392 | -66.58884 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b1fb555e-770e-3f64-8184-c0b08596829e | -8.96542 | -72.85741 | 2026-09-25 01:20:00 | TERRA_M-M | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 42.7 |
| f874f228-7d9f-337b-87ac-04f1eb16d095 | -9.0201 | -60.52672 | 2026-09-25 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| cc1c1dba-649d-3201-83dd-ec6d87be4508 | -10.04539 | -67.86993 | 2026-09-25 01:20:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a701db35-2db2-3dcc-8cec-2fe293336a6a | -7.52438 | -70.39221 | 2026-09-25 01:20:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b822bf64-6852-3891-a1f8-6e8fbaa8c234 | -8.63754 | -66.8505 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2ef63120-ba02-3ef3-bcbf-e9d5da493cff | -7.94445 | -63.49537 | 2026-09-25 01:20:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0424030b-6260-369a-ab6d-16c8314d7d53 | -7.51605 | -70.39928 | 2026-09-25 01:20:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b0a4b744-251d-3022-81bb-69c80309730f | -9.1709 | -60.79291 | 2026-09-25 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7dfc0837-3b7f-3489-905b-6a0f0428ec5c | -9.1682 | -60.80005 | 2026-09-25 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| a1753e47-3f0b-323b-a495-061782a3564b | -8.90393 | -71.34978 | 2026-09-25 01:20:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c55559d7-08b8-3738-9445-bc99141f6880 | -7.6739 | -67.13961 | 2026-09-25 01:20:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5ae2d0ce-fea9-355d-a931-c964a878fc54 | -8.96376 | -72.84418 | 2026-09-25 01:20:00 | TERRA_M-M | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 95286fac-3257-3e5c-a522-fb3d5b65bf14 | -8.64816 | -66.85891 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a7d35326-95b5-3fdb-a74a-b469c905a131 | -9.39025 | -66.51202 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ff10bf1c-69c6-3a27-aa95-ae31bfee137b | -8.95477 | -72.8588 | 2026-09-25 01:20:00 | TERRA_M-M | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 22e089e4-686b-37e0-8e63-04291085512e | -7.67527 | -67.14929 | 2026-09-25 01:20:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |


[Clique aqui para ver as próximas entradas](README7.md)
