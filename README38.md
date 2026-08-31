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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea45abc8-d6fa-3faa-82fb-a3da238098e3 | -6.2795 | -53.33271 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bf1c107-c322-3516-9c3a-4de11bed5005 | -6.87831 | -56.50646 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbe9aa03-f7f2-3e88-a2e8-d69e36fd5d23 | -4.92492 | -55.76744 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fea95c6-2368-3d6a-8e57-0167db6d0de2 | -7.97658 | -52.08618 | 2026-08-31 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d921e86b-b110-3bb2-b336-920d24dc8be1 | -6.20548 | -55.41908 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b7d2e7b-9c96-3319-90ec-91978b52454a | -1.62477 | -55.16766 | 2026-08-31 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33844963-4d98-3a25-ac44-f8853a58d4ea | -6.87488 | -56.57142 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aabf6693-b5eb-3319-8f49-693bd50a1af4 | -7.5468 | -47.322 | 2026-08-31 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e88e8ae5-6981-3cd2-bff4-e94c7a733194 | -7.28261 | -49.83489 | 2026-08-31 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58e74859-a56f-328b-a0b8-04c8344d30af | -5.9841 | -55.72526 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 066bc1d9-7c98-3e36-ad53-a4c0ff1ce800 | -6.2484 | -55.42944 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30f096e4-e6f0-37e9-b870-43b1597805e9 | -7.61008 | -44.89165 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 165a114f-986b-362c-a97f-c4e589c205e9 | -5.25503 | -55.89807 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 69194a7d-ed0c-325e-bfc8-ceaaf14eda0f | -7.31661 | -60.58275 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc2ddf9b-dc1b-3513-8d03-0fe80537ba92 | -5.24645 | -55.90802 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ffd2cb5-8f1e-3f03-8ee4-c499b62fd15b | -7.97862 | -44.28648 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d69bebf-22bc-3f33-a57f-29a11eb7e529 | -6.15129 | -57.8815 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0a281fe-7e6e-3842-9307-cc966cdc55f2 | -5.95998 | -53.59824 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b66dfea-c8f0-3a90-bdbe-7f74cd1bf575 | -6.67882 | -52.85331 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7f6cf50-f4ec-3f96-9f6d-2307b69eb9cc | -7.29869 | -60.5842 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7ee62b3-05a4-34ba-835e-957897b2c199 | -5.49497 | -57.13868 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7365a8c6-ec40-3b1e-b882-81a11ccf6323 | -6.91608 | -55.72194 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7624d82c-7b51-3edf-9e2f-ac5bb23e0b5f | -7.09599 | -59.68785 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a19d7df-a3a0-3da9-986f-edc5388a6cae | -5.49006 | -57.14633 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e205f2ee-6b71-3fbb-bf45-d4bfcdf84aea | -8.75967 | -45.38478 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b41c8142-5261-3c8d-ada0-485e7526e18e | -9.42111 | -45.65147 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e89f07c-7459-3c05-a1dc-17d247d863ec | -6.90696 | -59.48992 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec182f62-ea34-3477-b652-d5d308252bbf | -5.8763 | -57.77444 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2dfc1e5-e883-383b-b6df-79b348b61aaf | -6.31086 | -53.54932 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a49b72-91e2-36d5-a125-2be5d0cbf812 | -6.08207 | -57.8945 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c9acc5-bee8-38b9-845d-f656ac97ceda | -6.2612 | -55.39161 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e109b75-1643-3210-bff9-e620426fddfa | -7.50473 | -55.33394 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dc098c0-a299-396e-835c-37b450f8b4b8 | -6.90638 | -59.49347 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5208debe-4dd2-338c-92fd-19b42ce2dfc6 | -7.97448 | -52.08091 | 2026-08-31 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bc04c91-3a0f-3a9a-8011-73f67e1e5f6d | -7.10799 | -42.76799 | 2026-08-31 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 069d5e5d-2465-3b7b-ad25-e3cd62318b37 | -6.27896 | -53.33624 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cc0da1e-75d4-3d54-a4ca-608494cb4c66 | -6.11144 | -57.71069 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b8ab402-63cc-3110-80ce-909092855e0f | -6.42273 | -55.53025 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aa2c221-58d9-36d4-bf61-2bf049e22c6e | -8.04708 | -54.01677 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55995e1e-bd06-3f4b-9c8c-0518e3cadb27 | -6.1565 | -57.77975 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12e30846-f080-324e-9601-8ffd4387b7b9 | -6.3599 | -55.9923 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ccea5a-7e91-384d-b316-6c1e90ff5753 | -1.45018 | -54.20817 | 2026-08-31 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e92ba85a-b834-3513-aa72-258c52ddfcb4 | -6.53676 | -51.43591 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e79ba6fa-e06e-32ba-b4b9-a62f79c5b805 | -5.88889 | -59.9833 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 884c85c4-859e-3d0a-bb47-3229d2e79659 | -6.12523 | -57.69535 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 466aba72-b32c-31d1-ae29-119239d57519 | -6.90409 | -59.48223 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56328350-0491-3d6b-888d-82f0e11b2ee9 | -6.95132 | -55.71657 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34279340-d10d-3888-a2ce-7c7aaca34e96 | -6.85886 | -59.43148 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e35388d3-4b61-36dc-a572-dcf26eb70714 | -5.25726 | -55.90599 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f84804ec-f293-351b-b078-6127856171f9 | -6.89959 | -52.83056 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf072d2c-b322-3d9a-8438-1df6f20505c3 | -5.25221 | -55.89386 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f3d4a24a-3c56-3669-a096-a7e929db9c14 | -5.24539 | -55.89279 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 000d676d-f93c-31de-b805-d9c7724f3319 | -7.97806 | -44.29066 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac9877b7-82b0-35ff-aa9f-3d14d4083daf | -6.39968 | -54.96499 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9ebb7ef-09f0-322e-8f6c-dbae0c9ee004 | -4.84785 | -55.83046 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a654f857-d6e1-3b37-93a0-d4817b1aab91 | -6.48476 | -49.89149 | 2026-08-31 04:57:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c64e29f8-da8f-3f3c-80a8-52494bed2e6f | -6.57811 | -55.43115 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79c97b2a-4de9-3033-8be9-8f68a8be43d8 | -6.11964 | -57.68279 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b41cb94d-dfc8-33bf-914d-7d6db012c445 | -4.69144 | -55.66365 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ad7cebd-be42-3928-8642-26ff74589444 | -8.39028 | -46.47518 | 2026-08-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c467bb1-f345-3668-ac7a-83add1c774a9 | -7.09616 | -59.68787 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c71a9c5-f993-3327-8fb8-9ab03c630f3f | -7.34093 | -60.59568 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b2f0600b-4eff-326e-875e-47d6af673551 | -5.25269 | -55.91276 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8637dfe2-9ff5-3d70-9ef6-b715334b49ee | -6.90749 | -59.49462 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd9f8b82-aa48-3be9-b0a7-5bde6360e9ce | -7.61057 | -44.88793 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94283a36-3083-343f-9914-71b22a38bdcb | -7.33706 | -55.14633 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23a22d44-c834-3a2c-85c6-d839832b9d84 | -4.1562 | -60.69967 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e2513ad-cbfc-38fe-8723-e9f979e21c60 | -9.43791 | -45.66907 | 2026-08-31 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4247562-4879-3947-a930-4b907df3169b | -5.24986 | -55.90855 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| bf7b8ca3-10d1-367c-a80d-9fe2f0abc26f | -7.11882 | -48.06061 | 2026-08-31 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46b8ecfd-c05c-31a9-a92b-5109e3f49cc8 | -6.76863 | -59.44513 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01108781-529e-34f4-a658-4b8d614a2337 | -6.12439 | -57.67773 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 535e8fd7-ea96-38bd-9884-208307476e1b | -6.6098 | -58.59615 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86d83ba8-b716-31db-939e-be6e45569ea5 | -3.65577 | -54.848 | 2026-08-31 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b246838d-30a6-32a1-a8e7-b6405b0072cc | -1.60279 | -54.40819 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 84688877-a36a-3018-bb09-2cd01d516c60 | -4.36985 | -55.43467 | 2026-08-31 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e96a84c-134e-3f2c-b3a9-02a84949c43a | -7.33165 | -60.59832 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 33b7b5b4-8f7f-33c4-9c00-4566c11c6fc5 | -7.31303 | -60.57786 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d6c80bd8-697b-3fe9-86f5-74868d77f8b4 | -7.06358 | -52.71715 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 528499cb-6efb-3846-b13b-e82dbcc48eb5 | -3.61298 | -59.07267 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8050e028-1cd9-326d-8b9e-e748fa5241a9 | -7.48757 | -55.31327 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc3fb29c-9d71-39e2-822b-92e8d16687f3 | -7.30873 | -60.57717 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7bf0a00a-bc75-3c31-a8c2-1bb1c396caf6 | -4.95976 | -55.85561 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8539316e-3dd3-324d-93a1-4d63e5505add | -6.90281 | -63.06485 | 2026-08-31 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c565a6dc-d745-38a5-a2a8-5d2c7d05aefa | -4.06319 | -48.96118 | 2026-08-31 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd32e84f-7f80-3f5f-a9dc-d2492685ed0f | -8.09151 | -45.46186 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 292eb06d-33e5-3513-b23c-9b4ca9e34b6d | -7.62308 | -55.29582 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1868f40-a7ae-3dd6-87ba-0d8ba0babe01 | -3.76814 | -59.33565 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1607dbf-14f3-3b1c-9850-8b46785df8ad | -5.31422 | -55.85484 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deb40305-3435-34ac-9db7-955c02e4cbd0 | -5.25327 | -55.90908 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a3d32ab2-fb34-37dc-b09e-0ccf594123de | -3.48441 | -54.66236 | 2026-08-31 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4932aa3-374c-3709-9f06-93e1046bc495 | -6.53699 | -55.10799 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5999a1c9-96b1-3d43-b080-9ab01dc40851 | -6.9087 | -59.48753 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dfa1be6-0329-375f-b9c4-e91d9e8001a9 | -3.88488 | -59.39761 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54631966-2fa5-36c8-bfa3-e075a7054286 | -6.90812 | -59.48285 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe5eaeaa-fa5b-3f4f-9d79-e96526218968 | -4.84844 | -55.82677 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b07ff94-71f5-3aa9-b929-b686cfee9dac | -3.26949 | -49.52155 | 2026-08-31 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa1db90e-4786-3a8b-862c-95409a5763e0 | -6.77873 | -55.64142 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85383254-1da5-3eed-9f79-40974d6222c0 | -7.53075 | -55.34167 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fa551e8-81ab-3503-9907-53a12941265c | -5.89383 | -57.75919 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
