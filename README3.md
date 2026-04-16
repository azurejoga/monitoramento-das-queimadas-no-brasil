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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 068df332-36c0-3a2b-9095-c997c152fc00 | -24.93104 | -50.77868 | 2026-04-16 04:32:00 | NOAA-21 | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5d6e2dc8-3458-39f7-816e-fb89f19ea900 | -20.16018 | -46.73298 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a86915bb-943c-3545-a1e0-cf1c2d2a9b47 | -21.08743 | -43.09959 | 2026-04-16 04:32:00 | NOAA-21 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bfb6a4ff-cad7-3fc7-8a12-b2f991688415 | -20.53875 | -49.4947 | 2026-04-16 04:32:00 | NOAA-21 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eedaa5c2-8a4b-398d-8352-2314e1814503 | -21.70954 | -48.43251 | 2026-04-16 04:32:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1f047043-ecae-3794-b975-992f510ed71c | -20.24902 | -46.53466 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a0f0c0b-9cb9-3081-8c9e-09e543881b50 | -20.68302 | -49.39859 | 2026-04-16 04:32:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27eafd48-e392-3ef1-8dac-4673e945b868 | -20.17573 | -46.59507 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fb9c74f-12c1-3673-bbc6-18d9cedf8f92 | -22.80521 | -47.30236 | 2026-04-16 04:32:00 | NOAA-21 | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6baa8b1e-7bd8-3198-95a3-c0fe8be8a29c | -20.53543 | -49.49412 | 2026-04-16 04:32:00 | NOAA-21 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c96dc423-78dc-3e61-87a7-8fb296911721 | -21.18935 | -47.70825 | 2026-04-16 04:32:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df951f19-43d8-3ec6-b2ef-6b0383cfdb18 | -20.68634 | -49.39918 | 2026-04-16 04:32:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ab20f299-415e-32e1-831e-f65091b15691 | -20.1763 | -46.59097 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 568533a3-8e87-3424-8aa9-a24f6ff1652c | -22.92067 | -49.20733 | 2026-04-16 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9721becd-fbb5-3137-a255-733019930314 | -21.71347 | -48.42924 | 2026-04-16 04:32:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 75abb9c5-8143-3f0c-9e2c-98d7f9986dc8 | -21.46143 | -48.61666 | 2026-04-16 04:32:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36dd45c5-e000-3b03-9384-1693821ca564 | -21.70675 | -48.42815 | 2026-04-16 04:32:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 650c0ea2-6451-36f1-8f3c-32777b35d0e6 | -21.18901 | -47.71095 | 2026-04-16 04:32:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a31b5377-e9ff-3fe9-923a-c66bb07f7250 | -2.75359 | -54.59237 | 2026-04-16 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| faa7fa52-487c-3efd-b090-eedadb34269d | 1.80814 | -60.94035 | 2026-04-16 04:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b750ff4-4ba3-371a-a668-11a450ee9bd4 | 1.81326 | -60.93558 | 2026-04-16 04:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70a47bb5-89d9-35e1-a835-8e88c607d7cc | 1.80754 | -60.93647 | 2026-04-16 04:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cbd9e2e-7c73-35ec-9417-1c27e1f993fe | 1.81386 | -60.93947 | 2026-04-16 04:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b0f1011-cc3c-3d41-9873-589eb0cab58a | -11.6009 | -55.32716 | 2026-04-16 04:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa6a8b6d-2f50-3d5c-a07f-1f915ac2e02d | -8.36831 | -48.07977 | 2026-04-16 04:59:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e4332ae-18a7-3cb6-b990-df1e6905d1e9 | -12.84299 | -43.8207 | 2026-04-16 04:59:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3324b5ce-63fa-36a3-991c-070414c0aaf2 | -11.60428 | -55.32773 | 2026-04-16 04:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 017aa284-856c-35f5-a058-91e53bf50955 | -12.08536 | -51.22161 | 2026-04-16 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9a82f44-f3b6-3401-82ce-f39b3e983e0f | -11.42866 | -55.09714 | 2026-04-16 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f4bedda-c437-34d1-a6b8-8d15ae513716 | -8.36781 | -48.0833 | 2026-04-16 04:59:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32dfbf40-9a4c-3a02-a26a-befa578764f2 | -11.43203 | -55.0977 | 2026-04-16 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b414600d-386d-39a1-99e2-300f93c39ee7 | -17.67066 | -46.73502 | 2026-04-16 05:01:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75f79007-78d8-3b6e-b7ce-dcb74db152a6 | -18.51354 | -48.16571 | 2026-04-16 05:01:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd77cb1a-8352-3bb0-baf3-074a3cacd0a5 | -11.92295 | -58.0716 | 2026-04-16 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fb073e8-2d1f-3a50-8d69-196912f3495e | -17.67101 | -46.73199 | 2026-04-16 05:01:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da8bc552-ad68-3809-87b1-c995e72bf95b | -16.60558 | -43.35779 | 2026-04-16 05:01:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76cc3a05-b9ea-36c2-b035-551ec9d65913 | -11.91916 | -58.07091 | 2026-04-16 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ede95c4c-a406-38d3-af12-d4c17702a031 | -20.24712 | -46.53436 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49a801b6-f39a-3328-9a57-49315c86f6b7 | -11.84347 | -55.02106 | 2026-04-16 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4666179-2c7b-336b-964a-00b107f0a127 | -20.17229 | -46.5913 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c632e294-e051-33dd-98e6-bbfc2c079696 | -20.18829 | -46.59167 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f332b878-f17a-3feb-a058-e24aee3c9824 | -11.83953 | -55.02411 | 2026-04-16 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a2d19b6-b01b-3ce3-a603-271caabfe792 | -20.24675 | -46.53786 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85874592-0033-388b-a029-54baac54fcd7 | -20.18863 | -46.58852 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27169358-0c97-3076-82a5-6e42f39f1799 | -20.18269 | -46.58762 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d04d93d2-20e8-34a3-9d70-de545da246fb | -16.42905 | -54.92508 | 2026-04-16 05:01:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaef5663-71bb-356c-8791-b005a6f852c4 | -20.17781 | -46.58962 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e07e02d6-c549-3cfa-901f-1e939975ac01 | -18.51287 | -48.17121 | 2026-04-16 05:01:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bce74d3-b05e-3ce9-b164-4495b0317368 | -20.17747 | -46.58632 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 451a86d7-55bb-3f45-a0df-af35f6577861 | -20.18762 | -46.59171 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfa49ab5-0353-3b98-9b07-33c774a85416 | -20.17714 | -46.58954 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a269960-09d8-3b61-ad29-cc77b4afe5a7 | -20.17682 | -46.59275 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0888e221-88e2-3d32-b4dc-531753d69010 | -20.1716 | -46.59772 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6d6417e-2ddd-3e84-89fc-c1bed7ec1444 | -20.18338 | -46.58761 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd9618f6-9223-3da4-b24b-454f30c84c94 | -16.45946 | -53.43432 | 2026-04-16 05:01:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 630005e6-82f5-3370-9b8c-553acf6ccad0 | -20.1841 | -46.58094 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 901c24f7-5963-3342-b3bb-d19cf59a1a3d | -16.46285 | -53.43489 | 2026-04-16 05:01:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 117b34c5-a8be-3180-bbe6-7d7ddbacb064 | -18.51621 | -48.16746 | 2026-04-16 05:01:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee3667f2-1ceb-38f3-912d-702f88d75984 | -20.17193 | -46.59463 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f21366a7-64eb-37aa-85a9-7daf4ee4221e | -16.60505 | -43.36291 | 2026-04-16 05:01:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81540116-fbb3-3179-8efa-09e6c8398b4d | -20.17816 | -46.58644 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34168477-5716-396a-ac55-91833dcd74e8 | -18.49532 | -51.61406 | 2026-04-16 05:01:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 175c8362-9d66-3566-8637-c45b69470eeb | -20.18794 | -46.58856 | 2026-04-16 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b4398d3-1c7b-385e-ba4e-bfff1663a543 | -11.92214 | -58.07627 | 2026-04-16 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdd7ea14-d6ab-3d3f-b44b-35c6b1a3c177 | -20.68411 | -49.40067 | 2026-04-16 05:04:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d9a1135-0a81-3710-93f9-9070b4fbcd87 | -21.70679 | -48.4305 | 2026-04-16 05:04:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04929411-2f5a-37be-a5ab-36534858496c | -20.32524 | -55.00066 | 2026-04-16 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8850c1d3-3b6d-330b-b26b-029f0b3aacf2 | -20.53499 | -49.49598 | 2026-04-16 05:04:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27ef5980-f4bb-34e7-9d57-a4a8bbca64b1 | -20.32581 | -54.99691 | 2026-04-16 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26a029be-ac11-3cae-a6b1-904b993f5e41 | -21.71159 | -48.43091 | 2026-04-16 05:04:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5a16edb3-2827-3435-a637-eeb5230fe0e2 | -20.40976 | -49.75684 | 2026-04-16 05:04:00 | NPP-375D | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2b3f455e-5ddd-3f79-b404-94eee5e9f0c5 | -21.70739 | -48.42498 | 2026-04-16 05:04:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d08c52bd-03b9-3221-932b-ca9a5831a347 | -21.19265 | -47.37026 | 2026-04-16 05:04:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 154316f1-c2bb-3373-ac4f-ec1b73006a10 | -22.96219 | -52.70384 | 2026-04-16 05:04:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 012abf2b-0437-3e87-8b22-24f7ca34e9d5 | -20.32859 | -55.00123 | 2026-04-16 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 728663de-c317-3b5a-ac4f-3a81b9386a83 | 3.27316 | -61.19689 | 2026-04-16 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bfbf350-aa56-31d5-b837-794245455735 | 3.23671 | -61.21743 | 2026-04-16 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a634040c-1f20-3d78-8d48-a442284344c7 | 2.56829 | -60.54875 | 2026-04-16 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37c076bc-a9f9-30b9-a4e8-30f98d2d031a | 3.24608 | -61.2011 | 2026-04-16 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be6579d9-9a3a-32ba-acef-a19b3228d841 | 3.27024 | -61.19527 | 2026-04-16 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14275540-0a5c-3cc2-9972-f40c5f115470 | 1.80789 | -60.94516 | 2026-04-16 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17891d39-f6ad-3475-8a4c-b26138372973 | 3.27483 | -61.19953 | 2026-04-16 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebeafc84-8e57-3b3b-8690-e10a0f2b9657 | 3.23284 | -61.21804 | 2026-04-16 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d31577cb-7b8b-3ae2-a382-bf8c39cee935 | 1.81022 | -60.93566 | 2026-04-16 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19664ff3-aa9e-3795-909c-f1baf9b53e02 | 3.24147 | -61.19687 | 2026-04-16 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 353c148b-5f15-3a30-aadf-8be1b0ae2a6f | 1.81163 | -60.94458 | 2026-04-16 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 316339b4-8604-3268-a713-44070f44ebc5 | 1.81092 | -60.94012 | 2026-04-16 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13361d10-f755-3efa-acda-08108508dd27 | 0.74926 | -60.08786 | 2026-04-16 05:18:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 236d0a3c-98f2-3836-afe7-d47dbec4198f | -11.42855 | -55.09797 | 2026-04-16 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c263001-56d0-3e6d-ab01-7b3d9e60d744 | -11.84231 | -55.02035 | 2026-04-16 05:21:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4fb6d27-f894-3b53-810d-050ee91c7c4c | -11.42906 | -55.09445 | 2026-04-16 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf7136db-85dd-3eea-bcc1-5aa9799e7d3f | -11.8418 | -55.02396 | 2026-04-16 05:21:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b7daedf-8755-3ddc-8da6-3125099bc971 | -11.92198 | -58.07304 | 2026-04-16 05:21:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38b48e7b-e031-3824-aa2a-12576931f394 | -11.91853 | -58.07251 | 2026-04-16 05:21:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c628bb59-96bf-31f2-a712-2bea1ff4be97 | -11.83774 | -55.02335 | 2026-04-16 05:21:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ed556d9-35e0-3bdb-b2be-3d101b800d97 | -20.41094 | -49.75896 | 2026-04-16 05:23:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d595cbe-83af-3c8d-9556-8d0e36f137ee | -20.41139 | -49.75372 | 2026-04-16 05:23:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c6d47c41-6f6a-3fc5-a701-a6d82d49bdcd | -21.7064 | -48.43497 | 2026-04-16 05:25:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d8eae44f-4b15-3b93-bfda-73af36bd6984 | -22.96132 | -52.70423 | 2026-04-16 05:25:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 911a6d77-7dbd-3ddb-bef9-397db851755d | -21.70813 | -48.42725 | 2026-04-16 05:25:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README4.md)
