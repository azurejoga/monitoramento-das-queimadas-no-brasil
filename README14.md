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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47cd8d3a-5325-3904-82c1-2ff035770f0f | -13.3955 | -56.91608 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 09d5c6dc-0bee-3492-9edc-afe6c8f8c287 | -14.01851 | -55.1203 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cf5a97a-498c-3d7b-8365-8667e8443c40 | -13.46408 | -60.28926 | 2025-05-17 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6e00b1d-e9a1-383f-9779-453cfe341553 | -12.82809 | -62.00845 | 2025-05-17 05:31:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2725985-323b-33cc-b3de-be42fba8ee1e | -12.46159 | -57.19828 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93cb364e-e30a-305b-a289-b53d2492a7eb | -13.391 | -56.91542 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aaabc9bc-ac00-3869-bc47-6013cc546bba | -13.04432 | -53.71602 | 2025-05-17 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 675a5f4d-03cb-3121-b078-57983cfb8362 | -12.45231 | -57.2013 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cddfd09-1e96-3e81-b576-311995a44942 | -14.02137 | -55.14014 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eda8966f-ec46-3564-b1f5-5667d5f9b5bc | -15.27051 | -51.48035 | 2025-05-17 05:31:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfe9436b-e0a3-3c19-9687-c8e3183d6353 | -13.40061 | -56.91205 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2f7986b5-d00b-36f3-bf85-d232270ac785 | -12.14965 | -63.05505 | 2025-05-17 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec25944b-6d21-31ec-8f95-8ea9ee1f9f8c | -12.64693 | -57.18893 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 839fe092-db1b-307e-8bef-0e4b3506e44a | -12.44851 | -57.19643 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8edd9713-feaf-35a6-97e3-6c1c0fba34b9 | -13.14342 | -56.81089 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b52be0fd-ace7-3a43-ad96-4625477e8e5c | -13.66842 | -52.19679 | 2025-05-17 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c5108ae-246e-3a6f-b84a-46cf637a01fb | -14.0225 | -55.13061 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f976c88-e186-3716-9f2a-f7f2ec553e6a | -12.65131 | -57.18951 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8df20334-7132-321b-a4c8-4d7e3b013c1a | -21.60427 | -51.59849 | 2025-05-17 05:33:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| aef19268-2b60-3c59-bbbb-b3c502f1cb10 | -20.62888 | -55.71389 | 2025-05-17 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d815a0ee-e966-3e20-b7dd-4bd0e48c6ed1 | -20.95804 | -56.60826 | 2025-05-17 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d038647d-83c7-3d27-aea6-e83649b4efba | -20.9563 | -56.60887 | 2025-05-17 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 28f762e8-bd1c-3377-87e0-09a52cd34617 | -20.95154 | -56.60487 | 2025-05-17 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d9ec022b-89f3-3394-9f4f-4c5a828da73a | -20.95296 | -56.60759 | 2025-05-17 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 66c1adc9-fd7c-32e9-b430-f5e511beadba | -20.9533 | -56.60431 | 2025-05-17 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 921d3d3a-a098-3fa1-9a3b-c2dce6e17497 | -20.95769 | -56.61156 | 2025-05-17 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c79259d1-fb32-31d4-bf44-7b47dc274e30 | -21.61057 | -51.60239 | 2025-05-17 05:33:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 40fe06a0-f7e5-3ec6-93d5-d87cfe1c5beb | -21.60361 | -51.6019 | 2025-05-17 05:33:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 263d1b76-07a6-3e59-a4cb-8bc5f6e375a4 | -21.61124 | -51.59885 | 2025-05-17 05:33:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dc043a58-0a6a-3ee8-b0c8-2102bd47e95c | -20.95121 | -56.60815 | 2025-05-17 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b8687831-57c4-32de-8a34-92df90dcf898 | -21.82003 | -57.55658 | 2025-05-17 05:33:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12fbd387-8db4-31c3-bf7b-fe0e7cdbf983 | -20.63148 | -55.71264 | 2025-05-17 05:33:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a88d7c0a-6301-34b0-8778-b177d150b46e | -20.95261 | -56.61086 | 2025-05-17 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4a90813f-5134-3c4e-9b1d-2f666e015efc | -21.60376 | -51.60538 | 2025-05-17 05:33:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0d3ab511-e596-3177-986a-0496d70b7ae2 | -21.6066 | -51.5878 | 2025-05-17 05:40:00 | GOES-19 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.0 |
| d7cb86bf-a80a-30d6-8220-9e97a85c5b05 | -21.606 | -51.6104 | 2025-05-17 05:40:00 | GOES-19 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| 5c80c559-0b62-326c-8027-d505e8cf63f4 | -9.25604 | -60.32151 | 2025-05-17 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 714b07e2-fda0-3842-bc0c-685afa6ee4b8 | -9.25646 | -60.31832 | 2025-05-17 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d079960-91a4-33f2-b92c-8112736f106a | -13.84884 | -59.72402 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c89bb978-d861-36d2-9d43-a69c5836cbff | -12.14098 | -63.06285 | 2025-05-17 05:57:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 216f9f59-b284-3f10-8f6c-84d8c25e5668 | -12.45799 | -57.19903 | 2025-05-17 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 313e326e-533e-3342-979e-756314c5cccb | -13.39412 | -56.91799 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9425a3ef-de18-35bb-9133-2c6bb373d06e | -13.39422 | -56.91591 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 317ad473-5d4e-344d-a930-67c83c424175 | -13.84866 | -59.72598 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 609e750b-2cfc-3d63-a793-6eb776667da3 | -10.04948 | -64.99243 | 2025-05-17 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3869624-c088-379d-b4e8-7490f461f4a7 | -9.66373 | -65.75411 | 2025-05-17 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a3680f5-26c7-33b1-9aa6-b8e7bbe9b8dc | -12.45428 | -57.19825 | 2025-05-17 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90a1a9d9-1447-3dee-9727-4ee32d7e7ba5 | -13.14145 | -56.80208 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5af9a8f5-f719-3e08-acc2-47c98dbf645f | -12.45131 | -57.19825 | 2025-05-17 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fab255fc-c5e6-3014-8153-67c1ee4b01c0 | -13.14773 | -56.81137 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 576498ac-cc9c-386c-ab29-d48f8af4b5b2 | -13.84911 | -59.72196 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| becba12f-96ad-3549-991f-6bbb5f6600ce | -15.60611 | -59.28952 | 2025-05-17 05:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43237f5e-6854-39b3-a703-daf4550dbb3b | -12.64486 | -57.1876 | 2025-05-17 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c975d97a-a21d-3f79-91f2-dbfd6673c101 | -13.83197 | -59.66706 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 577014de-331b-37ab-8bc2-12cb33005e49 | -13.82612 | -59.66653 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2edcda98-cc41-3367-ab57-b59f02119523 | -13.8314 | -59.6689 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 392fd79f-be05-3415-8bb9-414f26ae0520 | -13.85417 | -59.72874 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f22848cb-a211-38a2-8dea-67355f4c3e98 | -13.38727 | -56.91708 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bc9d33c-cd6a-3984-9b4d-853281c2beb0 | -12.65157 | -57.18824 | 2025-05-17 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14a81ed0-26da-36ca-a893-263ac8d5b64c | -10.04858 | -64.99558 | 2025-05-17 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 136285bd-1b59-3a2c-9d5a-8c34d40e15b0 | -13.14151 | -56.8042 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f1166c81-77b0-3f76-91bf-7fdc009607c7 | -13.14082 | -56.81072 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 61f30734-e5fd-3013-92bd-0961d73e4909 | -12.4476 | -57.19749 | 2025-05-17 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7920c561-7c22-32b8-99dc-5a41d6d2e804 | -12.46096 | -57.19902 | 2025-05-17 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ee2a70f-c819-3aac-b639-e35554d1933d | -15.60559 | -59.29441 | 2025-05-17 05:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 869c297c-c1b2-31da-b1d8-a006f7560444 | -13.14842 | -56.80483 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f00d319a-956e-313f-9765-bb012319cfff | -13.14072 | -56.80858 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7d7dc99c-187e-3280-a1c6-cdd082ab139b | -13.39488 | -56.90948 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 833f72a3-260e-39f7-a638-03d0f5c65965 | -9.64293 | -67.22424 | 2025-05-17 05:57:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 446f2d09-cc74-3907-b511-67402f61542b | -13.38737 | -56.91497 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c90dd122-987f-3742-b185-6f1eb29383f4 | -12.64417 | -57.19372 | 2025-05-17 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51de1890-4741-3f07-a6f2-6d7fffac3a28 | -13.8266 | -59.66244 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9105b283-b4f0-348b-aa00-5344d3edfab3 | -13.85447 | -59.72672 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcce93cf-0760-3f51-8602-d6dccfc5867a | -13.39482 | -56.9115 | 2025-05-17 05:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 429c2a7e-7020-3b9f-8818-18658fb7bed9 | -13.85401 | -59.73072 | 2025-05-17 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0de05f26-5109-3b42-8b3c-51c087e3e4dc | -13.14649 | -56.80079 | 2025-05-17 06:44:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| a5908818-f37c-3b1d-acb5-1f5ac6fb09d1 | -13.39506 | -56.90824 | 2025-05-17 06:46:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 02f816bc-ae0d-37e6-925c-81785fb216de | -12.461 | -57.1879 | 2025-05-17 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 18e67499-6bb7-3ccd-ae4a-fd29d7d9d97c | -12.3515 | -49.9833 | 2025-05-17 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 963449e7-05a7-34a2-b524-bf7d38f612e2 | -12.461 | -57.1879 | 2025-05-17 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| e11b2a52-f46b-3948-b107-6b9831e5a8be | -12.4608 | -57.2079 | 2025-05-17 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 893620ab-849a-312c-833c-b6399d1b05c1 | -12.3519 | -49.9617 | 2025-05-17 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| d5dc215b-6e73-3689-afa5-f76732d2d5f9 | -12.461 | -57.1879 | 2025-05-17 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 157.5 |
| a4f2f3e3-bc33-3d25-9988-40a51c2dd340 | -12.442 | -57.1895 | 2025-05-17 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| c9ed7885-cdc6-381e-be56-b41320040349 | -12.4608 | -57.2079 | 2025-05-17 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| de053efc-6149-35f4-af67-849de8843f1c | -12.3519 | -49.9617 | 2025-05-17 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 867d2ae9-b5eb-3ba5-800d-0845c4b81e18 | -12.4608 | -57.2079 | 2025-05-17 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 415bba1b-4dfc-3b40-a46b-8e84806efc06 | -12.442 | -57.1895 | 2025-05-17 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| f293c368-9948-3d9b-9ba5-47b57dad4c48 | -12.461 | -57.1879 | 2025-05-17 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 187.9 |
| 8175a2a1-2d0a-37b0-a40c-f8dba468b7d9 | -12.3519 | -49.9617 | 2025-05-17 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 7a63d989-86e8-3e1c-9dc0-bcf646f9c834 | -12.4418 | -57.2096 | 2025-05-17 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7596e39c-7f54-322a-96ca-25183b5b02e4 | -12.4608 | -57.2079 | 2025-05-17 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 8b473f69-7014-37a1-8582-a2d7afa50efa | -12.3519 | -49.9617 | 2025-05-17 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 67753d5f-40ca-3f49-9ce0-844360ef70cd | -12.3515 | -49.9833 | 2025-05-17 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 6c575b74-d78b-3bf9-8772-d556acf87964 | -12.442 | -57.1895 | 2025-05-17 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 89d2b4b2-8dd5-3a78-983c-1a9633196c1b | -12.3327 | -49.9641 | 2025-05-17 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 13033108-4a9d-3d80-9030-e005ff513bf1 | -12.461 | -57.1879 | 2025-05-17 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 224.8 |
| bf85b38b-0b90-3574-9014-4bbae178ad5e | -7.54096 | -39.73531 | 2025-05-17 12:00:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e5981388-9b70-378e-9d01-48e0dec06234 | -6.72298 | -42.12853 | 2025-05-17 12:00:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| ffdf1e3a-3181-3c8e-b4b3-58386ea3ced8 | -6.94303 | -42.80046 | 2025-05-17 12:00:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |


[Clique aqui para ver as próximas entradas](README15.md)
