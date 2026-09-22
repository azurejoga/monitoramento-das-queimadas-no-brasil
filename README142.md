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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eca06a19-7471-3f5f-9d01-0c3d7237ae6c | -11.1563 | -51.0839 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 7cac401f-48ad-3621-9287-486e70c43bf0 | -3.6452 | -58.7685 | 2026-09-22 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f4d23c39-1252-3e5e-ba2b-85b54eee0b1b | -6.1839 | -47.5039 | 2026-09-22 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 409c1f82-1b05-3db6-aefa-a4ba8df8ea2a | -8.5803 | -44.5322 | 2026-09-22 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 264.4 |
| 0e0d1bac-96bf-38cf-85f1-b3d55d78259e | -6.2396 | -41.6634 | 2026-09-22 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 331.6 |
| c9ddf4ea-3d43-3caa-8384-407eed073e2f | -11.1183 | -54.0062 | 2026-09-22 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4c7a8f59-5b6a-39d9-b08e-1adcd6250486 | 2.2187 | -50.8769 | 2026-09-22 14:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4364ed14-66cf-3a50-a692-cb8ecb46afa8 | -6.2399 | -41.6394 | 2026-09-22 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 258.3 |
| 2bb91713-12a7-372d-8595-9b88adbfc2da | -3.8279 | -58.899 | 2026-09-22 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3f779d26-1607-3de8-9e4a-c8959400315c | -6.3436 | -55.8243 | 2026-09-22 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| bd780942-825c-31d9-9ec4-1111881c8a72 | -9.5356 | -47.9349 | 2026-09-22 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 544a081c-c71a-3451-a0be-c098bd28754b | -3.478 | -59.597 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 5ba3f673-788e-35cd-9bb6-615573749792 | -4.278 | -56.2602 | 2026-09-22 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 885263f3-d573-30c7-9122-653b0717c558 | -11.2488 | -54.1378 | 2026-09-22 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 215a963f-6ce9-398f-a7b0-71a4e4d6e674 | -12.3824 | -47.0057 | 2026-09-22 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 76cd7a09-d044-3965-967b-59c3720c4a8a | 3.9534 | -59.7206 | 2026-09-22 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 498a07bc-443f-3e9d-b968-b2235e878304 | -7.6272 | -45.4507 | 2026-09-22 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e90fdc91-ad8f-3aea-973f-1e38ac43394f | 2.2003 | -50.8773 | 2026-09-22 14:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d13ad0d0-c02e-39e6-a418-b05c2a6c9f79 | -2.8608 | -57.8188 | 2026-09-22 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 07dce1d9-146f-392b-8075-5d4b502ea76d | -6.1836 | -47.5477 | 2026-09-22 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 01e65065-ca3c-3b60-ba92-a9b3525800df | -12.3478 | -50.221 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a60c5941-6778-32a1-a7fc-e3b18b168212 | -11.6793 | -43.4684 | 2026-09-22 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| baaf679f-518c-3261-b6b0-3c3ea9dfa023 | -5.8675 | -49.7864 | 2026-09-22 14:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e5f8156c-2df3-310d-ac1a-33d2817ca481 | -12.6796 | -50.974 | 2026-09-22 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 78c598c4-6e20-30f3-b404-1142fa201347 | -12.3484 | -50.1779 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 893.8 |
| 58992137-0016-3201-b32a-7a714a76c518 | -6.0172 | -45.2462 | 2026-09-22 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 867926de-eee1-3362-9b93-ca2bd93b195a | -9.6111 | -43.9243 | 2026-09-22 14:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 406.0 |
| bfac184f-eca4-3e03-b41d-291c89e1f8e3 | -10.5748 | -46.7296 | 2026-09-22 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 803.0 |
| 44964929-2244-3757-83ba-07ed15a89f02 | -10.4102 | -50.311 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 24cd2703-967c-359a-8ceb-7bd89070e5ae | 3.7498 | -60.4684 | 2026-09-22 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 138663e7-2775-3af2-94af-28c2a508ce66 | -3.7673 | -60.7339 | 2026-09-22 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| a7802100-0b5d-3c52-bbee-eba975e1c961 | -4.6401 | -42.0738 | 2026-09-22 14:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| de3f5930-4f77-3c1e-8507-23aa624bdc20 | -6.183 | -47.6133 | 2026-09-22 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| f73003b2-ca21-3a40-8b6b-92cf7eefa29a | -7.1392 | -42.0811 | 2026-09-22 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| 50b49a1a-5aea-3ca2-afdb-728f65d0bdf2 | -12.3293 | -50.1802 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 290.9 |
| 69b7e6b8-6025-3f0f-950b-f58a6385c189 | -10.7819 | -50.7837 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 49b698ef-8fe1-3308-a023-c82add659c86 | -9.5857 | -48.433 | 2026-09-22 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 99dc9866-191d-3fdc-8878-f900ffd41782 | -7.1203 | -43.7323 | 2026-09-22 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| e9b315c2-ca31-3d57-93d8-9501865c77be | -11.118 | -54.0268 | 2026-09-22 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 32040ccf-579e-3271-a77a-edf766085aff | -8.4611 | -57.6292 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7c5af3d8-2261-32ad-b9e0-4e7de57aa2f7 | -14.1258 | -45.5904 | 2026-09-22 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 69596353-e009-30bf-95c6-2d1bccd3aca9 | -12.3824 | -47.0057 | 2026-09-22 14:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 8b526de6-fa5d-3535-9f15-0b791150a6eb | -3.331 | -59.8483 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 811ab559-89d7-392a-bc04-866e959e352b | -11.3784 | -44.2195 | 2026-09-22 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a0e4d821-1a3d-346f-81d4-b789a1c19d0f | 3.9503 | -60.6922 | 2026-09-22 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 275d6fdd-4903-32f3-b7a4-c7f4aab4985a | -3.4598 | -59.5591 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 81e90b9f-4232-3d7d-958d-a1ff2eb71827 | -3.7364 | -58.8626 | 2026-09-22 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| bf8e5a3f-813f-3512-9100-ca59b8dcda6c | -12.3478 | -50.221 | 2026-09-22 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| c32c25f1-2256-378a-a5fe-7ef7624fc274 | -10.6711 | -50.5825 | 2026-09-22 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7ff1891e-c0d8-33eb-811e-69ecc44b9342 | -6.5829 | -58.9851 | 2026-09-22 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e34759e2-1d23-3bff-a3b2-792dcae09db7 | -3.4272 | -58.2138 | 2026-09-22 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 28c9c5a6-7651-3bff-8092-d41efd784b72 | -6.9414 | -42.907 | 2026-09-22 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 161.5 |
| 17b9d626-e15b-3b70-88a8-5f0988c758fc | -6.3012 | -59.9962 | 2026-09-22 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| e33f8c26-ffef-39f8-a7e3-0aa6dfb6b8b1 | -12.3407 | -50.6728 | 2026-09-22 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| d05b4e29-708a-308e-b562-45420f770401 | 2.6715 | -60.6012 | 2026-09-22 14:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ef24c54f-41d9-3c7d-a47e-c56a71631749 | -3.2955 | -59.4476 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7838db4a-3c4f-332d-be0c-2f18f7fc49df | -13.8731 | -48.5727 | 2026-09-22 14:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 5c1f4a16-3fea-3365-8da4-2273ffb88d5e | -8.1686 | -54.7634 | 2026-09-22 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2b38c411-84de-37fe-8158-fe0f02c61b98 | -3.1901 | -57.8704 | 2026-09-22 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e9134b5f-8884-3696-be81-39842a76025d | -6.2396 | -41.6634 | 2026-09-22 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 231.7 |
| e21fd5a4-4601-3249-956b-4b4776d4ef81 | -3.2212 | -53.9422 | 2026-09-22 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d9dc05b8-f81f-36d1-aed9-5937d9ca7ff0 | -12.3297 | -50.1586 | 2026-09-22 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 726.7 |
| d5db5a32-e254-3d90-a233-df1b244da6d6 | -6.7648 | -59.4408 | 2026-09-22 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 79939865-ec14-362e-bd9a-2705f8bdab4f | -6.9871 | -47.4885 | 2026-09-22 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 445df021-d253-3f6a-9665-8ef5c98ebd9e | -6.6648 | -52.3307 | 2026-09-22 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d2cb48f9-69c8-3283-b863-0d127f7a67d7 | -3.7547 | -58.8622 | 2026-09-22 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8d4435fb-59b2-3f4b-9251-ab302afa0439 | -3.2183 | -61.0472 | 2026-09-22 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| cc2e372a-a28a-3358-a96e-45f7614e5771 | -7.6943 | -61.5283 | 2026-09-22 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b762946a-ca60-364e-80ac-a39b2798cab2 | -10.5748 | -46.7296 | 2026-09-22 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 761.6 |
| abfdca23-52e3-3f7a-800e-7f13962c1d4f | -7.1273 | -48.4366 | 2026-09-22 14:50:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 6225239e-7378-31cd-8de4-0ce985ced24c | -3.2818 | -57.8491 | 2026-09-22 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| bc2126d5-2be5-39b6-a125-9f3cc8b8ea63 | -6.3195 | -60.0147 | 2026-09-22 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 452a5dbf-f57e-38e6-8de2-e01cc91a3a77 | -6.0926 | -57.6652 | 2026-09-22 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 179.2 |
| 3274943c-b1f0-3942-80be-8e4561e16621 | -3.2817 | -57.8685 | 2026-09-22 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| cd2dc49a-2b55-35ac-bc55-3c2e6947e27a | -5.6223 | -43.3701 | 2026-09-22 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 8dc2a109-c376-373e-b0dd-eecad7f55ade | -12.4004 | -47.0706 | 2026-09-22 14:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d72d7ce5-05c3-3caa-a8c5-1f7513e539a1 | -2.8534 | -60.9206 | 2026-09-22 14:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f75d266b-4b38-3ff1-bb6c-e6d35d170036 | -8.7916 | -44.2778 | 2026-09-22 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 057bd690-b151-3a93-87ad-bfb519c35bf5 | -8.4922 | -47.0257 | 2026-09-22 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| b2ebd677-b044-3be1-8dc7-bbdc9449b2c5 | -12.2827 | -50.7226 | 2026-09-22 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 150b4b3f-38f8-3e7f-bb74-8e4995e91d91 | -5.8675 | -49.7864 | 2026-09-22 14:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 979c0e83-a5ac-3ab1-86b8-804941519a78 | -7.1203 | -43.7323 | 2026-09-22 14:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| e967d14b-6daf-34d4-9d2a-3c6f19b83e8a | -3.331 | -59.8292 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 123476e2-309e-3b19-92b5-1c6f402bfef7 | -6.7589 | -47.8995 | 2026-09-22 14:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8f248400-e41f-30fa-9489-51a3e8b3f1c5 | -3.0534 | -61.2767 | 2026-09-22 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 587911be-0a90-35e9-b7a7-e181c268aee4 | 3.7498 | -60.4684 | 2026-09-22 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| cc99c88f-df31-35a0-82cb-dc445f7ca220 | -7.6942 | -61.5473 | 2026-09-22 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| b804f82b-0a35-31b0-9d04-a88f63533a4b | -2.9997 | -60.8047 | 2026-09-22 14:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 0aebebea-6e05-3e95-9d74-66eac0827477 | -6.9174 | -41.6957 | 2026-09-22 14:50:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 164.2 |
| f7a77037-f923-3404-aecd-52e53063584d | 3.859 | -60.6561 | 2026-09-22 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 13c813e9-5489-3e88-82ef-988ef1281914 | -6.8573 | -43.71 | 2026-09-22 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 4e71bdea-37c6-33e1-8594-17c7049466df | -6.9681 | -47.5119 | 2026-09-22 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4d64b9b3-3142-332a-a3e6-a207b4db1949 | -10.4105 | -50.2897 | 2026-09-22 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 6887cccb-26c2-382a-b07f-c0facc04b757 | -3.2372 | -60.8007 | 2026-09-22 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| bbc9e02f-9ea5-30a2-bed4-974b36643a31 | -14.6688 | -45.6565 | 2026-09-22 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 297.3 |
| 74786152-7ca0-3813-ad79-a5400b52a694 | -12.3481 | -50.1994 | 2026-09-22 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| f5f67278-4c67-3be6-9cac-4b68ca0055fd | -8.3134 | -44.7446 | 2026-09-22 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 87e1c9d9-ffa8-3615-9234-dfe37886f9dc | -11.118 | -54.0268 | 2026-09-22 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 7faab9bc-0771-37e9-a589-1aa7d0742b33 | -3.4009 | -61.0629 | 2026-09-22 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8411483f-3339-388d-94a2-c864e726b1ec | -10.7256 | -50.747 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |


[Clique aqui para ver as próximas entradas](README143.md)
