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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9088954e-1486-3da8-938d-de1b39b94bbf | 3.28451 | -60.61763 | 2026-09-29 05:53:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3826dc04-4ce4-319b-9666-26e1d12bd55a | 1.82133 | -55.62159 | 2026-09-29 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a46c1ce2-7836-3248-a9f9-ecc4177a889b | 1.67406 | -55.90492 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28246919-c301-3dcc-b04b-34a96c0921d8 | 4.27925 | -59.80918 | 2026-09-29 05:53:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0910ec0f-8ab4-32f6-824f-ead1ab58659f | 1.86346 | -55.57196 | 2026-09-29 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ebc356d-67a2-38f0-8d79-c4f10ae1f170 | 4.27839 | -59.80639 | 2026-09-29 05:53:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f694d590-44e1-3bc9-bc21-0e2fc5d8f6ab | -4.04618 | -54.9237 | 2026-09-29 05:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2a75442-5bd3-3113-a878-bc1a429ab2a2 | 1.67106 | -55.88697 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac0370af-200c-33a6-adc7-f44170159ad9 | 1.86883 | -55.56631 | 2026-09-29 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0efdd63-62e4-31f2-829e-4dcf9549c712 | 1.67332 | -55.90045 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23f61cf2-fc41-31f5-b729-0fffbf418873 | 1.67121 | -55.90382 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c29a52c-147f-38fb-acf7-8c578d485452 | 4.07564 | -59.94603 | 2026-09-29 05:53:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d62dd0dc-51f7-32b3-89da-012ac12b7471 | 1.66905 | -55.8903 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 72461544-c8a0-36ff-a422-0b69e641346a | 1.67648 | -55.89826 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 656476e0-f308-3574-8109-e76a25dabbf6 | 2.78957 | -60.0043 | 2026-09-29 05:53:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32b1567d-0d84-35cc-8d67-f2e855acd84c | -4.04525 | -54.93036 | 2026-09-29 05:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 992f9c62-741c-3716-98ee-dc1916c55302 | 4.07494 | -59.94188 | 2026-09-29 05:53:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e149b7e3-d82d-3912-aca0-92946a4bd5c3 | 1.69267 | -55.94271 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f62262e-55f0-3458-bf84-4fdeadd304a9 | 1.69552 | -55.94064 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd7bebd-a408-38aa-8e47-4863e334740f | 1.67049 | -55.89933 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c6aba80-725d-3603-9c1d-e6fddb1e766b | -4.05224 | -54.9307 | 2026-09-29 05:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d45e370c-9b4e-3f5b-8921-8290b8a0f440 | 3.5859 | -61.24828 | 2026-09-29 05:53:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a80dec4-d075-3a0c-9000-5507a48c7f47 | 4.41573 | -59.81666 | 2026-09-29 05:53:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8b762cd-0349-32fa-9c0f-39b7b9e88853 | 3.28027 | -60.61835 | 2026-09-29 05:53:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d2b04e7-9759-312e-a3d6-bae946cc1762 | 1.86403 | -55.57166 | 2026-09-29 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0b7cf34-f79d-3443-b6a0-51a7d1addac2 | 4.2791 | -59.81063 | 2026-09-29 05:53:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3be83bb8-538b-3b9d-828f-9cbd77a2c65c | 2.79263 | -59.99461 | 2026-09-29 05:53:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d5a426-a2aa-3ded-95fe-e0e40be4c571 | 1.67181 | -55.89146 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd716b01-74e2-3c84-b7af-65f40bf13857 | 1.67257 | -55.89597 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f17350c-507c-309a-82da-292893a56aeb | 3.28154 | -60.62631 | 2026-09-29 05:53:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04ccca07-0ddc-3531-a828-f5d08cfafdd1 | 1.82668 | -55.61599 | 2026-09-29 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41ee0d41-4cd7-3798-bf36-625ab84c0ff6 | 1.6934 | -55.94713 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61bc8ea3-49ec-3241-ab99-510a35cffe9d | 3.58532 | -61.24469 | 2026-09-29 05:53:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da5369d2-d325-3ab5-a1bb-d8475e55e3b3 | 1.69193 | -55.9383 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8dc9ec8-1ce0-3176-96ee-747fe0c9fe44 | 3.28218 | -60.63028 | 2026-09-29 05:53:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30871850-1c82-3f1f-af65-e2522f067856 | 1.82745 | -55.62072 | 2026-09-29 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 236a228d-7ea5-3732-9c00-8a8c9ae5114d | 1.86938 | -55.56607 | 2026-09-29 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd1d5e52-f876-3576-98e6-3fce8c0be1ca | -9.13825 | -67.93143 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeadf614-8145-321e-8bb5-48ace8e84a97 | -10.38998 | -61.26471 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16d1d275-4cae-3dae-86de-7f38ea4fa899 | -10.38628 | -61.25377 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| c53663d8-8508-3dc1-9171-3ad0fe88a0dc | -10.38239 | -61.24454 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 844dae42-31d0-391b-8714-31229ce2f1c4 | -7.79819 | -73.00883 | 2026-09-29 05:55:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bbaaee2-f887-316e-91b7-354844bd025f | -9.11246 | -67.86129 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af523ab6-64d8-34b2-a9fb-8f39102bc2e2 | -10.39672 | -61.25208 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9c2a53a-d0bc-3a08-9c2f-b4f936614f4f | -8.9079 | -64.14612 | 2026-09-29 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea159f00-40b9-30e3-83f7-f47185d6b247 | -10.38495 | -61.26378 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 283f404c-043e-3575-a0b4-7456d6ca01df | -9.1688 | -67.72852 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b77d123d-dfaa-39af-85df-86ec7d84df79 | -10.37622 | -61.2525 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab31f04e-7a22-3b5b-ad52-b1b420bb1b59 | -8.01816 | -71.2545 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ca7ebc1-9600-37aa-bac0-dd56e0fbf95c | -10.39504 | -61.26504 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7656615f-9708-3f07-9eb5-8f50a86acda3 | -9.92588 | -60.72332 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8677d162-c2c9-3c33-ac6a-13ffeaca890a | -9.16494 | -67.67603 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6644e25b-a1c0-34f1-b47d-604b77dfa537 | -10.40281 | -61.24387 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06c2572b-7ee6-3614-891f-ba04fc2a91d3 | -9.93148 | -60.72087 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7336f7bc-b58d-3d90-8aa9-0d46b909a424 | -10.38413 | -61.26999 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e7471b4-9512-3f47-af34-058dddf35fa9 | -10.40047 | -61.26251 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bd0f827-c3d2-37c4-b931-fb258820969f | -10.80637 | -69.29417 | 2026-09-29 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0df66463-c4de-33bb-a61d-bc2ab83e5622 | -7.70349 | -73.10986 | 2026-09-29 05:55:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd3b3e57-dc3f-3e92-a24c-39f249bf9f4b | -10.37695 | -61.24696 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8796b924-bd8f-342b-b65e-9200001a3f9d | -10.28592 | -68.76579 | 2026-09-29 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 334e9c57-2761-3956-bf8c-251727891cf4 | -10.3904 | -61.26134 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1a3ee798-a8c8-3f4a-8a5a-446a35f2376a | -10.39038 | -61.26139 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a022a62c-7ad1-3091-a410-c6e6fa3559f1 | -7.18452 | -69.89066 | 2026-09-29 05:55:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 895894cb-8ea8-3971-8d8f-c1a01475868b | -6.95681 | -71.49005 | 2026-09-29 05:55:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08b16608-2437-35be-babc-bcf9b12c9953 | -9.93315 | -60.72078 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62565e6a-3e99-3931-9bb6-3c5a04d7082a | -10.40088 | -61.25923 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00944237-3f14-3ecc-9655-486aa0051d2b | -8.46924 | -70.87759 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be0e3f6a-2f22-3da0-88e7-1b21240939e2 | -7.81478 | -70.63798 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa82848f-8d35-3f63-915f-98de81c5a04e | -10.28646 | -68.76227 | 2026-09-29 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c92cdad6-3188-322c-9795-ca159d5bea23 | -8.78882 | -68.96918 | 2026-09-29 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0b2a646-0bd2-33a3-9c41-ef657e1a9872 | -8.88735 | -68.79246 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbcb8051-47af-372c-8992-e64f0f06ae7d | -10.09576 | -68.22949 | 2026-09-29 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6c4c875-ecb0-3fc6-961e-eb20f3040e34 | -10.37735 | -61.24396 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5cc675e-2c3c-34f0-a39f-1908cf084f5e | -10.38363 | -61.23515 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6910df80-8754-32e5-9441-40ecd9510e43 | -10.38538 | -61.26052 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8d91d724-46c8-363c-820d-762e05423cac | -10.40133 | -61.25587 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf590ccc-363e-3086-80e7-86adf0d76043 | -10.40215 | -61.24974 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba9b65f1-7970-34c2-b93a-da9870498426 | -8.77784 | -68.97456 | 2026-09-29 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2277f2a9-c3ae-34d2-80c7-afb9bb3a9b61 | -10.40175 | -61.2527 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cea9ef3-1fea-371c-8368-09ad96d3c15f | -9.92631 | -60.72016 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e853db7-8cd3-3834-8116-32d1d118ecb1 | -8.90269 | -63.74027 | 2026-09-29 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac1566f7-98d0-3a9c-b4c6-11e1f0db07d8 | -9.19755 | -67.74415 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f765a0ab-9161-3cf7-a72b-fabf26719d15 | -6.68203 | -55.11214 | 2026-09-29 05:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d1fd9fa-2b82-3757-988e-87c47f51caa4 | -10.39129 | -61.25447 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 479f17a1-cffa-3911-adb4-b3411474cd71 | -10.40207 | -61.24968 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7b4d764-d92b-3e1c-96ec-baf4169834b0 | -10.39546 | -61.26174 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4a25fe13-378c-3295-a8c6-9dc507159b77 | -10.38044 | -61.25928 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deffc704-f710-3262-8470-33e2ffc328ab | -7.06325 | -55.47977 | 2026-09-29 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| faf21fa4-aa40-3711-9926-ed50072d6390 | -10.498 | -67.88488 | 2026-09-29 05:55:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 640538de-14e6-333d-b0b5-fcc754f307c7 | -9.33784 | -68.22997 | 2026-09-29 05:55:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d58cc14-ee46-37dd-b474-c2b5b754dc86 | -8.90437 | -64.14197 | 2026-09-29 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41f4c976-f983-3a29-b0ab-6473be025b89 | -10.39463 | -61.26835 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b6bd250-7971-3e7c-972c-941cfdc0c75d | -8.40948 | -70.7668 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76b2ca47-af8c-3d7a-af5c-381ce7df0382 | -10.37659 | -61.24974 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69f495d7-cbe2-363c-a3d4-ec6c7b825f78 | -10.08656 | -68.4697 | 2026-09-29 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6f23371-450e-3a43-b7fe-2b4600bd8626 | -10.77503 | -68.27856 | 2026-09-29 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d89347f7-b0f5-309f-8752-b3c2803f4450 | -8.91193 | -64.14669 | 2026-09-29 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e074341-745d-3eb3-90d6-2e96955ad195 | -10.39126 | -61.25441 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 152.7 |
| c512d39e-fede-3a93-a387-98d93c7d1c86 | -7.7913 | -71.98303 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0506ea77-b12f-344f-a478-1aa050832657 | -8.47322 | -70.87447 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README68.md)
