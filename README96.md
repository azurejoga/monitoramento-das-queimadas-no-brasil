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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58d15775-6ab7-314a-986c-421c0d22b86d | -5.59656 | -60.24844 | 2024-10-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fe3580f-7c5b-36b9-8a0c-43b6cd9794e4 | -5.60019 | -60.24897 | 2024-10-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e3dd0fd-c450-3835-8d46-2b7e4ea86aae | -5.31243 | -60.11934 | 2024-10-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df65b3cc-65f9-35b6-b9a4-e1c530cf6392 | -4.51855 | -61.14065 | 2024-10-26 05:36:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd175776-43f3-37f2-8a82-a2e09494d33f | -4.51511 | -61.14013 | 2024-10-26 05:36:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fac564e0-f318-326a-9a38-2c0bb1901429 | -3.05653 | -61.66718 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d179e477-2bdc-38ad-a8fd-aea3d7e5ce36 | -3.03924 | -61.66813 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9937e6a4-6e87-32df-bfad-9d88f3128cf4 | -3.09475 | -61.70198 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18b72d01-24cb-37ec-84da-3d0498a3af31 | -3.09141 | -61.70145 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaae30a1-e402-3efc-a87d-1df850de8635 | -3.09086 | -61.70499 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 595c0bcd-de76-3c6b-9b2e-4aba4964a342 | -3.06068 | -61.67859 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c205178b-4e34-37e3-b8db-d8b6079bde21 | -3.05988 | -61.66769 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f34a1429-84cd-3837-8adf-1538fb7aad3f | -3.05932 | -61.67123 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34f86faa-11bf-3fdf-b2ad-948458185e79 | -3.03589 | -61.66761 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89009977-8136-3585-8397-f25ed442ecfe | -3.01753 | -61.69738 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df811fa8-f49c-3e65-b8f2-f3fad561b9b8 | -3.01698 | -61.70092 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 165c67c3-a8de-34bb-84e5-267f3f4e4477 | -3.01419 | -61.69687 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c201a93-5888-3983-8b75-3bc5c34c4e07 | -3.01364 | -61.70041 | 2024-10-26 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9452805-2200-361a-bc0f-c9289f0be771 | -6.53497 | -62.94088 | 2024-10-26 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 594d895d-b16f-353e-8834-ffd9a181aad8 | -6.53443 | -62.94437 | 2024-10-26 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4c0193b-8b7d-37b4-bef1-85cc0ed8aa08 | -6.53111 | -62.94386 | 2024-10-26 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db881973-be15-3583-b038-40961d5a4a9b | -6.53057 | -62.94735 | 2024-10-26 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dddceae5-fb3a-36b1-a0c8-5d7a8cd533e4 | -3.15992 | -68.14471 | 2024-10-26 05:36:00 | NOAA-21 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cbadb57-f894-3ead-a445-4e0ff9983b98 | -3.15586 | -68.14407 | 2024-10-26 05:36:00 | NOAA-21 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41b32077-c98e-32e7-9dff-39bd0ac040eb | -10.55115 | -67.83659 | 2024-10-26 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 362a0fba-938c-3aa3-9c4c-ea91b5465270 | -10.46676 | -67.75465 | 2024-10-26 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22604862-f243-3d3c-88c9-c0dcd3fcc2e5 | -10.34154 | -67.76424 | 2024-10-26 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a506a69f-dbbf-3ca3-ad5e-f708f17ab453 | -10.12619 | -67.59344 | 2024-10-26 05:38:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ad7f5bb-4e83-389b-af22-08282b3afb06 | -10.12262 | -67.59281 | 2024-10-26 05:38:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8433a1f-bc75-3486-8e96-fb8bd66a5d14 | -10.11613 | -68.12457 | 2024-10-26 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd48f183-8985-36df-9b50-bdbec4629576 | -10.10062 | -68.37382 | 2024-10-26 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09fda8c8-70d9-30b4-97f0-3d8c8ada4719 | -10.0969 | -68.37317 | 2024-10-26 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cba4846-7f8c-3c20-bd4a-a73116d03d83 | -10.91478 | -69.23352 | 2024-10-26 05:38:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ed48f4b-8385-3049-b0f6-6ffaf39240f3 | -9.25664 | -50.68903 | 2024-10-26 05:38:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e9f8370e-791b-3c1f-9fbf-b1fb72cb460c | -9.25513 | -50.6858 | 2024-10-26 05:38:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5548d67f-9678-3a8c-b113-c6ad3e2c7ec9 | -9.25433 | -50.69258 | 2024-10-26 05:38:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e11a14f1-c37c-389d-844a-9e73170378b3 | -10.99719 | -52.87585 | 2024-10-26 05:38:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| afbf8980-7dd1-3d05-abe6-e3e279951d48 | -10.99406 | -52.87535 | 2024-10-26 05:38:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7044e8c9-00cf-39ef-af5a-21d752933593 | -10.99344 | -52.88041 | 2024-10-26 05:38:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ac45b92-156d-3609-81bf-7b55e7276113 | -10.99028 | -52.88018 | 2024-10-26 05:38:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ce6b76df-d277-3a31-9d1e-775e726610ce | -9.99884 | -56.24857 | 2024-10-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f36af24-9dc2-3ee7-9b0a-a51fa4e7fdb2 | -9.99422 | -56.24504 | 2024-10-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f2f295db-ab99-362f-a179-6cda7044f2e4 | -9.99384 | -56.24791 | 2024-10-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0f0bd944-6465-3ae2-bc78-f8a4d8359bd0 | -9.6677 | -55.72995 | 2024-10-26 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d910c728-73f2-34d3-8cee-176bb0fc4989 | -10.61409 | -55.98679 | 2024-10-26 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57b9723c-9b50-340d-9ce7-7363c9dd3db4 | -9.73987 | -57.36474 | 2024-10-26 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6bc553c-0414-326c-8c6e-d2b4c225dc16 | -9.4535 | -58.92704 | 2024-10-26 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b71c76d1-1b68-37c7-9eed-27787a910529 | -13.49288 | -61.63124 | 2024-10-26 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51d2cbe8-0d14-3e8e-a6fc-ce537bd39812 | -13.49105 | -61.61721 | 2024-10-26 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9dc0f0-09f6-3f19-b910-7603eec4a900 | -7.89952 | -61.52335 | 2024-10-26 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 80ad7609-05c6-37c9-8325-f57188c0cfde | -7.7296 | -61.37518 | 2024-10-26 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d40e6f1-1f23-3b7b-8dcb-4347852846e1 | -12.9775 | -62.73581 | 2024-10-26 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46606bc7-cf6f-36c1-a4f9-d29b7d0f464b | -12.9746 | -62.73133 | 2024-10-26 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9da9a810-0aad-32b0-bf83-e976d6033b81 | -12.97285 | -62.74315 | 2024-10-26 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9319776b-f134-3645-830e-58748a8756a4 | -12.97227 | -62.74709 | 2024-10-26 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 845c2d18-5e76-3eea-b703-3eeff0dd0fc1 | -12.38298 | -63.38779 | 2024-10-26 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08ef8bbb-4b7d-3bc0-bc83-c42b3637456a | -7.64936 | -63.45109 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fda470f-7422-38dd-ab49-e8237a01545b | -7.64882 | -63.45457 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2420ca88-fdf8-3232-8956-7185ea2e84c0 | -7.64605 | -63.45057 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95259336-828b-3592-a9eb-84a4d4baaf3e | -7.64551 | -63.45405 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 887f219e-0770-320e-b32a-0ced2f0fa6c2 | -7.64274 | -63.45006 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4983423-06b2-3d80-b51e-2789c6b47e1a | -7.6422 | -63.45353 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 699a839c-2139-3dcf-befd-fc6b8fd39573 | -7.64166 | -63.457 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be1cf033-f942-35a4-a828-4251eda18161 | -7.63944 | -63.44954 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad0a99bb-f475-3e8b-85e5-fd5a013200e0 | -7.63889 | -63.45302 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdb6700a-1f45-3a1d-9ff0-5c4f7e3641ad | -7.63835 | -63.45649 | 2024-10-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ae213db-039b-33b0-9314-e372a930a101 | -7.03885 | -63.11243 | 2024-10-26 05:38:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6357f43-9d6d-3f78-ac92-663ec3b9df81 | -7.03831 | -63.11591 | 2024-10-26 05:38:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffa1e019-d3e5-367a-b983-12827057a8f5 | -7.03777 | -63.1194 | 2024-10-26 05:38:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abdefbf3-5fc4-3245-8bfd-98bf9d96a848 | -7.03722 | -63.12289 | 2024-10-26 05:38:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73eb0373-5e17-357e-b024-255f4b633aca | -7.03554 | -63.11191 | 2024-10-26 05:38:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38562037-3ed8-3acc-ba6a-4b20bc0c28b7 | -7.00107 | -63.04933 | 2024-10-26 05:38:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bec1ed7e-ccc5-3a13-99ff-372cc881c216 | -7.94803 | -70.72348 | 2024-10-26 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ecbf6e5-7352-3f97-8739-e4c5f71cfe22 | -9.45062 | -70.60248 | 2024-10-26 05:38:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6544b653-1461-362e-82db-63aa854c6443 | -9.44907 | -70.60227 | 2024-10-26 05:38:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ca2d7c8-97f8-3757-9fee-2c77944f360b | -7.82236 | -72.78053 | 2024-10-26 05:38:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3f7bb2a8-6cb5-36ef-a6d0-fbeda282c317 | -7.8218 | -72.78366 | 2024-10-26 05:38:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 42382437-1372-306a-a49f-5805dc996be4 | -7.39616 | -72.65342 | 2024-10-26 05:38:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 895537d4-e91b-3e3f-92e2-0da106833fd5 | -7.39099 | -72.65259 | 2024-10-26 05:38:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 409df6a5-eee0-31bc-b101-09d9a7f79da4 | -7.33741 | -72.80224 | 2024-10-26 05:38:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7857acc9-db8c-335a-aad8-7010817454f1 | -17.9333 | -57.56686 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 542aaa12-4964-33de-bf83-58916881e309 | -17.93011 | -57.54882 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| dcf1caa6-798d-3ff1-b43e-9973993c31e8 | -17.22761 | -56.67254 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 32c09f39-637b-3c39-a421-ae75db9f8a39 | -17.2253 | -56.67408 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aec629cd-d1ba-3987-8ec6-2fcddf548fdc | -17.02073 | -56.00458 | 2024-10-26 05:40:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7bb5a3f8-795b-3be3-8459-24accf37ff96 | -17.01615 | -56.51131 | 2024-10-26 05:40:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 902ae63d-a9af-3f49-835d-d0010338a1a2 | -17.01555 | -56.00002 | 2024-10-26 05:40:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 02e8ead8-3f28-3741-acab-5fbe4f075504 | -17.01514 | -56.00389 | 2024-10-26 05:40:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a29a6b3d-0e7e-3983-bafd-6ef6eb95fd07 | -17.01075 | -56.51064 | 2024-10-26 05:40:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2b1bac7d-e9cc-3fd9-84f8-c6058e09a870 | -18.30492 | -56.18042 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62b91524-bb73-385e-8326-6dfe685e3013 | -18.27258 | -55.99112 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b3eb9055-e506-3ce7-ae7c-6281c8bb6091 | -18.27005 | -55.99127 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a0bcfde9-53e3-3992-9bdc-d7ba48e97904 | -18.26691 | -55.99044 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7d02cf34-1c64-3656-a8d3-53d65818a6cb | -18.26493 | -56.01058 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 61c6211d-5a08-3f7d-b3db-174d8903ce49 | -18.26226 | -56.01072 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2c8666db-e5a7-3856-bb26-4b3eae8ede40 | -18.26183 | -56.01474 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9b20ed65-0b27-3eee-8ffb-512998b64642 | -18.26044 | -55.99782 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 07f86053-20e4-3806-ac7f-72ff6fe6ae04 | -18.26005 | -56.00184 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6781b0c9-99f4-341e-ac7b-9cb90a883cf0 | -18.25926 | -56.00988 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0b7830bb-9cc8-3862-acde-656e796c8abb | -18.25786 | -55.99798 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |


[Clique aqui para ver as próximas entradas](README97.md)
