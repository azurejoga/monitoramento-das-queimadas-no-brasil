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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64161fcc-efae-3717-9998-13dc94856364 | -8.52819 | -54.82074 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afc72642-a7dd-3203-a5bb-4fda109d21c6 | -9.17427 | -58.07231 | 2026-08-23 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54b3d509-96df-34cd-9549-4c8d832f1b0a | -6.79897 | -59.42766 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c4aa54d-34a8-3233-be58-a8b1b4bbadc2 | -11.21338 | -55.0431 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21d86f81-99a9-32a7-b8c3-c42d32608554 | -8.92832 | -60.71576 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b0d856-5f59-3140-ba97-a3129c401ab0 | -8.19966 | -54.98526 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f00402-afd3-3402-99a3-c890cef968e4 | -8.63567 | -54.69901 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5e5adcf-c5a1-3441-b7e6-5af7c523cb70 | -11.93513 | -45.52407 | 2026-08-23 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd6b759c-fb44-383f-bd4a-5c7adccbd7dc | -9.02068 | -50.74163 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db921530-e005-30cf-8a76-5d0a91094f22 | -6.67477 | -58.73172 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5924d4b3-0db9-3bce-a8b5-ddee62ccff30 | -6.75854 | -58.67744 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df5bce12-224b-3a81-ab5d-20c9b961ae5b | -6.76396 | -58.66167 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b8beed2-d376-3dab-97c5-dc5b76fdab6f | -6.79986 | -59.59501 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1fc40587-c549-3023-a094-6ba0bcfd6dd9 | -9.10176 | -61.59779 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 080a5de4-ba1b-369e-82a9-da1ef4c86e18 | -6.60347 | -56.36684 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b26d2766-99f5-3121-8f49-075106178d56 | -9.79862 | -46.61691 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 886fb632-b16f-3a20-b01a-542e393a4ea1 | -6.80289 | -62.9141 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75762bb9-cac0-3160-b85e-7a33e15287c6 | -6.96416 | -59.06778 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 210f8016-e843-3eb0-ac7f-874d648969fa | -6.54731 | -56.25971 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f00afded-c7b6-326b-a351-8723394d0b03 | -6.84351 | -59.43172 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a20fec84-1ef1-39a0-9db5-9da50e218d02 | -7.34951 | -55.67344 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0880a28-42d6-3c8b-9c2d-82d7a9526829 | -11.20842 | -55.07475 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4288e14-cdf4-3409-b4b3-1902b6106e3f | -8.08499 | -47.26432 | 2026-08-23 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4b463ba0-f861-385f-9f2d-df7f240a38a1 | -6.79223 | -58.65683 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a526718-7c01-3536-9012-bfd6226a600f | -8.53813 | -54.84369 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b527d0d-ed4b-395d-8d1f-4e778345f5e9 | -8.51983 | -55.34343 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 83e7e693-f63a-3471-ac21-00acaf42024c | -6.66631 | -58.73514 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 85d484cb-e7a2-3885-926e-c53e802d016a | -11.14409 | -46.20035 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 932b599d-1a61-3fb7-883a-4b2725374b40 | -6.7938 | -59.43396 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93a9cfa7-e93f-3c38-86cf-19a2beaaba94 | -6.81208 | -58.65531 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1ffff288-0519-3fdb-88d7-ac771d8976be | -12.23759 | -43.18562 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 466ae21d-8cd6-34ad-9c0f-40368f48b494 | -6.75781 | -58.65795 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b677c58c-3d37-3c94-afad-ac7182a3a986 | -6.76846 | -58.68883 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2826e40a-2b7f-32a8-83ab-842dadbd3546 | -7.56286 | -61.19986 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15d73fcd-49cd-31ca-983d-925b7397be40 | -10.04883 | -46.41763 | 2026-08-23 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 637aa7e3-dbb4-3fb6-99f8-2d9136d6d7ec | -9.13642 | -65.95778 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1c704d2-5da4-3d96-adba-372267cc777c | -9.17997 | -59.45773 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7223837c-9f16-34c3-b047-489ef14cd86d | -6.58038 | -56.24994 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0688b42-3cef-3a7e-9df7-f5c34c827a94 | -6.78531 | -59.41119 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49de995c-38ba-312e-b920-66232d278d89 | -6.80302 | -58.63924 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 787765fb-5635-32d1-a549-8aca4e2ba97e | -6.90683 | -58.99979 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57d35e65-10d9-38a1-a9e0-ba07a32c79d1 | -8.92347 | -48.54122 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e51b861d-e007-30df-bc46-5d54198b6726 | -6.70248 | -59.45448 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1846f4e-84f8-3cf4-8962-0b23f211e852 | -6.55482 | -58.5954 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0372c93d-364d-3761-a972-35e6712f4a3c | -8.53868 | -54.84021 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d369efb-26a0-3b2c-bf72-7a278af3292b | -12.06856 | -50.59549 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d29fa3c-d74a-3b0f-954d-f28ee8188d53 | -5.76546 | -57.5774 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| febb48d8-c045-3bcb-9ebd-489f683c6134 | -7.67713 | -61.11521 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36325b86-d588-3e54-b52a-1fb45c51570c | -5.7691 | -57.57798 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bb2326f0-9d09-3015-9c6b-73dafffc0a01 | -7.50051 | -60.0732 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f94a900d-e6b6-3f97-ac8f-95b51adc1c72 | -8.53592 | -54.83621 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7212a7be-1895-3037-9b0d-b2ff48425873 | -6.90295 | -58.99911 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00840f6f-5562-3ec5-b3c3-43d036f31d60 | -6.81495 | -59.43047 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54222259-741b-33db-8bf0-6df859faacbf | -8.53863 | -55.33215 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad79ce6c-cbbd-3e65-b2f1-94b831fe143c | -6.19926 | -53.51815 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 607d0166-b906-32c2-9ca9-c8960e42ca3c | -6.94773 | -59.07008 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f659bde-a277-3a39-9d2d-5cae803b6dd1 | -6.17364 | -55.5686 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 406429cb-60f2-3f26-9622-bc8920ddcc5e | -7.58506 | -61.20377 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f180bd2-3c59-3284-b426-77f182a397e7 | -4.96321 | -56.27537 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ee3c00b-7ec6-35d5-8498-6b2ced9f6b5e | -9.2139 | -60.89499 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b18cbad5-58b0-3162-8f8c-b61c2752f71e | -11.6105 | -50.55133 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b8e19599-720f-3bac-b2f3-6b988b139ba7 | -6.7101 | -58.73266 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4c2d273c-b425-3a29-bf11-bdadabb755f7 | -6.1871 | -53.53059 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0c66ec2-bf25-3289-8dec-8f2495d2c936 | -4.53041 | -55.51783 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a34c3b6f-bfbb-32f2-bd1e-be63ae90b566 | -7.66833 | -61.11359 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 371d3006-4380-3858-a7cb-a9a4c2e34c52 | -6.79985 | -58.6581 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b19beb0-619e-3661-98cc-37b78f34d234 | -6.24681 | -55.38419 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c07122c2-c48b-30bb-ba1e-6a8f1e055f76 | -9.01751 | -50.73642 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55e4a34e-b8eb-3d63-9931-0eb642e8881c | -6.85894 | -59.41284 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 89621882-d742-3063-aaaf-f9329fda4e60 | -6.69671 | -59.46426 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 579c832b-13c4-38dc-909f-a05d7c939177 | -8.62465 | -54.70438 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18a4bc61-685b-35bb-a0cf-d507b19d110b | -6.81751 | -59.66441 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb0558cf-b14d-3a70-a01b-5553f6617ad5 | -7.01147 | -59.55325 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04b677a4-a06d-3621-a8f0-87d07d9108b9 | -11.58491 | -46.94012 | 2026-08-23 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 222d0e75-470e-3d71-aa0f-30b40d7df63f | -8.92475 | -48.53208 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 167606eb-0084-3d1f-8c56-83054e637dfc | -9.1736 | -57.00072 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6817e35b-2e00-3658-9e8a-d5fce6a8e183 | -6.7816 | -59.65442 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad29f1b4-943d-3e70-adba-dda804da2b52 | -8.68309 | -54.69944 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da15584a-0725-31b6-a427-460e38ebdf54 | -12.36485 | -46.45352 | 2026-08-23 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d25a6e80-761c-3dbb-9276-b63d07158150 | -9.39426 | -60.58695 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8f0cf50-9b99-30a2-a6b0-cbb021f30801 | -6.83144 | -59.95393 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe5196f-c9e2-3636-9641-2350e1b1bd94 | -9.44043 | -51.59933 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d12a6e9a-9bc5-3276-9595-d5ca726f2778 | -8.95287 | -60.57663 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a93dfbcf-c034-3a32-9a24-74ba207ee2a8 | -7.60106 | -60.82722 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96b9c586-f21d-31ef-b4a7-1181b09fe00c | -6.79272 | -59.41597 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5b11be7-b305-3702-88f6-87da8dd0c733 | -8.53033 | -55.34155 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcbc3a3c-051d-3b50-b10e-322d631c4fd5 | -6.81035 | -44.81207 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa8f18ce-306f-3ba3-8675-e1b5fb6e8148 | -9.21084 | -59.79404 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a5057a6-9d1e-3c2c-ad02-9d66568b6687 | -6.75854 | -58.67042 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4165b867-b0ae-37b6-8669-cdb0ce3342f9 | -9.27666 | -60.91045 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed6284d7-cd1f-3799-82fe-7f5d76f38b90 | -9.53241 | -63.56592 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a30f3568-812f-3c22-a63b-7cb5c90c40cf | -6.78059 | -59.43904 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 867663e9-2a6e-33db-acbe-9687396a08fc | -6.66854 | -58.74529 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 84f31047-b4d3-3a28-8ff6-36244516ed41 | -6.75704 | -58.66264 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f01794d1-6fc5-3d9e-9bb5-ede50d394407 | -6.90065 | -51.56404 | 2026-08-23 05:04:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e98b828b-fb69-39ab-a981-69aaecc213e4 | -6.53326 | -56.1743 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e724b00-42ff-32b6-83f9-98ca70245cb9 | -6.80937 | -59.39028 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeaa4f00-9c4b-312d-b584-6fa96d1472e1 | -8.91714 | -60.72999 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34b49e8c-6029-36c8-b13e-3c852c817daa | -8.81518 | -46.62149 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b2e28c5-64dd-3a25-b79f-be444181ea66 | -9.51505 | -51.67474 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README49.md)
