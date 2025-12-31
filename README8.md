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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5213cee-c789-338c-92f4-26f2ba8fff13 | -33.71783 | -53.3794 | 2025-12-31 04:53:00 | NPP-375D | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 7b8016d8-bdea-3916-a9be-dd8484a35041 | -3.01173 | -46.71399 | 2025-12-31 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d29fefa-3b68-3cb6-8227-689b7bf801c8 | -1.96159 | -53.36109 | 2025-12-31 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 596a2794-f663-3d21-b915-7b5d0933c5a8 | -4.31567 | -43.78584 | 2025-12-31 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56a71a6e-99ed-38c5-bfe9-6241658213e6 | -3.01218 | -46.71098 | 2025-12-31 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 067f2fcd-3f23-39c6-8865-8870a3a9df4c | -5.72405 | -45.04795 | 2025-12-31 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7b557b82-7f37-3a5c-9798-76389f306be2 | -5.7253 | -45.03913 | 2025-12-31 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 56b0fb81-2560-3b2a-9820-3023a0016463 | -1.08045 | -47.99765 | 2025-12-31 05:03:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9af5f4c8-c613-3a52-bada-09bcc052c753 | -1.78764 | -45.90214 | 2025-12-31 05:03:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8fc1f52-75ae-300e-9d13-c98b03517163 | -1.62238 | -53.8762 | 2025-12-31 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1f477d7-f866-3dc4-9891-2533de3bc956 | -0.94252 | -46.93911 | 2025-12-31 05:03:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b288a7b-1d06-3544-9256-72f432b71b7f | -2.89928 | -45.10419 | 2025-12-31 05:03:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50bd3d98-1e05-328d-946a-de56ab4b9b1d | -4.989 | -47.9336 | 2025-12-31 05:03:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70d57b42-2310-3761-acd9-60c5be87acbb | -2.6283 | -47.29475 | 2025-12-31 05:03:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2471ff7e-71f5-3c4c-966e-c8cee24788f0 | -1.07211 | -47.99163 | 2025-12-31 05:03:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80f9cdd0-13ea-3750-b1f7-d3426bb6e5c9 | -4.31304 | -43.78303 | 2025-12-31 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99b27b83-2acc-3a6e-9f6b-fbb88e6c6182 | -0.92982 | -46.89297 | 2025-12-31 05:03:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5e595db-b47d-36ff-b977-86c68cc241f6 | -1.62293 | -53.87268 | 2025-12-31 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ea936c3-451f-3b34-952d-479491700753 | -3.18333 | -51.10633 | 2025-12-31 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1391697d-f40b-3aa9-a94e-238e4620afc7 | -5.72467 | -45.04356 | 2025-12-31 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8c17a7d9-c1d4-3471-b512-f74f96e6160e | -1.07592 | -47.99694 | 2025-12-31 05:03:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a91350f-6a12-35f8-9028-8da210c6c3fc | -5.72591 | -45.0348 | 2025-12-31 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f23974cd-ead9-3ec3-a512-48be34cb0a7f | -1.9582 | -53.36057 | 2025-12-31 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29419367-b02f-314f-9fc0-5d0f5aba81e8 | -1.1573 | -53.50861 | 2025-12-31 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc71f1b0-2e11-371b-a240-3b7e3bf14c7a | -2.90496 | -45.10507 | 2025-12-31 05:03:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08371b06-72ec-33c0-bb73-030afea169a4 | -1.16065 | -53.50911 | 2025-12-31 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 654f7943-d40d-3c05-b439-f682b1c49fdc | -5.71875 | -45.04257 | 2025-12-31 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60a2c5a5-b980-383d-8ee3-5cb38988e013 | -2.06769 | -53.4882 | 2025-12-31 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73fb94bd-6bdb-3aa1-9304-74dd4187d1c1 | -1.79342 | -45.89975 | 2025-12-31 05:03:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e0ab606-052a-3815-868e-2c23f60e7047 | -2.63072 | -47.29357 | 2025-12-31 05:03:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e00400f-db05-3735-8707-e932ab3517fc | -4.31229 | -43.78839 | 2025-12-31 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8a7692a-969b-3c9f-9dce-d3b9dc6db540 | -1.07664 | -47.99237 | 2025-12-31 05:03:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab70d829-6ac9-3007-9ea7-ba08e741c010 | -1.61925 | -54.22132 | 2025-12-31 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13fa7fb0-3e5b-37bf-bf5d-c1583a5ce70d | -1.6438 | -54.34554 | 2025-12-31 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 396019c4-dd57-318e-b254-e612bc858f7a | -5.71813 | -45.04699 | 2025-12-31 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7387109-696c-39e6-bdca-29df480d7631 | -4.30938 | -43.78479 | 2025-12-31 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3a9d389-b2aa-3260-942d-06a3258729bc | -9.4177 | -62.70797 | 2025-12-31 05:05:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1d81faa-40ab-3ed8-a726-2c40883c7034 | -9.11935 | -62.55306 | 2025-12-31 05:05:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81a1d84b-e4e9-381c-9e1e-71ea532fca86 | -11.15608 | -43.32122 | 2025-12-31 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 76fe25ac-f037-350d-b06a-229c8d7e9a21 | -11.15767 | -43.327 | 2025-12-31 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5c6b07ce-090a-3695-87e4-5f48f963cfaa | -9.11507 | -62.55231 | 2025-12-31 05:05:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b152221-8f36-314a-8f4a-08a0a7cb67e9 | -11.14902 | -43.32036 | 2025-12-31 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fc43c577-fc23-3936-b0ac-138cfca3ff40 | -11.15847 | -43.32015 | 2025-12-31 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8b6f9ecb-9ba0-35f5-a1e0-2aa9b8fb3a9b | -7.78484 | -43.10511 | 2025-12-31 05:05:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f6d79401-c6fe-3610-ac23-2d02cb5b703a | -12.65898 | -46.7653 | 2025-12-31 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37832053-e111-3ab6-a71a-3d3ad556841a | -11.15142 | -43.31929 | 2025-12-31 05:05:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 806e3c9e-ad5d-33f9-abdc-5fb98c7116c2 | -16.31305 | -57.562 | 2025-12-31 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 11a7c1eb-d1ba-3222-befb-f25a9697eebf | -19.32461 | -54.02602 | 2025-12-31 05:08:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc970f37-c016-3d6b-a008-80748a9530b3 | -15.12779 | -52.94424 | 2025-12-31 05:08:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fefed01-d13c-3e35-b2de-48ccd5719d4c | -15.58024 | -57.38685 | 2025-12-31 05:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47f82a2e-0f41-39dc-94ff-dea7abb07c4c | -14.71976 | -53.97086 | 2025-12-31 05:08:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbeacbc8-fb28-338b-a7a2-07d761a3125b | -15.62249 | -57.31247 | 2025-12-31 05:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 191568f6-72c5-3a8c-8cff-b47b254bebea | -14.7243 | -53.97425 | 2025-12-31 05:08:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69e866cd-7078-3238-bbd1-7b617f585ac5 | -16.31581 | -57.56617 | 2025-12-31 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 879934a0-c6e3-3255-91ad-fc2c9d0b00d9 | -16.30584 | -57.5645 | 2025-12-31 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4fc179d4-777b-3288-b357-82547d22e611 | -14.7235 | -53.97141 | 2025-12-31 05:08:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37bdaac1-94f8-3bbc-83e2-e7152c552b62 | -19.32855 | -54.02668 | 2025-12-31 05:08:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1135b302-79e6-30c0-81d4-2121e42c7d6f | -15.03399 | -57.18744 | 2025-12-31 05:08:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b00c197-54ce-3ed9-beae-982a4f2ab301 | -14.72119 | -53.96912 | 2025-12-31 05:08:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03e6d6a8-a973-3d47-9e29-bb25034ffaab | -16.55803 | -51.31153 | 2025-12-31 05:08:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e73b8ebe-3a19-320b-8dcd-1895b0265b50 | -16.59525 | -58.21035 | 2025-12-31 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a81ec7d1-2df4-34d8-aed3-8e2abce8331d | -19.49302 | -53.95064 | 2025-12-31 05:08:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 308256fd-d11a-3a74-b295-39bda4489b51 | -15.62582 | -57.31301 | 2025-12-31 05:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a57707b-bedf-3d65-8e38-bebf13560e22 | -16.07101 | -57.08634 | 2025-12-31 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2fa14ead-b4bc-3478-afad-0e1d778de790 | -14.72056 | -53.9737 | 2025-12-31 05:08:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 548a2c86-4301-3b43-8af0-0cb3723766ef | -14.65227 | -52.89569 | 2025-12-31 05:08:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32c9bfa3-a429-3a6d-92bb-7e9565b9d8de | -14.72494 | -53.96965 | 2025-12-31 05:08:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 248e12f7-aefe-3917-af55-07274224d26e | -15.48085 | -59.8631 | 2025-12-31 05:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c5f12ab-3ed3-3d92-89fb-f056eeb50df3 | -16.59857 | -58.21091 | 2025-12-31 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| dca64abc-0a5d-3069-85cd-3cd249d569cd | -20.36655 | -56.26468 | 2025-12-31 05:10:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25184546-a3fd-370b-9b5c-dcc2953ad11c | -20.32054 | -55.92374 | 2025-12-31 05:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| ab4e763a-6c77-3f44-b94f-10c67012b55f | -20.32114 | -55.91935 | 2025-12-31 05:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| e5d67fb9-4465-3936-b37e-1a3a6035b625 | -20.32415 | -55.92431 | 2025-12-31 05:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c576e298-0240-3346-8b71-b5929584344c | -20.32776 | -55.92487 | 2025-12-31 05:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 69119417-0947-368e-83a1-59b3189560fd | -33.71571 | -53.37931 | 2025-12-31 05:12:00 | NOAA-20 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 680ac826-acb3-30d5-96fe-c5b57e4f72d9 | 3.19741 | -60.24052 | 2025-12-31 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7834f188-bc8e-31b8-bc35-ba1c2837564a | 3.20108 | -60.23567 | 2025-12-31 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db33a138-0762-384d-81c0-09c85130e0e8 | -9.11706 | -62.55128 | 2025-12-31 05:57:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2372fa34-9c03-37b1-a029-da1afdfba2ed | -9.12155 | -62.55196 | 2025-12-31 05:57:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bc796d9-579f-3419-8451-8685f3c80b1b | -2.16851 | -48.02156 | 2025-12-31 06:16:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fda0be3b-0b4d-32cc-b61d-b406d59d0acc | -1.07233 | -47.99122 | 2025-12-31 06:16:00 | AQUA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6fef1f08-47ba-3bc1-a8f1-e3a04ade31c0 | -1.08109 | -47.9925 | 2025-12-31 06:16:00 | AQUA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c6f14641-6cf7-3a82-9188-39e3035a10f3 | -2.90614 | -49.3769 | 2025-12-31 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d2a0a241-2b2a-38cd-9472-95f300f5411c | -2.89854 | -45.0966 | 2025-12-31 06:16:00 | AQUA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 19b8668c-201a-3e9d-b4c5-3429fa7efbb0 | -4.30996 | -43.78587 | 2025-12-31 06:16:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d06b7a22-fe73-3644-b8b0-8ebb5ee97760 | -3.14984 | -48.13593 | 2025-12-31 06:16:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd76bd87-1b6e-3329-83a0-350b9c6c6b6a | -2.9075 | -49.36793 | 2025-12-31 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4c43cea4-5898-3ee3-bf2b-24bf6b3188e0 | -12.66093 | -46.76542 | 2025-12-31 06:20:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 83c64b2e-ae5d-344f-87b4-b5bee7d4c2cc | -12.66335 | -46.76005 | 2025-12-31 06:20:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| da912c9f-6e02-32cf-ab79-78e56af23ca5 | -13.55953 | -47.75254 | 2025-12-31 06:20:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cbf00b9e-3198-3430-9276-bc0b72e07cff | -15.12757 | -52.93945 | 2025-12-31 06:22:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fa8c1b72-3594-3398-963b-018b3680a880 | 3.20126 | -60.23915 | 2025-12-31 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e96e41cc-efdb-3281-8723-9bd7c0d07eb6 | 3.19461 | -60.24021 | 2025-12-31 06:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea884f7d-d418-3c7b-a5c3-9c68c9f220e3 | -0.09145 | -51.28448 | 2025-12-31 12:33:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0be5ff8b-f785-3b9f-8004-c87e7328162e | -1.60196 | -53.54839 | 2025-12-31 12:33:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 68084397-6af7-35e1-bc4d-953b9a7fb885 | -4.30822 | -43.77564 | 2025-12-31 12:33:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| f294413d-54f4-3a84-9961-784f3792056f | -1.08077 | -47.9863 | 2025-12-31 12:33:00 | TERRA_M-T | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| ac405df3-1885-37cf-b3e7-c771b5f2bf6c | -4.31626 | -43.77008 | 2025-12-31 12:33:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 31166056-5383-36bf-bce5-84f2db5c97e8 | -1.60327 | -53.53933 | 2025-12-31 12:33:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6202bb6a-62fb-3c1b-83b6-1e297d6eb482 | -9.71965 | -48.90445 | 2025-12-31 12:38:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |


[Clique aqui para ver as próximas entradas](README9.md)
