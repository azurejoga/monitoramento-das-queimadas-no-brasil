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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8615b02a-7649-332c-bcdd-b03eca82c8e5 | -12.69354 | -60.81579 | 2024-10-03 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 424696fd-c8ba-36ad-b9bd-673594b8c893 | -12.69023 | -60.81525 | 2024-10-03 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5952a716-3587-3d46-9275-442112cafab7 | -12.67331 | -60.92154 | 2024-10-03 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66b9b129-3982-38d9-a98f-5de2fb77f7b8 | -7.9198 | -61.27194 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88ade1e9-2258-38a2-a56a-fdbd234d4048 | -7.90089 | -61.47538 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1053828f-78ff-3651-b8e2-17d182711266 | -7.90034 | -61.5226 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03d1de78-fdf4-379c-a17d-aeff83dab67b | -7.90027 | -61.4792 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e5fd532-00df-3f13-987e-eb6dea0c959e | -7.83997 | -61.33284 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdd43e75-794b-3719-8bda-212364a8922c | -7.76499 | -61.57602 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 326e91fa-7950-3590-adc5-ef008bd50587 | -7.75463 | -61.12263 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67b8a2df-be49-3cd6-be65-14bf702c8a72 | -7.75403 | -61.12637 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d8d7f09-1dd2-32ab-959c-4fd83b7c6685 | -7.73371 | -61.10004 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1d3e986-d991-3de4-af20-af6859b7c000 | -7.59239 | -61.235 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a2ed21-ba0e-34d7-9b9a-bf0f4a9ab451 | -7.58895 | -61.23444 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adebac39-46f8-3539-ba80-774b2064727f | -7.88941 | -61.61191 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 803299db-9f6f-33ce-a3ee-5607f42029cc | -9.17678 | -61.89494 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58c27707-fc4a-3f2d-8621-f1eb3ff78d27 | -9.16681 | -61.67204 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 158e218d-4bf6-34d6-8f85-f51e1b4913ba | -9.16556 | -61.67965 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d973c4fb-5fcf-3574-952d-206c7f0dc90b | -9.16398 | -61.66766 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 31035ae8-730e-36b6-bc83-0169567836f1 | -9.16335 | -61.67147 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 611c17ec-32fe-3aa3-8d8b-eec7501e6035 | -9.01622 | -62.58643 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45b430e2-204b-3cfd-ae6f-71e35e34a638 | -8.97593 | -62.01877 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8c096ed-c6d0-3365-b21a-12f11ef902a0 | -8.90257 | -62.39422 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4be61d8-07e4-3ba0-a668-a993fea88696 | -8.88721 | -62.33907 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1ee8ea61-1000-30b3-8155-457a7e1f0bf0 | -8.88466 | -61.84836 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c400b44-28a2-3552-b3bb-088884205dce | -9.24998 | -62.37819 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 777495ed-e749-3f0d-bb2d-ff0edaf493a1 | -9.24643 | -62.37759 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90c39875-3500-374d-88c0-728a08a8514c | -9.08061 | -62.35201 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd523111-cc61-3ad8-9096-d42fe2b77e20 | -9.07705 | -62.35143 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7eabeb7f-cbde-302d-89fe-4503131452fb | -9.05419 | -62.33511 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6350d284-ef86-362e-abe2-c5d8f40a9907 | -9.01263 | -62.58581 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1496bb60-9254-3c4e-9199-c011a54837d4 | -8.94607 | -62.17701 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 284f0e4d-02a2-3332-91a9-e25e4fd522b0 | -8.89565 | -62.33213 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 331211c7-8762-321b-a486-d820c6959e3e | -8.8921 | -62.33154 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a07c6d1-a87d-3eb5-8d2f-9fdf51bb4951 | -8.89144 | -62.3356 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e4c1f5e1-11ce-395a-bf5f-cbd683d4d887 | -8.88854 | -62.33095 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e428b48f-299c-3412-a398-feb5fe0bb164 | -8.88788 | -62.33501 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a9bbaff9-463d-360a-9da7-49892b96ef1b | -8.88432 | -62.33441 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1cc6e8ef-7be0-32a4-9d3c-ba460a7fb91d | -8.88366 | -62.33847 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1beadae3-a012-3945-a42d-978369fe5c3a | -8.8801 | -62.33787 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a3ced583-d1a8-3f57-a881-842edc06ce2d | -8.79162 | -61.97007 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef5cdb40-865d-3ab0-8459-a89d0594a813 | -8.78811 | -61.96948 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcc98b16-8857-300c-bd8b-8a704624fd2b | -9.09564 | -61.13584 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5adb47b-c09e-331d-b6d8-d4810443560d | -9.09505 | -61.13951 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10a8fd8f-cc0e-3c09-82e0-93825458ce00 | -9.09284 | -61.13161 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5849a333-8326-375f-81e4-d16d6588d714 | -9.09225 | -61.13529 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70d65fe6-e3c5-378e-b06e-1d0b7ca919c1 | -9.09166 | -61.13896 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04efda58-5e8c-3731-bd99-a0b366be3cf1 | -9.08827 | -61.13841 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ec41650-70cc-3611-b66d-5324d60c5b29 | -9.08547 | -61.13419 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d8de607-6f40-37c3-88df-3a8330adbefa | -9.08208 | -61.13364 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8925640-ee76-356c-a5ba-e90493ec451d | -9.07869 | -61.13308 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b41a9ff-8d42-3b79-8964-512ce62de17e | -8.17654 | -61.37834 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9ce7377-1d0c-3b31-b3fb-b9b252de5096 | -8.17594 | -61.38211 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66175ca9-d142-39c3-921d-ebeb667895e9 | -8.17553 | -61.36265 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56e83516-5a21-308c-8ebe-0c34788e223a | -8.17492 | -61.36642 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea11ee5b-74f8-3672-8779-51e115596378 | -8.17432 | -61.3702 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ce91d00-2fdb-35f7-9de4-27b1f2055cf6 | -8.1731 | -61.37778 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a80babe2-7f0e-30c3-a999-a22fa4867fcc | -8.17148 | -61.36586 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da81c115-ae1f-3911-8ef5-1581fd314b04 | -8.17027 | -61.37343 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c39bb7b-39bf-37d7-b17c-dcc3133548b5 | -8.16966 | -61.37721 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddd40fe8-b41e-353e-ad5a-addf6bcd64e0 | -8.14534 | -61.39653 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83ef8d90-7a7d-34c5-86b7-297d9d3114ba | -8.14189 | -61.39596 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40308b77-54fb-3110-af96-bae44bd893f6 | -8.13845 | -61.3954 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2bff995-2c8d-31c5-be14-d3abad40020f | -7.98925 | -61.42577 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d348cfc-52f6-3c9c-8340-98b5329a7cf4 | -9.18026 | -61.89552 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ecae104-10d8-38dc-ab7a-dd193899a6b4 | -9.16743 | -61.66824 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e3ad0196-27a8-3aa3-a7bf-1078bf50da40 | -9.16618 | -61.67585 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f9b76104-1594-3cdd-9c76-0f88ed280acb | -9.1646 | -61.66386 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 664123ad-48d8-3158-b355-1c90366bbb35 | -9.16286 | -61.89263 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f81f6d1-223c-30e5-96df-ada0af4dd903 | -9.16273 | -61.67528 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e843df83-983e-34ee-900a-fc41b7060579 | -8.87328 | -61.84294 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50a22b2d-7165-35e2-b6d9-85b834db616a | -8.8698 | -61.84236 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34a070b2-71ca-3f46-97e2-339474a43823 | -8.86506 | -61.84954 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 726dbcd3-2978-364c-95da-3b5a6c6d53d7 | -8.78876 | -61.96555 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b139b3e8-8f98-3b73-85d1-2995dc463841 | -8.09119 | -62.01856 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 774f9c4e-de1b-3d33-9ed4-ba0e27431f5c | -7.9388 | -61.79911 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5d2126d-1f0f-3d24-86e1-7f4b56752764 | -8.59002 | -62.4222 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 173ca06d-6930-31bc-b852-36e02b7132cf | -8.58714 | -62.41742 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56a761df-c5e1-383e-b002-5f3d3eaee23b | -8.58645 | -62.42157 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 742e1c47-2678-3bb4-a02d-44f8b4bdbe8e | -8.58356 | -62.41681 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3584d2f9-3a46-396b-be4d-f80e512f04e8 | -8.58286 | -62.42095 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0419e9b5-e734-31a6-a51e-fc4ac4f522ca | -8.57928 | -62.42033 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cac3be8c-b6c7-3a0e-b8e8-4bf32829bdda | -8.56366 | -62.44759 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 817f9152-fe0d-3e8c-a6d9-1e731006fecb | -8.56102 | -62.48545 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40ded8ee-f962-3a06-9544-994e40209d78 | -8.56032 | -62.4896 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13a2d792-87fb-3ad9-b582-d96e5dedf10a | -8.55742 | -62.48484 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88b45e26-ae12-36f4-88ce-aa7429fe31e6 | -8.55672 | -62.48901 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9e88c61-6898-3bbb-9019-0267fc3b9ad5 | -8.55635 | -62.48144 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28703f01-7642-330e-b97a-57928fc5523a | -8.55567 | -62.4856 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ac5001c-f22a-3944-85ad-8c910b14d9db | -8.55452 | -62.48009 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0e7e458-f4dd-3e10-a13f-88423775f83f | -8.49773 | -62.52313 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f8ed1b6-cb62-3330-8413-563fdb62702a | -8.17292 | -62.24776 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 746e23b7-1d86-3cde-a7b4-9c4023188fe1 | -8.17224 | -62.25185 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acff9938-9f0d-354f-9d95-a31d50d61e9e | -7.93529 | -61.79852 | 2024-10-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cea17cbd-4897-36ba-92bc-04feb7e7c16d | -9.08945 | -61.13106 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cffdf3b8-76bd-32d8-af57-e79c30f91036 | -9.08886 | -61.13474 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39372f3c-53cf-3180-8ff8-f6b0416e71e0 | -9.08606 | -61.13051 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ba2ca0-83aa-3d17-8398-75efa2a34928 | -9.68811 | -62.36028 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e91a3d51-06ca-3a5c-aa73-0038a3f7a0a1 | -9.61185 | -62.22913 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c694ac53-5c49-3bae-87f9-de642975d7ec | -9.55351 | -62.38372 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README166.md)
