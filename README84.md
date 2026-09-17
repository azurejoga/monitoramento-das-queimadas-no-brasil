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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa6c49a4-0f2f-327b-997e-1b7ee78b8b29 | -12.54424 | -50.74732 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| adfc674a-99a9-365b-ad41-4f13bdd5f531 | -7.0055 | -43.63671 | 2026-09-17 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 240.6 |
| 7cc1f3b9-1c54-3920-95c1-abe31f1b283c | -7.01997 | -44.64978 | 2026-09-17 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 7c4b7fcb-4cd6-3444-a6db-5b9b0cab22dd | -12.46764 | -50.75579 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2d131426-23a6-3be6-a49a-bc276a72a57e | -8.47856 | -46.89044 | 2026-09-17 11:47:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 252fea70-297f-35ed-920f-33de9c85260f | -12.50813 | -50.86306 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9ffaed59-ad3b-3a3a-b8f7-71d33d3385cc | -8.87956 | -45.85863 | 2026-09-17 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 60e31090-a811-3bd8-b7cc-f8435598ae7e | -8.56519 | -44.47332 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7f5c953-b095-3d89-aa0f-83417fb83cfd | -10.91604 | -46.30846 | 2026-09-17 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| f6e86a34-0274-314b-92b9-ba9028577552 | -10.83513 | -46.15501 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8538404e-9247-3573-a855-cb2f9868b5a8 | -8.28552 | -45.63136 | 2026-09-17 11:47:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c77b9bc6-06a6-3b22-ac0c-7d1133f5affe | -9.75744 | -46.10099 | 2026-09-17 11:47:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c0f3f969-fbcd-30a9-b8bf-f9be52158cf6 | -9.83705 | -48.36559 | 2026-09-17 11:47:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5feee372-fc8b-38a9-9e56-7c11a7face6c | -11.90207 | -47.58178 | 2026-09-17 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b07be5d6-8088-3757-b3c3-467439e74b5d | -11.89049 | -47.59912 | 2026-09-17 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3898396d-70c6-3d95-92ff-9eb63698496a | -10.8003 | -50.85223 | 2026-09-17 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 05ae7d7e-c897-3af4-9160-dc29841625ca | -12.48606 | -50.75859 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f391742a-30aa-3777-bf9e-cb834c724e98 | -9.91269 | -46.51814 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| fcfb5234-4f8e-3b1f-a4e0-6b686d37f9dc | -11.59298 | -46.88545 | 2026-09-17 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 41332282-d575-338a-9774-0c29ff785aab | -7.37054 | -44.47622 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 22455822-79e6-3f80-baf4-03ac44284fc9 | -12.3528 | -50.85744 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5228e6c7-bda9-3393-84d3-d83825a76d41 | -10.83376 | -46.1653 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 0b880021-00e8-399b-84f1-de2e7154b6a5 | -11.88613 | -50.07858 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bc1f9ee3-d371-360f-9928-517f3b42f2ff | -12.14868 | -48.25702 | 2026-09-17 11:47:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dcca90f4-6ca1-31d1-b978-730ca0112b7c | -10.82432 | -46.16396 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ba99c6e8-5f65-3d67-878b-3844dd25ea6f | -8.52052 | -44.51006 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 53eebce1-3448-3936-bf02-b557edbfd4dd | -12.51482 | -45.24926 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e2980fa7-eb93-377f-bda9-bbe2746377ca | -8.583 | -44.57415 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5c9e23d1-98a5-3795-8271-b917c6748565 | -9.87614 | -48.3594 | 2026-09-17 11:47:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| bf385f1f-8e72-3f58-8d30-66ceb231d9f6 | -12.44082 | -48.48 | 2026-09-17 11:47:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 60707e14-96d3-396f-b5d6-d152a634db54 | -7.36051 | -44.47474 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f7d30930-58da-3542-ba05-ea2a485cfc0e | -12.40008 | -50.77932 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 78ac6df1-2c16-3763-a8a7-68a487438272 | -12.36186 | -50.84443 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 60359297-3966-3bac-a08e-5e8c6ec25fca | -12.40157 | -50.76945 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1483eda2-3952-3736-a1ac-4e2287983c98 | -12.35132 | -50.86741 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 130f2d22-a48a-305c-ab33-fe95bc945904 | -9.37955 | -46.84053 | 2026-09-17 11:47:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| e4617a3a-b606-3b37-b56a-18894e1974fe | -9.96372 | -45.32513 | 2026-09-17 11:47:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 940818fc-3b53-3680-a742-d47b674dfce9 | -6.9806 | -43.33227 | 2026-09-17 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| bf329737-de5a-3d19-a5d3-63a7b54c28c7 | -13.2761 | -43.61934 | 2026-09-17 11:47:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9699bf8b-a0a0-32d1-b44d-a778c39a97ac | -6.04155 | -44.0335 | 2026-09-17 11:47:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bfb11ae6-8c6e-322f-85d5-a7d7dd063690 | -12.3202 | -47.95998 | 2026-09-17 11:47:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 97f84016-4075-3c97-be9d-eaf615ba06d6 | -11.32189 | -46.78011 | 2026-09-17 11:47:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 407d1f77-9e6c-396b-995d-d5f80b4be4c6 | -11.88023 | -47.60713 | 2026-09-17 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 41b48561-0447-327f-9c1f-2327576692e0 | -11.89308 | -47.58055 | 2026-09-17 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 56b52edc-193d-3cc6-9d8c-8502adb01686 | -9.92189 | -46.51941 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| db584c18-4fd0-3487-93cd-f664f9617060 | -8.46481 | -44.53988 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 6bf7fdf6-9922-36ec-be4f-7efce23c6d51 | -8.7971 | -46.92176 | 2026-09-17 11:47:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 61a52658-a407-3224-b6f3-4f18741f74a8 | -12.52103 | -50.71371 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| bd877419-4df9-324f-b509-d111269f980a | -7.64579 | -44.33279 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| bae89174-280d-32ad-bd7f-b9b55bcca069 | -10.81283 | -50.83315 | 2026-09-17 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3902b448-84df-30fc-9575-c36e2741c5e4 | -11.40562 | -47.64164 | 2026-09-17 11:47:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1bbbbfc1-7500-36c2-bc3f-feba6a34c3cd | -10.82706 | -46.14335 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 22cd4c0b-21aa-3f72-ac99-595b2d542ca6 | -8.39818 | -47.20342 | 2026-09-17 11:47:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e48661c2-576a-397f-8bd4-5514f021e1a9 | -10.81127 | -50.84339 | 2026-09-17 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| fd7a7165-a463-3840-b4ec-881dbc1f2fd6 | -12.37793 | -48.46454 | 2026-09-17 11:47:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f431126a-5cc9-3a20-9a22-997f319e84bb | -7.07247 | -47.51297 | 2026-09-17 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 01524c97-c65b-3f93-863f-fb1f0f56e14f | -9.75606 | -46.11116 | 2026-09-17 11:47:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d6ad3422-5ecc-3443-810b-2c161f21aba5 | -9.86351 | -48.3848 | 2026-09-17 11:47:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 4a72d894-ece0-300d-8313-56cd701645e7 | -8.47488 | -44.69691 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9f847daa-12ec-384b-8e72-007196321c8c | -7.65164 | -47.85327 | 2026-09-17 11:47:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 25d7ec02-4771-39a6-a64f-3c359c303859 | -9.78694 | -46.09469 | 2026-09-17 11:47:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| eb308581-4cac-375e-9c2d-e68d82c143ae | -6.90844 | -47.43266 | 2026-09-17 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46d92c05-a9b9-3ddf-ae59-1cbf1f04809a | -7.83928 | -44.86009 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8c686263-5aff-3d77-bebc-f3c010b1fa56 | -7.73856 | -44.70228 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3fcefd70-4d4f-3db0-92af-068e10c66fa1 | -6.88907 | -45.46406 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f2a1210f-e973-3195-a24b-a0db9dad374b | -12.35238 | -50.79644 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c8545777-5ce3-39dd-b37e-a67f58848417 | -7.96823 | -44.82067 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5e466b27-1c68-368d-816e-b52cc275f577 | -11.33931 | -47.25705 | 2026-09-17 11:47:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4b84a81f-88f3-3fa9-bc90-69c57ca689c2 | -11.33027 | -47.25583 | 2026-09-17 11:47:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f44932f0-8532-303c-a304-6862f4b12a07 | -10.79936 | -46.16521 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0cc92058-7e75-3ac4-9cf0-916e78133425 | -11.88152 | -47.59786 | 2026-09-17 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| be0245d8-c2c2-3c90-85db-8b0cea8448fc | -10.14813 | -45.39612 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 9bd257d2-1d52-34c8-ba29-a844b0993773 | -9.83078 | -48.34658 | 2026-09-17 11:47:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 5a078696-d5f4-3d96-ad78-6bdefca62a04 | -12.51184 | -50.71231 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| f11b0d20-47d6-35e4-ad07-15eaad54f55f | -7.69174 | -46.71653 | 2026-09-17 11:47:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d2a3c969-fc98-37c0-8ec5-1c004f665d74 | -11.88751 | -50.0692 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 241abf7e-ad70-3be2-bff1-47630067d73d | -7.37165 | -38.99847 | 2026-09-17 11:47:00 | TERRA_M-M | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 36.3 |
| 6bf4aa52-9664-3493-927c-6cb2db2d9cf4 | -7.57329 | -42.6589 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 869be699-b6bd-3a96-9aa4-f8a7cd50df6e | -10.83239 | -46.17554 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| deba03e0-39c1-39d0-8bd1-5fffac4309d4 | -10.60045 | -46.53144 | 2026-09-17 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c9175254-8955-3aa2-9683-05986f40e3c9 | -12.42629 | -50.7934 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ef1cee92-5e1c-3dd6-8954-92a628e542d6 | -12.37921 | -48.45552 | 2026-09-17 11:47:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c510271e-2dde-3430-9441-383bafd2f9da | -9.91404 | -46.5084 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d2228641-ead8-34eb-9704-ed63dcf409ef | -5.81082 | -47.24137 | 2026-09-17 11:47:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cf4c92bd-4744-330f-82ef-a311caeeed39 | -9.37826 | -46.84986 | 2026-09-17 11:47:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| fa71d93a-06f3-3133-bb87-37f1cb213a2d | -7.01432 | -43.65121 | 2026-09-17 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| de7c6c02-1eee-3711-b82c-951a697a48f7 | -11.8892 | -47.60838 | 2026-09-17 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| a4a1bfbb-0a3a-30aa-ba66-8bf95e0e954a | -7.00371 | -43.64981 | 2026-09-17 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1428.7 |
| f20d2a9c-38f2-30c5-9a5e-78b414ea4e1f | -7.9465 | -44.82311 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 1862ce11-b85a-33e3-a385-5fbabf8e8d57 | -7.39752 | -44.50369 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| e4ed311a-9e3b-3855-aba6-cae5cd913693 | -9.13715 | -46.39221 | 2026-09-17 11:47:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f0e57c4b-0469-30c1-a7b1-21b0f8305a0c | -8.1473 | -44.85682 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f8515fcf-be7f-348b-b0e7-f58adfda4ab6 | -8.47088 | -46.88003 | 2026-09-17 11:47:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 617a9b92-f4ec-3f2e-97c0-2dac1c9ee478 | -10.59911 | -46.54136 | 2026-09-17 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6da83771-1999-33ae-8cf0-54925af62d34 | -6.99488 | -43.63534 | 2026-09-17 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 0b09c0c0-d896-366d-bff6-09aa32dc3089 | -11.8841 | -47.57932 | 2026-09-17 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5dc38d03-bd76-3e82-be5a-6e61bc4d741d | -12.32946 | -50.82338 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 82feb7af-b598-3fd1-bda9-6ebd08b89ec3 | -8.58459 | -44.56222 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 394b4b60-3d1b-37dc-92e0-d35f6c2abe64 | -8.43108 | -47.75087 | 2026-09-17 11:47:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 294b329d-180f-3a3c-962e-9ae36a8ce098 | -7.9667 | -44.83224 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README85.md)
