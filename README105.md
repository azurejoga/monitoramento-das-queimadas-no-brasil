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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7d83c16-b84c-3002-bed3-ed401694af60 | -6.5136 | -55.40289 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b563d37-b693-376b-bc7a-15881f22f1e5 | -3.59228 | -54.68472 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 617c938d-af10-3b94-a5e1-4b05ed85c230 | -3.29238 | -54.0202 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4aa39ec-688b-3234-9fd7-1747db8f9a2f | -2.98476 | -54.11417 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2c565161-91ba-3e68-bd72-dc7bae558016 | -2.83487 | -54.13319 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f06a2046-2f70-3419-ac15-9fdf75d698ba | -5.87232 | -53.64676 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef39f4d-d1de-3968-893c-7e93634ec12c | -7.38469 | -55.21184 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fcffa2f-14c3-3901-874e-7f13c0c29740 | -7.51022 | -46.58323 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c87cfd4-ec9b-3509-9f09-cbf527f958a7 | -2.50556 | -56.1703 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5ec41f30-287e-374a-88c1-2ab50775a2fa | -2.51137 | -56.16264 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 187e4dbb-9ec7-321d-a496-e6181a63ce6c | -4.27328 | -54.86821 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abb70a6b-3fdc-348f-bb2d-8aa0641e26c3 | -3.51384 | -54.66494 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb9612ea-00a9-3c1a-a790-e93e37a8b598 | -11.65069 | -43.67704 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd0773d3-8468-39aa-b498-8074b08e98c1 | -8.72121 | -45.16824 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| da708021-609e-30bd-9309-c3da3663ed0d | -3.50237 | -51.69418 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbf64d50-f357-3bb6-bc67-4b22326fc9a6 | -3.26831 | -54.03103 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 61fa69ec-c9a7-3a6b-b0df-5cff9d7321e8 | -2.76785 | -54.11011 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2fa7228-1dcc-36ad-aa34-66184af4ad2a | -5.75245 | -42.06149 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8c65480a-9e8a-36eb-b03c-ee8e0054d6e4 | -5.33912 | -50.9841 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9146cd9-4c9d-3f1d-9f17-765e22b739a0 | -3.11988 | -56.66325 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a63bab1d-9b9e-3f9e-bad5-1dd466246b22 | -5.51898 | -50.0229 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5797758-4919-3bc2-b6ca-24f00497ce7d | -3.1141 | -53.77685 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e60e7f85-de61-3324-984b-9a393e7051ea | -7.22433 | -44.27882 | 2026-10-08 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd581f93-9ceb-3144-a6f0-60eb75f5b556 | -3.01667 | -54.05643 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 44a09fbf-7a02-3a8d-a949-c08023581297 | -11.76139 | -44.93655 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91384033-9d56-30a0-8cd8-ad1e91056419 | -3.72183 | -54.21944 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98dc2bd8-b8a2-3ad4-8278-0bdfffc9f238 | -3.53162 | -54.65128 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90ba45f1-c024-3e1d-b013-54d744debbe9 | -3.03656 | -53.93119 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2201ecb6-c239-315f-a79c-a6566131a913 | -3.01437 | -54.04715 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c93a35fe-e740-3199-9db0-d9a6018223ac | -3.10184 | -54.18035 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cfd0caab-a2d2-3bd3-8fae-0c97714f2e51 | -4.98377 | -56.22274 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ba5cf2a-1516-3d48-9f36-636100a65af9 | -9.67732 | -47.89677 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36b66b1e-ed0b-321c-9d0e-55ba127d31b7 | -5.29511 | -60.08963 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ed7a5fb-2655-3709-9e1e-c9249766a9a5 | -4.74995 | -55.65152 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 99cac79c-39f8-3edb-a78d-48dee517d00e | -3.04726 | -53.91096 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72acf21e-d244-325d-ac55-8f69bd7e0053 | -3.1785 | -53.83919 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4f1fa80-b12d-3650-99d6-dedce0cbcca8 | -7.14285 | -46.52336 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1dc2666-d257-3220-b801-e1eb075f97f4 | -11.2613 | -45.18363 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76397d01-1a43-3899-a56f-19e564bedf8d | -4.0064 | -56.25371 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c25602d-e604-306c-ab1d-be0c107edb05 | -3.14235 | -54.36827 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d9c743e-f256-37ee-9ec9-db6fb6b76828 | -8.59079 | -44.86317 | 2026-10-08 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51a696a4-df1e-3911-9b5b-3ccb46bc62a2 | -3.94798 | -49.01247 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8adfaade-5d3e-35ef-a189-5d7a35c06844 | -4.34567 | -43.79101 | 2026-10-08 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa1c886b-cdaa-3b7a-ad18-3c51f2f0d3b6 | -7.23029 | -44.27012 | 2026-10-08 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fd3b593b-de37-3e71-a0de-83afe30381aa | -3.14231 | -53.71692 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8b54c35-a03c-39c6-8534-2b78aec2fc58 | -9.83977 | -47.47417 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3416c5d6-e5c8-3890-bb61-7ccc9ab59efc | -2.88196 | -54.87763 | 2026-10-08 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc4042a7-0515-36ec-98f5-87bc38b6e063 | -3.48462 | -50.09078 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 976db6c3-0894-302a-a400-affa5ab924db | -6.11893 | -55.69963 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccf8472a-682e-3ce2-9ace-daac6ae54ab0 | -2.90561 | -54.023 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec5b8b20-3036-369d-b108-6d2075022a71 | -11.39452 | -46.68439 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d5b75f5b-9d7f-3bb1-8a27-809732a82c25 | -5.50633 | -42.83962 | 2026-10-08 04:46:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ecbda3f-ed69-3141-9b9b-d7d8324b295c | -7.1508 | -46.52458 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70de3bae-ce2d-3a02-9861-b665f31ecf56 | -3.27755 | -54.06795 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bc7e8c1-bcbb-3592-a587-e4f3c92492d1 | -2.99755 | -54.0579 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc7bb3d6-98a8-3cdc-93b5-6d3c9c4dcad5 | -2.94961 | -54.16741 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3293c240-9c23-3a0c-8ffb-83aff567886d | -2.98334 | -54.12301 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b6f3a7e-15a2-3a38-b9ae-4fc03e3ac307 | -3.04224 | -54.26683 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5df851d2-0978-3562-ab92-24df333ead86 | -3.316 | -59.47251 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6314de3-3828-3215-8450-ddd6222b5ae0 | -3.03886 | -53.94034 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 058a31aa-9113-346a-a88f-99e1dfe87174 | -3.02897 | -54.51579 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c60a2ff8-47e1-34b8-a018-4c525f3b0643 | -11.75996 | -44.94751 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb1bfbb0-e527-3b3b-8bc3-fb107427a55b | -5.95542 | -55.34622 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5795803-ccb7-3d8f-90a5-3e0576235e7e | -3.30147 | -54.0569 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 49f2d169-3a09-3d74-a0f6-67ec0a46a6ca | -3.58459 | -49.88338 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 727b7f93-aeed-3004-8de2-7bb06b94e3fc | -3.57175 | -54.66725 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e77ff573-d87c-32e8-905c-d279c6ac9cd3 | -2.5723 | -56.16056 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24a1d525-8eeb-35de-b5f6-93368a0a1ff6 | -3.09233 | -54.28796 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 756b9180-bbba-360c-8759-763ad67f3cfa | -2.50163 | -56.16931 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90cf42a9-0284-3105-a077-83cc5f9b96f9 | -3.39797 | -60.8422 | 2026-10-08 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39e0cbda-35e4-315f-bc46-9eafae0ea72a | -4.25041 | -51.04772 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0e1b895-4422-3277-bacf-df45b65d7c4d | -3.22692 | -54.37539 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1694e1e-1fc5-38bf-9ffd-0968e477f500 | -3.27892 | -54.05923 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c0cf67b-d437-3d18-ab22-63943eb9f1bf | -2.78989 | -54.09092 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 552565d5-b901-3062-9b28-2a76335a1e3c | -3.57776 | -54.65392 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7fe608ab-e59e-386c-b9ca-e00c1953d0ce | -3.17408 | -58.62621 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd1ab46a-75bc-3565-95ec-1f186b3567e9 | -11.63027 | -43.69542 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b7a1ed0e-0bf3-38a2-a303-52fa0d145534 | -8.71427 | -45.18536 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d6f157d-e454-3d89-a60f-c76300dfbb6b | -2.78459 | -54.07658 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 784bad55-4b5d-32ea-aba4-c608251a9f1c | -4.35884 | -59.94786 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 278e38d5-09bf-372c-9fab-400946ca9c6b | -3.64954 | -54.06316 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff13afd4-c47b-3d00-8299-cae72cd2c9bd | -10.77325 | -46.5853 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f446fd7a-6e4a-3f1a-9855-aafa6b6af099 | -8.08264 | -55.30218 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 746ffa83-2bde-39a9-b2f5-0ca2cf41380b | -9.80218 | -48.92544 | 2026-10-08 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 993c8fd5-cd7a-34aa-a567-0c2eb9d6a452 | -3.48463 | -55.43956 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93bbe27b-fb61-3f50-b116-f1765a09074d | -6.22773 | -52.83655 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 987813cd-3c7a-3f8e-b7c5-945e752dc467 | -2.96683 | -54.08442 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 685f0199-accb-3c82-a13e-713f04683412 | -5.20775 | -56.07825 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05511549-de17-30f4-a249-6ba985dd0ccd | -3.58007 | -54.66377 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e2a08c43-7c97-3adf-8040-2565b2cf7e64 | -5.87444 | -53.48803 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe583dda-7257-303c-bc65-d49d5cfc381f | -3.27508 | -54.05719 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 260ac0f2-2dba-3cc4-bef2-da903c7e233a | -6.40019 | -56.17174 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23dea705-0f90-3f19-9931-251b4fdba2c1 | -3.65991 | -57.09356 | 2026-10-08 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99943c74-8549-3642-bd44-9adc9d786878 | -2.8325 | -54.13371 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 810aca05-7506-3084-ba50-9233fca8ee86 | -2.56743 | -56.16384 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a0cabf3-8ed6-344b-8698-5c5e770c1981 | -3.0847 | -54.26396 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11d41f0b-ed01-31e4-b1b6-86acecc7afc5 | -5.73784 | -45.1549 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9620d6e3-42ab-3a74-8d56-922c26b9dea1 | -7.34884 | -50.01999 | 2026-10-08 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5b3f145b-ff6d-37cc-b0c6-417cabbaed7d | -9.36931 | -45.93492 | 2026-10-08 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d40085e-dbfb-3364-b546-35bc09a2dc82 | -3.54355 | -50.10338 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README106.md)
