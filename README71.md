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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5de2f729-3c4b-344b-ab76-8841263c37e7 | -7.50024 | -55.02096 | 2026-09-28 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fa327fd5-0a6c-3f00-861a-b8cb055af56e | -1.23298 | -54.10337 | 2026-09-28 12:21:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| de07f42c-ad53-332a-9789-d0d57fc16da1 | -10.81205 | -48.72147 | 2026-09-28 12:23:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c4e81cc7-ee2f-3325-b9c3-5dfbb955d99b | -11.21913 | -54.09072 | 2026-09-28 12:23:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| c1266d66-bc33-3f33-a9dc-73ded7da3ef9 | -11.39028 | -54.42967 | 2026-09-28 12:23:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f091e5e4-e033-3c6c-bf3a-c7f00bc25f9f | -15.20544 | -50.26037 | 2026-09-28 12:23:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| e1b0a03e-20c3-3081-b108-fab4aa0ae35c | -11.12849 | -50.06246 | 2026-09-28 12:23:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| ceaa225e-9def-3cfe-bb2a-915c084085a8 | -12.39761 | -58.03593 | 2026-09-28 12:23:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0e98044d-b9fe-3dc6-8fe6-2b35bc7d1163 | -15.20838 | -50.23127 | 2026-09-28 12:23:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 5f5d68af-e0fe-38f0-95d5-2e39de767b6b | -13.16869 | -48.53752 | 2026-09-28 12:23:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 9bb13d33-795e-3665-8b97-9116de5d0b84 | -12.28142 | -50.16077 | 2026-09-28 12:23:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 7e2ef2e5-8b2f-36a5-a5f9-9303b1f6f206 | -11.14043 | -50.05723 | 2026-09-28 12:23:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 37d9b531-b13b-3339-b1e1-11e151765d77 | -9.93657 | -60.71618 | 2026-09-28 12:23:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b3d3cdc4-1d23-3733-9c29-8ce0ab09eda5 | -10.8176 | -60.7324 | 2026-09-28 12:23:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 732233ce-c7f8-31bc-8644-eae4d08b9cd1 | -10.94644 | -50.67575 | 2026-09-28 12:23:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| aa53f93f-58f1-352e-9272-a481fac90d25 | -10.80591 | -48.72569 | 2026-09-28 12:23:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 282558b2-d832-3f3c-8188-21e142b31ef2 | -10.82426 | -57.23346 | 2026-09-28 12:23:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 68cd430f-58cb-3438-a1eb-b4cb130a6bdf | -10.89551 | -50.68625 | 2026-09-28 12:23:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 12550040-9e17-397c-8324-1d57e3e97046 | -11.27729 | -54.4332 | 2026-09-28 12:23:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d3c1a36b-6c9c-3c2b-aa10-0262e17cd9da | -10.80829 | -48.75425 | 2026-09-28 12:23:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 57ae3bff-55c6-35b1-a367-5f9dff65186c | -11.22077 | -54.07789 | 2026-09-28 12:23:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 2a557930-f244-39b4-b345-e63b0dce630c | -9.08848 | -61.43779 | 2026-09-28 12:23:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9667f2a2-e9ea-394b-9fa0-54223c27dfa9 | -9.17516 | -61.40514 | 2026-09-28 12:23:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 9fdde2f3-631e-38b7-9ff8-3c5e1451ec47 | -12.14168 | -57.23705 | 2026-09-28 12:23:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 632239eb-eb9c-3e8c-a25e-5d0f0e9a237d | -15.2066 | -50.25508 | 2026-09-28 12:23:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 9eabea65-6c28-3239-9c1a-1b47f22ab61f | -15.09579 | -54.71102 | 2026-09-28 12:23:00 | TERRA_M-T | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| dde9e1bd-9320-3d61-95c7-19c40786aa61 | -12.05448 | -54.01489 | 2026-09-28 12:23:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 218e52c3-22e8-33d2-a272-60d2bcb84ad0 | -12.44744 | -58.41206 | 2026-09-28 12:23:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac5f1ce9-bb07-3218-bec6-0ab9cab179dd | -10.41632 | -53.82677 | 2026-09-28 12:23:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 214f513f-204f-32fe-a121-27d973b08a4d | -11.78085 | -54.25221 | 2026-09-28 12:23:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3477a165-1efa-37bc-b174-abc53f413593 | -13.16529 | -48.57002 | 2026-09-28 12:23:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 6526d64b-fd49-3b92-b3b8-3b63610fdf8f | -12.06511 | -54.01624 | 2026-09-28 12:23:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b040bff8-0934-3754-ab38-c5c9dcc9529f | -12.88026 | -58.28018 | 2026-09-28 12:23:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 94cefc77-ae1c-33a7-95b4-85ae7b89399e | -11.40912 | -57.85292 | 2026-09-28 12:23:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d30dd16f-eb9e-32da-b7f1-c82d004d3027 | -10.81592 | -60.74331 | 2026-09-28 12:23:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| b5bb5187-e7ee-3dd8-bf18-3d61f48e59be | -9.98119 | -50.13073 | 2026-09-28 12:23:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 76c2698d-366a-3707-998a-f3fef113724f | -10.94922 | -50.6526 | 2026-09-28 12:23:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 2b4228a4-9d02-31cd-b8e6-39b35722b8cc | -10.20864 | -49.99197 | 2026-09-28 12:23:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 45231e0b-ce13-394d-a41b-c499d10149ae | -10.51264 | -53.5003 | 2026-09-28 12:23:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 05905c2b-76fe-334a-9fd3-161596b5edd1 | -9.08654 | -61.4505 | 2026-09-28 12:23:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0910fabd-3ed6-3052-b74a-5cc7d148386b | -11.78251 | -54.23944 | 2026-09-28 12:23:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e2c8465b-26af-3f5a-a15b-d30e86f2d0c4 | -9.97827 | -50.15531 | 2026-09-28 12:23:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d08d38eb-6dcb-31e1-9a5a-0a0232379c2a | -10.82552 | -57.22447 | 2026-09-28 12:23:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ac908629-00ec-3360-982e-e284fe3e897e | -10.21194 | -49.99918 | 2026-09-28 12:23:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 36312d36-4f3a-34a8-9661-7af8eff2e558 | -9.16476 | -61.40354 | 2026-09-28 12:23:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6f4fea4c-fa07-328a-a88e-817017b37630 | -17.88544 | -50.77999 | 2026-09-28 12:25:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 3f5c1942-8468-3711-bd87-d26bb226f0ca | -15.29461 | -56.66917 | 2026-09-28 12:25:00 | TERRA_M-T | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 86a61b37-1637-31ba-b6bc-bbda1a5870a2 | -18.72304 | -49.10581 | 2026-09-28 12:25:00 | TERRA_M-T | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 9a96ff3d-af7e-3fdc-9a53-d9a75c77438b | -18.71973 | -49.14627 | 2026-09-28 12:25:00 | TERRA_M-T | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 34186dab-218e-3e35-b235-dd6db208afa7 | -16.689 | -50.66699 | 2026-09-28 12:25:00 | TERRA_M-T | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 9a6112d7-a898-3f5f-8c72-de1e4f4793a9 | -15.43569 | -56.06582 | 2026-09-28 12:25:00 | TERRA_M-T | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bd2be4af-dff4-3c01-a129-29a5a6905292 | -18.71626 | -49.14086 | 2026-09-28 12:25:00 | TERRA_M-T | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 600a2b45-f3e3-352e-b543-854def3dfe8a | -16.68869 | -50.67366 | 2026-09-28 12:25:00 | TERRA_M-T | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c77fcff8-577b-302f-9d4f-3c7cfad7ec40 | -17.88467 | -50.78555 | 2026-09-28 12:25:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| a6dca296-8b91-31af-bb21-f6e8d38e981a | -15.29598 | -56.65879 | 2026-09-28 12:25:00 | TERRA_M-T | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2abcf71b-704a-3ff8-ae3a-99bfbbc9b8c7 | -12.7028 | -47.3189 | 2026-09-28 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| d89ca6bc-1408-3646-8401-b162fe37f1ff | -12.6832 | -47.3442 | 2026-09-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 288.9 |
| 6c773a5a-da1c-324c-9ef8-5e8e9c3a683b | -12.6836 | -47.3217 | 2026-09-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 4e01c28b-14e8-3b18-a7fd-e2364155a0b5 | -13.161 | -48.5437 | 2026-09-28 12:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2f87b38b-959f-3b78-9883-c3282b7aac56 | -9.9781 | -50.1626 | 2026-09-28 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 77692fc1-f142-33a7-a795-b987295eb2ec | -8.2293 | -45.4375 | 2026-09-28 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 438b66d2-2134-3251-bf06-a24c3ac8ef46 | -10.8967 | -50.6866 | 2026-09-28 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 2c197516-f2d7-32fd-a4bd-17d34fefd8f9 | -8.0361 | -42.8187 | 2026-09-28 12:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 116.9 |
| b9580e77-eddb-33b3-bbb3-127eaae4b4d3 | -11.4425 | -44.9303 | 2026-09-28 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 70bc1ab2-1517-3148-b70b-85c1ff1411e8 | -16.6932 | -50.6608 | 2026-09-28 12:30:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 98501d7e-ec40-3a6e-b43d-ced1cc0d9b61 | -8.2859 | -45.4317 | 2026-09-28 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b21316d5-a488-35fb-b69b-b0b8788d7dd5 | -8.0358 | -42.8423 | 2026-09-28 12:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| dfed2683-0b1a-3a3b-9fb1-19ef2c35f609 | -11.1327 | -50.0624 | 2026-09-28 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 58eaa35c-7807-35b3-8ce9-5b31a5dca81a | -11.4616 | -44.9276 | 2026-09-28 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| d1f60134-c4b3-39e8-88bb-f5eddaa84866 | -8.4438 | -44.8683 | 2026-09-28 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 3e31dd4f-a413-3f57-b356-b72e98ee1aea | -8.2291 | -45.4602 | 2026-09-28 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 548f35c3-3b88-339b-a800-145631c832cb | -9.9396 | -50.2304 | 2026-09-28 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f4071c3e-c7c9-3948-8b66-50e1507d74e4 | -10.9346 | -50.6825 | 2026-09-28 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| bdf23c74-bb60-32ab-91cf-425b79f033e0 | -10.9349 | -50.6612 | 2026-09-28 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 0661f0a6-6815-33ab-8237-fe512ce22fe5 | -8.2862 | -45.409 | 2026-09-28 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| af58e8d9-4663-399b-8627-1d543eac24c2 | -8.6631 | -45.4152 | 2026-09-28 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 2e1b0d96-fb4e-3435-accc-54baf8d9e9e4 | -11.8641 | -47.1004 | 2026-09-28 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| cb77ae9a-a7c1-37d9-9e00-e5dfbd8fabdc | -12.6263 | -47.3075 | 2026-09-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| e0f036c8-4c7d-3add-988b-e1facea4fea2 | -8.3608 | -45.4695 | 2026-09-28 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 2fc8efbf-b233-3e0d-9301-3e3d9d79d601 | -8.3666 | -46.5263 | 2026-09-28 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a95ec5e3-642b-3847-9262-545f8524a838 | -10.9156 | -50.6845 | 2026-09-28 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0eddb464-7798-36ce-86c1-7c6b66d131b2 | -12.7417 | -47.2909 | 2026-09-28 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| bc2de10c-979f-3b3b-9e0b-1a81387f7348 | -8.3617 | -45.4013 | 2026-09-28 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 191e3a54-12d2-3f11-9d87-6587db52cf7b | -9.9784 | -50.1412 | 2026-09-28 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 224927b2-3727-3baf-b070-7c983a74edc6 | -12.7024 | -47.3414 | 2026-09-28 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 3873d6df-f29c-3e86-be7a-9ef4f608cf8b | -12.6878 | -45.0192 | 2026-09-28 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| d9caf53c-07f9-3b11-a623-f90fd66936c1 | -12.6643 | -47.3245 | 2026-09-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| cf1993ef-e6a2-3392-a563-ef39e959bd6b | -7.4869 | -44.5751 | 2026-09-28 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 7e4348c7-8586-33d1-aa2c-d23e7891c04a | -11.4425 | -44.9303 | 2026-09-28 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 1d78dd2a-f662-32ee-b28f-658529b53404 | -8.4249 | -44.8703 | 2026-09-28 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 135.8 |
| f2e29325-34dc-3649-b597-1b6906994a90 | -9.9976 | -50.1179 | 2026-09-28 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0908ce5d-42ec-3ef2-99fe-07c6ed091d01 | -12.6832 | -47.3442 | 2026-09-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 361.1 |
| dfdfb8de-2171-33c1-9dd2-9d5cbea018d5 | -12.6836 | -47.3217 | 2026-09-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 209.2 |
| b076f531-e0db-3ba1-81cc-2f3950801d78 | -12.2897 | -50.2712 | 2026-09-28 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 206.4 |
| d3f8c194-340e-3183-b072-ef9ec2b9f6e9 | -8.4438 | -44.8683 | 2026-09-28 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 3e349270-8569-32be-8b1b-c06903b4ff09 | -12.3088 | -50.2688 | 2026-09-28 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 14c7374c-87a9-3dc9-997d-55c2b0aaff8a | -8.2862 | -45.409 | 2026-09-28 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 5541379d-cb66-371a-bf94-ebc43d65e656 | -16.6932 | -50.6608 | 2026-09-28 12:40:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 356d9f05-3601-3818-9706-eb7eda9c6442 | -12.6878 | -45.0192 | 2026-09-28 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| f658e43f-9e5c-3acd-aba2-36229b4d4898 | -11.4616 | -44.9276 | 2026-09-28 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 183.2 |


[Clique aqui para ver as próximas entradas](README72.md)
