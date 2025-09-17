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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 590ad8d2-cb3a-3cac-b22d-8fb623f600a2 | -8.91092 | -46.28088 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 158ae6ec-354c-3af9-85b3-c6321e92585f | -7.2716 | -46.58289 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8fd9a484-f40a-3fd5-9965-22478b3631f4 | -6.42244 | -44.00964 | 2025-09-17 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc7d3453-38f7-3a00-878e-108c633593a6 | -7.09111 | -44.53452 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c47505b-a3cd-359c-970a-43b287d79132 | -8.63608 | -46.43184 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d93b5595-88d8-3b53-8594-7069b3f69c1d | -5.212 | -45.18316 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f80d30cb-17c3-302a-ba60-1293f2d328bd | -6.34781 | -43.15726 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 89419adb-7cc3-3fe2-8ec5-cfcb064d390e | -6.1742 | -41.22941 | 2025-09-17 04:32:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec1a5f5f-ca9b-3ba7-8d11-6b0789cbe7f5 | -8.1623 | -46.76278 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41489778-b647-3288-bb3a-f11a80a989dd | -7.25822 | -48.6811 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dbf7255-71d5-35e2-bf9f-3c15b7b17193 | -6.8649 | -38.44042 | 2025-09-17 04:32:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ab2a402-45fe-3add-ade8-b0d2b32ede40 | -5.56813 | -43.43982 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37f53e4d-5f2e-3d95-b602-161c2a7cc2cf | -6.91846 | -44.8099 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36931c5e-8bcf-3000-afd8-9170ac8337b7 | -6.34387 | -43.15665 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 088a82ff-8b67-3de9-a6f8-1f2f694f04e2 | -8.92301 | -46.27094 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d0079c2-9a08-39a8-9fde-881b1520ac0a | -11.12101 | -45.35535 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3e54bad-72ee-329d-987f-03af30a76264 | -7.88396 | -48.16092 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b728a745-b20a-3066-b3cd-16c45097e02b | -7.34429 | -46.74845 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9423ba27-0abf-3577-b5ab-279d6afb867d | -6.40755 | -42.66569 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 412f899a-4716-36a4-be4b-5bb141ec911a | -6.17336 | -44.50201 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e98e2e5c-0a33-3394-8b06-c2e2459cc492 | -6.8708 | -45.19074 | 2025-09-17 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ceed5bf-2f09-3212-96db-1493f6c8a86d | -6.09312 | -46.50135 | 2025-09-17 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 140d30c7-93fd-30fb-983a-37c8f6bba292 | -5.48197 | -51.53271 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b1ea674d-5da6-353d-a796-2d609c926b15 | -5.6203 | -45.41895 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b28ce939-80eb-3cbc-a6fa-3cafbd78cca5 | -6.76438 | -43.40046 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4fe1eb8-c0ea-3027-ab7b-ae9e2ff827a0 | -7.34134 | -44.58572 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51ae8ce8-205d-3519-8e1d-ad4fb351fb2d | -11.20523 | -47.67055 | 2025-09-17 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0874293f-ef13-32a6-82cc-3e2ff1da94a0 | -6.10324 | -45.93916 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f5b944c-e144-37df-a4f6-766b45d865bb | -8.27392 | -49.78466 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c35ef709-6cd6-31f6-9a61-4aeff09edc53 | -11.02832 | -45.06516 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b7e323c5-4137-3a9b-b3a0-d99303966edd | -4.63572 | -46.07343 | 2025-09-17 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e4b0661-899c-3cc2-9232-c31f267b715a | -5.62486 | -44.82864 | 2025-09-17 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea538f2e-454a-3229-955d-1a5e735aae2c | -5.59735 | -45.36073 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cbb9cfe7-c161-3de3-bdfb-5a5b581a6174 | -8.91553 | -46.25037 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54ce76e9-ef6c-3c88-bd6d-c29197f2a414 | -8.06625 | -45.45786 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1395a291-91e7-3b8a-af52-fed7f216e2f0 | -10.80975 | -50.65242 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ab7647f-72bb-3943-8e95-b133ba850bd2 | -7.48899 | -46.1266 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 228f76ad-650e-34ee-8aab-4c2b3592ceac | -6.87717 | -43.9664 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67109f73-3802-3619-9883-69a19e91c4d1 | -5.76623 | -45.89985 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3658ca4-5ea7-3fe3-a2e8-091e55fb0055 | -6.96531 | -44.55261 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce9a8f9e-0db7-3c2e-9d20-46a765575198 | -6.29517 | -42.38937 | 2025-09-17 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c9c1ead7-88c1-349f-b98d-5a6e6e363967 | -4.73925 | -49.28172 | 2025-09-17 04:32:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 519f05ba-6454-36b0-88c2-a10eb0fb4e6b | -7.32536 | -43.96777 | 2025-09-17 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01dfc861-aede-3c69-87da-db067d62aab5 | -7.52961 | -44.72521 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aca557b7-afdb-39e7-9a74-a0f68c394cb7 | -10.55015 | -51.95285 | 2025-09-17 04:32:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1b1fb11-3fc8-3832-a6f6-a2c7b85c7b96 | -10.32448 | -46.62914 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52554c77-3d7f-3b38-b2eb-2f938db225fb | -8.16175 | -46.76638 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3d5af69-f7ae-3ac9-8dae-bdab0f793a37 | -8.16285 | -46.75919 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4b44f77-fabb-3035-9097-523106f68ebd | -7.50107 | -44.71639 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 112b6a7c-ac5a-3709-a7a1-e35cb17fdd32 | -8.87232 | -50.14027 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d907e5c-0363-371f-bff4-b8115f08021e | -6.40163 | -41.79327 | 2025-09-17 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c512c711-e1a2-3cbe-afdf-da4dd0f8a5b0 | -8.53954 | -48.97648 | 2025-09-17 04:32:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a830ae8f-79c8-305a-9faf-1ca7ab783cd4 | -8.96951 | -44.1925 | 2025-09-17 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8919b721-a25e-363a-86e1-6dae5ec64772 | -11.47065 | -43.56586 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f3f78a5-6f4d-3607-924a-4a5906f64894 | -5.62749 | -44.33108 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a30607dd-d4b2-3f1f-b0e8-22ec1379c7c1 | -8.13466 | -43.63991 | 2025-09-17 04:32:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37171b86-1010-344d-84b1-33340e149d48 | -8.23066 | -49.48542 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f1860ab-1c92-397b-ba8d-5f6265248c20 | -10.22475 | -44.98122 | 2025-09-17 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65a9c9af-edeb-39a4-879d-b021edf02631 | -10.41654 | -50.65359 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d788957a-8666-3c0f-9447-180704daae9d | -8.21723 | -49.48324 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20fdd10b-ba5b-3e43-965c-55f018ea40dc | -7.83061 | -46.1594 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d101b35-c61b-36dd-ae2a-204b0dd81dc8 | -5.54841 | -44.97194 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60a52e57-ceb1-3259-b47e-07b2c1cd1927 | -8.97744 | -45.03365 | 2025-09-17 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d776a16-7188-3907-ae0f-24570c693cef | -5.66371 | -45.04559 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6714de11-5c4d-3088-aa0b-6622daeedff1 | -4.17758 | -47.99174 | 2025-09-17 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffce07c2-0858-33d9-a11b-a9a19bb7baa4 | -5.89418 | -45.72959 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83734ebb-8204-33a3-8c9d-9acd4b86c334 | -8.98329 | -45.75161 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7fc4340-e989-327e-b2e0-f7d5a656373f | -7.5408 | -47.42617 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 997fb69d-1f56-316f-83b3-cc80c673a069 | -7.71908 | -45.29427 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcde32cd-6cad-3a79-8fa3-ec4b457ea5b7 | -7.9978 | -45.65026 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c814350-e8df-3edf-8b11-ee19a2ae86a4 | -8.56926 | -46.34126 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abd3e7b1-4122-3c51-90c7-8a4adfb9f1bd | -10.67937 | -46.50593 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd9fc20a-424b-300d-ad62-562ddb5517a4 | -8.39472 | -47.24261 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e617e26a-d405-3402-82d1-44942c3f99f3 | -3.83519 | -48.94849 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1455a93d-379c-3fd8-9216-c25da14d60fb | -6.9795 | -44.53251 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6908ea84-921d-3dc5-a490-79f7277f2007 | -11.50484 | -43.7108 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 198c5ade-9c28-3afb-90fa-f2e032a06b3e | -10.80572 | -50.65557 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4a8d384-7850-389b-8165-676a72b35508 | -5.7838 | -43.4713 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a97b0072-a0e5-35b3-84ac-db0793c4e964 | -8.2273 | -49.48487 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1222b61a-cb1e-3494-bdab-62d5106b6301 | -9.37765 | -45.38254 | 2025-09-17 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5919af83-2e3b-3ec5-9922-0d7bf8351b98 | -7.83175 | -46.15186 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5306006c-3314-3e89-a7e0-b4bc34695e57 | -6.16219 | -45.98959 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4de13517-ffb5-3f08-9482-80755a46ddb7 | -7.21184 | -44.38317 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15f3916f-f65f-3086-9c4f-53cdb5c3be3c | -6.48909 | -45.72915 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47cbb2e4-189e-3a93-8c39-ba9860643404 | -3.38847 | -50.26471 | 2025-09-17 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39bac506-1525-3b84-8d76-05736f75983c | -5.13162 | -45.11609 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c87761f9-b31e-3bc4-83d7-df6bd5fa08ae | -7.33641 | -39.71257 | 2025-09-17 04:32:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c369653-696b-3f19-915a-c85e97c91d84 | -10.42619 | -50.65902 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db64d8d5-b7b8-3ab4-8401-965a8aad959f | -7.26878 | -46.5788 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f355bdf4-7397-3e45-bd37-9a904871fccb | -7.58083 | -44.58366 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1056aa23-72d0-385d-9b3d-00f8901b3a1e | -6.92905 | -44.76495 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2b16931-76a7-3ada-b246-fbd682d0436c | -10.40032 | -50.62402 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90dec528-f7e0-382b-9906-d55e824ca484 | -6.12655 | -47.82562 | 2025-09-17 04:32:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 878a9254-511b-3afa-95d0-55b68a928c99 | -7.45935 | -46.18424 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae339bb0-b877-3e65-9f8e-bf4eedbd3a9a | -9.17707 | -46.9435 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4afbcea3-b15b-3f86-9df9-ecf9c829aa88 | -4.32845 | -48.38837 | 2025-09-17 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c31f9b4a-5d3b-3ccb-bc12-3b68c8fbccc5 | -9.71913 | -47.4072 | 2025-09-17 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaef3b90-4caa-3856-8dc3-da1307adf157 | -8.57612 | -46.34231 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b13e73b-e866-32c7-aabf-e8542343f290 | -7.44453 | -46.18955 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c280420-db82-3f00-ba3e-deccec7d20cc | -7.64564 | -44.47072 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README41.md)
