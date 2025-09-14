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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e818434-1a57-360f-9e1c-26614ce89c62 | -11.3301 | -50.8528 | 2025-09-14 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b187e8ed-697d-3abe-93c3-6f0436de8d63 | -3.581 | -47.5149 | 2025-09-14 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6b09bafc-a5cd-3f30-9628-7563bc4041c8 | -11.3491 | -50.8507 | 2025-09-14 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 81e4953f-09a5-36bd-a306-6c6221f190cf | -11.3259 | -51.1505 | 2025-09-14 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f459f9e2-8824-3c48-84e8-7d1e7253d4a2 | -11.2924 | -50.8356 | 2025-09-14 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 2ca2c698-b32c-3de9-9d92-e048cb2b7f70 | -11.4759 | -48.7003 | 2025-09-14 01:50:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 61812458-5fbe-33bf-9cf8-4b271dc49d83 | -12.6824 | -54.6968 | 2025-09-14 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5755a805-46e0-33db-9d0f-05da5f1f80f0 | -22.7282 | -49.8866 | 2025-09-14 01:50:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 43d48ace-75d1-3615-81ce-a82f5a661529 | -12.6826 | -54.6763 | 2025-09-14 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 72e59385-7cb2-3100-9f95-e4aa2e1cef26 | -11.3114 | -50.8335 | 2025-09-14 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 0030bf03-eba7-33b3-b423-9349a69a84c7 | -8.9427 | -48.6491 | 2025-09-14 01:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a765550d-e11b-3672-82de-eaac95d05679 | -12.6633 | -54.6988 | 2025-09-14 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ba2fed48-7204-323d-b947-ce863c2f5d1d | -12.7863 | -48.0209 | 2025-09-14 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 02741eb8-16c0-3a5e-9a94-868b430456f9 | -12.7867 | -47.9986 | 2025-09-14 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 74356927-f64b-3acb-82df-b7affa3bdda5 | -12.9294 | -54.7333 | 2025-09-14 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| ca1e3ca9-e2da-344b-ab2a-f3ad0b540c60 | -10.7579 | -44.7721 | 2025-09-14 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| bca574f2-8939-3905-b3cb-943ff11ab0ac | -15.8018 | -52.2043 | 2025-09-14 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 141.4 |
| b868395b-7acf-32ce-ad4c-d2157806457c | -3.5994 | -47.5359 | 2025-09-14 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0da79c92-a7d7-3f43-9afe-cb56c7895958 | -11.2924 | -50.8356 | 2025-09-14 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1b0f19b5-e832-3a64-9306-c036dd6946c7 | -11.3259 | -51.1505 | 2025-09-14 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 956fc846-44b6-38a1-b578-4027650237f2 | -12.3202 | -64.0757 | 2025-09-14 02:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8dd937d6-1a11-3a4e-8e6a-9d5220f65e13 | -3.581 | -47.5149 | 2025-09-14 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 35d94640-6c33-3dd0-b95e-2b56ecd95d39 | -15.8018 | -52.2043 | 2025-09-14 02:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| e435b7ba-4f69-3db4-8959-a163d9726b08 | -12.7863 | -48.0209 | 2025-09-14 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 122e009c-d64b-3342-afc6-06d2941010dd | -12.6821 | -54.7174 | 2025-09-14 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a29969cd-5fe8-3ebf-b326-0cb4743c78cb | -10.769 | -46.4583 | 2025-09-14 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 54285af6-70fa-39e4-917a-5bf93320861e | -12.7867 | -47.9986 | 2025-09-14 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ebaf82e0-90be-3406-b668-bfb977e5308f | -12.6826 | -54.6763 | 2025-09-14 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 3e8541f3-6db2-390a-86b5-02656881890d | -3.5994 | -47.5359 | 2025-09-14 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| c89b0787-2539-3757-ad3b-b0c4feb3a9c7 | -12.7675 | -48.0013 | 2025-09-14 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cd29ff20-9d8b-3663-a15c-dcd8c8fbfe30 | -12.6636 | -54.6782 | 2025-09-14 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 54579cee-848e-31e4-a7e7-a933befe637d | -10.7579 | -44.7721 | 2025-09-14 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f3e09edf-e1d6-3b3a-8596-328d2afbc5bd | -3.5995 | -47.5142 | 2025-09-14 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| df891707-33c3-3bdd-8d26-24bc99e5e7ce | -14.6394 | -52.1094 | 2025-09-14 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 900ac3a5-033b-31b9-87e5-ec6e1af1c262 | -12.663 | -54.7193 | 2025-09-14 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f6feea28-2ead-33e4-b49f-67f0eda2a677 | -12.6633 | -54.6988 | 2025-09-14 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 178.9 |
| b590040a-d74c-352c-b191-c8f534788b13 | -12.9294 | -54.7333 | 2025-09-14 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| e421225b-c5a6-3563-ad01-fdac036f8666 | -11.4759 | -48.7003 | 2025-09-14 02:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 54eaf7ef-042e-33fb-aa91-31f64b5b0cfe | -12.6824 | -54.6968 | 2025-09-14 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 206.8 |
| 81ea4604-fa7c-375c-b4f6-42bcd8d4dcaa | -15.8018 | -52.2043 | 2025-09-14 02:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 7c4f3026-a107-3fad-af55-1368723e6702 | -11.445 | -50.7762 | 2025-09-14 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| be5d7c17-99e5-3ebd-bd57-16615e819dab | -10.75 | -46.4607 | 2025-09-14 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 7d3d4322-3359-315a-858b-849e07f95b47 | -10.769 | -46.4583 | 2025-09-14 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 69701be7-c363-3b67-8139-368e09826ea8 | -12.6636 | -54.6782 | 2025-09-14 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 35380fb0-6f8f-38a6-8671-793787745c8b | -10.7687 | -46.4808 | 2025-09-14 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 097055a9-8aec-36b2-b72a-af61665f3584 | -12.7863 | -48.0209 | 2025-09-14 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 3160afd3-c28a-36ad-81c1-f3db9b29b23b | -14.6588 | -52.1068 | 2025-09-14 02:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| bd20d5d5-d9a1-3ffe-8ff9-a82efbfa3e78 | -12.7675 | -48.0013 | 2025-09-14 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| f3523df3-2bd5-3598-bb94-6aa7ffc10332 | -11.4643 | -50.7528 | 2025-09-14 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 789982d7-fb87-38e9-a583-173865173716 | -3.6181 | -47.5134 | 2025-09-14 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 33f0cfe6-00b2-3e1c-bc44-cedcc5246ad5 | -11.464 | -50.7741 | 2025-09-14 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 135eb962-6325-3212-9e4d-098f566e2e42 | -11.3114 | -50.8335 | 2025-09-14 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b679c71a-8887-387f-b3ba-3e4d78ede44b | -12.7867 | -47.9986 | 2025-09-14 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c1196490-c2c6-3628-81b2-7d5c2e80d01b | -12.9294 | -54.7333 | 2025-09-14 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| cf8c3b5d-c7ed-3f89-9a47-5459f42cdab4 | -11.4637 | -50.7955 | 2025-09-14 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| b9b10874-d161-37c7-9cf7-ec1068bf6d51 | -14.6394 | -52.1094 | 2025-09-14 02:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| aff71a3f-a10b-3bc9-92b9-b6f8ae655d31 | -11.483 | -50.772 | 2025-09-14 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| cf928e80-f46c-3524-a65a-12ba04bcd638 | -12.7671 | -48.0236 | 2025-09-14 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 40661656-6477-3234-bbd6-bf63dc6e9d3c | -11.4827 | -50.7934 | 2025-09-14 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| eba5aebd-011a-3ee0-a21c-ed639b6ce909 | -11.4759 | -48.7003 | 2025-09-14 02:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0a37bd98-90ce-31bf-9544-fbc9d27ab428 | -3.581 | -47.5149 | 2025-09-14 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 36c688e5-640d-34a2-af65-f52495939fc4 | -3.5995 | -47.5142 | 2025-09-14 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| a8436fbf-cbca-336a-8887-51476864db5a | -10.7579 | -44.7721 | 2025-09-14 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 18a33a9a-a61b-357c-a3ce-8a71a3279d56 | -22.7282 | -49.8866 | 2025-09-14 02:10:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 41faffa6-4824-37a3-ac05-2ce665b0fb95 | -11.3259 | -51.1505 | 2025-09-14 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 810b14f2-b4d6-35df-8366-469ea2c5aee2 | -3.5995 | -47.5142 | 2025-09-14 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 0e6116aa-b834-36cf-a834-e7a30b6addfb | -11.4643 | -50.7528 | 2025-09-14 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 8ccb79af-25ec-34a1-a037-a73c5ec80f79 | -12.7867 | -47.9986 | 2025-09-14 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| b8fcf20e-f88f-3376-ab2b-19b725aaadac | -12.7482 | -48.0041 | 2025-09-14 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 698514d1-3cea-3793-93c0-a5b659e86208 | -12.7863 | -48.0209 | 2025-09-14 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 9b39e992-3251-3786-971c-8557aeab2afb | -12.7017 | -54.6744 | 2025-09-14 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3a774040-6d8e-3cde-acc9-200b3f4275a2 | -11.483 | -50.772 | 2025-09-14 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 9e752b9e-7e6a-33bc-a1e7-8b6c3862a820 | -12.6824 | -54.6968 | 2025-09-14 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4d28b80d-f251-3db0-bac6-ce970ddf59c9 | -12.6826 | -54.6763 | 2025-09-14 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| c7f91a5d-38a7-368e-9f8a-9ca3c17fb092 | -11.2924 | -50.8356 | 2025-09-14 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| f23c55b4-5d8c-3561-a3d2-0a9ce1c8c8e0 | -10.769 | -46.4583 | 2025-09-14 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6b83aae2-6eec-38fa-8afe-7409bab8384e | -12.6633 | -54.6988 | 2025-09-14 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 0a532d13-fca3-3ab6-99f9-e836bc475515 | -11.4569 | -48.7026 | 2025-09-14 02:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 94704deb-bd3d-3901-8262-444697c6e409 | -12.6636 | -54.6782 | 2025-09-14 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| c620bc7d-48ee-3015-a08a-5dc3fbbe71cd | -12.9294 | -54.7333 | 2025-09-14 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 34c57feb-00a3-3e3d-8cf5-de29d6204a34 | -11.4827 | -50.7934 | 2025-09-14 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 5796232d-1527-3c2b-9c0f-2dd7336ee991 | -8.9427 | -48.6491 | 2025-09-14 02:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ccc730fd-a4dd-3d7f-bfcf-53992d448556 | -10.75 | -46.4607 | 2025-09-14 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2711a5ec-bfad-3fd6-bcbe-05e3c84625a3 | -11.464 | -50.7741 | 2025-09-14 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 48ee42af-fa67-3570-8afd-256d31894f0a | -11.3114 | -50.8335 | 2025-09-14 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 98b6ac2e-f13d-3b8c-87e3-1301da777863 | -11.4637 | -50.7955 | 2025-09-14 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e986c9bb-eab8-3b58-a995-1d5ad0c18073 | -14.1917 | -46.1552 | 2025-09-14 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 57d7861f-4c8a-36de-9014-c22b35cb8c7a | -12.7675 | -48.0013 | 2025-09-14 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 392e64ea-2075-3aa8-af58-36bcfcf37187 | -12.8055 | -48.0182 | 2025-09-14 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 2992781d-c2dd-39d5-a778-f6b9ccd80641 | -22.7282 | -49.8866 | 2025-09-14 02:30:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| b1313339-779e-34eb-8c9b-1e25418f9ae8 | -3.581 | -47.5149 | 2025-09-14 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e1e90f9c-0891-3501-b18e-99aff238faba | -21.3821 | -48.5382 | 2025-09-14 02:30:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 73.3 |
| dc32bac9-5c72-3482-9394-57fc185eecf3 | -13.9283 | -44.8341 | 2025-09-14 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 14d3da11-1f8c-305d-b61a-99f65fb6974f | -12.7863 | -48.0209 | 2025-09-14 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 7a583cc3-cdcd-3d5d-9e3b-00ef070817f4 | -12.7675 | -48.0013 | 2025-09-14 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 1f7c6721-7140-391d-9553-98bc0920ca13 | -13.9278 | -44.8576 | 2025-09-14 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1382de73-9f0e-3b70-8e91-0c4acc6659b1 | -3.5995 | -47.5142 | 2025-09-14 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 43553d17-b88b-3e54-9261-b84fb21bd77c | -12.7671 | -48.0236 | 2025-09-14 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 25ac0828-1923-3849-adc1-cdeaa366f42b | -11.3114 | -50.8335 | 2025-09-14 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| ca50a6bb-765e-35b6-83c0-7af94288dc2e | -12.7867 | -47.9986 | 2025-09-14 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |


[Clique aqui para ver as próximas entradas](README6.md)
