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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 998ba189-71bc-39fa-bb7a-e4362e24ed9a | -0.53717 | -49.18927 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36a172d3-1ad5-3298-a964-8b2c0a1d37cc | 1.96204 | -50.9033 | 2026-09-27 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e1fb115b-72c7-3b2c-93e3-3d43f247289c | 2.63785 | -60.17629 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad147296-9364-3af9-b1a3-de689b2229e9 | -1.75909 | -48.73983 | 2026-09-27 04:49:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 68dbf23e-b491-3454-a23d-8ba8db0cfd10 | 1.66407 | -55.96093 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd87ccb3-c122-3060-80ad-a3c560760ad0 | -2.32069 | -49.16566 | 2026-09-27 04:49:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8355094-70b0-3a19-a862-bb320c7e70e8 | 1.65058 | -55.92729 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3ece21-19d1-3e1a-b2d3-cb6a8b735b9e | -1.0477 | -53.56713 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f5a42337-76d9-3d7e-a9c5-c3960983e89e | 2.26156 | -50.7722 | 2026-09-27 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22f6fd4b-c355-3a01-9deb-c9ac9c0f2723 | 0.48264 | -50.94884 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3a411c1-4960-3ad9-807b-cb2048e7549c | 0.47658 | -50.95329 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d736da2-a243-39a9-af8c-04c04d6bdeea | 0.5218 | -50.78812 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0ea2949-1c5d-389d-8ec9-33e3fe7eb17d | -1.51287 | -52.59593 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 263ff855-756c-3487-90fe-e0f993b6fdab | -1.86127 | -47.97977 | 2026-09-27 04:49:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| adbd556c-1339-3692-87ee-78a95fba615b | 1.66292 | -55.96818 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89289bb9-6fa4-3c4e-bb28-000d6a3a7161 | -1.05112 | -53.56768 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1d17b3a2-b775-32ca-baa5-f6fefa3e71ce | 2.63631 | -60.16578 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24d8b4b0-8393-323e-8b18-cbb07c996fa2 | 2.8898 | -60.27897 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7c903a5-f3a1-39ef-ad74-b276a53179e6 | -1.14272 | -54.09862 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19208346-fbbc-3c72-869c-85fdbd833d72 | 0.70046 | -51.43059 | 2026-09-27 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 47e4dab7-f170-3f81-b31b-0aa60b77b84c | -1.05169 | -53.564 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c7af38ee-87ca-35d3-823e-b6e052ffa577 | 2.63088 | -60.16658 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa18bd84-af43-369c-84e7-341fbe760fec | 0.63853 | -54.37645 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4155ae44-3aad-3506-b775-f74d5516e201 | -1.14743 | -54.09145 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2523f29e-28ab-351a-b153-22bf239eaee4 | 1.65567 | -55.93364 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b19345d3-6b21-3518-9e72-2d5c0079883c | 2.6438 | -60.179 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56269921-28fc-3766-acd3-585b4570ee20 | 1.9689 | -50.89804 | 2026-09-27 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0be1672c-585a-3100-9232-8f2db9478ae3 | 2.63682 | -60.16929 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea636c3d-f186-3dfb-960b-c3f7577f9671 | -0.53776 | -49.18547 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9be0b74f-2a58-36cc-a485-08bedcab87af | -1.21743 | -54.56625 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42a131e6-6b20-3e94-a7ed-1d1b1b657b52 | -1.21405 | -54.54135 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f5dd837-bf95-353f-82c3-d92a042baf4a | -1.14908 | -54.10354 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a6601fb-9f9e-3a7d-b008-e71ab5f92afc | 1.66516 | -55.96789 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e973719f-7298-31d0-8eea-b01b489e7b8b | 2.89529 | -60.27818 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5767412d-4c8a-3aad-92f7-55c1ecfe1468 | -0.51831 | -49.12782 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0353446-dd39-3380-b56d-759fb99cb20e | 0.32855 | -51.44315 | 2026-09-27 04:49:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee72193a-f5a0-3eb5-95a6-b1fb9b248998 | -1.04828 | -53.56346 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0c199e93-8a56-3558-9fec-34faac3eeb5c | -2.06747 | -45.9957 | 2026-09-27 04:49:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e131f539-8676-3768-9869-521c774b546d | -1.04544 | -53.55923 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fa93b05-8921-371e-a00c-1dad8efaf2f2 | 0.47934 | -50.94935 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f202d12d-a054-3519-9f6d-ca1a5052df62 | 2.63455 | -60.16633 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62514df3-6c18-39cb-8335-c62f623638e2 | 2.63509 | -60.16982 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3208a93-6a15-37fc-8fcc-e6d22647ed18 | -0.50613 | -49.13766 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95cb8d73-974d-3b8f-a398-01664fb497cd | 1.69255 | -50.87486 | 2026-09-27 04:49:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d759a0b0-6f78-3554-bdf2-d9c7953ebd30 | -1.14681 | -54.09531 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5acad76d-896e-343b-80f3-c9176204a869 | -1.0302 | -53.72382 | 2026-09-27 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdb09629-7ae6-30e7-9c24-11d36eed7722 | -0.54122 | -49.186 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| effbe605-99f2-323a-bf6c-59ad17c89775 | -1.86198 | -47.97529 | 2026-09-27 04:49:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f8c52dd-c33f-3d7f-8e65-eec3d5538ace | -2.34739 | -46.09341 | 2026-09-27 04:49:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3299a008-220f-399e-ba6c-8374469dfa09 | -0.50554 | -49.14148 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73b0b780-16b9-3315-a393-5126adfed51c | 2.63402 | -60.16284 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b41ec210-ef7b-340a-8657-1758930f5ecf | 1.66461 | -55.96441 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dfacc28-d82a-3863-99bb-6ec524b5b944 | -8.3398 | -44.16697 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 278b97dc-50c9-3dd6-b7b1-33f1d32b1e8e | -3.7745 | -51.99463 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09df3ec0-45bf-328d-9a76-c649df434f0f | -2.38046 | -50.40952 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f2ebc0b-caea-3bdc-adc4-af32111230b9 | -8.36009 | -44.17077 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 3d8cd009-b6c4-38c7-8692-ba37fc9fec07 | -3.56931 | -50.2966 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca8b8527-491b-3d25-8e52-f24ab267a745 | -3.44559 | -56.48294 | 2026-09-27 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e22ec2-0699-3773-b4c4-40919806fa83 | -4.71835 | -55.71917 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49c47228-526c-3434-b4b2-60c263ae225c | -2.92034 | -54.16231 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1900c7df-7a6a-3975-84cd-f9d8864ea50b | -2.02063 | -52.11308 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bce43695-d266-3b85-828c-172097460e9b | -3.35791 | -50.75646 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1e8f804-ce68-3445-a2d5-05553dbd21db | -4.50795 | -54.95254 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1971faf-3b49-3664-b889-ecfb6b7098bd | -3.74312 | -49.36539 | 2026-09-27 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47ea51e3-86fe-3155-a999-81be2a09ec4c | -6.09122 | -57.62374 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 662480b9-1935-3b46-8e5e-3b4236783b3d | -3.76585 | -51.80669 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eec56042-1288-331d-98cd-6bcc9801b909 | -8.59636 | -54.65179 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e5552de-ef1c-3fe4-9a17-0dd5f587e5f2 | -6.84114 | -43.51619 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10839a5e-7542-3b80-9c79-a2f531b910c8 | -2.88089 | -50.23409 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e5357ab-3bdc-3a4c-ad4b-e7fc4c345535 | -3.96128 | -48.12022 | 2026-09-27 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 60630168-7cf0-3e10-88d3-2cde8d88f012 | -4.54594 | -55.53033 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ba4e8f8-b433-34d8-bc57-2f7bf217c31d | -8.33894 | -44.16738 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 895cab09-f0fe-32f6-b67e-7c6944f2088d | -1.84202 | -54.72134 | 2026-09-27 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a4745f74-db10-38cc-be38-1a281d2d5038 | -6.92989 | -42.86875 | 2026-09-27 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce65e5fe-a13d-374d-bb89-4c996a1ff889 | -7.36957 | -42.11154 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b9b0c459-281d-301a-86da-07cafad5d3d3 | -8.08601 | -54.74017 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf1f14f2-157d-396a-a8cd-396be80b4151 | -3.11834 | -45.43339 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59029bcc-0f56-39b8-92dd-aeee9f139950 | -8.35393 | -44.17667 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 214.0 |
| c154b6f7-82c1-3edd-8875-70243bfbc322 | -3.07534 | -54.37944 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b477c5e-58ee-3c27-83c4-b3e576a27cb7 | -3.8537 | -52.01108 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 293975bb-8212-3602-911b-e90881de0643 | -4.56666 | -55.05836 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb0cf69e-cd58-3878-b424-7921ee101b7b | -6.08954 | -57.63411 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b88f439b-ad9d-325c-b863-dbb20cfa2393 | -6.08668 | -57.62655 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 201e911d-8d7d-318c-a4d6-31a32eae99c3 | -7.0244 | -46.45042 | 2026-09-27 04:51:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3be74d02-6247-3e76-a914-a07ee34072dd | -2.8983 | -54.10133 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f959222-3391-3313-8ea6-02fa4c7f6c78 | -2.90466 | -54.19459 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b82e92b9-fe84-3af8-b784-a6d2a85f40c3 | -4.99863 | -49.03267 | 2026-09-27 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce4a0039-8d62-3e67-abfe-63a2847fc39d | -8.34945 | -44.17535 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 224e501e-2fd2-3dac-8356-d829deb990aa | -3.56989 | -50.29289 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4f013c8-297f-384e-ae0a-4469189655e6 | -4.52935 | -54.97588 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53846c1a-2218-3e02-ac14-78d27f85952c | -3.45253 | -50.07753 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff4936cd-5cc7-3f09-95b8-b027216b424a | -8.35794 | -44.15284 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dd0b4aec-b97a-34b3-8ea4-4d42726415c8 | -6.31336 | -43.33949 | 2026-09-27 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98fd7deb-2d91-3f76-9da6-c80fca7818c6 | -8.35738 | -44.14995 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08eea88e-9e72-3fd1-bc08-9e5d0f6832fc | -4.57997 | -54.92808 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0928ed9-a718-37b0-94cf-1e45dd0859a4 | -3.42223 | -50.43112 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff7353e6-03ea-3da5-aed3-028d27d06706 | -8.03735 | -54.89321 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 43e5d125-80ac-3da9-a151-b642ba11ef0b | -6.13391 | -53.05027 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a128d9f-bddc-3e4d-a01d-29cce7c6fead | -3.06194 | -50.33562 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9de14b45-69eb-3a26-bdf0-78753e9cec12 | -5.7348 | -45.01607 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README24.md)
