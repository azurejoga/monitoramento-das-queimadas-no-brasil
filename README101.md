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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a22946f-899d-3539-8770-5a787a766c13 | -3.09754 | -50.56057 | 2024-10-30 12:53:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 911ee184-a59d-31cc-b0c7-559cb84bf96b | -2.91733 | -50.27568 | 2024-10-30 12:53:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1427192c-e4cc-3c8c-a2cf-2653c743d88d | -2.83002 | -49.22982 | 2024-10-30 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2272832f-acad-3786-9ced-7626276241f9 | -2.82875 | -49.23862 | 2024-10-30 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 919feff3-ed3c-3e7f-bf23-74d7801a2e74 | -2.44958 | -48.8583 | 2024-10-30 12:53:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 30ee366a-12d5-33f4-88ad-b3a095ab39af | -2.38832 | -48.58113 | 2024-10-30 12:53:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8105a9a1-6e55-30ca-8dcf-aa6b9f965f03 | -2.1313 | -48.38134 | 2024-10-30 12:53:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 746d2725-7e58-3a48-b6b0-925ee27c5632 | -2.05523 | -49.48447 | 2024-10-30 12:53:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ecba22e0-f5e0-3606-a800-0e39252425e3 | -1.74023 | -47.44635 | 2024-10-30 12:53:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fed45c97-a4c4-35b1-b35b-6cb6b90aeb3e | -1.55049 | -52.08445 | 2024-10-30 12:53:00 | TERRA_M-T | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 302f99ad-3e12-3cac-b60d-aa979bc32389 | -1.54409 | -52.12906 | 2024-10-30 12:53:00 | TERRA_M-T | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 98c887a9-1971-3288-b421-b281433ea057 | -1.42013 | -49.21114 | 2024-10-30 12:53:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ae2b3892-5ea7-3eee-aea5-24305ec531f8 | -1.32944 | -48.95052 | 2024-10-30 12:53:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b12ba8b9-5c2b-3175-b219-7bf94e5a6f74 | -1.28887 | -49.10615 | 2024-10-30 12:53:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bc1ecdc6-42d7-3491-b816-d342cbb18d09 | -1.08362 | -53.66245 | 2024-10-30 12:53:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| ade9fd28-1cac-3d15-ae8e-71b9f349d194 | -0.9858 | -53.70158 | 2024-10-30 12:53:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 72b9a8ed-e740-3ef6-b624-cfacbbdd3f44 | -0.89371 | -47.88325 | 2024-10-30 12:53:00 | TERRA_M-T | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 059f93ce-0ff1-39d8-b282-d63acce6024b | -0.16113 | -51.56573 | 2024-10-30 12:53:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 884b9008-5d6a-32aa-9b2f-a3ffbcb07923 | -0.16265 | -51.55498 | 2024-10-30 12:53:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8659c94c-f339-336b-b4b6-8f0689e9d751 | -4.8486 | -42.47032 | 2024-10-30 12:53:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 305.0 |
| 4850a0c3-2f51-3aba-9577-238bf2aa6396 | -3.40787 | -41.6279 | 2024-10-30 12:53:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 205.2 |
| d752574e-3906-35f0-8d94-02a0cf3f1aae | -6.46846 | -42.01915 | 2024-10-30 12:53:00 | TERRA_M-T | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 0d680752-517b-3675-bc00-407d72771f6f | -6.46567 | -42.03923 | 2024-10-30 12:53:00 | TERRA_M-T | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| ac0847fb-5529-35de-b4e8-a49b186bd349 | -5.55886 | -43.73154 | 2024-10-30 12:53:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 269f398f-4e64-33db-a835-d40885af232d | -5.46304 | -43.17968 | 2024-10-30 12:53:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| f3dcb247-7cf3-3835-a049-3c32001b6475 | -5.45462 | -43.24219 | 2024-10-30 12:53:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| d48e141f-c98b-3dd9-80c3-5c55d7d1f73f | -5.45188 | -43.26258 | 2024-10-30 12:53:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 315fec7d-2187-367e-986b-b484a497012f | -5.44987 | -43.17779 | 2024-10-30 12:53:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0286918e-012a-3e50-b8f9-5f555a7fa1c5 | -5.29091 | -43.89262 | 2024-10-30 12:53:00 | TERRA_M-T | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 10673566-a5f1-39d1-bbe1-b8a00e3fc40c | -5.28877 | -43.88583 | 2024-10-30 12:53:00 | TERRA_M-T | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| a05c30ca-d474-3130-aca0-4accdd36ab20 | -5.28856 | -43.91079 | 2024-10-30 12:53:00 | TERRA_M-T | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 54ef52c8-75e5-3b7b-bcbd-4c0ec38026bb | -5.28628 | -43.904 | 2024-10-30 12:53:00 | TERRA_M-T | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d02eb5de-7ffc-3b70-a905-1ba976135be3 | -5.28139 | -43.26929 | 2024-10-30 12:53:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| fb79f54d-313b-3126-bffd-f396615c35ea | -5.25922 | -42.96046 | 2024-10-30 12:53:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 7f815361-0f0a-3f3f-aba8-71703cccace0 | -5.0166 | -43.58487 | 2024-10-30 12:53:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 8e26b7c0-6f14-3aeb-838d-6f9bfa1b7ced | -5.01403 | -43.60407 | 2024-10-30 12:53:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 6919758a-0360-36f3-ac8b-a0300cbf3fb7 | -4.93861 | -43.18472 | 2024-10-30 12:53:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| b39bc651-d4d3-31b7-b888-7986c3bc0604 | -4.92787 | -43.17752 | 2024-10-30 12:53:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| edb213bb-f20f-32a6-9601-2e97aef82385 | -4.86241 | -42.47226 | 2024-10-30 12:53:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| b1c39ecc-cf1b-3b60-baf3-7d385243285d | -4.8563 | -42.46596 | 2024-10-30 12:53:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 219.9 |
| 23f88a71-a81a-332b-a59b-c1234d6ad91c | -0.16438 | -51.56177 | 2024-10-30 12:53:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.7 |
| f8845c30-f869-30de-af17-23d7225742df | -4.85311 | -42.48915 | 2024-10-30 12:53:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 9e9ac157-98b8-3b5a-91a2-65c7fb2d6805 | -4.84559 | -42.49359 | 2024-10-30 12:53:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| ff5de4d1-7a5a-35b8-a137-407847003188 | -4.84249 | -42.46393 | 2024-10-30 12:53:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 4329fc12-4926-3e5d-a5f6-ce1de5d166fa | -4.83931 | -42.48731 | 2024-10-30 12:53:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| d3178730-2105-39a5-8eea-af4ce0049f5f | -4.7702 | -43.18621 | 2024-10-30 12:53:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 86d99fe2-612e-3687-87f0-3b29bb567e41 | -4.76826 | -43.19157 | 2024-10-30 12:53:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 00b9668c-5bf5-329c-916f-1f0be10a8034 | -4.76736 | -43.2066 | 2024-10-30 12:53:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 958962cc-c81b-3af9-9d01-d36ff4cac4ed | -4.53877 | -42.95382 | 2024-10-30 12:53:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 6e0f8ad5-cf8d-3e63-8e8e-72a9b004d237 | -4.51986 | -43.48204 | 2024-10-30 12:53:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| ecfc9709-180a-34a9-a2bb-bcb0fc2a2264 | -4.35011 | -43.77441 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3ff3240c-4421-3900-9e3e-98126df17d1e | -4.33781 | -43.77259 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 886e9bc2-ef92-3ed0-ac5b-dd30cf9af4c8 | -4.27568 | -43.74047 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| e863e08e-a8d2-3dcd-b5c8-f422a41a6485 | -4.26566 | -43.43641 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 222.3 |
| 2be05a09-447f-3eb2-ae38-7840d22e162e | -4.26525 | -43.42964 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| fbde9bce-82eb-39e9-8eff-24cd1f5a4e74 | -4.26317 | -43.45525 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| be3b604d-febd-3060-99e4-a8881a2b6ae5 | -4.26259 | -43.44862 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 562fd493-5a93-3bc5-ac2f-f0cccede4a8a | -4.25301 | -43.43461 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 71d2162a-6747-3390-88e1-858733377754 | -4.22399 | -43.63398 | 2024-10-30 12:53:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6fe81235-6a2a-344b-9aee-b2013b55d92d | -4.1469 | -43.06065 | 2024-10-30 12:53:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 51b3382f-17bd-3908-a8ae-f65d942d91ab | -4.14463 | -43.06696 | 2024-10-30 12:53:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 71bc2d0b-4247-35d8-829b-ece78ca553f4 | -4.02915 | -43.24831 | 2024-10-30 12:53:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| cfbce5c0-b5e4-3e8d-b566-0dc7afb33d43 | -3.94217 | -41.48569 | 2024-10-30 12:53:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 380d9d6e-c467-389d-96b9-67e16a9abf60 | -3.71826 | -42.35981 | 2024-10-30 12:53:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 60bf50bc-87d9-3613-af58-3d7ac7fa3ae1 | -3.68805 | -42.58285 | 2024-10-30 12:53:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 47594b28-0cca-34f6-95bd-84d808c724ab | -3.6746 | -42.58109 | 2024-10-30 12:53:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 21e29f44-4c56-33aa-8bc9-c7693d7ec502 | -3.67159 | -42.43848 | 2024-10-30 12:53:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 08fcef60-f31a-3ed2-8da3-f1e6a9684ac9 | -3.66827 | -42.42192 | 2024-10-30 12:53:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 2b7379f7-dd44-35bc-9654-6db1d9058c60 | -3.66527 | -42.44466 | 2024-10-30 12:53:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 1a99b3e9-c63b-3759-a0fd-094086beb0fa | -3.66113 | -42.41416 | 2024-10-30 12:53:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 41.1 |
| 0219599f-d494-3225-a0c7-d78132b6355c | -3.65796 | -42.43695 | 2024-10-30 12:53:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 41940953-2d01-3c87-bcef-a84e2e5c30f3 | -3.64687 | -42.61457 | 2024-10-30 12:53:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 3a42cdc7-845b-3773-a710-0f7a4ccbb7c3 | -3.64202 | -42.62062 | 2024-10-30 12:53:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 185.9 |
| ddaa6fb7-c0b4-34ec-9cde-50dddea6f5c2 | -3.56117 | -42.06466 | 2024-10-30 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 4b21c490-ab07-37c4-a968-7590ddd5bb81 | -3.55297 | -42.0812 | 2024-10-30 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 7f7af3e0-7a76-397b-8f70-9f7b6a49042f | -3.54397 | -42.08696 | 2024-10-30 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| e9acce37-98da-392f-99d5-bb8e7d39d10c | -3.40577 | -41.62081 | 2024-10-30 12:53:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 151.9 |
| 731a691a-223d-3c82-8bbe-6311ebd4641e | -3.4045 | -41.6535 | 2024-10-30 12:53:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| e05516eb-8b13-3666-bde4-8d878f705528 | -3.4022 | -41.64646 | 2024-10-30 12:53:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| ca426465-d162-3979-8e29-75f941b803df | -3.37951 | -41.36963 | 2024-10-30 12:53:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 35.2 |
| af905c7d-d90d-3c83-b714-ae8869bb51d3 | -3.33355 | -43.26336 | 2024-10-30 12:53:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 46353c3a-07bc-347f-8b8c-2ea34b386c23 | -3.32092 | -43.26165 | 2024-10-30 12:53:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 28e35688-f437-36d1-87b4-6e04f1d704c4 | -3.26605 | -42.22134 | 2024-10-30 12:53:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 811c96e3-8370-39e5-99cf-0bab89fe0c16 | -0.70489 | -51.98888 | 2024-10-30 12:53:00 | TERRA_M-T | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f85b6f48-91e2-3041-99ba-b02ba1e45ad9 | -2.75967 | -41.87128 | 2024-10-30 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a32b04f4-092a-3ee5-a806-ed994f304541 | -2.75072 | -41.87553 | 2024-10-30 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| e3a14702-832f-3022-8664-094c837f24fc | 1.7535 | -55.84548 | 2024-10-30 12:53:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 48ca63b6-2902-3945-8954-66ea48b4824e | 1.74397 | -55.83981 | 2024-10-30 12:53:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| f04853f4-36cb-3ce1-8c5a-37fbbfe7c8bf | 1.73946 | -55.84734 | 2024-10-30 12:53:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e4337717-4690-3682-92a2-23299a4fccb7 | 1.69737 | -55.85298 | 2024-10-30 12:53:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 53ca317b-d003-32b9-9ef4-9ade2d839c20 | 1.67265 | -55.88081 | 2024-10-30 12:53:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 1ade0c97-cb10-3e85-9aae-02c6a5d57520 | 1.66809 | -55.88746 | 2024-10-30 12:53:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d3574bec-1e20-35a3-a5fd-fcb28a6b97bc | 1.65858 | -55.88265 | 2024-10-30 12:53:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e50befae-53a2-38a5-b2e3-ee85b6314900 | 1.59529 | -55.6267 | 2024-10-30 12:53:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 4b884f3b-9b92-3ed5-a5aa-9be403c4b41b | 1.13243 | -50.74079 | 2024-10-30 12:53:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5dc43644-86ad-364a-ac75-225ab2b16757 | 0.59495 | -50.78146 | 2024-10-30 12:53:00 | TERRA_M-T | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 62ea9fa4-78b1-3de0-a599-f9d67449b9d4 | 0.52922 | -50.76624 | 2024-10-30 12:53:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d5468a34-3af9-3da5-847c-3ad198222578 | 0.06389 | -51.20359 | 2024-10-30 12:53:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e2e166ae-b788-3660-aaad-c68d40900492 | -5.65703 | -45.28959 | 2024-10-30 12:53:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8afa8fa7-eb72-3191-886b-e76677d1da20 | -5.15506 | -45.02148 | 2024-10-30 12:53:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |


[Clique aqui para ver as próximas entradas](README102.md)
