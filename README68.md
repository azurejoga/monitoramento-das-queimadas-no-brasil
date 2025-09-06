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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04d091b8-179b-3642-bc18-1af3865feec0 | -13.66042 | -46.95749 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e98b8241-5da5-3ff5-9265-bf85b61b87dd | -13.85063 | -46.26225 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 69854d6a-3ced-3ea3-a345-21f7c8ac98e4 | -14.8314 | -48.19815 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ae6627c-e50c-3ba4-972e-d22a3b58d3e9 | -13.85041 | -46.29419 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 781a6f3d-1e95-32fc-92f9-ff1dcbd11036 | -16.31307 | -52.93883 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62ae3823-9dae-33f4-9cd5-983f76af99a9 | -14.75315 | -47.49778 | 2025-09-06 04:40:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc336bed-5f5b-30f9-8c1c-9282710f98bd | -16.30295 | -45.69463 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9b0aa91-e1d2-31ac-aa5c-2f62fffa8d5f | -14.58692 | -48.08514 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 603fbea5-7088-3240-ace0-31db10b82b93 | -15.3592 | -46.41008 | 2025-09-06 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbf12ef8-21c0-39dc-a650-e24ec86088d6 | -12.50794 | -53.87135 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5eb9c165-d438-370c-b2a2-83e876545aad | -10.15945 | -46.23511 | 2025-09-06 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7a3029e-2ff4-3d4e-8588-f2e24ba07852 | -12.9962 | -54.81057 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d7d143c-e00d-34de-8ce3-b1e497baba1c | -14.33234 | -60.32877 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79fcf873-bede-398f-9efd-4c327cf212c4 | -12.73092 | -45.09285 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a2300537-0aa9-38d6-9f25-4aaa58e37bb5 | -10.23031 | -50.54933 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2780cbcd-6edf-3d9e-8ae3-f9c05c634dcf | -13.00715 | -54.83604 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16aa10c5-4656-3bea-81dd-9f71994ba2fe | -9.71286 | -48.99298 | 2025-09-06 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06360488-efc7-35dd-acb3-b9b0ab934669 | -14.57219 | -48.02705 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a25f536-ac8e-38bc-9073-8bb530b1a22b | -12.50864 | -53.8672 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9c8b90f-1e19-3a8d-8566-1d52fd58074b | -15.21136 | -52.35364 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1f003bd-b619-34d2-9488-6ca4f875a758 | -12.98399 | -54.83665 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 417c9cc9-8aaa-35ab-963e-eeeb441555e1 | -9.80275 | -48.33597 | 2025-09-06 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70303baa-9ae0-3f49-bab6-aebd10266029 | -10.20756 | -49.72066 | 2025-09-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65913233-775f-3f6a-8485-e250409feada | -11.61169 | -52.18987 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8fd9c55-e9bf-3c1a-8279-b800c772dba4 | -14.832 | -48.19401 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77409e49-e4d3-3f1a-9960-b71c4d7193af | -13.0093 | -54.84587 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f626848-284c-3b6a-8df2-c39bce57cfd0 | -12.99463 | -54.81965 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c69c96c-efbe-34e2-bdbd-51c98b0dcea0 | -16.54495 | -42.35075 | 2025-09-06 04:40:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 008b4750-9cb4-3252-a7c4-9e1ee9ee32ef | -12.98712 | -48.05301 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2024411b-eb4f-39d9-a82a-cf5932a43598 | -10.75337 | -46.3456 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e05ad11-f4ff-31f6-886a-f26fa361d4a9 | -13.00184 | -54.84456 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34a9531f-bb73-3349-96d4-0ade08d21d23 | -15.71607 | -53.58413 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b7471b6-8ca3-3aa0-b92e-3452fa665858 | -10.0737 | -48.71729 | 2025-09-06 04:40:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5edc986d-427e-35a5-9ada-13b0fbbbad53 | -14.58329 | -48.08463 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf6d0740-3d98-3c97-bf45-6bf960f65970 | -11.5385 | -47.3134 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d2d5453-a680-3f3c-b4b3-b82f4f5792ed | -12.97227 | -54.81571 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e849af2-b18e-3da6-a80b-8eba5a8c03b0 | -12.95819 | -54.8084 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 746d9ed3-8cce-35f7-b575-a85dafa0154b | -10.79101 | -47.7445 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7adf715-7194-3e11-9f72-d7319e36d522 | -9.707 | -49.49009 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 905b489e-5ae1-3eb7-b408-f45304c4a150 | -11.54214 | -47.31393 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9560d42-2a85-3c48-8ff6-4b3878fe383c | -12.88241 | -56.94746 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0590622-3d74-3623-978e-e00fcae25d65 | -13.5918 | -43.35291 | 2025-09-06 04:40:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b39bc016-4b7a-3a61-981e-f6883358065a | -15.85971 | -52.29312 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba7b9b2c-532d-300a-862e-8e5abaacaabb | -11.13194 | -46.34618 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e075224d-a172-377a-a762-bb6818691c6b | -17.23617 | -46.71337 | 2025-09-06 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a02707ad-8331-3b48-8a73-064e367b9b56 | -11.10526 | -52.02376 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 127f2dd9-2cd2-3e48-8c94-ead3f530e181 | -16.33051 | -52.94889 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a1c3af69-85ef-36a1-aff9-613c29024b75 | -12.51362 | -53.85953 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c3a05a2-6d29-3af7-b203-0eec8e7e416d | -12.99112 | -54.79563 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaea38c6-7c46-3fc2-be8e-bb1c74e81f29 | -12.69365 | -52.99578 | 2025-09-06 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e4c7a1d-1804-3390-bc96-23466e569868 | -11.20534 | -55.02987 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c767829-8c3c-3163-bbf2-8616bf762f7c | -13.01916 | -48.05814 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9a8c78e-37cb-33f7-85d3-3736c02fffd6 | -11.60891 | -52.18562 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82ac8afd-6526-3844-81cf-9c2e34fbd82f | -12.08611 | -45.69402 | 2025-09-06 04:40:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee56212a-dfdd-338d-846b-6c8d70630854 | -12.97813 | -54.82618 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbdfa305-3c1d-3e0f-b5e4-2b870be98981 | -14.57517 | -48.03201 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f878272-36e1-3a2a-a781-fef0f0475b7f | -12.49507 | -53.86058 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a072573-dca2-329f-8147-85d25d2cff08 | -11.59817 | -52.18756 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ba20d78-2f73-374e-8486-dcd22acd321f | -10.2142 | -49.72172 | 2025-09-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 031bebe9-c570-34af-9bd1-d9732f2f6216 | -15.28695 | -51.42922 | 2025-09-06 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d45dddf-f3ea-3e1a-b13f-fd8298f4aadf | -15.85697 | -52.2889 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50dbb392-7a4a-367e-9a7d-c4775772ed60 | -12.48365 | -53.86289 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f268d19b-26a9-3d47-9d39-aa21f6060165 | -17.69152 | -44.50579 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6953dac-991e-3f40-b992-ea0a6dc5f21c | -12.98076 | -54.78908 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83a020d1-f570-30fc-99ad-5ee0f5b854a7 | -10.13917 | -46.24126 | 2025-09-06 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d1ddcda-97f8-3c4b-9f35-a6b8f7b70a97 | -12.48722 | -53.8635 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70a15f2e-dcfa-3fbb-997c-f2949121c33d | -13.72166 | -46.9091 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b87438c1-efec-316b-9e78-21f083f20ca2 | -9.21392 | -57.0958 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0641891-87f2-3f2c-9ad8-6e8a2147bce9 | -14.57901 | -48.00573 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e275d72-5fee-3371-b420-545b4f4f1f73 | -16.33327 | -52.95309 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be0537b5-0998-319c-8526-5a354e99780f | -9.3309 | -55.20299 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e21f1075-8cc5-3058-af35-5be963769687 | -12.54086 | -48.06934 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ecffcbb-4c15-36f7-8c14-25339d2a3f12 | -14.58396 | -48.00096 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d80e8e89-c65a-3890-88fe-a93182b9ddd5 | -12.00388 | -47.77304 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a657792-6aaf-35fb-8ce8-60a0079ef951 | -9.55484 | -53.58763 | 2025-09-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceb4acb5-6406-3b41-970f-f9a5abce173d | -16.30044 | -45.69154 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4216e480-d025-3b73-8e06-5b39b81e8059 | -11.64303 | -54.54454 | 2025-09-06 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c13ae866-6c26-31bc-adcc-d6e4eb88308c | -15.14705 | -52.3279 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 815700e0-81a0-3ef4-8d0c-df6386408e94 | -11.53484 | -54.4064 | 2025-09-06 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 731d3e87-f4cc-35ff-81fb-eadab72cd5b7 | -11.09909 | -52.019 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55ac11c0-8cbb-3dcf-bba3-16753119a54d | -16.91935 | -45.75693 | 2025-09-06 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4512249-26e3-361c-8e7d-0fa95cf9730c | -14.11847 | -51.71106 | 2025-09-06 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf2e9b04-7767-38dc-bcd1-13464666e746 | -11.19329 | -55.00764 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4ab6f97-8408-3de6-9230-5dac476370d0 | -12.96377 | -54.77665 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba72c424-7f84-374b-8338-f4d73d67c030 | -9.68346 | -51.10211 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f88c92a1-299b-3d4c-aee8-3807c97b651d | -11.54881 | -47.31928 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcd2e62a-f6b7-34cd-9b17-b9cccd11a962 | -10.75718 | -46.34608 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e12e39bc-92c9-3ac4-8ea2-89859b17fb1c | -13.29778 | -51.76424 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 240768d7-b21f-3c67-8dda-e1d9bc2701ee | -12.48937 | -53.87244 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c496c6b-ebb4-3a89-b563-e6c86eedc850 | -14.82901 | -48.1891 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d35c39a-cf24-323a-a001-bd0604cb0057 | -14.89983 | -49.44857 | 2025-09-06 04:40:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e571a8a7-f73a-37a1-85a9-5b9bd773ba8a | -12.89237 | -48.01104 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8516c578-1e99-31b1-9812-c82906a2295e | -11.60296 | -52.1582 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e8fe4d6-ef31-3f46-9a96-a176b7fc945d | -9.23014 | -57.08415 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e23543c-1a86-318b-b008-81ae6cf7d968 | -12.9334 | -48.02961 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09310271-5a20-3dbc-8e1d-e8d47eb8874e | -12.96277 | -54.77405 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba2a44b2-8c18-33d2-a364-db5eb2885728 | -13.85599 | -46.25249 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9828b3f2-b754-3fbe-89c6-2e4e4f1d51cf | -11.2092 | -55.03059 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec2f6c3f-eca1-3eda-b3ab-de45831c05d6 | -10.1395 | -55.16293 | 2025-09-06 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f2fbcf8-114e-3c5e-a626-d10a6cdecded | -10.79222 | -47.73642 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README69.md)
