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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b463c25b-6531-3fa1-911c-b209c2c98287 | -9.968 | -60.1937 | 2025-08-23 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 1bdbaad1-b6c3-34d7-a101-ecb141a4eb68 | -14.2936 | -58.5249 | 2025-08-23 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 6ca957cb-316b-37f7-849b-2172edd4c16e | -8.5944 | -62.6126 | 2025-08-23 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 245a2ec1-59ad-3443-9e79-c23efd98f9ae | -6.6044 | -44.5624 | 2025-08-23 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 13f06a59-7d86-366b-bc3a-487eabfad2dd | -5.7614 | -57.6002 | 2025-08-23 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| a3813842-6d19-314d-bb4f-0afc0d484117 | -5.7429 | -57.6009 | 2025-08-23 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 217e1a7d-ee24-3ce0-8d03-eecaf337d5d0 | -9.1897 | -59.6171 | 2025-08-23 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 761eddeb-e1ec-3aea-b275-852e063bcb6b | -9.968 | -60.1937 | 2025-08-23 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 170.6 |
| e9b07b62-e457-3260-b353-f156e3e96f04 | -5.7431 | -57.5814 | 2025-08-23 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 9cdc622b-6f51-353a-9afa-1f72b927df38 | -4.3482 | -46.4695 | 2025-08-23 04:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a5503701-3cae-33f2-a020-444e08078d58 | -8.5943 | -62.6315 | 2025-08-23 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 40bec192-4650-35d5-a37a-30f89dfcd3fa | -5.7615 | -57.5807 | 2025-08-23 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 6fd85a6f-108f-3630-b2c2-8f79256d11a2 | -9.9492 | -60.2141 | 2025-08-23 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 9f9b1e74-94c0-33a8-8e03-3321ad8f4e7b | -9.9495 | -60.1754 | 2025-08-23 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 588689b9-9731-3976-8279-ebd0def09dfb | -9.5179 | -60.5461 | 2025-08-23 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 96071348-7c83-3f86-aad1-0065b6e4604b | -6.37 | -45.5356 | 2025-08-23 04:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 0b2a19c5-a318-32d9-8c5f-891b182a5766 | -9.9681 | -60.1743 | 2025-08-23 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0a927013-5203-351b-8074-a1bd543b3582 | -9.9493 | -60.1947 | 2025-08-23 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 504.9 |
| af8d97ea-d591-3771-9338-945b44624e52 | -9.518 | -60.5268 | 2025-08-23 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 285eade8-e2ff-3af4-b3a0-79341e9d496b | -8.613 | -62.6118 | 2025-08-23 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| bff68e76-010b-32b9-ab74-48e76dcd05d4 | -6.3698 | -45.5582 | 2025-08-23 04:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c76991e6-eb0e-313a-bdff-b0fc8e3d7032 | -6.37862 | -45.54058 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e36acfd-bb8e-3cbc-ab50-32eef9e30265 | -6.36418 | -44.74735 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 380af454-bc72-330a-9d3c-6228c9fde5f8 | -7.60603 | -44.3712 | 2025-08-23 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 105d0f70-0789-36d4-a031-ab4db28028a6 | -4.30678 | -48.09855 | 2025-08-23 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66837017-a06a-3a3d-9a30-a89d88cdfb9d | -7.72458 | -44.08312 | 2025-08-23 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 439fa99b-40af-367c-b2b9-361ff87eb703 | -5.71998 | -38.30522 | 2025-08-23 04:00:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 28ab34df-3023-3f15-b8ad-5d91fc9e40d2 | -7.60297 | -45.252 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c9afc47-3e11-3a64-bd4d-1ecdabc4be18 | -5.80872 | -45.19747 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67eb6fb0-ac67-3577-93d2-d256bee7704f | -6.11882 | -44.38413 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94f9a537-794b-3f7d-858e-565521b19ed0 | -6.37319 | -45.54752 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 32c65d7a-579c-3d74-be38-e59c16d76226 | -7.63397 | -45.23886 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20f204da-e91d-32a8-804a-9db863498680 | -6.44299 | -44.54161 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c7ff126-c90b-3095-a79c-4ab1e950b74d | -4.30729 | -48.0955 | 2025-08-23 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 204132e4-7daa-319c-82c3-d08c121969b9 | -5.70111 | -39.12906 | 2025-08-23 04:00:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e3c364f9-c342-3fc1-92ce-4f8a5d0fa4f7 | -6.42379 | -41.22179 | 2025-08-23 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b024c445-16d9-3e74-b3b4-cad66062730c | -5.78012 | -46.29139 | 2025-08-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77ecb5db-0047-3cee-9f83-626d8ad72fcb | -5.49345 | -41.40645 | 2025-08-23 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 144cefc1-9ad4-3a84-89b6-0a4417b3e818 | -6.57137 | -42.9882 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8483b699-60ad-3542-8078-bde5efc0d0a8 | -7.07504 | -44.06592 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b402880-65ac-3fe3-a022-b7527e0ba422 | -4.08996 | -46.92463 | 2025-08-23 04:00:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12749923-f2a5-3af3-8cd7-13205ef23ea0 | -7.22056 | -45.1732 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7754922-bbbd-34b6-a91c-1df9ea90cd72 | -6.42575 | -44.52152 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7466ad4-13b5-3194-ad23-8972d9189fb5 | -6.97824 | -44.18002 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 344b0a28-40f0-3328-816a-80766c201760 | -2.55507 | -47.71242 | 2025-08-23 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd2a1fe6-a21c-340b-827b-505092c088bc | -6.11954 | -44.40403 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac405f5e-110f-3b20-8d10-45c97ed97238 | -3.51686 | -47.20622 | 2025-08-23 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5d3989d-c184-3888-9fef-ae6977d08c64 | -6.60661 | -44.57133 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cdcba396-9120-3010-b34d-2969becfcd4e | -4.01358 | -38.32541 | 2025-08-23 04:00:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b57f9a72-1e72-3975-86a0-bbec9a82f12d | -6.59494 | -44.56933 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 372f805a-9cf5-3f96-8b20-19b452aa3b9b | -4.13774 | -46.45977 | 2025-08-23 04:00:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f543662-48eb-3bdb-85c7-3307ca3c1006 | -6.39364 | -45.51133 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a136b53-f9a8-35eb-9d30-5398b64483e9 | -6.97981 | -44.17065 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f6c96f4-33ae-37b5-8be3-ca80c2914d0f | -4.65004 | -41.41656 | 2025-08-23 04:00:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1da8d6ed-8e01-3581-81c7-18691ea34f0b | -6.58246 | -44.57204 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7fa0fdc3-c247-3663-a366-f0c587135524 | -7.07077 | -44.60817 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17d140b1-ec40-3494-8ca6-af01e0d0a894 | -6.23506 | -46.24344 | 2025-08-23 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c77c9a8e-d5af-332b-8ed8-08366771ca6f | -5.49146 | -42.16031 | 2025-08-23 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ade1e809-f3ae-38e2-88dc-18f22db67e0e | -6.17928 | -45.43482 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9778452a-1ad3-34b5-a08d-997ef8f9f05f | -6.15842 | -45.03238 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8da8c4ae-49f5-3267-a794-8dc8073a5a8f | -6.37256 | -45.55129 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| d31dfd99-161c-38f0-95ec-5dee265e4ced | -5.09928 | -44.79802 | 2025-08-23 04:00:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9d79b31-3686-31d8-af46-3638c4cb72ba | -7.08399 | -44.60047 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d37754a-c854-3495-829f-e211d50b2701 | -6.41822 | -41.21357 | 2025-08-23 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f7a9626-8c6e-3d1a-aae9-8cd470003571 | -8.01318 | -45.49393 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60cc029a-1088-31a0-b8d2-9d8704031c7f | -6.98783 | -44.0304 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28dc7560-6269-3932-b92c-b5ff695701cb | -5.83391 | -52.07343 | 2025-08-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba6fa69b-6205-38e0-abf7-d5415df60919 | -7.03862 | -44.65759 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77ab5fde-b73f-381c-a701-f19a239706a2 | -3.43596 | -49.04148 | 2025-08-23 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d5e3046e-b0fe-35ce-b90b-3c0e87fb53ba | -7.59836 | -45.25494 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abc25cd0-e36f-303f-99dd-ffcdc6bf67ad | -6.37798 | -45.5444 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 81d0340a-4088-3af2-91df-320fa8b650f1 | -5.59446 | -44.53876 | 2025-08-23 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60f96700-cee2-366c-9759-c4b3480c9890 | -5.82865 | -52.06578 | 2025-08-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ec9eee9c-3fd3-3f88-9446-962117ec465b | -7.59073 | -45.39957 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58c67ff0-e74f-3ee4-9126-8813dd94d3c3 | -6.94243 | -44.16249 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09fa1cce-7d77-31df-aba5-46507ca51523 | -6.11875 | -44.40886 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de49383e-2abb-3016-9b78-8a31fcfcdd4c | -6.77226 | -44.32378 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4678fa66-dafa-3260-b9e2-43f6fe59aee8 | -5.1039 | -44.79515 | 2025-08-23 04:00:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2ff486a-73a4-3561-a08b-3b1c1d1cfdda | -2.38102 | -47.66581 | 2025-08-23 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edeefbfa-0223-3790-82f1-7dfba8f2ba94 | -6.11566 | -44.40335 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cce4cd5f-6853-3ad3-9d7e-cbec627df6dc | -5.09986 | -44.79446 | 2025-08-23 04:00:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b108bc6c-f0b3-3b9f-9ac5-aafe6ec290b9 | -6.37925 | -45.53676 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f245c80e-50bd-3dee-bcde-eb7be930804d | -6.42714 | -41.22234 | 2025-08-23 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b3c6fd7b-99d8-32f7-8bc8-262b957cb29b | -7.22397 | -45.17735 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0affa656-41dc-37f3-8b49-4a9233ecc66b | -2.44191 | -47.33096 | 2025-08-23 04:00:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85620ceb-113f-3a8a-a0a4-6219840be9fe | -6.94426 | -44.28934 | 2025-08-23 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31ae0d07-880d-3a9b-bdc5-ea90ed32dddb | -6.06177 | -53.88912 | 2025-08-23 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| badf9e42-3cb6-3148-8d74-fb5597a74b07 | -5.71659 | -38.3047 | 2025-08-23 04:00:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 27a8d77d-2889-34e9-a7bb-705030232595 | -7.64563 | -46.2862 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e10039e-e4a7-362c-8296-7106b0bcab52 | -4.52841 | -38.23003 | 2025-08-23 04:00:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 281b4b32-71f3-3c62-a37d-3b90592405e6 | -6.97746 | -44.18469 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1583ca1d-fe84-31a3-a247-07f76dcf05da | -3.04432 | -47.01403 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd94c009-36d6-32ea-8976-3e0f15620cfa | -6.31937 | -43.7522 | 2025-08-23 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ff6bb97-a954-3795-8052-0992a461d2a0 | -6.13402 | -43.14848 | 2025-08-23 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c5cb5623-d147-36a9-8035-9bd277658856 | -6.57071 | -42.99228 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f647225-59bc-36ba-a221-540eb75196b6 | -5.79143 | -50.19002 | 2025-08-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f84988f-e258-3e85-bb58-e8bfa886499a | -6.50133 | -42.96833 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9108db52-5efe-3d16-9d8b-3e7fae55c841 | -6.37735 | -45.54821 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f3e5ec6e-26aa-33db-9e93-1e9137fa15d0 | -6.78217 | -44.33525 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5976ca73-0670-334e-b455-a274a2778bf0 | -6.42492 | -41.21466 | 2025-08-23 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README22.md)
