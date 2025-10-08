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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cb0f71d-94db-30b4-8436-1256de9e1ce5 | -12.5109 | -54.714 | 2025-10-08 07:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c0ffe763-af4c-3d37-9446-75b0f4b2d7f2 | -17.9224 | -57.5128 | 2025-10-08 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| c32b1ef3-d301-383c-bca0-7fc3828dda0b | -11.1642 | -54.9007 | 2025-10-08 08:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3e6a0685-2845-38ea-b507-54a834ac4450 | -17.9224 | -57.5128 | 2025-10-08 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| f726af1b-9c96-3947-b678-387fba61a051 | -11.1644 | -54.8804 | 2025-10-08 08:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 338e19ad-496c-37c0-88b1-af28ab572179 | -17.9421 | -57.5104 | 2025-10-08 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 37957b35-5dbd-3d0d-8137-419669e027bc | -11.1833 | -54.8787 | 2025-10-08 08:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c1e78e47-71fa-31e3-80da-0d8857ecf602 | -11.183 | -54.8991 | 2025-10-08 08:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2c86d7dd-a828-3689-ac62-e675bd718281 | -11.1644 | -54.8804 | 2025-10-08 08:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d5eb5bec-7861-3e4c-ab89-f25def429dc1 | -11.183 | -54.8991 | 2025-10-08 08:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 04a42584-5083-39e6-bf4c-1d778f490227 | -11.1642 | -54.9007 | 2025-10-08 08:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0c69ac88-90d4-3ce7-933c-87799a371b44 | -11.1833 | -54.8787 | 2025-10-08 08:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 8c7b68b9-9654-32d9-b4b1-8a324e8f8424 | -17.9224 | -57.5128 | 2025-10-08 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| a1ff7eb6-6f11-370c-9828-35dd067bc116 | -11.1644 | -54.8804 | 2025-10-08 08:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 488c15dd-306b-3648-b689-b19b215b30a5 | -21.6049 | -51.6554 | 2025-10-08 08:20:00 | GOES-19 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| f175f461-660a-3aa8-9639-388fb9bddd7b | -11.183 | -54.8991 | 2025-10-08 08:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 7b3117ad-d471-3145-8f21-f10a96df115c | -21.6054 | -51.6329 | 2025-10-08 08:20:00 | GOES-19 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 205086d8-0c9b-38f2-a474-4fa89566234f | -11.1833 | -54.8787 | 2025-10-08 08:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 66566570-ae0c-3bec-87b9-6e68a717ba41 | -17.9224 | -57.5128 | 2025-10-08 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| e25df0e1-e941-3cd6-8dd9-887028f24cc5 | -11.1644 | -54.8804 | 2025-10-08 08:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 9a52a244-c2ca-357a-8a92-52e6d98219c0 | -17.9421 | -57.5104 | 2025-10-08 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 30e12c71-7214-3920-8b50-247e9a80086a | -11.183 | -54.8991 | 2025-10-08 08:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a52bb303-255f-376b-bf4f-5e73a45b6bd1 | -17.9224 | -57.5128 | 2025-10-08 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| f66027fe-a1dc-383d-804c-d3539725daad | -11.1833 | -54.8787 | 2025-10-08 08:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6109a10f-14bb-3f77-9835-f5a58e657aa6 | -11.183 | -54.8991 | 2025-10-08 08:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ce34f348-194e-33d8-a03a-91657c1f1db4 | -11.1644 | -54.8804 | 2025-10-08 08:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| dd2633a2-daef-363b-ad0a-e843e97cdfb0 | -11.1833 | -54.8787 | 2025-10-08 08:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b5d2e818-7f11-32e1-860b-ee42f40352dc | -17.9224 | -57.5128 | 2025-10-08 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 368fea09-a05c-3834-8538-a47d3d5b3a91 | -12.3088 | -50.2688 | 2025-10-08 09:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 4c69d269-075b-349a-aa0a-2abe00c00fdc | -12.328 | -50.2665 | 2025-10-08 09:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 352b6bae-4861-3827-9588-dd0b97081edf | -12.3088 | -50.2688 | 2025-10-08 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 1def2d34-8d6c-3e8d-b9b4-8900bdb82b4b | -16.189 | -45.1314 | 2025-10-08 10:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 3af540ee-5036-3fd0-949c-60e7f0e2b216 | -11.6895 | -50.9406 | 2025-10-08 10:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 18859bcf-8845-37d7-b668-faabf085740f | -14.4079 | -46.026 | 2025-10-08 10:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 8eaf7c4f-8de1-3034-85dc-f2fccd57db74 | -16.1692 | -45.1355 | 2025-10-08 10:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 31a53cd1-ffa4-3ef1-9276-13c3e4313fdf | -11.7088 | -50.9172 | 2025-10-08 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 335.6 |
| 5e620143-bc24-36fd-aa23-093ed325f9f5 | -11.6898 | -50.9193 | 2025-10-08 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 4da8a900-c50c-3ea4-9061-7198ac66bcb0 | -16.189 | -45.1314 | 2025-10-08 10:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f8745287-3429-366d-a400-791b499d65fe | -11.7085 | -50.9385 | 2025-10-08 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| f75cc45a-e451-38fb-9322-b87ba6516d5d | -13.8112 | -45.8057 | 2025-10-08 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 7114c246-77de-3f45-85ad-f3b642d2210b | -11.6898 | -50.9193 | 2025-10-08 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1cfea181-cab8-3365-afad-066d85c32717 | -11.6901 | -50.898 | 2025-10-08 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a1ed79e7-e839-393f-b1d2-b4c201caad5a | -16.1692 | -45.1355 | 2025-10-08 10:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| aea14503-d101-31f2-9f69-7d397bfe4083 | -11.7088 | -50.9172 | 2025-10-08 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 0897a14f-be99-3a59-8a52-7f38ee7321e3 | -16.189 | -45.1314 | 2025-10-08 10:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 5a6c6a7f-cb8b-3639-ac49-7216dadea138 | -16.1692 | -45.1355 | 2025-10-08 10:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 111c2be0-0264-321b-aff0-3a8c3fca827f | -11.7285 | -50.8723 | 2025-10-08 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| a03dd64d-8d29-34e5-817b-a1113c19fa1b | -11.7091 | -50.8958 | 2025-10-08 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 282.4 |
| bf0f4b39-0ee8-3618-99d0-b797138e3c00 | -11.7094 | -50.8745 | 2025-10-08 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 369.4 |
| 43dd0ac6-31a8-3b7a-89b2-62bf7564082a | -11.6901 | -50.898 | 2025-10-08 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 49642df5-ae34-34d9-bdf4-de5fc96a5b19 | -11.7088 | -50.9172 | 2025-10-08 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 83945f30-502c-3007-a6bc-f10174db4c50 | -13.8343 | -51.8529 | 2025-10-08 10:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 33acb9bf-8f46-38ea-b69c-c4bc5d6132b7 | -14.7179 | -46.0867 | 2025-10-08 11:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 16210266-e3ee-373f-952a-c3ce29991984 | -13.7364 | -45.68 | 2025-10-08 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 3d91cf68-bec8-3575-a182-09edeb4d8aa0 | -13.7368 | -45.6569 | 2025-10-08 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f5132a92-32cf-32b4-8d9c-5d1c10e5ec11 | -13.8343 | -51.8529 | 2025-10-08 11:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| f0fca2ba-8200-3289-b688-1e2ce7c4a53e | -14.7179 | -46.0867 | 2025-10-08 11:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 141.2 |
| e4e05b9a-f1d6-308c-93e6-465a7ce650e2 | -14.7184 | -46.0636 | 2025-10-08 11:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 001e406b-ef0d-3a14-ac7e-655a5521a970 | -10.9106 | -47.1353 | 2025-10-08 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 1369f12c-5ab7-36fb-b7bd-859977363111 | -14.7184 | -46.0636 | 2025-10-08 11:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 175.0 |
| fb61eb73-965e-3f4a-8d5e-22a9dc0dc458 | -10.4251 | -46.591 | 2025-10-08 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e5c00a32-bf46-3a8c-9f5f-a625fd35e2d0 | -10.4435 | -45.3882 | 2025-10-08 11:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c6959be5-62c4-3ae7-8a9d-44c6b60c8661 | -10.4245 | -45.3907 | 2025-10-08 11:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3423aefc-2c18-358d-a71b-aec137b3e616 | -14.7179 | -46.0867 | 2025-10-08 11:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 251.8 |
| fa40f0a9-c08b-3657-95a3-107bfce74aa4 | -10.9296 | -47.1329 | 2025-10-08 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a861ec03-628f-39ce-a826-965aad4f370b | -13.3513 | -47.6042 | 2025-10-08 11:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a493f18d-2bb3-3a63-8c36-b12702063e8f | -11.1644 | -54.8804 | 2025-10-08 11:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 49696681-3cf6-338a-92ff-8735fac8d979 | -10.9106 | -47.1353 | 2025-10-08 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8268a245-b2a1-365e-8df4-ef8db55e1972 | -18.4125 | -45.2155 | 2025-10-08 11:30:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| efecbfa2-ea83-370a-9abd-ef8e71317a0c | -11.1644 | -54.8804 | 2025-10-08 11:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 8c69cb0f-c93f-3e47-82bc-3ec11c86ee53 | -10.4245 | -45.3907 | 2025-10-08 11:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 0860f074-3306-34f4-8d5f-6bea7242d900 | -10.4251 | -46.591 | 2025-10-08 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 167d7bd0-dcea-3d07-9a84-0f86158db481 | -12.5107 | -54.7345 | 2025-10-08 11:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 9b06e174-cd01-39e4-922a-37276cdd2328 | -14.7179 | -46.0867 | 2025-10-08 11:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 197.8 |
| b9f811d3-007c-3c11-8393-cadc9d55a84f | -14.7184 | -46.0636 | 2025-10-08 11:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 5f491686-c779-34a1-851d-39fb4f40c35b | -12.5297 | -54.7326 | 2025-10-08 11:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| f8ebd89a-5163-3b71-8fd5-a59b9eacf00f | -13.8343 | -51.8529 | 2025-10-08 11:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 172.6 |
| f19a85f3-5a61-3dae-b9cb-cc9aeb8e7cc4 | -10.9296 | -47.1329 | 2025-10-08 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a0038652-1d86-312b-b36f-579516a26ecc | -5.36372 | -40.99911 | 2025-10-08 11:36:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| c4e56e12-6d6b-3adb-bc23-b8b8dcad34d3 | -3.86568 | -41.54312 | 2025-10-08 11:36:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 05b2ed7e-a335-309f-ad95-0067733fd4c4 | -3.86345 | -41.55774 | 2025-10-08 11:36:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| dae1b823-82a4-3bd1-9527-ebda76e923b9 | -3.86657 | -41.53645 | 2025-10-08 11:36:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 31.1 |
| ec0ee139-aa3e-3cee-86d8-df852e020de9 | -4.4524 | -39.06384 | 2025-10-08 11:36:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 4deb90e7-1211-36e2-89ba-806f867a08b9 | -3.86444 | -41.55118 | 2025-10-08 11:36:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| f90b5128-8834-3545-83c4-af2960afb825 | -6.24997 | -35.41378 | 2025-10-08 11:36:00 | TERRA_M-M | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 741dbdbf-c1f5-30b9-b2ad-d3327488ebd2 | -6.2592 | -35.41502 | 2025-10-08 11:36:00 | TERRA_M-M | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 80a2dc89-7886-3af8-847e-694c8d6f12cf | -6.69303 | -35.21865 | 2025-10-08 11:38:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cb2a0fac-fe40-3d61-8cdb-570de465622e | -8.68501 | -44.73662 | 2025-10-08 11:38:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 0e0559da-a93b-3c33-9dc9-2d968451b8c4 | -7.76738 | -42.38145 | 2025-10-08 11:38:00 | TERRA_M-M | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 319e987f-ef2f-3056-add0-529d166a89d6 | -8.30017 | -36.8894 | 2025-10-08 11:38:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 920f9dbb-b492-334e-afd5-e33ec15db35b | -7.02258 | -42.88036 | 2025-10-08 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 929.6 |
| 9f2f5d63-e22a-3a5a-a186-9f0af436c3e4 | -7.4565 | -39.95884 | 2025-10-08 11:38:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 24bdac02-088b-3f08-b311-3daf6161bd70 | -10.92861 | -47.116 | 2025-10-08 11:38:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 60d85085-25d8-3e49-9c1d-7bb8a852df9c | -10.42826 | -45.39983 | 2025-10-08 11:38:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 6adc747c-3f15-394d-ae2e-06caa0421cd7 | -8.23891 | -44.17587 | 2025-10-08 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0ffbf575-1086-3b98-96b5-649da64107a4 | -11.31285 | -41.02409 | 2025-10-08 11:38:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 91148740-8e70-3ce9-9531-b1a0aa9adeac | -7.90797 | -45.50933 | 2025-10-08 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e183af16-eed6-3b61-96e8-4d518eeae09c | -8.19062 | -43.33967 | 2025-10-08 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 156.9 |
| da64e786-77c4-3dd9-916d-21c2476e9f47 | -5.86994 | -44.29182 | 2025-10-08 11:38:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| fd5059b2-75db-338d-a0cb-00a0e7107590 | -7.44394 | -43.13145 | 2025-10-08 11:38:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 141.0 |


[Clique aqui para ver as próximas entradas](README98.md)
