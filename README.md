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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45055f50-ada1-3b62-9b3e-162fd70ea484 | -11.0345 | -46.5143 | 2026-05-11 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 820c0972-0176-3f1e-af8e-241c695f6a42 | 3.4377 | -60.9487 | 2026-05-11 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 688df3fe-4b53-36fe-bc1a-2e6adad8a3ee | -11.0536 | -46.5118 | 2026-05-11 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 63533b48-094b-3d55-818b-d1d8ece41d7f | 3.4377 | -60.9487 | 2026-05-11 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3384ea66-a30d-33c9-922c-12bf74218236 | -11.0345 | -46.5143 | 2026-05-11 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| fc08867a-9300-379f-af2d-933ebf7a1caf | -11.0154 | -46.5168 | 2026-05-11 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e431d850-ee2d-3007-99ed-80f1ac9ece48 | -9.4621 | -47.7888 | 2026-05-11 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4687e6a2-c56d-39b4-8701-1e3a7596f059 | -9.4486 | -47.772202 | 2026-05-11 00:22:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98ee6622-c558-3e65-90bf-d462b2060f59 | 3.435 | -60.9272 | 2026-05-11 00:22:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 905410b9-fcf3-3561-b8e8-075988eba087 | -9.4529 | -47.790298 | 2026-05-11 00:22:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6e4804f-2f48-34f9-aae0-98d455024b05 | -10.5485 | -56.310699 | 2026-05-11 00:22:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1127e460-afc6-3ad8-964f-98139c55f357 | -9.4606 | -47.778999 | 2026-05-11 00:22:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27923e75-8d51-364e-8f52-d14e81f47d80 | -9.4508 | -47.7813 | 2026-05-11 00:22:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0bdc6b3-ce98-3cf4-97a1-051b2c802c9f | -10.5582 | -56.308601 | 2026-05-11 00:22:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd1b04e-2bf6-30b7-9c82-a390c8835f96 | -9.4621 | -47.7888 | 2026-05-11 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5a85ce47-7584-3b20-a8ed-968f666660fb | -9.4553 | -47.79239 | 2026-05-11 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a616ebfb-9404-3d53-b130-3cf91b60c030 | -11.05191 | -46.52639 | 2026-05-11 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ea53fec7-846d-3faf-8cfd-100972c99c64 | -13.1776 | -52.69837 | 2026-05-11 00:33:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 642b9742-2dac-372a-84c5-0cbd67496baf | -11.05564 | -46.53137 | 2026-05-11 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 4a012ccf-2378-31b7-a5a8-7a5c66633203 | -16.11072 | -49.23499 | 2026-05-11 00:33:00 | TERRA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 70a33cb4-c30f-31d2-96c4-d8443a90b990 | -16.1083 | -49.22962 | 2026-05-11 00:33:00 | TERRA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b48179b2-7386-3807-95ca-c27137b264f5 | -10.65672 | -49.72629 | 2026-05-11 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2fdaf269-d9f6-3908-9e42-dca3d7b9c28e | -11.0424 | -46.53341 | 2026-05-11 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 057e9995-dab2-3e67-8193-63e450bb6c2e | -9.45822 | -47.81086 | 2026-05-11 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| dc77ca2f-2e84-30a1-9c8c-e36ef677942e | -13.17635 | -52.68935 | 2026-05-11 00:33:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4401cd3a-6680-3876-b2b1-35d8d3b9db83 | -11.01242 | -46.51606 | 2026-05-11 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 5c0a216b-2c00-3722-9715-238f6ca99799 | -12.8316 | -49.7967 | 2026-05-11 00:33:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ae47e9dc-fd68-368e-9b9c-64eca6b91f55 | -10.5595 | -56.3318 | 2026-05-11 00:35:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2676b44d-fbc0-3205-aa8c-b40316137c31 | -10.54572 | -56.32902 | 2026-05-11 00:35:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 2283f518-e79e-3320-9a5a-897c5bb93052 | -10.55536 | -56.32767 | 2026-05-11 00:35:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| b778e1a8-0aa4-3068-b33b-e9ba96942dc7 | 3.43737 | -60.96036 | 2026-05-11 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 89b0feb6-e42b-3a08-a45f-770d905aeb71 | 3.43532 | -60.95423 | 2026-05-11 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 10a75b9e-7d8f-3538-b2e1-47474959c7cd | -10.5529 | -56.326 | 2026-05-11 00:53:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 760d5960-c1b8-3344-a43f-62b13be82bab | -12.8348 | -49.794899 | 2026-05-11 00:53:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e3d99e7-cc55-3278-b196-9b4d9878bad0 | -9.455 | -47.787899 | 2026-05-11 00:53:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a695f022-2b13-39d0-90e6-f1e8ad819d0b | -13.1784 | -52.686199 | 2026-05-11 00:53:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 110f9cf4-97e2-3d53-b1b3-a18787b2469f | -11.0269 | -46.5005 | 2026-05-11 00:53:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2059f222-cfff-3d74-b666-1b24a20ae12d | -9.6509 | -42.955101 | 2026-05-11 00:53:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7aeb6fbc-a3aa-3388-b2c4-6f938c17b2ff | -9.453 | -47.779301 | 2026-05-11 00:53:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 642b91e8-efe6-3993-8064-15698c70ace2 | -11.0292 | -46.510101 | 2026-05-11 00:53:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07a4c99c-b78e-3548-9e3d-d817d9e2a82a | -13.1801 | -52.693901 | 2026-05-11 00:53:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1596b3a9-c8e5-3540-ab4a-b3c21e7b6ace | -9.4571 | -47.7966 | 2026-05-11 00:53:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3446bf57-526e-31c0-8b93-844939ff7a02 | -10.5506 | -56.314999 | 2026-05-11 00:53:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff6049b-a721-387f-afe9-fe3ec93c260b | -12.8332 | -49.7878 | 2026-05-11 00:53:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 897de10b-c0e8-3227-bd12-b1531a1ce8f9 | -10.6609 | -49.718601 | 2026-05-11 00:53:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb94d14-b91a-3fb1-8b2a-cdd6913147f4 | -9.4647 | -47.785599 | 2026-05-11 00:53:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7a28342-a582-3438-911f-f0af182178ee | -9.4621 | -47.7888 | 2026-05-11 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a0937b69-a497-3ed3-b88b-74fb132ad979 | -9.4621 | -47.7888 | 2026-05-11 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 8071050a-b7bd-3788-820c-f3dc8d8af32a | -9.4621 | -47.7888 | 2026-05-11 01:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| f049406e-3560-38e8-969c-0c4da29b11fd | -9.4621 | -47.7888 | 2026-05-11 01:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7c3d5347-9d43-37ee-8b1f-1a20aca1fc04 | -9.4621 | -47.7888 | 2026-05-11 02:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e4a2259e-2f4a-34cd-a3ae-46910453a3e2 | -9.4621 | -47.7888 | 2026-05-11 02:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d14aec6d-e7dd-3ac4-961a-3b2f49322192 | -9.4621 | -47.7888 | 2026-05-11 02:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| e3c908c8-467b-33b0-a822-e8d35b8f9da0 | -9.4621 | -47.7888 | 2026-05-11 02:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 5bf78e95-61f4-31cb-ac10-fbbe814153e8 | -11.8425 | -43.96812 | 2026-05-11 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7535c694-b97c-3db6-96fd-4c1b051c1fab | -14.00296 | -42.54196 | 2026-05-11 03:19:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 41bf9b96-f166-3462-8948-77a2503face3 | -11.84696 | -43.96958 | 2026-05-11 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 50454235-1c20-3aa0-b1bc-8a6a4510bca0 | -14.0013 | -42.53848 | 2026-05-11 03:19:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fc31a5a8-d1fb-314f-a39b-9a997bc94995 | -20.34836 | -40.94632 | 2026-05-11 03:21:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3ad87815-13f2-3c90-af39-4171582267c4 | -20.34779 | -40.94904 | 2026-05-11 03:21:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 998b424e-49b0-3fc5-9311-a3c78567f3c9 | -20.34722 | -40.95175 | 2026-05-11 03:21:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3108daa8-0a8c-31a3-88af-2bcfc7789e70 | -20.34896 | -40.94349 | 2026-05-11 03:21:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0f6380b9-5b9b-3227-b33b-6532e320d6c1 | -11.05382 | -46.52672 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a603abd3-e244-3dcf-8b6d-4066b28d6a2d | -11.05233 | -46.53453 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 907a8368-f5a5-3b0a-b819-3c95fc22932a | -12.50568 | -41.59781 | 2026-05-11 03:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 315e0ac3-5201-3105-9422-cce0d81f0c53 | -11.03691 | -46.52366 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba85f7e2-3f19-3b67-bd6a-05ecf1de5b34 | -12.50809 | -41.59643 | 2026-05-11 03:51:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a73016fc-6a57-35e0-abe9-73a692a10043 | -9.64626 | -42.97005 | 2026-05-11 03:51:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3ef16ff-beae-3617-8dea-201f41d302e0 | -11.05558 | -46.52958 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70c0fc4f-81b4-389d-bc2b-6b8c502f33ab | -11.04431 | -46.52754 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93e7410e-15b4-370f-b81a-15377371adb3 | -10.93146 | -44.17495 | 2026-05-11 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 690bba32-4b4e-3369-aa17-91aaaf1d275f | -11.03129 | -46.52255 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8977a91d-bd79-3ff3-8a62-27dff79f0a3e | -11.04254 | -46.52473 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 513a515e-bb80-369b-81d5-841372ab79d1 | -9.64708 | -42.9654 | 2026-05-11 03:51:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71cc747d-e206-3bde-9b38-255d8065f6b1 | -11.06288 | -46.52214 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd89a242-2517-3969-8718-492d18c9c32b | -14.14096 | -41.64075 | 2026-05-11 03:51:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f2ca97ca-1df2-35cb-a61a-d782ceb43011 | -11.06027 | -46.52345 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 343bc4b7-362b-3b17-87db-bee0f8a08770 | -11.84288 | -43.96963 | 2026-05-11 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c22219b4-637d-3c89-b806-c0bc5d521b61 | -11.8438 | -43.9646 | 2026-05-11 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9a7d785-331d-3416-aa1e-f311a8e800db | -11.05945 | -46.52774 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2d63005-7a6f-306b-9c15-a7b440490122 | -11.03767 | -46.51967 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33613420-678e-330f-bcef-0fe98d9f3462 | -11.04918 | -46.53241 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ec1b036-8ae8-3a6c-9a5f-4ad4716f10ff | -11.04995 | -46.52855 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3e266a2-ecfe-3c70-ac91-bc2e0e3db71d | -11.05869 | -46.53176 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c076a7c3-1bc9-36df-b7c0-04ae5f953a08 | -11.03205 | -46.51857 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ac06a0c-96c0-3e5b-8778-78586b649d12 | -11.05306 | -46.53072 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 610bf17c-6fae-3f49-b394-a1e9ce44594f | -11.04329 | -46.52078 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f01ea81-e175-3a57-9e2e-e6277c669777 | -11.0564 | -46.52545 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 760e4bcb-4e67-355e-821e-f2745fc4236a | -11.04742 | -46.52968 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 021b7c47-831e-3e00-96d7-6e81eaf9eafb | -14.00267 | -42.54052 | 2026-05-11 03:51:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 01e0077a-af77-3335-8bba-925388448f7d | -11.52611 | -43.33311 | 2026-05-11 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98585d46-3edb-3701-b601-94e1cb7618d4 | -11.05482 | -46.53344 | 2026-05-11 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f7fa32a-8ba1-390e-91a4-28bcc32b27c8 | -10.92664 | -44.174 | 2026-05-11 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aec4d8cb-e5c2-3cf5-9d08-55f3e008e11f | -20.35021 | -40.94262 | 2026-05-11 03:53:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3f1febd5-3920-3464-ac00-bef348586214 | -18.35208 | -43.30447 | 2026-05-11 03:53:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0b9e664f-e9bc-36a8-bb95-5c44884a6394 | -19.41718 | -44.3426 | 2026-05-11 03:53:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccf2b849-7c23-390b-a20b-fb351bfe3cbb | -16.98989 | -46.54361 | 2026-05-11 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a7ee267-6670-378f-8fa0-cedc63c5a747 | -18.34338 | -43.30664 | 2026-05-11 03:53:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9994cde-e0fc-3b46-80c0-41d3c2e77831 | -20.34606 | -40.94592 | 2026-05-11 03:53:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 534d5ad7-d575-38ac-8ada-b3d395a6a45b | -16.98888 | -46.53986 | 2026-05-11 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README2.md)
