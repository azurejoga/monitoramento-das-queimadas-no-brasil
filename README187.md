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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9acf5253-acba-3cf9-8376-4822fbb5ed9e | -12.87535 | -62.7743 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50f9d000-6ed7-3bc6-aa1e-c633e17c997d | -12.87477 | -62.77821 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb763169-cae4-3773-8dc2-6b767ba2cb70 | -12.87131 | -62.77766 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2438b196-374c-3605-a6f3-3b9851497ffb | -12.86784 | -62.77713 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef33992c-f1e7-3ff9-8b89-dbc5bd9602e4 | -12.86392 | -62.85205 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 564f4756-9bab-33a8-a526-f0d00cc7aee0 | -12.86379 | -62.78049 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bb49220c-7f0a-3246-9d43-3603f03b6ae2 | -12.86265 | -62.78829 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24443fc5-39db-3718-bae5-3fd272da07f1 | -12.85918 | -62.78776 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4b70e666-34aa-3ae8-a618-69a785978cd6 | -12.85571 | -62.78722 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5ac710af-7ab5-3ed4-856f-38275967dd1a | -12.85514 | -62.79112 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 198ff61b-87dd-3c3f-97a3-38cfc3005152 | -12.85015 | -62.78689 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1cd150e0-52ec-329f-b382-6a0243b9c7be | -12.84957 | -62.79078 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5e6c5de-4028-3e22-b59d-df57d4866db2 | -12.84821 | -62.79005 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8f9d6049-896c-3dff-a56b-36c601a50bd7 | -12.84707 | -62.79784 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d63a89fd-ae6c-3feb-9de6-30afae074cc6 | -12.84318 | -62.80968 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 479d84f2-a706-3f37-ad3a-953d093458ea | -12.84205 | -62.7936 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6302ef07-df35-3aa1-a964-c1f026051a24 | -12.84201 | -62.81744 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35a9f505-9971-3983-b03a-a72a6a7116a8 | -12.83855 | -62.81691 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35410cd2-cd9a-341a-9876-70dec157ddb5 | -12.838 | -62.79696 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a3ba44d-8edc-378b-928f-f714f2f6d05e | -12.83683 | -62.80474 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6bbceee1-38d0-3045-9f8a-a6642817472b | -12.8275 | -62.89042 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e2129f3-3b80-3a76-9db9-93358512759f | -12.77806 | -63.0319 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32da0962-d60b-34d0-8b39-7b462f7cdb78 | -12.77802 | -62.91432 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fe33ad2-1248-388f-bbac-b2a680359f52 | -12.77463 | -63.03136 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91ba6515-18de-3ca5-bee2-7c25484255a4 | -12.7692 | -62.75855 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1b05ce2a-b5bd-3437-a5e0-dabcb35b86cf | -12.75675 | -62.91498 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e16e95bf-257d-3b7d-af44-c7e1ad01d8ac | -12.75099 | -62.90621 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0542efe1-3e5a-3725-8ef0-7ca948b19917 | -12.87739 | -62.5335 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 28f16a79-92b7-3964-9dfd-94fb2999d5e5 | -12.87448 | -62.52898 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 564b2832-6740-3685-8921-5ac96d763dcc | -12.87389 | -62.53296 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 056965a4-cfaa-3e0b-988f-d9ac203e0faa | -12.87097 | -62.52844 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 2dc91bc7-d62a-38d0-9420-bd8fdc60bcd6 | -12.87038 | -62.53242 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1b3960b7-5208-3e24-86c9-09e839156971 | -12.86979 | -62.53641 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1adc0a78-c0f4-302f-a3ef-dac2eb485b1b | -12.8692 | -62.54037 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fe1bcf62-6bee-396c-9975-208143866e60 | -12.86747 | -62.52791 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9666d308-587e-3eff-b573-691925408bb0 | -12.86688 | -62.53189 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 75d47849-c87d-36aa-a2d5-3cc09046f5c4 | -12.86629 | -62.53587 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d9b232ec-be41-3e28-93dc-f26d75f850c3 | -12.86569 | -62.53985 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21ee8bca-e8eb-3928-9479-efa6313595bd | -12.86219 | -62.53931 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d98caede-9039-3410-8c39-0b3b660b4a1e | -12.8616 | -62.54329 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 545b4781-5f77-395d-b9d2-5ca6216cd838 | -12.86046 | -62.52684 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2cab7355-b05b-3702-9cfa-a7e3b8b14fd3 | -12.8581 | -62.54275 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0e7352f-6dfb-372f-b683-191b020f1398 | -12.85459 | -62.54222 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9595526-a29a-30a4-8b74-7c498507b37a | -12.85109 | -62.54169 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b507371-6057-345c-afdf-30df4c3c1175 | -12.84933 | -62.55361 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5f345473-6578-3c60-a7e9-d4e296b87520 | -12.847 | -62.54513 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39097c10-6d56-373c-9121-7425aacc44d6 | -12.84643 | -62.52471 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe3ab0eb-9b3a-3986-9918-ad863c2bcd61 | -12.84641 | -62.5491 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6fa6724-9068-3647-9606-c9c0585903e7 | -12.80671 | -62.52678 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af6cbf2f-0d45-3e88-b801-7315a4301445 | -12.8032 | -62.52625 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edff7b14-115a-3153-a9fa-463e55e1f45f | -13.00327 | -62.71292 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 808cdc28-2d26-3610-8863-0eaa1a29a553 | -13.00269 | -62.71684 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c34e3de-a38b-3cc0-9e4c-0ae547b92acc | -12.99863 | -62.72025 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d458002-4b85-3891-a0a1-3be5d7db742c | -12.98933 | -62.71079 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ae97729-c5eb-34dd-be2f-e0876e1ac94f | -12.98466 | -62.69398 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f79dba90-df33-387f-ab0e-db9ed64842d6 | -12.98117 | -62.69345 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0828fb54-efd9-3fc3-b078-15d1b4db8472 | -12.9806 | -62.69739 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8723ae37-7f84-3b03-a7e3-33329ed334ec | -12.97597 | -62.70472 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37e3fdfc-2dd6-3768-9c68-31d5cb4867c5 | -12.96121 | -62.65106 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb444561-9c78-3ea4-8503-fa2cdfc07a92 | -12.95827 | -62.67078 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 340e10b6-b57c-333b-ade8-36c8eb689717 | -12.95769 | -62.67472 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcf31286-9f7e-39c3-afd7-6af770808b3e | -12.9571 | -62.67865 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3c36057-417e-351c-8bd7-5b09c09b8dcb | -12.95651 | -62.68259 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90b4b281-0933-3b2e-bf90-50d961a7e972 | -12.95475 | -62.69439 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfe7105d-026e-32e5-8436-e8345bd1fff2 | -12.9542 | -62.67418 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fa24c89-9c4e-312e-9ec1-b33783664513 | -12.94845 | -62.61675 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 951d55df-c3cc-3fa0-8cf2-9540893907ca | -12.9472 | -62.69724 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d22d9762-ca8a-350f-8022-38e397ea0bd1 | -12.94087 | -62.61964 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2854d4cc-6a38-355c-bea0-7974937d507b | -12.94023 | -62.69617 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7504a334-b3f0-3e10-bbb2-dd6c74a81365 | -12.93616 | -62.69957 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52add7c1-22a4-3ad1-9321-ca42ed8fd70f | -12.9292 | -62.6985 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7ad5514-aee7-3eeb-9b11-6656d0aa1ced | -12.91817 | -62.70082 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4427a7b7-0542-3305-997d-785c97382195 | -12.91469 | -62.70028 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc82539e-9326-3253-85e9-9a825374acfe | -12.89898 | -62.66168 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfac4571-44bd-3617-abfa-e3c42ef82511 | -12.86484 | -62.72473 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1d5827e-94fb-3dc4-8ba4-bcbe5bc38d3c | -12.46887 | -62.68759 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f15ed454-f0ef-32ff-abf9-35eb9a2fed66 | -12.87799 | -62.52951 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4dc8cbf6-5232-3c0b-a9f6-00c85f5b9836 | -12.86861 | -62.54436 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 698c33fe-c8dc-380c-8c4d-1c8e263ced7b | -12.86396 | -62.52738 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8bb65e88-d9af-3631-9a6e-1d729b91c7bf | -12.86337 | -62.53136 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 67bbcd10-e039-3b70-bb80-36083ac30384 | -12.86278 | -62.53534 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6945ae8a-6147-33f1-8c85-e677a205413b | -12.85987 | -62.53083 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83165479-7813-3893-9223-fe637053135c | -12.85754 | -62.52232 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e2504649-cf56-3881-9a0c-995e06b0d398 | -12.85695 | -62.52631 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 54295914-606b-39cf-b0af-c88e323001d4 | -12.85403 | -62.5218 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 36386d3a-8037-3b90-a0dd-8f210eaaf475 | -12.854 | -62.54619 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0d2219a3-6689-3966-826a-83e5622ff631 | -12.85342 | -62.55017 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e021fd3-d1e6-375b-9299-0975361dd24d | -12.85283 | -62.55415 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 46c3cd70-c1a4-3829-908a-e173480cbb9a | -12.85053 | -62.52126 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d4b9053a-bf5b-322c-b85e-74bbc1016913 | -12.8505 | -62.54566 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4591f712-6e28-3f46-9684-adf5b0dabb2c | -12.84991 | -62.54964 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ca166d5-f117-3840-8853-61f8b24a7ec9 | -12.84876 | -62.5332 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb26cb7f-f866-349b-a135-3637d5ff9c38 | -12.84702 | -62.52073 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a126d0d8-a2cb-3b06-ade0-1c48e034d5c0 | -12.84526 | -62.53267 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7ed80dad-1b29-3ddb-8e5a-9b535ccb0e2f | -12.84351 | -62.52019 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82f9f25a-b120-3fd4-85b0-256e56d1e199 | -12.84293 | -62.52418 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aff8165a-041b-3829-8185-7aedf079a11d | -12.84175 | -62.53213 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f8038a06-5e14-3d0b-866d-79db8be1f500 | -12.83942 | -62.52364 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dc7d3b90-da0d-3849-82ee-72b2648a5bc3 | -12.83825 | -62.5316 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 37e7cb5a-dfe0-34c6-899b-452f5029d6a5 | -12.83592 | -62.52311 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README188.md)
