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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49f10a7f-aa8f-3fb1-b1a1-6a9142236124 | -11.0609 | -47.2503 | 2026-08-16 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 26cfd28e-a874-3874-b0e3-cec713c6ea08 | -8.9601 | -60.5165 | 2026-08-16 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| fbe5c86b-271f-32f2-980e-a8c21c7bf57b | -12.0282 | -46.4471 | 2026-08-16 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 98b49b48-b3b9-3c2f-a20a-e070a728419d | -12.6825 | -48.4779 | 2026-08-16 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 32e14887-4ad8-3450-9be6-6344ba8ed30f | -12.7013 | -48.4974 | 2026-08-16 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 963bf589-7ab1-3bb2-8118-304acbe27573 | -14.3729 | -51.8893 | 2026-08-16 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 22ef5d7e-3660-3f88-875c-b8891b8268bb | -12.7017 | -48.4753 | 2026-08-16 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d404169c-4de3-36fa-ab47-e1b76d4e391d | -15.0682 | -47.0098 | 2026-08-16 12:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5964fc22-7b11-3d16-9389-072498411606 | -11.9899 | -46.4525 | 2026-08-16 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 09cdf9de-e47d-3299-8e36-594b7714450f | -8.9601 | -60.5165 | 2026-08-16 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 165ed9a2-459e-3242-a8e3-d2e2becb4054 | -14.4105 | -51.9482 | 2026-08-16 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.5 |
| d77d85b0-1a1f-3717-8002-98c16ad4cc54 | -12.7017 | -48.4753 | 2026-08-16 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 3b899f42-4bd5-3756-8b47-b3da65a8892a | -11.0796 | -47.2702 | 2026-08-16 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f4fd9b0b-a4ea-38a6-85cc-9d75d0bff3db | -12.0286 | -46.4244 | 2026-08-16 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 70a9e3f0-1901-3982-b35b-0b2763df882b | -11.0609 | -47.2503 | 2026-08-16 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 98f96557-17d8-3a36-8b87-cd58c0ae1f7b | -11.8291 | -51.7937 | 2026-08-16 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 807347de-2b63-3bd7-aafc-4e899decdcc5 | -12.6825 | -48.4779 | 2026-08-16 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| cd9bac2d-68ea-37e1-bfab-e2b9985cb8ac | -14.3882 | -53.2826 | 2026-08-16 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f12a98ca-cc24-345e-88fc-7b55700a825c | -6.6852 | -44.0033 | 2026-08-16 13:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 824.0 |
| 17e98ebd-983d-395d-96db-cf483ad79871 | -12.0282 | -46.4471 | 2026-08-16 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 5da600eb-fbf1-3232-863e-31c0cedab7ce | -6.6664 | -44.005 | 2026-08-16 13:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 319.8 |
| 355308b9-b1d1-3693-974f-7ca7cafa13c0 | -12.7013 | -48.4974 | 2026-08-16 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 210.9 |
| f9b609d3-97a5-3c44-a143-c2ba0e156585 | -6.6666 | -43.9818 | 2026-08-16 13:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 270.4 |
| 018b4d8b-d670-3030-bff3-880c3480bc0b | -6.6014 | -58.9844 | 2026-08-16 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 2e330ba9-111d-3ca4-abcd-6d5bebe05d65 | -14.3726 | -51.9106 | 2026-08-16 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| dc05185f-d069-323c-beb8-90fdd386ccd9 | -6.6854 | -43.9802 | 2026-08-16 13:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 873.9 |
| c776cbf0-edf4-3db1-8d9f-5188e7b580f5 | -14.3729 | -51.8893 | 2026-08-16 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| cb1ef620-d057-3cbe-abe2-272e8cf2324a | -12.0095 | -46.4271 | 2026-08-16 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c6531625-f9a4-320c-aeac-57e860b97438 | -8.9787 | -60.5156 | 2026-08-16 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| cc69eb59-d869-3cdd-8511-470de69e3a27 | -8.96 | -60.5358 | 2026-08-16 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 71bb9576-6725-3908-a609-e19cfb587755 | -12.0091 | -46.4498 | 2026-08-16 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 86232236-b7e2-312a-a893-73cabe9d4ca9 | -8.9787 | -60.5156 | 2026-08-16 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 24307c92-fb85-3603-8edc-6905a595ac6b | -12.7013 | -48.4974 | 2026-08-16 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 15181875-a09d-3591-be36-480b6b9e4f49 | -15.0682 | -47.0098 | 2026-08-16 13:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e1521acd-80cc-3d89-903b-c71e6e73a056 | -12.6828 | -48.4558 | 2026-08-16 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 29290d32-2f23-3f47-bede-971c4a372fd4 | -13.6803 | -51.8724 | 2026-08-16 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 0049d7d5-74ec-3498-8662-0e6bd07faa67 | -14.3729 | -51.8893 | 2026-08-16 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 70732a62-4cc9-3f84-b1ba-1687c0b23abe | -8.96 | -60.5358 | 2026-08-16 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 37ce67e8-d23e-3c94-8332-30f6c8076b28 | -8.9601 | -60.5165 | 2026-08-16 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 45b51e65-ed33-3150-a949-80a91842cb10 | -14.3923 | -51.8867 | 2026-08-16 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 2ff63dbf-7e9b-3aa7-a83e-cdfff1591472 | -12.0474 | -46.4444 | 2026-08-16 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| f940d98a-a827-31e9-81eb-553c216c4cef | -12.0091 | -46.4498 | 2026-08-16 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 0482f4df-4f4e-37c3-b533-03a851c3760a | -11.08 | -47.2479 | 2026-08-16 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 29f120ca-cf90-3088-8bc8-f745b3938aa7 | -12.0095 | -46.4271 | 2026-08-16 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 309b3526-ce6a-323d-9f96-c8720dae15ef | -12.0282 | -46.4471 | 2026-08-16 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 0d803d42-c25c-3bf2-a8f6-f76ff0bf05d0 | -12.7017 | -48.4753 | 2026-08-16 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 322c366d-741a-3d08-949c-c6463e969cc4 | -11.8291 | -51.7937 | 2026-08-16 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 6ac82f4d-9944-3f5f-ab60-6171fb70342d | -14.3726 | -51.9106 | 2026-08-16 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| ee5373b2-0641-3548-99e5-d00bbe166d57 | -6.6014 | -58.9844 | 2026-08-16 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 08bd46f1-4b14-3c11-8ff3-621decc6ca71 | -11.9027 | -45.9654 | 2026-08-16 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e0f7f62f-0fbb-3627-a47d-17db341e1ee8 | -12.6825 | -48.4779 | 2026-08-16 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 178.8 |
| de5fab7e-8d4e-3498-9331-d676acd1930e | -11.0609 | -47.2503 | 2026-08-16 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 7888f06c-fa7f-33c4-bba5-e998bddf8799 | -14.3919 | -51.9081 | 2026-08-16 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 11da62db-bf79-3905-8315-b04e43c48b97 | -14.4105 | -51.9482 | 2026-08-16 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| bc513e92-bb49-360b-a068-22c5a11d6efb | -6.11 | -45.3298 | 2026-08-16 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 58e05d23-9b61-3715-a19c-446f00da2e71 | -11.0796 | -47.2702 | 2026-08-16 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| faa2dcb5-c589-343d-9ba4-f0df21a5217f | -6.67 | -44.02 | 2026-08-16 13:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e54656d9-9f42-3a9c-92cb-06dc07e38c8c | -6.67 | -43.98 | 2026-08-16 13:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 745db515-9260-3968-9b56-62c850a1ef75 | -6.7 | -44.03 | 2026-08-16 13:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4194e739-82cd-321f-b30f-709bceb2aacf | -6.7 | -43.98 | 2026-08-16 13:15:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83ec71c4-05b6-3b6c-9b55-8b40671e1dc2 | -11.3 | -45.83 | 2026-08-16 13:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87a7c0c5-3cec-33fd-90b9-49f5f38c8ff0 | -12.6825 | -48.4779 | 2026-08-16 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 342.0 |
| f2968400-9795-34b4-9d96-883c52a59e8b | -11.0796 | -47.2702 | 2026-08-16 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 79b642cc-18bb-3e98-8c71-4b3ce068be13 | -12.6828 | -48.4558 | 2026-08-16 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| fd9acb32-64f0-3a0e-868a-e7ec1ad025ba | -11.0609 | -47.2503 | 2026-08-16 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7bdde145-4677-3f0d-bca7-c2048b209e72 | -12.0095 | -46.4271 | 2026-08-16 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| d90b3d24-e6d8-3f53-8922-17ef9b3332d5 | -6.6014 | -58.9844 | 2026-08-16 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 6bf6d8e8-845c-3f01-8bf2-8300ced13f4c | -12.7017 | -48.4753 | 2026-08-16 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 2a937704-0495-36ad-8539-36387fb1687e | -12.0282 | -46.4471 | 2026-08-16 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 724c23e2-7e62-330f-98ac-be6be2c2503b | -14.3729 | -51.8893 | 2026-08-16 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 71c0b80b-add4-3907-93ca-b24a9cc5db23 | -12.0474 | -46.4444 | 2026-08-16 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 412cf646-ec96-39c2-aa88-37462410280a | -14.4105 | -51.9482 | 2026-08-16 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| cd66606f-29b7-334a-a87e-c4eaabf48e87 | -11.8291 | -51.7937 | 2026-08-16 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| f8f038dd-7944-3093-be93-74ee48945d48 | -18.3114 | -44.5207 | 2026-08-16 13:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 7c9b75b2-384c-327e-80db-1ff05008bc85 | -6.7123 | -58.9412 | 2026-08-16 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5eac5736-b063-39ed-94d3-5c9ba78c0153 | -12.2877 | -45.8635 | 2026-08-16 13:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d05f51e9-4e44-3a12-9e87-5a1457a7fd5e | -14.3726 | -51.9106 | 2026-08-16 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5ff68243-4e41-3939-bc85-0b0bdba6012f | -14.3919 | -51.9081 | 2026-08-16 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 604cbaaa-1bdf-3c74-8a45-d91168aaa8ab | -8.9787 | -60.5156 | 2026-08-16 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| dcff5ee6-dd96-3d02-b120-abc4a294b0a1 | -12.7013 | -48.4974 | 2026-08-16 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 31d3939f-77d5-3884-95b1-d11e56f653d9 | -7.5871 | -60.8845 | 2026-08-16 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 24c63a86-1fc3-3a91-b888-e60a54c91c54 | -8.96 | -60.5358 | 2026-08-16 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 3df0acc4-9c25-36b6-b7e5-34068f1c4622 | -6.1107 | -57.723 | 2026-08-16 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d2fa32fe-0b5f-34db-890b-c7457a5fdca2 | -12.0091 | -46.4498 | 2026-08-16 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c8e901e8-ea34-3140-b682-03d4c844f434 | -15.0682 | -47.0098 | 2026-08-16 13:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6ccf041c-5e06-317b-9608-d916dfcaa17a | -11.08 | -47.2479 | 2026-08-16 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| abdbfdde-6f6b-3500-bc7e-af43676b5212 | -8.9601 | -60.5165 | 2026-08-16 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 4cd27acd-5954-3e43-9fc7-a5b48e7dfd44 | -11.9027 | -45.9654 | 2026-08-16 13:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 18a10c9b-468f-3835-b092-6af7053d778f | -11.8482 | -51.7916 | 2026-08-16 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| bc13479b-2c09-3644-bf09-a71ef81427b9 | -15.2095 | -52.7127 | 2026-08-16 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 34c780b8-e1e7-3417-b0b3-a855840b6590 | -8.96 | -60.5358 | 2026-08-16 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 2e23493a-20da-3bf7-a4e6-62e1a5fa0515 | -12.6828 | -48.4558 | 2026-08-16 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| b364de40-7fad-3e44-8c5e-9f9d2a286421 | -12.7017 | -48.4753 | 2026-08-16 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 228.9 |
| f60027b7-624f-3a35-9c5a-4f5fb778c2c5 | -15.0682 | -47.0098 | 2026-08-16 13:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| c2421d23-9703-3119-8270-d52e88fb1f34 | -11.0609 | -47.2503 | 2026-08-16 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 2feda6d2-316f-3885-b9f2-754e982b88c3 | -6.6198 | -58.9836 | 2026-08-16 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7ccda485-617f-360f-afa5-effb70035cf2 | -6.6014 | -58.9844 | 2026-08-16 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 260622f1-a672-368b-9b4d-7b6474d9da3e | -14.4105 | -51.9482 | 2026-08-16 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 847c88f2-8163-3d58-91fa-60c7f8d1060e | -6.11 | -45.3298 | 2026-08-16 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 36355693-51f4-36e0-bddc-0868393806e3 | -11.8291 | -51.7937 | 2026-08-16 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 190.6 |


[Clique aqui para ver as próximas entradas](README62.md)
