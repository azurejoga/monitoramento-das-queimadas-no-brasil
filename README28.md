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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8661efc0-2c9a-3ff4-8671-e15d291bd86a | -15.28196 | -56.86415 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e74093d0-84e1-3310-a735-bfffbc1adda0 | -15.34984 | -59.40108 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 070f231f-b4a4-3113-9f2e-ee5111e6f2d9 | -16.11486 | -53.81339 | 2025-09-20 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b93a1e69-5a90-304b-bdab-edd406db112a | -15.91524 | -59.45543 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2e3df9d-53f6-3038-8a41-8f8b2434c1bb | -15.77738 | -52.187 | 2025-09-20 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb143695-abee-3fe1-a6e1-f18c4c751fee | -15.29509 | -59.41937 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e73f7237-1762-3fe6-87fb-e0d9764e69a1 | -15.29847 | -59.4199 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f79381-f5ce-305a-9b6a-68467eb6be98 | -15.79009 | -59.47348 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d07b0d9-479c-35e7-a0db-aa1cdbfe0ece | -15.92265 | -59.42941 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aa7e684-b9ed-34f2-a9bf-e6c3f164ac08 | -15.28344 | -56.82583 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54ce6101-9b97-3910-add8-bc527d58c9d0 | -14.83582 | -60.25461 | 2025-09-20 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc2c0bd0-c18d-36b3-a10e-7adfd263ce23 | -13.22832 | -57.1252 | 2025-09-20 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2253274-3981-304c-843e-de5c338c100a | -15.27507 | -56.85814 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b283075-320d-3b30-9e5b-697005817516 | -11.63206 | -52.86403 | 2025-09-20 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 149744b1-4ae9-324d-8d7c-2781141e4ffb | -15.27195 | -56.85276 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 656f4793-b729-3001-9fa0-1b0438a86fef | -11.99713 | -63.52268 | 2025-09-20 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a17a5ab3-9e87-3411-baa0-1a46cdf16571 | -13.22753 | -57.13204 | 2025-09-20 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 218aab4a-7ae8-31d4-adc1-57e085a4bbdb | -14.84246 | -60.25572 | 2025-09-20 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085e3b2f-0aad-33cd-9112-4ba3813a8fef | -15.28857 | -56.81687 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfcb6053-40d4-3fab-ae6f-c4176a116f87 | -15.27572 | -56.85349 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d6b0bfb-01ce-3a25-9374-578f4541e771 | -11.63272 | -52.85907 | 2025-09-20 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b04e9c24-e76e-3e9a-b368-8054590ffba6 | -13.22769 | -57.12949 | 2025-09-20 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cb3877e-2c1e-3998-9659-03cd3ddb585e | -15.30891 | -56.80997 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3eeedfa-2ba1-317c-9e2f-d88492aad47b | -9.55533 | -67.47549 | 2025-09-20 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 999c44e9-4ecf-3b94-bff6-4bf9ebc07e1c | -15.29237 | -56.81739 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1a94163-c13d-3234-a3c3-74f15849c4b2 | -10.23206 | -67.35189 | 2025-09-20 05:18:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a142063d-31f4-3c66-85b9-649480201398 | -15.28411 | -56.82105 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64c47e12-9e38-3c9a-9d9c-497dad6ced8f | -14.84191 | -60.2593 | 2025-09-20 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b579a602-3a73-3a63-b802-517f8072f2ea | -15.77259 | -52.18304 | 2025-09-20 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6976273-cc2e-337b-bbb9-c8e99c4a2dc0 | -12.09336 | -63.44141 | 2025-09-20 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4758561e-d987-35af-8f7d-d3288a93b35d | -15.31203 | -56.81537 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2465e468-565f-35ce-96c8-9c8f65ffcb45 | -11.64606 | -52.86588 | 2025-09-20 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccce2c3e-5623-3ed4-8c3e-29caf5507dd2 | -15.27949 | -56.85419 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f7c4f70-96fe-312d-8725-03a4e6f02369 | -12.21819 | -64.21594 | 2025-09-20 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2404feb-3efc-3bf3-9159-e340da208590 | -15.9215 | -59.437 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b690bd6a-4bd1-39b9-9fb9-145838aa59d6 | -14.26917 | -54.61081 | 2025-09-20 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 378a8bfe-4ed0-38cb-ac95-04a347689f7a | -15.33911 | -59.40323 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e417dd1-09a9-3028-815e-b4e772d8e5e8 | -15.90116 | -59.41048 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47ac62e7-1143-340e-9901-1989e63b038d | -16.11024 | -53.8125 | 2025-09-20 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c84dc5f6-255a-3836-b480-88d289e3789b | -10.22733 | -67.35094 | 2025-09-20 05:18:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d46ba4e8-df42-3bf3-ac60-208fc718627e | -15.90173 | -59.4067 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60814075-81ad-37da-904d-ce368ec2a754 | -9.94742 | -66.75104 | 2025-09-20 05:18:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eba8f2e-5f11-315a-b347-f3d3e6b9a4d4 | -15.27261 | -56.84806 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4142c91f-421a-3366-8795-4f0191116ed6 | -12.30559 | -60.47788 | 2025-09-20 05:18:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7df7dd63-0a5e-315b-9f36-3f0909ad49e7 | -9.92384 | -63.11802 | 2025-09-20 05:18:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8735a76a-2fc1-315e-9fa1-afd1f1f5ff41 | -10.38963 | -60.79951 | 2025-09-20 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37d80b3b-fa31-316a-ac3f-e4be77b29294 | -15.31133 | -56.82029 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b5b5062-217e-3177-84d0-d658c64cd97d | -12.00803 | -64.83847 | 2025-09-20 05:18:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf486206-2284-3de6-aef4-8bd70d803066 | -15.82387 | -59.50906 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11468628-e210-396f-9130-7901fe07069e | -12.85751 | -53.00607 | 2025-09-20 05:18:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4c205465-a909-3b19-9bc7-0103e36cf2bb | -12.12439 | -59.88239 | 2025-09-20 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93df69ba-5e51-3579-871a-f983786ec063 | -12.36332 | -60.77715 | 2025-09-20 05:18:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb5941d-14a7-3f38-9d5b-7b9b70371b81 | -11.63739 | -52.8597 | 2025-09-20 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a036b905-7fca-363e-9adc-7e3350069fee | -15.3346 | -59.41016 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f385e78-e412-3e68-afb5-05ff8f4223b0 | -15.92207 | -59.43321 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29899bc4-2460-3f64-a30b-ed3def19762f | -15.91527 | -59.4322 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b825d47b-f9e4-3f27-ba54-21f0bb9ce856 | -15.30511 | -56.8094 | 2025-09-20 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbcae28b-9f20-3e11-98fa-5d40889c70c1 | -13.22814 | -57.12774 | 2025-09-20 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6aa3c302-f3dd-3832-ab66-cee75b068558 | -9.6046 | -64.03831 | 2025-09-20 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92b1da96-08d9-3328-8eeb-b58cc75f829b | -15.29566 | -59.41551 | 2025-09-20 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f1a41ad-820a-31a1-bb7b-e74c746409a0 | -12.59387 | -62.96498 | 2025-09-20 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49a00621-51f5-38cd-be6a-86435f69ff85 | -9.9154 | -63.50561 | 2025-09-20 05:18:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0058227-6fa4-3eaf-8b75-253e5b6d4e14 | -12.85815 | -53.00106 | 2025-09-20 05:18:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 948388f0-cd7e-39c1-b1b0-0a4dba3b5a24 | -20.3547 | -48.793 | 2025-09-20 05:21:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43cd0323-e3d3-3db9-85af-fcac669a2f3e | -23.48176 | -52.18701 | 2025-09-20 05:21:00 | NOAA-20 | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eea7a9e8-0e80-30fe-a505-507f93fd5530 | -25.04807 | -49.24104 | 2025-09-20 05:21:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5bcf0cdf-a512-36f3-98e8-7cd75bc6aae1 | -25.04254 | -49.23584 | 2025-09-20 05:21:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f71c38fb-679e-3a88-b90c-ecc729001691 | -20.3527 | -48.78667 | 2025-09-20 05:21:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc962fbc-1df4-3286-a2f8-89fa7d1d6af7 | -18.3286 | -55.04959 | 2025-09-20 05:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2cdaa5e1-4d8c-39c9-a7e6-63141d846283 | -23.95947 | -49.76877 | 2025-09-20 05:21:00 | NOAA-20 | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 027446ba-9ee1-3b0a-8d75-d701f97258c1 | -20.34794 | -48.79261 | 2025-09-20 05:21:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 192da855-b2a9-3596-b2bd-315ebce36be5 | -20.35218 | -48.79293 | 2025-09-20 05:21:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99c71fd6-9f7f-377c-ac6f-b721bd11369d | -22.26056 | -55.98975 | 2025-09-20 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26245041-0662-3f0f-ae84-06de631305db | -19.61247 | -57.7481 | 2025-09-20 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9066aaf9-a9d9-341e-8af6-cc4cac54acbd | -19.54384 | -48.04128 | 2025-09-20 05:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 44eba686-5c8b-3646-ade5-be7b43645f13 | -20.34842 | -48.78636 | 2025-09-20 05:21:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c61cda8-e2d9-3667-8f4b-4b6b2bbe727e | -22.25616 | -55.98925 | 2025-09-20 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60088c07-546d-38ec-af07-bb01b5190533 | -20.60457 | -56.7277 | 2025-09-20 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5b96e3e-6c25-30c1-8f0e-a9b4e0cd062e | -20.33063 | -49.20479 | 2025-09-20 05:21:00 | NOAA-20 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63301e2f-6309-330d-b0ac-1dec276482d9 | -22.62687 | -54.97011 | 2025-09-20 05:21:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 4f278572-7a48-3867-8024-e25f08f6f6b0 | -22.19133 | -49.64788 | 2025-09-20 05:21:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 80c2fcfd-cdbf-3335-9435-0256f0836161 | -25.0412 | -49.24091 | 2025-09-20 05:21:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| edbc0a57-4dfe-3fdf-85ec-7c3a4d407a01 | -20.32907 | -49.20503 | 2025-09-20 05:21:00 | NOAA-20 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25e5fde9-8e25-3c90-a938-aaf101eb2f77 | -19.09426 | -56.50686 | 2025-09-20 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 832dabc2-828a-3ed7-ab66-3174fff15d61 | -18.32473 | -55.0445 | 2025-09-20 05:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9d8abb03-7548-30a7-bc0d-9f5cd39f6d38 | -22.6263 | -54.97535 | 2025-09-20 05:21:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| ad0dc400-0305-31e3-9c96-95d46cb5bc92 | -20.50303 | -56.87611 | 2025-09-20 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 807e32a4-b628-3594-87cb-869cdee5c9a3 | -19.61314 | -57.74321 | 2025-09-20 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 145d43b0-631b-3844-9a0e-745e11c56d32 | -22.19156 | -49.65363 | 2025-09-20 05:21:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| b05c7abf-92a4-335e-b903-16b7ea4ea894 | -20.60508 | -56.72373 | 2025-09-20 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df605e8d-7bf0-325d-8b56-0a57a1f65c63 | -22.19206 | -49.6476 | 2025-09-20 05:21:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| fdb4abce-beb6-3bea-aa05-7f44f5325401 | -23.96053 | -49.77347 | 2025-09-20 05:21:00 | NOAA-20 | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5abf57db-6b61-3a95-b053-5048a6eefdb4 | -25.04218 | -49.24186 | 2025-09-20 05:21:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ce8aa4de-e568-3096-8688-bf24fbad8646 | -19.61628 | -57.74866 | 2025-09-20 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 37437a3f-89b1-3359-9286-a371b4ccea4c | -20.49943 | -56.8719 | 2025-09-20 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4585e036-acd5-323f-ba88-d29437043198 | -19.60933 | -57.74264 | 2025-09-20 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f36de2a2-3d96-3a06-b81e-d5a80c5f7371 | -22.21399 | -56.2009 | 2025-09-20 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d508f24d-be39-3cc2-9da4-92b39144e71f | -18.32916 | -55.04509 | 2025-09-20 05:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 25930ff4-e207-3f8b-9ec1-5e26e5d332a3 | -22.19739 | -49.65472 | 2025-09-20 05:21:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| a8153e7a-ade3-354a-a705-6a9c41e577db | -22.19088 | -49.65392 | 2025-09-20 05:21:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |


[Clique aqui para ver as próximas entradas](README29.md)
