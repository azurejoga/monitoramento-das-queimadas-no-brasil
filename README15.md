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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1a40614-eefe-3d09-aa23-4d3206e4b82e | -6.13223 | -41.71558 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 133dff66-69f4-376d-9193-cec00d74c919 | -6.97645 | -43.50158 | 2025-10-26 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5086f760-bceb-3125-a2ba-a3117b5b6ef3 | -4.81419 | -38.66568 | 2025-10-26 04:00:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3f55bb9a-9b2b-3647-8f95-07226bd52381 | -8.20888 | -46.94087 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3308c7d-6047-3b2d-bf38-34faee03966d | -5.84876 | -47.19335 | 2025-10-26 04:00:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2388dd8-0e3c-3023-995e-98532f5afaec | -4.54522 | -46.55629 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4c5c60b-3401-3264-ba80-8d46c7aeb782 | -2.32653 | -48.58616 | 2025-10-26 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31622f1d-72c8-3abc-ab3c-583b5b474f48 | -7.64499 | -42.16653 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d65981ba-b6cc-3a2f-ab3a-e5ac81947b64 | -7.78314 | -45.39045 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72e980d9-72e7-3806-ab5c-7a35411d14ab | -7.64437 | -42.17031 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f6ef84a-a3a1-3b86-ba24-c2a4d67b4920 | -5.47019 | -37.85168 | 2025-10-26 04:00:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7d6c7544-98c3-3129-a12d-eda0fcfbb3a9 | -6.71335 | -42.0499 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 89d35391-20b1-3a13-8a0b-af02101191a4 | -6.13872 | -41.80492 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf74d7a3-8823-3551-969b-8b9530b39675 | -6.44136 | -45.73427 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd4e6d09-1b7d-31e7-8c70-9cf5ff1adc17 | -3.26519 | -50.05265 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75b1f014-28ce-3e22-8de4-4e49edf71808 | -8.03238 | -41.19827 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a91b168e-37d8-3ff1-8960-3b43d7be06be | -6.44457 | -45.73361 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90f2521e-ec6b-32b2-a80c-eec480d27a95 | -7.6169 | -46.8172 | 2025-10-26 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0c46b54-28f0-36d1-9549-d2718f3b4b11 | -3.7865 | -43.41282 | 2025-10-26 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93d3ea18-0e61-35af-b302-5a6188348b52 | -6.7283 | -44.14977 | 2025-10-26 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d9d678c-df7e-3817-b17d-592ea45846f4 | -6.72539 | -45.38032 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06a011f8-056a-3a84-9104-584fe4344c0d | -6.42951 | -42.32879 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e74e8b41-dd0c-3f9b-8319-382fe811de15 | -7.85344 | -46.41851 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 612b56c5-9cef-3733-bd40-3cba3593583a | -7.15049 | -44.1321 | 2025-10-26 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40df140a-83b5-377e-9073-681c1d9f9b4d | -7.84758 | -46.42623 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29d81c9c-812d-3eee-b425-216b30ccf13f | -5.13857 | -41.20073 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d599fc09-65f5-3b4f-8a20-fa7f406d700b | -4.48054 | -48.67347 | 2025-10-26 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2ccabd99-aced-391d-b8fd-b2ee35b5676f | -6.59974 | -42.66441 | 2025-10-26 04:00:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 81e53427-6e14-3dbd-887f-448d27f2a4aa | -7.69227 | -42.23977 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 342f6d43-f28b-31f5-8b11-d56752c2d1f8 | -3.60608 | -48.91961 | 2025-10-26 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79b2e16d-4ff1-30c7-9677-1d38838458aa | -4.26264 | -40.68952 | 2025-10-26 04:00:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f07d80b8-6f6e-3b7e-b0be-4965df18398d | -6.98124 | -44.00878 | 2025-10-26 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 069f3e74-e2ab-31dc-9baa-ba6ac54da7ae | -5.43063 | -40.91004 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a3659c7-26a3-3845-9998-6a8445c0aa92 | -6.6628 | -47.74309 | 2025-10-26 04:00:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0f2f614-d8ac-3602-87f6-1fa094b52eed | -5.82288 | -40.81885 | 2025-10-26 04:00:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b84eac61-8853-3693-b73f-1e6722513310 | -5.54043 | -41.24877 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7c39f7ad-f5d2-3689-9524-844fbfb2a1e9 | -6.71052 | -42.04552 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4e93e999-6425-3924-943d-6fb39bac9a12 | -6.12123 | -41.7405 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9cce23f0-495d-3178-bae9-2b5defde529d | -5.6527 | -35.69896 | 2025-10-26 04:00:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5574cadc-16dd-3689-b513-b7d3c12d7ac7 | -8.04853 | -46.75009 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aca83f1-9508-3b73-86e5-7375bdc0bd61 | -8.24162 | -42.35843 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7ebbf368-2daf-3fa1-844b-f5db9f5f72b6 | -4.02086 | -45.99939 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 540af242-f75c-3091-ba1b-42de396128b4 | -8.1521 | -47.75669 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5346a17d-e3cd-3dd5-a6d8-74251d8d689f | -4.72544 | -49.09443 | 2025-10-26 04:00:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db532ced-27ca-34bc-aef7-6a2bb38d44a2 | -7.79193 | -45.38803 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf4375da-44b8-3734-ac5c-3c4e19588e19 | -8.33255 | -48.17798 | 2025-10-26 04:00:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58677770-ab84-3e86-9bc1-63eb49c44b19 | -6.12214 | -47.01262 | 2025-10-26 04:00:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8426903-c7b1-343d-a492-54b64acfaebc | -6.72607 | -39.27543 | 2025-10-26 04:00:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| dff9aa9d-7323-33d5-b40e-c8cc8d895fae | -6.18649 | -42.6214 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 331898ef-1c03-3e0c-8c56-8a68ceaf2c26 | -6.16562 | -41.55375 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9630d6df-bbed-3b92-bc03-f1f964141794 | -6.44575 | -42.33934 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ae8b892d-c932-34b8-a646-222af4f3712e | -4.83353 | -50.92812 | 2025-10-26 04:00:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95b3dfd2-8cfb-3207-9e89-c3804af0f802 | -3.09353 | -49.45138 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b4e8a45-a2c0-398a-ad62-85d949e72901 | -4.73658 | -50.86979 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75c61797-652d-3ec5-a536-68609095fc17 | -2.31547 | -48.58424 | 2025-10-26 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0c51312-f641-349a-8ca6-4cce62b99ff5 | -5.10727 | -43.20369 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 9b993739-c355-3cf7-a2dd-5e828fa2e51e | -2.97674 | -49.12307 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66adc445-c376-3ff6-a0f4-3033cc76db2b | -4.27161 | -40.69809 | 2025-10-26 04:00:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9225960a-271c-3cd5-8cc3-5334d03ef74a | -6.12481 | -41.71809 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f7c5ab43-c2ed-3e55-9504-8ecb3d408d22 | -6.43486 | -42.03282 | 2025-10-26 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3f55e786-2f58-3fc4-87c3-c488963204ee | -8.32669 | -49.31289 | 2025-10-26 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02685554-c820-374b-8018-d23e661812d7 | -5.50638 | -49.58604 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| deb2b854-c2b1-310a-8314-07124a459568 | -7.8439 | -46.44521 | 2025-10-26 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 453bee62-f1a7-36be-917a-d624f4f4f5e0 | -6.70301 | -42.04816 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 16e6c4d3-464e-3f55-8f8c-afa6ac0b981e | -8.35256 | -40.489 | 2025-10-26 04:00:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| df628278-5a77-3a0d-af82-101272beb266 | -4.10414 | -47.29014 | 2025-10-26 04:00:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b905d00f-0702-3468-a40c-0d2ac0b57f3e | -5.6101 | -42.66725 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 42dc25bf-982f-3609-89a3-6c270f626d7c | -7.76801 | -42.9239 | 2025-10-26 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c5a8b6eb-3480-362b-9646-4acebf44c840 | -7.15487 | -44.13528 | 2025-10-26 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd7320d2-3e11-3abe-b34b-02eebd5f457e | -7.41754 | -48.77877 | 2025-10-26 04:00:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93687882-cfa0-36c0-a2f7-780085ce6bbc | -7.05023 | -39.74221 | 2025-10-26 04:00:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 449e2681-3b88-3e19-b889-2fe5fc910b1b | -6.58269 | -48.77004 | 2025-10-26 04:00:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da68a912-671f-3d1a-922b-cc6ee5e777f6 | -7.10889 | -47.95396 | 2025-10-26 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0906762f-d910-3573-8c65-2888ea6a9107 | -5.64894 | -35.69837 | 2025-10-26 04:00:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3e465fe2-c00f-3f4a-9b9f-9dd91274312a | -5.5886 | -41.32359 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ba9e0ea-1b93-3cc2-8df6-94e56323b2e7 | -6.14154 | -41.80922 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ba9aa1bc-0f18-35cd-954a-8b461107e49c | -6.15248 | -43.13396 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ca449e17-e6ec-3092-ab8a-6e6a5bfc1057 | -4.5961 | -49.59151 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11b97657-91a5-3ce2-a08f-01d8590c1c6d | -5.65444 | -48.46037 | 2025-10-26 04:00:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4406b6a-d2ee-370f-aeea-af73c451ce4f | -6.13164 | -41.71929 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5f599ead-48ce-3a8d-8dd0-e4e544606599 | -4.79742 | -42.77989 | 2025-10-26 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20dd560c-61ad-3d82-80f4-d84cb67a0b2a | -6.23743 | -38.42105 | 2025-10-26 04:00:00 | NOAA-20 | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8de53b39-8443-36a4-9ed0-8d910497e2ea | -5.61077 | -42.66317 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3bfa990c-ad7b-319e-8229-2427e382f01a | -3.76454 | -47.57558 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50f7f7b8-92d1-3f43-8750-25c381d392df | -5.85507 | -39.26251 | 2025-10-26 04:00:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ff9aa188-187c-3611-afc8-b6affce4a06e | -5.55018 | -41.38883 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c28bba4-5c13-3858-a1f1-e9fefc6a7467 | -6.16774 | -43.13226 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cab071c7-4440-383b-b3a7-99e0f342745e | -4.54985 | -46.55723 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dae3b878-d30a-38b8-b6a3-4ff77c87c8d8 | -6.83282 | -41.55056 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2787303b-bc0f-32d3-ad1c-b044f3a4c677 | -5.46427 | -40.87188 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6403145-5423-3bd3-867c-a69639c3956e | -8.40827 | -46.92321 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f03a544-9441-3f37-a32d-9766978a8c22 | -3.78268 | -43.41217 | 2025-10-26 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 439b9811-68f1-345a-9958-b63ab3979742 | -5.55175 | -41.2431 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19f8adff-34f0-32c8-89c6-b1efe1ee1a7d | -4.89035 | -43.24945 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b87a1ea-9cb1-3998-8c08-5da10f309076 | -4.27216 | -40.69465 | 2025-10-26 04:00:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c81991b-a544-32e0-adc7-1b8f9670002e | -6.84183 | -44.00636 | 2025-10-26 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a68c96f-975b-3e90-a5ee-42ce07d0f6d2 | -7.04106 | -41.6509 | 2025-10-26 04:00:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0e86224-7c7d-3f03-8cbc-5456884a609d | -5.33549 | -47.28978 | 2025-10-26 04:00:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 574677f7-82df-39e2-9594-930361d5e793 | -6.12302 | -41.72928 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 07f5ac17-1edb-3a40-b408-f0cf5f3b47a7 | -9.52246 | -40.30955 | 2025-10-26 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
