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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd55d765-12cd-3c9b-99b9-923f537cac5e | -8.22412 | -61.21618 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45afe9d8-e9f2-3107-88cc-845c96eac203 | -8.22356 | -61.21976 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98299d37-97c0-3609-bf28-a7ab99540f00 | -8.22301 | -61.22334 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3569e7ee-718b-3213-bf9b-c49c385fd2ff | -8.22187 | -61.20849 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59b09250-8b4f-3f4e-9b44-b52a27df17f0 | -8.22131 | -61.21207 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28c16a26-0b8e-327a-854a-76158e32bf2c | -6.27789 | -62.48362 | 2024-10-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16f9263d-4e30-3425-8987-36eb317bae2e | -8.83282 | -63.02817 | 2024-10-05 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90423856-a26f-3a96-a638-692646617505 | -8.83227 | -63.03165 | 2024-10-05 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 055bf644-e35e-3099-8720-79c001d62633 | -8.83116 | -63.01723 | 2024-10-05 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad2b881d-0675-3b04-8432-3c80b8f1a47e | -8.83061 | -63.0207 | 2024-10-05 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 055d3935-2a82-345c-99f7-3d4943140719 | -8.78149 | -62.83856 | 2024-10-05 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f38629-1b69-3af2-b505-e34415a52b8b | -8.77819 | -62.83804 | 2024-10-05 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a01ce332-ebd9-3dac-b75d-4b53e2684605 | -10.69312 | -63.46838 | 2024-10-05 05:31:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8aed674f-42dc-3276-856b-e30e9375d334 | -9.77708 | -63.14795 | 2024-10-05 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c94cfcb-6297-3777-872b-2f00a7a03342 | -9.71655 | -63.23111 | 2024-10-05 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7761e34e-e60e-38e8-a074-6246b6b91dab | -9.53818 | -63.15277 | 2024-10-05 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ee7f6a8-c1ed-3ccb-a024-ecc5b2f1a9e7 | -9.53488 | -63.15225 | 2024-10-05 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 938c0318-72c9-3537-8561-d843d5fed652 | -9.53148 | -62.98064 | 2024-10-05 05:31:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 529e7fe8-5a52-3700-88e6-6c92f00947ea | -11.99413 | -63.52644 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b4cb761-e521-3f04-9f55-94d2418a2c52 | -11.99084 | -63.52587 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acc60bb3-b571-3d2f-912e-d4bad6aa0b31 | -11.99029 | -63.52937 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04053888-e518-3427-b085-0963144188fc | -11.98699 | -63.52883 | 2024-10-05 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed48beb3-c03f-37d3-9af4-ec04afb96d98 | -11.00551 | -63.58023 | 2024-10-05 05:31:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c8c3ed6-4b45-33b8-9f31-4cddac0079ca | -10.88012 | -63.89859 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e02d194b-e5f5-3ca3-8e9d-9e6fc8d693f4 | -10.87736 | -63.89455 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1631cf7-b8c8-3115-bb86-4b6df8eb21aa | -10.8768 | -63.89808 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70468216-35c7-3c83-a667-9ab41a986e3a | -10.87401 | -63.91562 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 490ad153-78c5-399f-bd65-c50ce2cc7e35 | -10.87125 | -63.91157 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3260e703-eed1-3164-979b-b43ba548e02f | -10.87069 | -63.91508 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14ca8068-07b1-3ec2-86a7-cc58a29b6cf0 | -10.86737 | -63.91457 | 2024-10-05 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e380ea42-4716-3c4a-a669-8e69b0662887 | -10.85007 | -64.17027 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afac19e1-110c-3fab-b33c-6f55c7e8cdf4 | -10.84674 | -64.16969 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16536bcd-121d-3394-9ed7-fe0d5234c1f3 | -10.84618 | -64.1732 | 2024-10-05 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcf1b46e-a50a-37fe-b0cf-9ceda86dfab8 | -11.87854 | -63.28868 | 2024-10-05 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d3bf21cd-bcbf-399e-a51b-cb9febe69d42 | -11.87524 | -63.28815 | 2024-10-05 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38650bcc-ad55-3b1d-9003-c1888abfabe2 | -11.87193 | -63.28762 | 2024-10-05 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6c93e27-36bb-325b-9b63-a7b4fe68ec8d | -9.24106 | -65.60122 | 2024-10-05 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76a70a8b-097f-3bb6-a9a7-4647d4fe2cc3 | -9.2404 | -65.60524 | 2024-10-05 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ad03823-7386-3569-8487-afd57fc4cd3f | -9.23686 | -65.60466 | 2024-10-05 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8034b1bd-d74f-3f40-b3a6-fd7688cd8cce | -10.09988 | -67.34952 | 2024-10-05 05:31:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0023c85-dd08-3f99-9c15-10aac80b48c0 | -8.86416 | -67.48534 | 2024-10-05 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a34dd8b2-141c-37a3-b83d-b50d8c50cfe2 | -10.98 | -68.45764 | 2024-10-05 05:31:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08a104f1-55c2-3550-a391-ef1c8b18699d | -10.95307 | -68.34845 | 2024-10-05 05:31:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e64e13b3-4b29-301a-8fce-35a4806e53a0 | -16.10264 | -50.2406 | 2024-10-05 05:31:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a90579f5-3e26-32ad-8c76-f9a37a4d4edd | -16.10195 | -50.24834 | 2024-10-05 05:31:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 40261486-e730-39e9-bfa3-921c1759f11a | -16.09536 | -50.24175 | 2024-10-05 05:31:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 209266b5-47b0-3e24-8cc1-1bd076b93928 | -16.08819 | -50.24158 | 2024-10-05 05:31:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c5b989f-0720-3a98-a6cd-b8d4161abc90 | -16.08416 | -50.24319 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff4144c1-0ca2-3ce8-ab5e-1dfec0b2d541 | -16.08358 | -50.24927 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34cdebfd-838b-3db4-a7d5-30690c0ef81d | -16.08066 | -50.24543 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e6c5abbd-35a4-3000-a31c-b8d1371a1afe | -16.07667 | -50.24639 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f42b302d-480c-3abd-b1df-2b229ab81d82 | -13.14842 | -51.18597 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 797db90a-1328-30bd-b397-5f2499901564 | -13.14828 | -51.18492 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 647ee709-cbed-3d3a-ac35-c5791eab00e7 | -13.14779 | -51.19158 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ba5cbd5-6bed-3c5d-b880-be1b44e9564a | -13.14769 | -51.19053 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ade4ff2-db2a-3acb-9214-784a7f22419a | -13.14716 | -51.1972 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f967b34d-6944-3966-b497-b353809a0c5e | -13.14709 | -51.19617 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50fcca30-17ef-312d-9a09-cd3d127a956e | -13.12731 | -51.13756 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c372479-3223-3013-ad31-29878e99acbd | -13.12687 | -51.13631 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31f427be-85bc-3915-a8e6-232a560ac956 | -13.12628 | -51.14201 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 990840d8-ec0a-3954-9af7-900cb8049475 | -13.12077 | -51.13677 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0790ea9-ef90-3aef-9ff9-7a22b322e612 | -13.12032 | -51.1355 | 2024-10-05 05:31:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f97e67e1-95e5-3c0f-b680-22e1240dc7e9 | -13.11973 | -51.14117 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b455535-24ba-3f13-be0f-62952010556c | -13.05755 | -51.1152 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3ec7489-1977-3f77-891f-4cd57f75bedf | -13.05691 | -51.12086 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14c04658-e3f9-329c-9d41-45cf2e8560ab | -13.05654 | -51.11713 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0dad094e-f70a-359d-889a-e138567e8c72 | -12.99086 | -51.1183 | 2024-10-05 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4cfefdee-90b5-35a9-8190-8d8e3f142efc | -12.82707 | -50.55688 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3aca8cc4-1631-3153-85d8-7e7b4da9f68d | -12.82642 | -50.56301 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5a5392a-bc47-38bd-b916-fa8647e392ec | -12.82032 | -50.55601 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7c22b79f-dc74-3ae7-bb62-0729f94c0b7f | -12.81967 | -50.56216 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36a5bf8b-8002-3c84-bfdf-ecb083adac8e | -12.8117 | -50.54726 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4d502372-1638-32fb-933e-0be200672f6f | -12.81101 | -50.55338 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2fc8494f-35fa-3350-bb25-c96fa9339291 | -12.81032 | -50.55951 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ef05e162-4fbf-3eaf-89b3-edb8620103da | -12.80682 | -50.55431 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b9edfde0-c755-3517-861b-dba6562f25c4 | -12.80617 | -50.56045 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ae415232-632b-3e3e-9711-24e12bdfe94d | -12.80426 | -50.55255 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0a3c6b50-e228-3d7c-83b4-c213d6f4b343 | -12.80357 | -50.55868 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 93ea1b58-583a-36f4-b196-6e5eb5ad7d20 | -12.80072 | -50.54729 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 036eddf5-c104-3856-888f-e2a1ab0f72b4 | -12.80007 | -50.55345 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2f56c5c1-851c-386a-97a2-1cb022cdb419 | -12.79943 | -50.55959 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d65623b9-a33f-3754-b500-16b6012afcd6 | -12.79683 | -50.55785 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9f1327ab-920f-3cfe-a1d1-9515d3075308 | -12.7894 | -50.56315 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8eb5795-b81b-3247-a590-9e6616c72a50 | -12.78722 | -50.54557 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 36e50fda-af87-3f88-b8dd-bf470b023e99 | -12.78657 | -50.55173 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ab3b3f75-ab4b-32f9-b388-ad5b65e14e5c | -12.78529 | -50.56401 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ec8b8ba0-e8e6-33d1-b18c-ad986e881fab | -12.78469 | -50.54391 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 59fc3eeb-3d15-3b79-8744-a72d2225b2d9 | -12.78401 | -50.55005 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b063ece9-f6a2-3036-841e-2ce82963a83e | -12.78333 | -50.55619 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4eb8f09e-bdd8-3c2a-86d6-8a955e85d49e | -12.78265 | -50.56232 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2f503d0-3463-3451-88f3-8ce55225bd47 | -12.78047 | -50.54469 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 834fc965-74eb-3088-8707-237f92eb82a7 | -12.77983 | -50.55086 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 089708d4-5613-3d28-95b3-723cc19f59c8 | -12.77919 | -50.55701 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d2ddbec5-6de3-3124-8c26-52c0c660bbaa | -12.77727 | -50.54919 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d3165b08-6839-3a27-a044-f63af7eac9c4 | -12.77659 | -50.55535 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fd6dafa6-0f8c-3c48-9276-bd601efb5b59 | -12.77591 | -50.56148 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba77faaa-6083-3472-a893-f235e5f63292 | -12.77372 | -50.54383 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f7f8a476-d8c7-340f-aa82-0d3df352c432 | -12.77308 | -50.54998 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e20e8d76-4319-330b-849a-c5dd0dae0a3c | -12.77244 | -50.55613 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3bb7d20e-8961-31b1-a5f6-45fe52a62bce | -12.77119 | -50.54222 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |


[Clique aqui para ver as próximas entradas](README136.md)
