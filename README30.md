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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a526a2c-dbfb-3a46-b52b-e85540ff5ff7 | -3.38272 | -46.07613 | 2024-11-01 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79d14dc6-299d-3f99-b472-4c8bf0087b8b | -3.38217 | -46.07965 | 2024-11-01 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5f5009e-d510-36ff-92e2-55620468337c | -3.30289 | -46.19668 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc5f9490-39f1-3437-ae2a-d065fad115d5 | -3.27937 | -46.36808 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 766fa8a5-bcaa-3eab-9727-d5db1b4d14e7 | -3.23157 | -46.49933 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb2d9743-4071-3aa5-af4b-a0befb800b77 | -3.22826 | -46.49881 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ff55a10-5244-34f8-8c48-05c339d356e3 | -3.22494 | -46.4983 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2bdb89b-5570-31f7-806e-be1d4cf61565 | -3.20963 | -46.18218 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50a7fbdc-12f8-31f4-a582-ce245c758f20 | -3.20952 | -46.51009 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6318a233-4f5b-3e61-a2a5-286238bd7ee0 | -3.20738 | -46.17466 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 861959e4-6d2c-34a0-8a54-e976184ca9af | -3.20461 | -46.17429 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 117eef71-7109-3720-aee0-22274430d897 | -3.20128 | -46.17377 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed0bdb51-4263-38d6-9e74-daa6abf0cf5d | -3.15535 | -46.48746 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af5ecacc-948c-3682-8c54-480e209706c0 | -3.12209 | -46.04656 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68e63820-beee-32ff-9e90-bfbe6970ef89 | -3.12155 | -46.05008 | 2024-11-01 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5502cda-a7f1-3897-9b9c-3052a018f8b0 | -2.32401 | -46.7179 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d73d09d-a039-3d43-bdae-ba0a3d0b501d | -2.32347 | -46.72134 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f08d820-a749-3f7d-ba74-ea53743c0a0f | -2.32178 | -46.71052 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af0ac1ae-5a52-322e-8a3d-f96a3795c1e2 | -2.31248 | -46.72667 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5706ffc5-2b08-3d23-a4af-d7afc21f6559 | -2.31194 | -46.73011 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00395f40-bd1f-3cb0-ac60-2afb0430473a | -2.29489 | -46.73098 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc582d08-14b0-359a-8e9e-e01a299e438e | -2.29327 | -46.74127 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 042288ea-e201-368c-814d-7357ad2d5551 | -2.29159 | -46.73047 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ee7bfb4-714d-33ab-b7cd-4503992d4ad1 | -2.28721 | -46.73682 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b03795da-a72a-3cf1-80b0-52d6665d07e6 | -2.28391 | -46.73631 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49640992-5a22-34f5-a12b-c79c8bb01a1c | -2.28337 | -46.73973 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77e8848c-1323-34de-9afd-c69de686a5d0 | -2.28007 | -46.73922 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9457c488-0364-3841-8608-e3ac2d6cd64b | -2.27709 | -46.67193 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 333c82d0-ff4e-3792-bc85-004ee06c03b5 | -2.27433 | -46.66798 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61f395cd-07bf-3376-9c40-c01a2381d40c | -2.27379 | -46.67142 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4c550e0-0aa9-339f-bd97-d1cdaf59fa14 | -2.27332 | -46.69597 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a6796b7-04e8-3ffa-9166-1052edbaec73 | -2.27325 | -46.67485 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 412b34d6-15fa-3c87-b071-6268cd223b2c | -2.27278 | -46.6994 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd0ebb95-63d3-3656-9707-b2a2667360c1 | -2.27225 | -46.70284 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abe31c6f-867b-3fdc-9863-59094152514e | -2.27103 | -46.66747 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e385c347-168a-37e4-bb10-60d38963867f | -2.27049 | -46.67091 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 280cbb26-cf89-3ca7-b4e1-a9db9cc42cb4 | -2.27002 | -46.69546 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f33f13-5326-3d2a-9425-dac405c9d54b | -2.26995 | -46.67434 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1564ea12-da43-323f-ae03-5978d335dad3 | -1.12782 | -48.37383 | 2024-11-01 04:29:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab6cbff6-e302-33ac-a5b3-09630ec183e5 | -2.26948 | -46.69889 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31ffaaab-9b90-30cd-a578-e3294fd7c43f | -2.26941 | -46.67778 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aae3379-2a11-3c7b-bef4-34e927a2fea7 | -2.26894 | -46.70232 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc340af5-fbf5-3da0-9f80-51cae80a3fb9 | -2.26826 | -46.66352 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c942f65-578c-3df4-a77f-96438ae7c269 | -2.26772 | -46.66696 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ca55c70-8634-3376-a68c-2351a6252f7e | -2.26718 | -46.67039 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 816dce4f-666c-37c0-9fef-f98f6d14da0a | -2.26665 | -46.67383 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 273a31a1-c087-3b99-b32c-c5d35488156d | -2.26618 | -46.69838 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e9983ad-f90a-3c6a-83c3-2cd634400763 | -2.26564 | -46.70181 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 695f0c97-061d-3366-91cd-7f845d232614 | -2.2655 | -46.65958 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efe9e29b-9526-35c6-8dc4-c6c1f7cc7e39 | -2.26496 | -46.66301 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff36f84d-98fc-35da-be15-d40b3759291d | -2.26442 | -46.66645 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9911971f-547a-3eed-b503-9b58fe6e25db | -2.26395 | -46.69099 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c956353-457c-3de1-87c9-2f379a8a9bba | -2.26388 | -46.66988 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d17bdbd1-a32a-32e8-b9fa-3823b95149a5 | -2.26288 | -46.69787 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba838b7d-2d0b-3dc5-b17e-6ebd544c3002 | -2.26234 | -46.7013 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83ba4e9f-09c0-3505-8943-8b8bde1a1222 | -2.26219 | -46.65907 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6f58b1f-2f73-3291-bea4-74a6338e8a4f | -2.26165 | -46.6625 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38018b13-a2f2-329d-a338-9a61db2a6dac | -2.26112 | -46.66594 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 668bc1fd-d35f-3d8d-a695-09b802573e19 | -2.26065 | -46.69048 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8f9fbb1-63d4-3a8b-aaa3-c45b8c7ee032 | -2.26058 | -46.66937 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f570007e-483b-3b5f-b3d0-41b059902040 | -2.25908 | -46.65499 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05b0467e-b891-3833-9225-b27b84fb7e28 | -2.25854 | -46.65842 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82bbe970-975e-36db-994c-e980f6157dcd | -2.258 | -46.66186 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17e84ace-5534-372a-8fad-96df2ae0aea7 | -2.25746 | -46.66529 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c82783b9-b1cb-3ddd-a2b4-5a6a941f2417 | -2.25578 | -46.65448 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 947eb592-eca4-3d6e-89fe-67daade54f93 | -2.25524 | -46.65791 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53043480-e680-3a9f-95b1-0b8236407483 | -2.25469 | -46.66135 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26abab3f-1f57-34bc-9500-3c625a1cf353 | -2.23554 | -46.69707 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dbb5266-eef4-3fb2-b335-7b96360c6fe8 | -2.23224 | -46.69656 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64d26abb-6ece-3344-9ef4-992d37136dec | -2.2317 | -46.69999 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0154ac57-3ece-3209-b156-46a125de9635 | -2.22894 | -46.69604 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5650a563-7a51-31fe-8dee-25e810cc0fec | -2.22564 | -46.69553 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2087fbf9-cc3f-32b8-a036-aa372b9bbe9a | -2.2251 | -46.69897 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7280027d-2d43-355e-beff-d75a0fc373c6 | -2.2218 | -46.69846 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50f06149-c975-3d83-b780-e6ba1c5d268f | -3.2971 | -47.01464 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0008de77-c60a-3d23-a24e-90b62bdda71e | -4.95716 | -46.49908 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1742841-004b-333b-8df3-ca6ac2a6bf81 | -4.95662 | -46.50257 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44914240-163a-33ca-98ff-5863a607e18e | -4.94405 | -46.82277 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b170375b-6fac-3ad0-b440-9cfde6342cf3 | -4.94351 | -46.82623 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c03113b-3ed1-3d2f-aed2-d96c298ea926 | -4.9131 | -47.04169 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f402c938-8284-3c16-802d-9154a06c7873 | -4.91256 | -47.04515 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0feb02b-4166-3a5e-873c-32d346e5be28 | -4.90979 | -47.04118 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 05a095e8-541d-3c68-a119-964e44f79206 | -4.90925 | -47.04463 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 7d2209d0-5ab7-3651-9d8c-921820019450 | -4.90871 | -47.04808 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4121e88b-1c4d-333f-a543-f9a82f36515c | -4.90817 | -47.05153 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b631c04-ad5e-3e9f-a6fe-a6347a786fff | -4.90763 | -47.05499 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 635aae7f-a90e-3b72-8fdb-3d9a99d586ba | -4.8789 | -46.84832 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a8683cd-7cba-3ed2-8129-05c4e2c9ec05 | -4.85137 | -46.87243 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 070868bb-1c04-33ca-94da-b227b5b97a60 | -4.84806 | -46.87193 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2994a60-2b97-31e1-81ce-2a4b073ad875 | -4.80906 | -47.07855 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32a4ac84-d628-3f8f-9a81-cfdcb7eadc0b | -4.77711 | -47.84244 | 2024-11-01 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21aa4e17-689b-3038-a43e-aa6c33f6664e | -4.70762 | -46.61806 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c0812ec-5969-3f84-8ef8-c6af9777c5a3 | -4.70538 | -46.6106 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22e3ba3f-c10e-3f08-8db2-9a1086a23ebd | -4.7043 | -46.61756 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10eb6325-d293-361a-9e89-c5f88b10902c | -4.70324 | -46.84197 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f2f136f-2274-348a-bba5-3930f985ec24 | -4.70151 | -46.61356 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b64fabd-29d8-3957-84ae-af6085628ce3 | -4.70097 | -46.61703 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b867eea-bd2f-3077-a23a-c7ed54718400 | -4.69764 | -46.81266 | 2024-11-01 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cf863b1-0b29-3fc0-8dd7-c5775313b6d0 | -4.69257 | -46.32508 | 2024-11-01 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 920ed919-c3bd-3f95-8788-9a166bb4f80c | -4.65634 | -46.31586 | 2024-11-01 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README31.md)
