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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e80852a-9d3b-33db-ae82-8365da3404d6 | -7.21479 | -35.7769 | 2025-09-22 03:47:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b5c1115-eff3-3547-9ae1-dca7a05cdd0e | -6.84023 | -44.15891 | 2025-09-22 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 515bba11-8001-358c-a67d-ee9f062068a7 | -5.56017 | -46.28216 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05f82868-99ea-34d8-b02c-827662da7f74 | -4.99313 | -45.1562 | 2025-09-22 03:47:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eeab9b6-068a-306b-bd18-e2eafdfcb8c1 | -5.52228 | -36.85797 | 2025-09-22 03:47:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a3e2274f-5ad7-3081-a5bf-66a42b2e09b1 | -3.05041 | -46.92818 | 2025-09-22 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3f50269f-d147-363d-919b-06187a0f0c03 | -5.64448 | -45.9563 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d30bf834-c22a-350b-8f49-619265e27b92 | -6.55791 | -43.82933 | 2025-09-22 03:47:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a3a53f2f-f8b2-3c89-a758-b28420329130 | -5.10831 | -46.16663 | 2025-09-22 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9f978b5-975d-35ae-90ff-c84a17baca73 | -5.56078 | -46.27869 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c86bd32-4df4-3a91-9a0a-626797067c58 | -5.40366 | -38.57064 | 2025-09-22 03:47:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 26fc5f61-ae31-3394-aeff-b807d648bdec | -6.9001 | -44.76944 | 2025-09-22 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 3d83c9d3-e09c-334e-810a-963717cc970f | -3.42049 | -47.60535 | 2025-09-22 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22debae9-69d4-36e0-9cb6-b3f971751c1d | -5.63972 | -45.95193 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 58db4b2d-8209-32a1-a74b-f4e6f98c385c | -6.44722 | -45.68476 | 2025-09-22 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dfcb5b1-5291-3fe0-b7f6-c2de1ac681dc | -4.87505 | -45.81158 | 2025-09-22 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00a0502f-9494-3e13-afe1-e850c3a35584 | -7.44564 | -40.10299 | 2025-09-22 03:47:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3dce0095-61fd-36f9-93fb-092f5c23cd20 | -5.33308 | -44.8234 | 2025-09-22 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f6495b9e-28b1-3db8-b564-cc82bf14cc69 | -4.87566 | -45.80805 | 2025-09-22 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba5d0660-6a90-3db9-a8fe-661f096ba8e5 | -5.56325 | -42.13118 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2696cd29-252d-3301-823e-d3ddcb0530c0 | -5.63914 | -45.95528 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a9d4831-3b66-33b8-9131-84cfd4d4ed87 | -5.33404 | -44.82171 | 2025-09-22 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aedec4fa-4183-3d07-bc84-98a76982cb12 | -6.85175 | -35.2636 | 2025-09-22 03:47:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 89c44dc1-f2f0-32ca-a49f-21b2406b0284 | -5.33351 | -44.82475 | 2025-09-22 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0d4249d-f8ef-34b2-bb05-a0cd0f35f962 | -7.21534 | -35.77333 | 2025-09-22 03:47:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 47bceecf-a247-3709-be0d-248f3b9c71d0 | -5.33704 | -44.17984 | 2025-09-22 03:47:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6555b7b8-0f71-3b9c-be97-ebfb4dea375a | -6.85514 | -35.2641 | 2025-09-22 03:47:00 | NOAA-21 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| deef740e-1dbe-3fb0-98d0-78efe1c91842 | -4.31263 | -48.10349 | 2025-09-22 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 826118a5-9708-3d99-a55f-8409f64b44e6 | -7.25863 | -40.25214 | 2025-09-22 03:47:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2be00752-6015-3bde-bef7-fdd83ea3ed35 | -7.83898 | -38.24617 | 2025-09-22 03:47:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d7293a86-045b-321b-bbdd-27ac397bcab4 | -5.56989 | -42.13283 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 5b610084-2646-376b-be44-bc96c8d71bae | -5.6403 | -45.94859 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5789088a-28e1-3371-a718-033c5f18fc23 | -5.10989 | -46.16292 | 2025-09-22 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 590c0dc9-55a1-3c6d-a9e1-35d37e9bcd11 | -6.01467 | -44.33462 | 2025-09-22 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 72a5a0a2-81b1-31be-8206-3d17c7bab843 | -6.4006 | -38.28372 | 2025-09-22 03:47:00 | NOAA-21 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7053fa2e-6983-303d-9fbd-c6aab2d72e44 | -4.31349 | -48.09846 | 2025-09-22 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eff373b7-e2e1-34a5-ad80-1ecf27167fb5 | -6.09428 | -41.0038 | 2025-09-22 03:47:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 593d2780-e887-3a26-8d78-9388f010dcfc | -5.56799 | -42.12812 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 18ff1282-1deb-347f-a536-7bb03869c5f8 | -4.31435 | -48.09345 | 2025-09-22 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2923a60-6f78-3c5e-9422-b7e50e15aebb | -4.99365 | -45.15317 | 2025-09-22 03:47:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0e866c5-a309-3e54-af3f-9338f4c82a8f | -5.59145 | -38.12276 | 2025-09-22 03:47:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32e8c55f-a168-31c4-9861-2b51342277e1 | -5.06207 | -40.47145 | 2025-09-22 03:47:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d900244-b38f-3923-b1d7-1201a0249385 | -6.45294 | -45.68256 | 2025-09-22 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4367c5ea-600c-3ae9-bb1b-f85acf46a4c5 | -5.56739 | -42.13183 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a1436af3-e282-3464-9dda-26b8ce7ff16d | -6.03825 | -44.13949 | 2025-09-22 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8395b566-6c43-3737-8583-52e316da4d40 | -6.00993 | -44.3337 | 2025-09-22 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| efccf522-93ef-33d2-893b-52ce600311d7 | -6.85119 | -35.26725 | 2025-09-22 03:47:00 | NOAA-21 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 058e5cd4-f60f-3aae-8d45-6e63d10324e2 | -7.20812 | -40.24456 | 2025-09-22 03:47:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7cf01e00-b220-3bbc-b14c-5203905a964e | -5.64563 | -45.94962 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02353a00-7010-3b85-823a-eb03d007bc2b | -5.57465 | -42.12979 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 9af1a296-31da-3d8f-8c1f-6c3e768e1ea2 | -3.85561 | -40.34216 | 2025-09-22 03:47:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b68b55e9-e7a2-326d-9f79-6ae14c87e314 | -5.55438 | -42.13356 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7cad931a-e365-3d28-a420-420fdf9bea67 | -5.06582 | -40.47206 | 2025-09-22 03:47:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e66ebd33-e481-3e7f-92ea-81c05cc77098 | -6.90098 | -44.76435 | 2025-09-22 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 13afccf0-4d44-352c-ae26-fda5d9ca7a3b | -6.85457 | -35.26776 | 2025-09-22 03:47:00 | NOAA-21 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e6ecb6fb-f0a8-31d6-ae52-c3f26df8b025 | -5.55499 | -42.12983 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ecd5efb5-bc7a-35c8-bc35-4b5a83d192e9 | -5.59296 | -46.25541 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 718829f5-a961-328a-9685-f94de2c65a8e | -3.41967 | -47.61017 | 2025-09-22 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4167a083-3f66-39ec-8785-5af97d072d76 | -3.85939 | -40.34277 | 2025-09-22 03:47:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b192bcd6-f142-3c4a-8900-2de1126c61e7 | -5.58751 | -46.25441 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99b2a68c-3b2d-35da-acde-3b65a94039ff | -5.64505 | -45.95296 | 2025-09-22 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23702240-ae45-3e43-819d-6abd3286971f | -5.10928 | -46.16641 | 2025-09-22 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea981ae3-3d51-34ec-a7e0-f90695aed4c0 | -7.4414 | -40.10651 | 2025-09-22 03:47:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 53b822a2-961f-3988-8236-ee9133317798 | -13.72835 | -43.90565 | 2025-09-22 03:49:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c755796f-6e79-3620-b953-c79ebe37d62b | -11.66378 | -47.49792 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f66bbec8-e54a-3fb4-98a5-3af2cfcccd0b | -10.32307 | -46.10149 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ec13da7-f218-3a5b-8e54-0f773952ec9f | -10.40763 | -47.85334 | 2025-09-22 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2293eb35-3d39-300f-988f-06b2e1c76c89 | -7.5171 | -43.6876 | 2025-09-22 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fcdaf67f-976a-3c07-9ec5-23d399b0a310 | -10.37435 | -46.07445 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a260248-d794-38e9-9f05-f28af4f2b104 | -7.35888 | -44.54176 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24abc08b-b272-396f-a755-7fcba7b816f5 | -3.88175 | -38.39917 | 2025-09-22 03:49:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f14e82d6-c158-3a6a-9b5e-157cae7c7c4c | -12.96849 | -46.93842 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d23118f-449c-349a-ba02-9096ba2e122b | -10.38381 | -46.07893 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0edf01c-9b55-3e01-8759-7f6742834634 | -12.73615 | -46.82925 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c940c207-df24-3fb0-a3c7-568de4169b81 | -10.36276 | -46.08165 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8559350b-eb6c-3788-ba43-67b3b5b0c227 | -11.63975 | -44.33372 | 2025-09-22 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0738b7c-91e7-318e-80b7-5a2cba32f2b4 | -10.34511 | -46.06586 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 574381a4-da34-3492-affe-5ab5bc135d46 | -11.55634 | -48.59096 | 2025-09-22 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b516381-c606-38b3-92df-64999d6954b6 | -10.37152 | -46.06184 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 144e6681-3736-38f2-a9aa-bd6908dc4848 | -11.50513 | -43.56776 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da541721-97f1-3078-81ee-f1b1b70b1681 | -8.73949 | -40.97491 | 2025-09-22 03:49:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6ece980-eea1-3951-ae4a-f055c2101e56 | -7.79628 | -46.19192 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ef574021-fabd-3384-81cc-e9867459303e | -12.96284 | -46.94071 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c05568-b8f5-34f5-a58d-c4f1dd3b185f | -11.49146 | -43.57304 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa0fa302-97c6-34f3-81c1-206645b533ff | -10.06854 | -45.63461 | 2025-09-22 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb9cbcbd-bf65-3e2a-b015-2c961674b1b7 | -9.25975 | -45.84064 | 2025-09-22 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffba1535-97bb-3352-ba31-6266646241a1 | -13.61845 | -47.41312 | 2025-09-22 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21361e91-f15f-3ccb-8e24-7c0b5ea9b26b | -2.91293 | -40.39032 | 2025-09-22 03:49:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6b40e9f7-1222-3240-a0cc-ebd857df41bd | -10.37719 | -46.08704 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 503423ac-c09c-37f8-9830-17293f110cde | -8.01069 | -45.72557 | 2025-09-22 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86511028-6395-3418-92fe-21afbe043542 | -12.74049 | -46.88899 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18d564ab-bde4-3053-8c25-201b74b71c90 | -9.99201 | -46.24276 | 2025-09-22 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2192a8b1-7617-3302-8033-831ffa2a63b8 | -9.16261 | -44.61851 | 2025-09-22 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83363c13-8ee4-3cf6-887a-f2d148340503 | -13.7475 | -47.84171 | 2025-09-22 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0024296c-5cd8-3b6c-b4b9-98c60a4ddc2b | -7.79636 | -46.1912 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a4c9a244-4aba-3f68-b5e1-2009b865a576 | -11.4603 | -43.5326 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 796b7ed3-4f5b-3a95-b74b-215679945097 | -11.46441 | -43.53337 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a335a95-ac3c-3a3a-99c3-b8d09e1533c5 | -12.33475 | -43.44548 | 2025-09-22 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7907c8cf-de8f-3d50-8a20-23a28596fbd2 | -10.34459 | -46.0687 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 443cbadc-15a2-3faa-8570-3aca02de2eaf | -7.91415 | -43.87679 | 2025-09-22 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README10.md)
