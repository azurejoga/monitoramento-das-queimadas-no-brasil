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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef11b2a3-adb6-334e-8767-97b552cea7c3 | -3.68408 | -54.56723 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81f951b4-6a0b-3033-b1e9-79b885b7f332 | -3.68353 | -54.21517 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8120b39-587e-3008-8258-960b222df314 | -3.62786 | -54.67392 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ade505f-8563-3d38-a353-4d54418e917b | -3.62416 | -54.67333 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a54ee55f-8abe-3f31-9c06-1cc6623df6db | -3.62114 | -54.66836 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb3cce1b-7504-39a6-9a23-b7da3c56d800 | -4.05194 | -53.88045 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaef9fbd-fad1-3157-8cc1-155231108d3f | -4.02598 | -53.97233 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 602cea10-83ce-361a-adbf-ab6b7f663eea | -2.061 | -55.86335 | 2024-10-19 05:14:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e05b2ba3-dfab-38cb-adb1-7e3ec3300d6d | -1.74019 | -55.01204 | 2024-10-19 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e94e313f-f8ee-32be-9e1c-372e7d390002 | -1.25875 | -55.90655 | 2024-10-19 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1627806f-786a-3613-ab73-d90503ac98eb | -2.46981 | -55.62465 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c5ec696-5bff-3599-80a7-48b683f1baad | -4.71901 | -55.98757 | 2024-10-19 05:14:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa6d4c36-555b-3a26-9c2e-163509fbb2af | -4.57576 | -55.83787 | 2024-10-19 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b780b6f-bda6-36cc-a2f3-0c2e587f5c1a | -4.50795 | -55.83194 | 2024-10-19 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3923230-1798-3870-9f2c-928ca0dcf813 | -4.1441 | -56.10125 | 2024-10-19 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56522506-ccda-3231-9b4f-6880310f3a91 | -3.43137 | -57.5585 | 2024-10-19 05:14:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1312e994-6182-3b4a-9261-a8f570cd032a | -3.26192 | -57.03736 | 2024-10-19 05:14:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f59cfb9-1a7e-3eab-84b7-5dc396435133 | -3.2302 | -57.08673 | 2024-10-19 05:14:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2096c218-7c4e-3848-9dd2-8bcc57fbc962 | -3.08396 | -57.32591 | 2024-10-19 05:14:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ce33da8-7966-32f7-872b-afbecac28a1a | -2.41022 | -57.8969 | 2024-10-19 05:14:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10b3d101-a9fc-3ca0-a4b3-fec69d3584ac | -2.40968 | -57.90033 | 2024-10-19 05:14:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77fa9ed6-9c59-3059-8ee7-cf7e84cbccd1 | -2.40638 | -57.89982 | 2024-10-19 05:14:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b175305d-8e2e-35ff-bfa4-6ff4b5771311 | -2.37633 | -57.18126 | 2024-10-19 05:14:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21bf36ea-5a04-3123-99c8-ab6517b2329a | -3.79234 | -58.44074 | 2024-10-19 05:14:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27edf144-76f5-36d7-b309-42388012cae0 | -3.65834 | -58.79703 | 2024-10-19 05:14:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e89d27de-b211-386a-af94-cc8100951252 | -3.21687 | -59.35572 | 2024-10-19 05:14:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ba9bcd3-9b81-37c6-bb4c-b519408e1915 | -3.21353 | -59.35518 | 2024-10-19 05:14:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfeb10d7-e54f-3c8a-9664-bdbc52ca8a50 | -3.20963 | -59.35819 | 2024-10-19 05:14:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a41c78ae-0f04-3982-83f6-710b5c2a318e | -3.17249 | -58.96902 | 2024-10-19 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d123cb0-9814-3c2d-9e67-27aed31c4918 | -3.15178 | -58.56234 | 2024-10-19 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caad4178-1dab-3a6a-bd7e-39778b7cdf17 | -3.06577 | -59.19168 | 2024-10-19 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ee56572-c0c8-3a9f-9f5e-3cd46cd6747e | -3.06521 | -59.19519 | 2024-10-19 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad6bde64-cc9f-36cd-8524-bfa2272f8c69 | -3.06244 | -59.19116 | 2024-10-19 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c941e477-c17c-344e-aa2e-7667055f2fd4 | -3.06188 | -59.19466 | 2024-10-19 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1331d6d6-a53f-3e49-831b-45159cca5cf6 | -3.05966 | -59.18713 | 2024-10-19 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c46599a9-171d-3174-8068-b7ff369e5afa | -3.0591 | -59.19064 | 2024-10-19 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ec169db-fef9-3ef0-8000-78a30e445ce3 | -4.27115 | -59.99093 | 2024-10-19 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4f81ea1-5dd2-3e4c-8593-a600740022d9 | -4.27058 | -59.99453 | 2024-10-19 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 162b1bad-f694-368c-92b5-fe29451a5c44 | -4.26778 | -59.9904 | 2024-10-19 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd5d3973-d157-314e-b69c-a0f638a93488 | -4.2672 | -59.99398 | 2024-10-19 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 937598cb-18b0-3f08-afb3-b18c52310027 | -4.20161 | -59.96141 | 2024-10-19 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5424745f-5528-3821-92ca-14ab50336c5a | -4.19824 | -59.96087 | 2024-10-19 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8348022f-21d5-3f2d-adb6-2c2926ded328 | -3.98944 | -59.21836 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4efb039e-3f51-3f76-bad0-bfdf4cf7a363 | -3.98889 | -59.22184 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41e36c9b-ecd4-3572-a043-42c1dc2e5afd | -3.98834 | -59.22533 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad29e71c-4185-315e-9cce-38c38bea9928 | -3.98612 | -59.21783 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 731359bc-f1ce-3a8e-9e74-64eb5b63d5ff | -3.98557 | -59.22132 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4ae90a0-0d4f-3a2b-9243-999a340e07c6 | 1.15898 | -59.44967 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6541d9f8-c8a3-3bad-a878-597db89f8783 | 1.15553 | -59.4502 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 715d9b3a-a966-3b2d-a2f9-d3b954784871 | 0.99758 | -59.44607 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f0ae106-f808-3d8a-8879-f4632f391f17 | 0.997 | -59.44234 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81492ca3-fc9e-335c-a5a4-e9f7b8b6131d | 0.99641 | -59.4386 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbcae56d-3548-3b05-8e9a-ef081cb1bb54 | 0.99414 | -59.44661 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b5ab7a3-9f23-3c31-9939-5a930140a896 | 0.99355 | -59.44287 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcd49100-4c01-3fc1-962c-a2f8daa7440f | 0.99296 | -59.43913 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22ade92f-ad5d-319e-8343-520b51600fa7 | 0.86962 | -59.61693 | 2024-10-19 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b4d64ad-a8dd-3337-9cda-cfbec267f21c | -2.08766 | -59.93706 | 2024-10-19 05:14:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec7f999a-e4e2-3092-ae73-53cac93e06d0 | -3.27838 | -60.23398 | 2024-10-19 05:14:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b8dfc133-037c-3284-bccb-435f2c856027 | -3.27495 | -60.23344 | 2024-10-19 05:14:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3b47819e-013b-3925-9e46-a20562160148 | -3.18608 | -60.54732 | 2024-10-19 05:14:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7862990a-22fa-32c8-a409-70e750513e8a | -4.70953 | -60.80437 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25ce192a-a6ad-3112-92a9-34db87d87575 | -4.70893 | -60.80817 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e95da38e-b3fd-36ed-822e-152796e341ad | -4.51139 | -61.11744 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c982dcaf-e330-3b7f-b294-be95239ea55e | -4.50852 | -61.11295 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b97decbe-53c4-3014-9372-c3a6af2bbd2d | -4.50788 | -61.11687 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6b84ac5-e342-3182-9c51-8c23ac44a9c7 | -4.50501 | -61.11239 | 2024-10-19 05:14:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b23ba6f-1a2b-3c78-86d0-5c202d0bc6b1 | -4.31587 | -60.89289 | 2024-10-19 05:14:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2db87cdf-0052-3cd2-b950-fd97e56b54fa | -3.99918 | -60.39884 | 2024-10-19 05:14:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d170c5e-1355-3a09-bd13-17b3557d369d | -3.99575 | -60.39829 | 2024-10-19 05:14:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1094069-b953-34d3-b353-cd138a9900ca | -3.99233 | -60.39774 | 2024-10-19 05:14:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78640902-0df8-337c-b4c4-421a7316068e | 2.14267 | -60.85432 | 2024-10-19 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4030a515-2343-32f9-b9ab-1189d5d87b10 | -3.51256 | -62.73141 | 2024-10-19 05:14:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 939ab3f0-4801-3c15-a863-128f119c2c0d | -3.0905 | -61.69996 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66d7ead0-8818-3542-a497-401e67b67a53 | -3.08683 | -61.69938 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 963082cd-8e13-3718-a1c4-c09bf0ef10f5 | -3.05678 | -61.67824 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01faa009-5ce4-3deb-bb05-0a23ffaa5af1 | -3.0561 | -61.68254 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9603a7e-1691-3569-9fbc-3ec32f971a1d | -3.0538 | -61.67336 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ff5caad-e945-39d1-8011-7a90714fa699 | -3.05311 | -61.67767 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61fc28ac-4a7f-38c2-a541-6cf9b48f23a0 | -3.03478 | -61.67472 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5022417e-55cf-3fc5-8108-20b5b23dfa89 | -2.87678 | -61.88894 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2aae9799-6fac-3f58-8a61-10f4665b91bf | -2.87378 | -61.88392 | 2024-10-19 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8afee56-c171-3f20-8073-d88c4c763d88 | -3.70646 | -64.45279 | 2024-10-19 05:14:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc6520df-1f5d-3676-a251-5a0583fa6584 | -3.70213 | -64.45206 | 2024-10-19 05:14:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b195de0e-17bc-3156-bf90-fe6aa6c3cc84 | -2.8556 | -53.3256 | 2024-10-19 05:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| cff3b831-f33f-38bd-867c-26d583edecdf | -2.9489 | -52.9174 | 2024-10-19 05:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c8c8fcec-1c3a-3076-beba-53fd755e8770 | -2.9489 | -52.897 | 2024-10-19 05:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b77b671c-d7ad-35c5-90d0-a87f1c42e5fb | -3.4202 | -50.2164 | 2024-10-19 05:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 059b2510-bc9e-35ef-9bea-3d10cfc8d470 | -3.4203 | -50.1954 | 2024-10-19 05:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 48a28c06-9506-38c6-b631-a80216933b8b | -3.4387 | -50.2158 | 2024-10-19 05:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 189560ce-d10e-3675-b10c-f790eff32864 | -3.4388 | -50.1948 | 2024-10-19 05:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c19e57fc-9fef-3479-bf6f-b2486ffd09ca | -4.6873 | -45.8504 | 2024-10-19 05:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a262d6ba-f469-344d-b56b-82274d7e854c | -4.6875 | -45.828 | 2024-10-19 05:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 48b8390c-237d-35ef-8964-453523a708aa | -8.93596 | -65.90435 | 2024-10-19 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82c7c2cd-aacf-3e77-8141-260ad4430c32 | -8.93233 | -65.89927 | 2024-10-19 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b87b858-eb34-33e4-921c-b5c5a29a83b7 | -8.93158 | -65.90354 | 2024-10-19 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aec90f05-9dcb-3614-bfdc-91382fbe4e9e | -8.45337 | -66.96222 | 2024-10-19 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04eabdb8-7787-3344-93c3-a8a0e71785fa | -8.94238 | -68.56022 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f16cf80d-78cd-3572-8915-9f878574cad3 | -8.93715 | -68.55922 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d184e0b0-ee8f-3d49-9f04-6d6ce75f1669 | -9.08162 | -67.83928 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 071f86f4-509e-3c39-9807-ef734d76a8b9 | -9.08147 | -67.83974 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README44.md)
