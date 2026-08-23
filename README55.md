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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb3886a7-39e5-33c8-b3b1-061e2e0f12ef | -6.76839 | -58.68177 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea7f456d-f5bb-3198-a4b4-109375b0d3a4 | -6.80188 | -59.41039 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 600f0e29-4197-34cf-b65d-8c9db5c42059 | -6.12095 | -59.92557 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 414938d3-9172-3285-b6e2-c1a29609d995 | -5.65058 | -47.08641 | 2026-08-23 05:04:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9577cab1-cc7f-352a-b988-de739d709c3a | -10.83352 | -50.96641 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 08e057e7-22ba-3674-a26d-751d32bbad6b | -9.6557 | -63.84121 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f9c7244-9540-34a9-83f4-16c5e1b1fdd2 | -9.15897 | -59.46412 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e334a87-728c-38da-9bec-8db3a4595cb7 | -6.79682 | -62.91911 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1e3c90d4-a3f6-3a11-8d58-4f861dfdc188 | -7.43477 | -59.79138 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cc84297-ec5c-3a20-b8e5-c926000ebb0e | -9.45615 | -56.90475 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa87e40f-f652-3590-b0f6-e97bbde02f58 | -7.55072 | -55.56115 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0ca1e2b-7149-3b98-8a9a-08c5342d7c7a | -10.04841 | -46.42085 | 2026-08-23 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc7cdb5d-5729-3555-af85-86f07fb7526d | -6.75167 | -58.67145 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6ea8136-8c60-3f33-bc53-0f3e25bf1211 | -5.7698 | -57.57376 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 96448c4d-c5b2-34fa-882a-c9f8d3fb42a1 | -10.6889 | -45.05244 | 2026-08-23 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80d0fd5e-b809-3a3f-98a4-096199290538 | -6.80247 | -59.65439 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bf568b8-409e-3aa5-a54d-929c12a61966 | -11.20951 | -55.04609 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1cc4f3d-e731-3e75-bfdd-50fab62212a2 | -6.79886 | -62.90728 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d60da8d-af82-38e4-a095-3ca062f5bb90 | -6.81042 | -59.68182 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2f10ca5-67d9-35cd-9b7e-235ed7bd35cd | -9.16367 | -59.45993 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3118fd0f-0590-33f8-ab68-8a68811de612 | -8.09243 | -50.05052 | 2026-08-23 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 830d0d0d-b0cc-31ce-a7b4-4a18aebba3c3 | -10.7083 | -47.73812 | 2026-08-23 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42dc5f73-9d74-30ec-919e-c3fa475314ac | -6.13783 | -57.77486 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31e49056-e2c0-32f3-8333-2a0d52d9036d | -8.53367 | -55.32063 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5698e06-edab-30e2-b554-49059beb54c0 | -5.53115 | -46.60851 | 2026-08-23 05:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 971f8e18-c0bb-3537-8100-284ef395c33b | -8.40089 | -62.69818 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39c35e93-1b66-3e48-aecd-801a4d04e02a | -8.15987 | -52.05117 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a1c29c0-7ec6-3d6c-86d4-3fd2f1da7bb6 | -9.79441 | -46.60924 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3f53a0cf-19b6-3d95-91de-c0c50116f50f | -10.24098 | -54.37875 | 2026-08-23 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 673d88fa-ec41-3eb4-9d53-15ce0af7dac4 | -6.77404 | -59.7497 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4c4c735-eca0-3f98-8d4f-4d0345b66db5 | -8.68925 | -62.8739 | 2026-08-23 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cff1e3d9-d5a2-3a1b-bd82-8d9f7ddc3fad | -6.76848 | -58.66461 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55de8e1e-372c-3d70-b69a-e99572a70ced | -12.22038 | -43.16136 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 28c15067-0d4b-351e-aec4-17b73ca1fd2a | -5.65328 | -47.08765 | 2026-08-23 05:04:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7c4b5b7-2f6f-3419-81a9-1ba0c49a1324 | -7.26856 | -49.90859 | 2026-08-23 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 07486e31-c8bf-308e-8311-8732f1a7b6da | -10.06516 | -60.50457 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 19ec4411-d686-391f-b86b-f674c809817a | -6.69555 | -58.72537 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2206037c-c899-35e1-abb2-793b4c6eb821 | -7.26842 | -49.9057 | 2026-08-23 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| decbd1c0-dc18-3c75-88a3-eba45ecadf25 | -7.77581 | -61.06759 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| deb64d75-d6f9-3217-a8fa-ec0c37d9e75a | -6.13241 | -57.83152 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 63e334dd-8c50-3111-abb1-aa448c609a73 | -6.20563 | -53.08873 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 925a3307-31bf-3c2a-bffe-53f1c4f462d2 | -6.78637 | -59.42922 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd4c7c69-70eb-387d-8ed2-b14e04179e5a | -10.79405 | -50.96561 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d80a9bb5-583c-3563-aebd-6450900a628e | -9.40252 | -60.5885 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82ded4e2-c5ad-30aa-999f-2edf0f7064c9 | -8.19691 | -54.98125 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e8fa5d7-ed4f-34a8-a572-0cfcb25d86be | -11.47183 | -54.32257 | 2026-08-23 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f73b3688-9726-3258-82f0-934609c930c1 | -10.84127 | -50.96755 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8658ca39-871c-37eb-90ff-00899fdeca92 | -9.15644 | -59.47878 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e1d031-6322-3dd2-a6a7-c4e6e282e843 | -6.79684 | -58.65275 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c5b6755-6eb3-3f4a-958b-e95c01532355 | -9.23334 | -60.38583 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8098a30e-3518-3a67-8bd3-2616ee2f6ea9 | -6.5511 | -58.52262 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d847f4c-f033-3975-91d6-5f71992c1f60 | -9.06658 | -60.43712 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecce1338-5d7f-3dd8-b94d-8b0edb026bfb | -4.53832 | -55.51171 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4036c793-71f4-3382-9a1a-af757e8b7b83 | -8.53807 | -55.33564 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec7624cc-6be7-322f-8df0-26a066f963af | -6.82185 | -59.41376 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a72152d-0a8e-392a-8426-7158ea319b94 | -9.11607 | -60.33895 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dac4e6e5-02a8-3dda-be29-de69fb93e286 | -9.17914 | -59.4626 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 928f9b6c-ee93-30af-a237-faa87dc963e3 | -14.79648 | -48.78366 | 2026-08-23 05:06:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 3723c374-e877-3dd2-9eb7-e7b0cf2f7342 | -15.24953 | -52.82971 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ab65b25-a486-3ee4-9536-b8738887193a | -13.19282 | -51.44733 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2155a99-fd23-3dc6-a057-356e440d0b43 | -13.19955 | -51.42797 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9551a644-d550-3d30-9a19-998d2800863b | -15.30465 | -53.79456 | 2026-08-23 05:06:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a05cb9d6-422a-31b2-90e0-85f907ebd139 | -12.84825 | -48.47175 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3504e195-172c-3894-8eb6-f2bd93b0c1ea | -13.53808 | -48.19118 | 2026-08-23 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f877070d-5aac-357f-9b72-afd74d8195be | -13.20765 | -51.4311 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69d76fce-f253-360b-95d7-6690522c4512 | -14.47622 | -53.01997 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35491eea-623d-3f54-b6dc-b1c0a2bbe3b3 | -12.75063 | -48.41057 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 246e9bb5-9f3e-307d-8bf1-60af0d1372eb | -15.24891 | -52.83405 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d82fb9d7-c7a1-33a3-a7cd-e5d1677fc488 | -15.84806 | -56.33966 | 2026-08-23 05:06:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a5752b5-0c7f-3268-9548-34740d196390 | -15.76233 | -55.55655 | 2026-08-23 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 368f1002-5e99-3640-93e3-77698e6a105c | -12.85358 | -48.46776 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 119757ae-6403-30bc-ba20-1d306302c288 | -18.59743 | -47.12955 | 2026-08-23 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 962e3c77-aba2-3ef7-9e7f-ea0dbcdd6085 | -13.1702 | -51.43895 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dee5fd86-fbc2-3806-91db-a11b50583820 | -16.04702 | -50.43808 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04dfffe2-fd87-3696-b006-31f2cba7e051 | -16.04758 | -50.43391 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc010805-bdb8-3345-8784-52fd6ac653db | -14.96336 | -52.66917 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44c69c82-5c17-3516-bff5-67c539a2dfff | -11.7962 | -55.24508 | 2026-08-23 05:06:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98838472-3be3-3328-84d8-8afb794100b2 | -13.24835 | -51.59366 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6863807-c7e8-3517-bd4c-f56a053e7953 | -14.95787 | -52.65463 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7c98484-da8b-3684-beea-b9030278da2f | -13.25221 | -51.59422 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96291369-7e8f-32b2-aa62-6c1a6097add8 | -12.75591 | -48.40677 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1385fe90-7162-3f3b-836f-df20c28c82e0 | -15.72865 | -56.04029 | 2026-08-23 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 0a10739b-4511-39bd-95cf-d170535cdfa1 | -16.05694 | -50.4466 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2d3120de-5d3e-3f79-ad00-962c44607707 | -12.0018 | -53.41848 | 2026-08-23 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddabcc90-7f05-3f8a-ae47-a820100164cb | -13.38804 | -54.36375 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9895083-75be-3ea0-86f0-3e4a31515c8c | -13.25606 | -51.59477 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ec8c70b-ab57-385d-ade2-1858fca4522a | -15.2085 | -52.80037 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 692679dc-e958-3125-945d-c073bc18e519 | -11.31864 | -57.89111 | 2026-08-23 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f145f59-99ba-3f13-88ad-0ccb74136e7d | -14.34715 | -51.77728 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd2f1626-807f-380e-bda6-48d1e8b4360d | -12.11857 | -57.20584 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 245a2a6d-fad5-3751-8978-0ac26ecabf3e | -16.06231 | -50.43885 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ab0c4aa-ffaa-3a80-abfa-c27af5e8b1e8 | -16.05472 | -50.42941 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 641bcaec-9377-3895-9933-b89694bc42cb | -15.22327 | -52.77576 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c35ff4c-99be-3820-992d-a937052a1d1e | -13.15216 | -51.42613 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 0fdad15e-ea4a-353a-95e7-5816e77912d2 | -14.7972 | -48.77783 | 2026-08-23 05:06:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 6bf0af8e-a356-39b5-999f-34604a8ae603 | -13.15605 | -51.42671 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a3e46bf6-43ba-3a37-98c0-1d8d7770cbe9 | -14.34219 | -51.77414 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80991d93-007e-321d-a1ed-0779a232c864 | -13.84329 | -54.01107 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82268615-112e-3e2e-862c-60fd03bb4df7 | -14.30381 | -53.23325 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a62da6f6-8cfa-3fc4-87f7-4c2400228e8f | -14.37036 | -51.7807 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README56.md)
