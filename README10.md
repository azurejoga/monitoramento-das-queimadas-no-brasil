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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7df816c2-8088-3446-84f4-92b83c2d0d5e | -20.51336 | -54.72403 | 2025-07-21 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 34fba427-90e3-3152-86c0-ece978de625a | -20.27395 | -54.80713 | 2025-07-21 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5923ca1-0672-379c-87e7-c95e0465668b | -19.01676 | -54.65713 | 2025-07-21 04:23:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a74c0466-5316-3ae6-a25b-d3dacd5bef42 | -20.26619 | -54.80037 | 2025-07-21 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0cb60ba-deee-3b01-8dd0-e0329eff0b1b | -23.57524 | -47.19129 | 2025-07-21 04:23:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ae9a5562-15ca-3dba-8dc8-ac6185216f4b | -23.43535 | -47.42785 | 2025-07-21 04:23:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f78cfdd4-8951-34ae-8cab-8d87adf993ca | -21.90362 | -47.60567 | 2025-07-21 04:23:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cea9eb6-b3c0-321c-a5f6-9aa4176bb637 | -21.25763 | -47.50401 | 2025-07-21 04:23:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63a97364-5057-3275-a307-aa97ff0d284e | -24.54648 | -50.79666 | 2025-07-21 04:23:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b11c4f61-4532-3677-9ea1-46958236298f | -20.19299 | -50.49529 | 2025-07-21 04:23:00 | NOAA-20 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6200c975-eb3c-3387-b5be-ecc289218ea6 | -28.90769 | -49.96416 | 2025-07-21 04:25:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ac6bd07-d927-37a4-924c-418384262161 | -28.90709 | -49.9681 | 2025-07-21 04:25:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4fa03998-21b9-3631-8c65-4ba392d4fb38 | -7.2957 | -60.169 | 2025-07-21 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 7ff209a0-0e84-34dd-8476-5604feb46b0c | -7.2772 | -60.1698 | 2025-07-21 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9e2fed9c-da4f-3962-b290-a6e55a2c68f2 | -7.2402 | -60.1904 | 2025-07-21 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 615c6a9c-dc77-36ec-bce1-81dbd666c284 | -7.2772 | -60.1698 | 2025-07-21 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 79872fc2-3b72-3d10-9695-32fc83b41d28 | -7.2957 | -60.169 | 2025-07-21 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| eb1f9584-1970-3256-bf41-ef01d14664cd | -7.2772 | -60.1698 | 2025-07-21 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e049b5a4-74c4-3533-b496-d78938514729 | -7.2957 | -60.169 | 2025-07-21 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f04629d6-6a6a-3212-bd43-5a56dfac6367 | -7.2402 | -60.1904 | 2025-07-21 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 415b3820-7381-3de4-a1a8-4957033b15cc | -10.6693 | -46.7628 | 2025-07-21 05:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 754816bd-27ff-3489-be77-d62a43092a85 | -10.6689 | -46.7853 | 2025-07-21 05:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| a51f0f6b-1349-3238-9f45-1496d0132137 | -7.2402 | -60.1904 | 2025-07-21 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c3f50330-8ef1-3ec7-8fe0-47d6b38f7032 | -7.2772 | -60.1698 | 2025-07-21 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 2f64a9ec-a9cf-3908-886a-91b372e8cbd0 | -7.2772 | -60.1698 | 2025-07-21 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 39d16aef-d783-3fb9-a732-0a2c11d7527d | -10.6693 | -46.7628 | 2025-07-21 05:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 995892c1-1d5f-333f-a28d-ebfca7099707 | -3.14253 | -47.01307 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ec1c440-5fd0-3b67-8376-8c7882997d83 | -5.26384 | -44.87067 | 2025-07-21 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59d73768-a233-3146-9b2b-d674854f2cc5 | -8.27337 | -46.07113 | 2025-07-21 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2cd8309-b8e6-3e70-a979-63f099af7906 | -5.79752 | -46.10263 | 2025-07-21 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0df65634-a3f1-3b7e-8e7d-1e6676d8e81e | -7.7074 | -47.29431 | 2025-07-21 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b5af448-e7c0-34cc-8d24-338c914436fb | -3.58718 | -47.52138 | 2025-07-21 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 320d51d2-0649-3150-b6a4-7a31d1c7c6de | -6.25879 | -55.76298 | 2025-07-21 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 920136f9-485b-3bc1-bc69-d522beaf6143 | -3.50466 | -49.04897 | 2025-07-21 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f46e15e-b9e3-314c-ad6b-54e409de6adf | -3.13248 | -47.01278 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38b5cc5f-9c54-3a4b-80c6-2d766283be7b | -5.09164 | -48.4245 | 2025-07-21 05:10:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 347fe686-8fbb-3969-a9fd-9909fc217d63 | -8.27706 | -46.07233 | 2025-07-21 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ee94206-75cd-3fdf-b780-d7afe500083e | -3.10963 | -47.01309 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 349358bc-a479-3c6f-8898-c8ce0e3d58d4 | -7.70794 | -47.29344 | 2025-07-21 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 855b989b-7032-365e-a68f-663debc268f5 | -3.0367 | -47.86288 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 815ec4a0-c38d-36fa-8f89-1051d06370c8 | -7.70849 | -47.28938 | 2025-07-21 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8ca3da2-574a-318e-bb8c-695464583b46 | -7.70792 | -47.29023 | 2025-07-21 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 204c3186-dad9-33eb-bf04-d03a4e5856a5 | -3.13696 | -47.01214 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7a54ba7-26c0-3c36-bc65-725b3d9b42b2 | -5.3047 | -55.97258 | 2025-07-21 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55b5341e-0639-331e-ae96-12eaffd02b83 | -3.50387 | -49.05444 | 2025-07-21 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73c56538-93d9-3eeb-9fc7-f05966b26b7b | -3.13139 | -47.01125 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f134c50c-a018-3437-a08f-1131553fcea7 | -3.03717 | -47.85965 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aab3061e-c6d0-313b-b8dd-89d7160acb08 | -3.5926 | -47.52218 | 2025-07-21 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43938daa-71f5-3b15-b514-30a8fa75b708 | -3.71428 | -49.07004 | 2025-07-21 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f488147f-557c-3c85-b011-4f59cab9f230 | -8.26071 | -46.06889 | 2025-07-21 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce4d3efd-718d-39df-853e-8239f730b390 | -3.04149 | -47.86688 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 95f20f6e-acbf-342d-845c-cbcdb13263b7 | -5.09221 | -48.42455 | 2025-07-21 05:10:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6b0f1f2-066e-34f7-93d2-6b8ab126a94c | -3.13805 | -47.01365 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de9e05d8-16ac-36f6-b8d9-486bf155719b | -5.32784 | -50.57727 | 2025-07-21 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6826cce6-7a86-32b1-baf6-f416f02732c4 | -8.26431 | -46.07087 | 2025-07-21 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7773413-f9b2-3231-ba62-33ac92a4938c | -3.83669 | -49.15865 | 2025-07-21 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1529bb4-ce13-3fd5-bb78-7ec02cbf9b73 | -7.10302 | -51.60041 | 2025-07-21 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbb06517-2b15-3cf9-b950-cc304595df3c | -3.11521 | -47.01393 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63874fcc-64ec-31ed-938f-6cc6d7677798 | -8.26702 | -46.0702 | 2025-07-21 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e4e90bf-b7f6-3f0c-b37c-576414c4f13a | -3.04195 | -47.86374 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 22532d8c-2dc3-35ef-96ca-f3d2c2e47019 | -3.12691 | -47.0119 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32ec063d-61c1-38e5-a9c6-eabf76b3022f | -3.04242 | -47.86053 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb203cdc-94ff-3c19-b036-e39baa6170c9 | -3.03624 | -47.86601 | 2025-07-21 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9f0933e-da52-316e-b858-6873f73db70a | -5.27903 | -44.9476 | 2025-07-21 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59333764-e110-39fc-97e1-9ad5040a736b | -8.27139 | -46.06618 | 2025-07-21 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b3fa81d-b732-35b4-8c28-c39c9f7429f6 | -7.25561 | -60.18729 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 083d8bfd-a03f-358f-ac48-bb5bacef92b7 | -7.26344 | -60.11707 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d16b1e0-ce6e-31a5-a5bb-1bd62ed87599 | -10.38195 | -62.76772 | 2025-07-21 05:12:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a4626bb-b71b-336e-b54e-ed6b4f8c5aed | -9.00985 | -59.7642 | 2025-07-21 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caa5684a-3684-3baa-956a-4777efb67916 | -7.28663 | -60.17239 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b669263d-7cfa-32c2-905b-d244fc38ea7f | -12.27468 | -57.36082 | 2025-07-21 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d443aae1-1879-3740-b832-3a9e5d8be8f4 | -7.23754 | -60.18837 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6f22fc82-b5ce-3885-a7f8-ce73baa01187 | -11.80858 | -56.96379 | 2025-07-21 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2ccdc3cd-b989-3ac5-912b-37b22de89f6a | -12.57859 | -56.96816 | 2025-07-21 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f778aae0-3675-32c7-a9a3-91c7e763e5be | -11.78271 | -46.45683 | 2025-07-21 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39592dfa-5be8-30d2-b12f-d8df3f2cce59 | -10.66194 | -46.78272 | 2025-07-21 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 60c7adac-9a54-3b4c-9928-b73622497052 | -13.46056 | -48.01681 | 2025-07-21 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f949250-2f24-3a59-84ea-0c5a4149278e | -8.96915 | -61.50549 | 2025-07-21 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cfce355-3c50-3128-97b6-398ca10fcf95 | -10.38278 | -49.93097 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df7e0888-3de2-32de-b4b3-072a81248336 | -7.2591 | -60.18783 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce1c0f6d-a226-3e4d-bb52-42013891ece4 | -7.27082 | -60.18176 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee5ff298-6ca4-34d7-b172-3cea9b97c26f | -10.13274 | -49.66157 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ed0f518-08cb-3f8b-9ba5-8139428887f1 | -12.58031 | -56.98009 | 2025-07-21 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02c3ccab-e9e5-38f2-8836-be9b7a9277d4 | -7.27493 | -60.17847 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8275a3aa-e273-38f5-afd8-4c8c300cfe39 | -9.01826 | -59.53821 | 2025-07-21 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e422991c-b349-33ad-9bc7-210ecb22c873 | -7.26754 | -60.11381 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54949eee-097d-37b1-8df9-c8e1646e6e6b | -10.13872 | -49.65602 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a0fec7e6-292a-3803-9224-d89df596d8de | -7.16888 | -59.63716 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a993066-a60d-379c-8c4f-9a6dfa1812cc | -11.78728 | -47.55174 | 2025-07-21 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab6c9fba-f1fe-370a-99d0-6b64c8ebb940 | -9.63107 | -61.45651 | 2025-07-21 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0ab3234-1aa3-35f8-8367-ab386caaec1b | -10.73097 | -52.5182 | 2025-07-21 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 476267a7-4b10-3562-bf87-e07f78af1241 | -10.84875 | -47.15528 | 2025-07-21 05:12:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63d19823-455b-3e75-948c-0840d66a04ef | -10.68193 | -46.7753 | 2025-07-21 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32aac917-306a-3084-8795-686a5d1031dc | -7.2743 | -60.18233 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4db2bf28-4ec3-366d-96bb-3a391378be5a | -13.89643 | -48.73434 | 2025-07-21 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6cfc60f6-c4b0-3bce-b51b-0c92452c63a0 | -12.46995 | -46.92155 | 2025-07-21 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e079dbbd-18fa-3898-83ae-6bdc20f82a6a | -10.73525 | -52.51886 | 2025-07-21 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e11b7227-7782-3d62-8f51-82de10c945b1 | -11.14767 | -51.93536 | 2025-07-21 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 722cacd0-a384-3ed8-9814-953892482e4c | -8.49539 | -64.03732 | 2025-07-21 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa351438-db28-34d3-bdb0-46219d55f62d | -8.91756 | -47.36108 | 2025-07-21 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README11.md)
