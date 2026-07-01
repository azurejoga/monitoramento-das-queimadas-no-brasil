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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3a3e035-a2eb-3c0e-8230-39f3fbc64bf7 | -9.0175 | -45.7397 | 2026-07-01 11:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a37d07f4-2206-355e-af63-9e87ea77e3b8 | -12.8359 | -44.3422 | 2026-07-01 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 82a0a4c4-f488-3e5d-9dcb-62b05685bea5 | -9.0175 | -45.7397 | 2026-07-01 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 35dc432d-260f-3d3d-ac56-7da790a28384 | -8.9985 | -45.7418 | 2026-07-01 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| b0f99dd1-2927-3f5c-8402-55abbd009b0a | -12.8359 | -44.3422 | 2026-07-01 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| d5557774-2bcd-31d4-9b17-fd7d6abc16f6 | -8.9985 | -45.7418 | 2026-07-01 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| ab72279a-dd7e-3a60-bc63-8785fe37c89d | -9.0175 | -45.7397 | 2026-07-01 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 615c2b48-8fc7-300a-9926-48fbe18a484a | -12.8359 | -44.3422 | 2026-07-01 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| bd4cd34d-59b2-361f-8fa9-5a0fd50b4423 | -8.9989 | -45.7191 | 2026-07-01 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 021b8865-b47e-344d-9a4e-727d85fdb85c | -2.96934 | -41.05237 | 2026-07-01 11:45:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 013829f5-7964-3377-88d1-0b1082e8cc31 | -3.87208 | -42.9649 | 2026-07-01 11:47:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2711a28f-4720-3578-853f-110ce31be98c | -7.47839 | -44.74361 | 2026-07-01 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 09c20392-fe9b-385e-a327-4b7b68727312 | -7.48991 | -44.06241 | 2026-07-01 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 4fe34ead-3db9-3968-a744-a9b05d659413 | -6.40261 | -41.33661 | 2026-07-01 11:47:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b4aaaa25-c42b-3fe7-b46a-776b56b98ae0 | -9.01068 | -45.7279 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 4719c6d2-edc8-3539-92e7-50f9835e9210 | -8.35627 | -46.80863 | 2026-07-01 11:47:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9b10b93-f10d-3956-b2ec-df528bae7186 | -9.00942 | -45.73681 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ae289ab7-afa9-33af-ab15-8fa2b9e06df8 | -7.49913 | -44.06365 | 2026-07-01 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e29267a-6eea-30aa-afda-ee4e41ca2574 | -4.84668 | -42.93009 | 2026-07-01 11:47:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 23c5489d-ae63-3833-8334-cd0792599753 | -9.01825 | -45.73803 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0e897a3f-5783-3abf-b91b-c56cbd39c184 | -6.90434 | -42.85214 | 2026-07-01 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 647df2f1-d3fc-304d-8d7c-bd8eb8cba0d5 | -8.98296 | -45.71753 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| f0565613-66f6-3701-9858-533f99268256 | -6.90587 | -42.84112 | 2026-07-01 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 345345ff-879c-3638-8b48-a4522a1bb466 | -8.99681 | -45.74673 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 404faaa6-f9a5-3d0e-9519-e2f085beb2f5 | -5.42478 | -46.65121 | 2026-07-01 11:47:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a49a4ad3-c8ca-341c-bc4d-e569906f7bdf | -5.79767 | -43.63516 | 2026-07-01 11:47:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fe53aa84-d45f-3501-9ba9-7892b3f30159 | -6.92462 | -47.82947 | 2026-07-01 11:47:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b3b8e9d2-082b-3da6-91f2-d4c98c429cd4 | -5.79561 | -45.03909 | 2026-07-01 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 49f7f11c-377c-3f84-a2eb-1b306d4d9353 | -7.92762 | -48.28336 | 2026-07-01 11:47:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e72780f9-41b5-30aa-9814-d1071a6cb3bb | -8.59705 | -48.00352 | 2026-07-01 11:47:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 986f44a2-7b42-3599-9bdf-c7c4251ddc4e | -9.00691 | -45.75464 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b5099633-b760-3851-9e3b-ddffa204cc63 | -9.00817 | -45.74573 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 704d6a30-c9ad-3d64-80b7-603256a5c831 | -7.47709 | -44.75283 | 2026-07-01 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97c5f31d-f984-302b-91d1-423a974b74cf | -5.80193 | -45.05802 | 2026-07-01 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 187536f5-c491-32e0-9a4c-41597a2afe88 | -8.12696 | -47.87794 | 2026-07-01 11:47:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 547c046a-c684-36fc-a223-b01a38f7a17a | -8.98422 | -45.70861 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7af48868-c9da-3392-850d-b93b9d4e9b0e | -5.79686 | -45.03025 | 2026-07-01 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2c4adfb1-51a0-32a6-90ca-5129603ec14d | -5.55909 | -43.9653 | 2026-07-01 11:47:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 988b4474-9d27-3015-9716-c5a7eea64cd3 | -7.0229 | -45.43153 | 2026-07-01 11:47:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 33fc45f0-442a-388e-962a-91af6745d498 | -7.73742 | -45.91379 | 2026-07-01 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9aaf1b25-2702-3eb8-aff7-7b31d57858ff | -6.306 | -45.72152 | 2026-07-01 11:47:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 14782c2e-d2b6-3280-8ec1-637615d12cce | -7.29334 | -46.24846 | 2026-07-01 11:47:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9670fd45-a9c5-3d82-af87-4f6fed560f45 | -8.99808 | -45.73782 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a4373ecb-bf31-3edd-b6ca-3fb7025d4b79 | -7.09851 | -46.50615 | 2026-07-01 11:47:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 122286d9-3cb4-3bec-95a0-72d8e1051901 | -6.93383 | -47.83093 | 2026-07-01 11:47:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 356a4462-ce28-3044-9b18-1740e2875bc6 | -8.63851 | -46.52308 | 2026-07-01 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 29c3b6e7-1564-38aa-9aa3-26a6b13ab393 | -5.81305 | -43.79552 | 2026-07-01 11:47:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 42300624-9fac-3905-b4ca-9e1b3b2bc6e7 | -5.80067 | -45.06688 | 2026-07-01 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c63c0939-d0a6-3bef-b59b-ff0b0b71b041 | -9.0195 | -45.72913 | 2026-07-01 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 04e2e2e2-2410-3494-91fc-64437ffe7f18 | -3.87069 | -42.97495 | 2026-07-01 11:47:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| eaf79deb-656f-31d3-b5f4-47f1780b327f | -9.68356 | -47.01932 | 2026-07-01 11:47:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e01f38c6-a7cc-3296-8a2c-af64f668d5f5 | -9.97514 | -48.24036 | 2026-07-01 11:47:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| caa36b40-4d31-303d-b2d8-2ba336a89d25 | -6.30726 | -45.71275 | 2026-07-01 11:47:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8b4a394d-83d1-354e-9a43-09106708542b | -20.32409 | -50.42393 | 2026-07-01 11:49:00 | TERRA_M-M | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bb2c4b8e-671d-3e6e-b8a5-df695d9be26f | -17.71033 | -46.79415 | 2026-07-01 11:49:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 40af20e4-9d0c-3f12-88f6-7cb0fd4aaef7 | -10.38886 | -49.58797 | 2026-07-01 11:49:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f121ba79-a120-3235-8c7d-d63dd2cffc0e | -10.80605 | -49.34277 | 2026-07-01 11:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 93221947-c3e7-3ccb-b219-8e15dbaa3fbb | -10.80768 | -49.3321 | 2026-07-01 11:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 913f2cc1-917f-3daa-9b37-76a2323eb705 | -12.7668 | -44.4873 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| da6d0832-567c-3373-bc1f-84cebed4da59 | -12.612 | -43.34772 | 2026-07-01 11:49:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a5c072df-930c-32a1-bc92-c364e7eb1476 | -11.92204 | -43.38984 | 2026-07-01 11:49:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0232d372-b536-3349-a8b5-c4c70d59ef12 | -12.76824 | -44.47665 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8f6ef3c3-802b-3570-b515-5d5dc7df0979 | -12.7691 | -44.50436 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 554d8992-c81e-3a30-9a02-77a89f44fe75 | -13.73976 | -45.10717 | 2026-07-01 11:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd6ae281-c5cc-3152-857f-69eb1981f86f | -11.56786 | -50.45447 | 2026-07-01 11:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9ac80b47-e9fe-3b85-b828-da3b18a1b57d | -17.72064 | -46.7859 | 2026-07-01 11:49:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e2832929-bf97-3dea-9d9c-649763bf03d9 | -12.77049 | -44.49371 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| bf4ff45b-d24d-3903-ad3c-d3685776b712 | -10.79663 | -48.55822 | 2026-07-01 11:49:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| c1de48a2-0c50-3216-b7a2-b97082546696 | -12.50924 | -48.27535 | 2026-07-01 11:49:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| cd2c1438-d069-32de-9a41-27f91ba18718 | -14.80975 | -49.01621 | 2026-07-01 11:49:00 | TERRA_M-M | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b2fb4e2-1264-39e3-b4d8-13085e66e545 | -11.84091 | -45.52752 | 2026-07-01 11:49:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e061c963-a303-3584-b2a6-e6c4048538eb | -10.92626 | -43.04925 | 2026-07-01 11:49:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 0e74c739-0ffd-3fb5-bda4-51429a9739d4 | -11.5495 | -47.45755 | 2026-07-01 11:49:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 158a9696-5b27-3de3-8cf0-72e36f7058d5 | -12.82863 | -44.34806 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e665034f-9a73-39ce-af38-dded8bc63b03 | -12.83827 | -44.34939 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 4ea89274-1672-3bc1-8992-4ce69e3e5bc1 | -18.37741 | -47.57095 | 2026-07-01 11:49:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aaba052c-e563-3cc1-a972-412cc8fe4a94 | -12.83684 | -44.36024 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3ad3dc03-d52b-31de-aeda-d7424fa74092 | -13.74113 | -45.09694 | 2026-07-01 11:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cf2aa351-1b1f-36c5-b304-ee872597bfd7 | -17.56643 | -46.56276 | 2026-07-01 11:49:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| aac02f84-dd7a-3a27-8986-397bc5d0ae13 | -12.5106 | -48.26605 | 2026-07-01 11:49:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 51fba240-854d-3753-8188-9b33b136738f | -10.80439 | -48.56934 | 2026-07-01 11:49:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 15acf6ea-4af9-30ca-bbf2-b83bc52ffbd0 | -14.81119 | -49.00666 | 2026-07-01 11:49:00 | TERRA_M-M | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 11a328e6-f4ef-3f46-b56e-08605f877d87 | -13.73026 | -47.88236 | 2026-07-01 11:49:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 117ce034-e2d2-3135-b10c-c131a93bb6c0 | -12.76536 | -44.49795 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 27ff0902-6a2a-3bda-b2f0-5aeedd89101b | -17.56774 | -46.55296 | 2026-07-01 11:49:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e241b227-a875-3d50-b07c-c51e8d629703 | -11.91188 | -43.38857 | 2026-07-01 11:49:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 4b170292-c27f-359c-84aa-a3494daf6e25 | -14.29569 | -47.15822 | 2026-07-01 11:49:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c6ab1a9a-7155-37a9-81d7-9a997f609499 | -18.37612 | -47.58028 | 2026-07-01 11:49:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5779b539-490e-3fd2-a2b3-d85d332381dc | -12.83971 | -44.33851 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3a49f7c0-932d-38d0-84b3-1089c96af0a2 | -10.79519 | -48.56801 | 2026-07-01 11:49:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 8e9dc1da-1f90-31df-b536-61f111ad58a6 | -12.77187 | -44.48304 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1cb2eeab-5fd6-344f-a001-e036e4083b12 | -17.71935 | -46.79551 | 2026-07-01 11:49:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 5b4f7629-97a5-31c0-b750-df3c8e6d7aeb | -10.13115 | -52.09389 | 2026-07-01 11:49:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 9a2ae024-b5cd-3740-8cee-dde305913c67 | -12.84792 | -44.35069 | 2026-07-01 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| fb174a8e-dbc9-30e1-a70b-6f616c154905 | -10.40128 | -49.4433 | 2026-07-01 11:49:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bcfb2517-938c-348e-ad1c-bf43d0c3359c | -10.80582 | -48.55959 | 2026-07-01 11:49:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 634de841-1a24-3fd9-b25f-b62bcb3f028c | -20.32563 | -50.41396 | 2026-07-01 11:49:00 | TERRA_M-M | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 1a72f294-488e-387e-b1b1-3f5fbda1bac1 | -12.8359 | -44.3422 | 2026-07-01 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 99b6bb7c-be0b-32b3-b829-b742ff8799f0 | -8.9989 | -45.7191 | 2026-07-01 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 62de1fcf-15a7-340c-98db-6444617d216d | -9.0175 | -45.7397 | 2026-07-01 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |


[Clique aqui para ver as próximas entradas](README33.md)
