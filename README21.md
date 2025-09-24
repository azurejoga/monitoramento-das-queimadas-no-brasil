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
| 92a5450f-f7bb-3543-8e0d-af4c6b864174 | -5.21905 | -43.73122 | 2025-09-24 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| ea48acfc-baed-30df-ab2c-370af88f3a87 | -10.3779 | -46.14784 | 2025-09-24 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b56d468d-0bdd-33ca-97bf-9d699645c7e9 | -9.56602 | -47.57735 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e19bca10-8c67-3fcc-a5ae-e197fd71860c | -9.55218 | -47.5481 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 8e7508ac-ce0a-3d90-b770-8215868e1d26 | -8.85183 | -46.18916 | 2025-09-24 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ae91a1b4-07e3-3a49-b938-4d3751de865f | -8.52827 | -45.01602 | 2025-09-24 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2760afa1-470e-379f-97ad-abd0e145ff86 | -3.79045 | -41.71479 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 071bed62-687a-3677-bf81-3df4558031db | -9.0598 | -46.67057 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c609bf80-4a26-397f-ab3c-b100b8eb7b9f | -9.57486 | -47.57861 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d73477b0-9d71-3adc-9e54-0a411e234081 | -8.24213 | -38.05536 | 2025-09-24 12:17:00 | TERRA_M-T | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 5875cbc7-c28f-374c-8971-6c56a31c62a3 | -8.26532 | -44.39758 | 2025-09-24 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 215.2 |
| fa5a44d7-69c1-3740-aa85-6dda70c7852b | -10.2918 | -45.22607 | 2025-09-24 12:17:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 55412e8a-8015-3ea4-9994-a12d01fb1a47 | -7.19379 | -43.50011 | 2025-09-24 12:17:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| b0192c53-488d-368c-9aa3-b020e6f55b6a | -3.29394 | -43.09048 | 2025-09-24 12:17:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8931706f-da4a-3a86-bb90-5c1586a91a07 | -9.03235 | -44.94652 | 2025-09-24 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| db482f23-55c4-3c0f-a26f-e559227752bd | -5.13552 | -44.97199 | 2025-09-24 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 189550ee-3d57-3767-8a48-31df3e9053b5 | -9.59493 | -47.5785 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d4a4cb58-098f-3c00-899f-23f1b65de17a | -6.43069 | -43.09362 | 2025-09-24 12:17:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 83240181-f707-30a1-811d-18cb14d75dc5 | -5.16499 | -42.062 | 2025-09-24 12:17:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 76fbf6cd-fb13-3231-a873-298109924839 | -6.13196 | -44.44125 | 2025-09-24 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4adac7ee-588f-3150-801b-6f2b7b7b98a5 | -9.18735 | -44.62223 | 2025-09-24 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e344d9a4-e549-3f99-afd8-8e8f34b7275e | -4.79639 | -43.53353 | 2025-09-24 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b921f26a-644a-3f92-984b-27370960d5a9 | -5.97269 | -44.12608 | 2025-09-24 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| f2fc84cc-8710-36c2-8652-eef46ce96151 | -3.86821 | -40.36287 | 2025-09-24 12:17:00 | TERRA_M-T | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 30.9 |
| ee31bbbb-fd64-333c-9a2e-ceec09444ea1 | -7.20412 | -43.49544 | 2025-09-24 12:17:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 160d5697-d940-3a7d-aa2d-97bb34b1258c | -5.97414 | -44.11567 | 2025-09-24 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a77256c2-33f5-3aea-b700-77847c31430f | -8.00419 | -45.73364 | 2025-09-24 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a0aaf30b-07da-3256-9dd4-8ca2e52a36c8 | -9.55846 | -47.56718 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7e864e4e-bae4-3152-8f14-8e540eb2bb32 | -8.4955 | -46.88777 | 2025-09-24 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f11c93b6-6aba-3b87-a4fd-a8318704565d | -9.56231 | -47.54045 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7b59bd20-2359-3606-9d41-9e2f4fa7d509 | -8.32242 | -46.22327 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| b2ae3e16-ec29-36aa-b917-73b5f62f3c0b | -3.6061 | -47.52824 | 2025-09-24 12:17:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c9d261ad-2808-3196-8d41-79d6136c2a67 | -6.42188 | -43.09837 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0ebc7fb1-667f-332d-b154-65407f57fcc6 | -6.89659 | -44.76376 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f14a37d8-0ce2-3a82-b6f8-e42339d5bbd5 | -10.80359 | -40.51183 | 2025-09-24 12:17:00 | TERRA_M-T | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 0ffd737c-9f11-340a-b88f-4ee7b13e711b | -3.46123 | -44.43206 | 2025-09-24 12:17:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8838f819-d854-302e-82d7-5795e0e99dbc | -7.64296 | -45.21982 | 2025-09-24 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ad85562d-4694-318e-b068-0a12bb63d6eb | -9.59621 | -47.56959 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6b46a523-252f-362d-be99-6e5e4f53d97a | -8.66763 | -44.00226 | 2025-09-24 12:17:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fc7b9388-c2f7-3be3-80e6-2c15464328d8 | -5.25329 | -43.72046 | 2025-09-24 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 93fab3a7-d621-31b6-8bbd-8f056190f98c | -8.23231 | -38.04862 | 2025-09-24 12:17:00 | TERRA_M-T | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 1e5463ea-4e30-3a8c-8166-10b52a1291b2 | -8.18143 | -46.36612 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a88bd7e6-3ac0-3242-9401-21529beacba4 | -8.50435 | -46.88902 | 2025-09-24 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 01c49c37-d50f-3aa7-8b00-912dd80132ca | -9.58608 | -47.57723 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 9d9cdd6a-24d5-32e8-b290-c4789b86f2ba | -9.56987 | -47.55062 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 418d0568-8606-3719-8523-829e04a88e7c | -9.56859 | -47.55953 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 14312dd5-16a1-37a8-befb-2db83df33746 | -6.98637 | -44.71159 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2f7e9543-f4ae-3c05-898a-157ac8908166 | -10.58715 | -44.07734 | 2025-09-24 12:17:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2e2ce9cd-81b1-3130-adfe-0e39517ea896 | -10.11518 | -45.31332 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 776071fd-6947-3bb2-a6cd-428ddb8ac438 | -5.84788 | -42.6413 | 2025-09-24 12:17:00 | TERRA_M-T | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| bcc61b62-7880-3c44-9f0a-10d510b4b67d | -9.56103 | -47.54936 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 57a811ea-2176-30e8-b219-525af30d7068 | -6.05595 | -46.60217 | 2025-09-24 12:17:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2fc3680d-9f6a-3564-b982-39a383d29fd1 | -9.21011 | -45.34144 | 2025-09-24 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e5373d66-38d0-3dcb-a076-925045db5070 | -9.73524 | -46.72352 | 2025-09-24 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4209c2ee-f2e4-3ec5-beb8-821844489cc7 | -10.11383 | -45.32321 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 905bd41a-a8e4-36f7-832f-787a1825a8cc | -3.46258 | -44.42257 | 2025-09-24 12:17:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 05078b80-3619-366d-a9ce-8ed4aeb58bc1 | -7.65102 | -46.01545 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 67ca4f6e-feca-3f96-a160-b494b4e79c92 | -6.05468 | -46.61099 | 2025-09-24 12:17:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f96868d6-dade-3116-a34d-0e2a506c6fad | -7.28244 | -42.98219 | 2025-09-24 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 8e4f1fbf-55ce-3d39-a6ee-423faa8edcd0 | -4.29446 | -44.92336 | 2025-09-24 12:17:00 | TERRA_M-T | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9b74de75-f2ce-304c-bbea-3e5b1bb1188c | -7.20388 | -43.5015 | 2025-09-24 12:17:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 1a444ac7-ad5b-3122-b383-425254d54c1f | -7.36808 | -47.0336 | 2025-09-24 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 23316121-9ffb-366c-a3b5-3abf16e273d6 | -4.79324 | -42.75621 | 2025-09-24 12:17:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ef0298ff-535a-3697-b3f2-68a9dffd08ef | -4.80183 | -42.76968 | 2025-09-24 12:17:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3bd1e26a-b5b5-303e-b7a5-18a67d5616da | -7.82924 | -47.85612 | 2025-09-24 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d4599962-8075-39eb-9840-5823525d1385 | -3.79234 | -41.70089 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 0aa73f79-6f8e-38fa-bd02-04c1ae14e6bc | -8.17158 | -39.62253 | 2025-09-24 12:17:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 23.5 |
| a0d410bb-6d65-3f5b-ac35-082fcb969040 | -6.23375 | -45.80244 | 2025-09-24 12:17:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b4432560-44cd-3007-8332-e378f69a1b6e | -6.38763 | -43.71583 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ca33c062-4eb7-3e4a-8cbf-2eeb50c46031 | -5.51987 | -43.8617 | 2025-09-24 12:17:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e3bf7283-7f73-3672-8367-a7f670f5d27e | -4.79485 | -43.54439 | 2025-09-24 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 242de2fa-f0d3-353a-91d6-a78dc52e72bc | -8.51092 | -45.00349 | 2025-09-24 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3dceeac9-cade-31eb-9e2e-817c6a6aeba6 | -8.1797 | -39.60542 | 2025-09-24 12:17:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 23.9 |
| d1263079-3bb0-3dbf-a1a1-10c7f79ced55 | -9.57615 | -47.56971 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 65ee6574-570d-3ba2-b32e-148dfa8add02 | -8.33391 | -44.81225 | 2025-09-24 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9ac52e10-780b-348a-8fcd-5503882224cb | -8.3237 | -46.2142 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| ad8dd47d-80f7-3b0c-97ac-7f1e12080c84 | -6.42356 | -43.0863 | 2025-09-24 12:17:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a99e1ff2-24ee-3dc7-8c85-0cbede166f8f | -8.50689 | -46.87125 | 2025-09-24 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 96dd7b52-0c46-3e98-b69a-a89f455292d8 | -7.20256 | -43.50721 | 2025-09-24 12:17:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| ae4a8af7-f077-324e-852c-d09afa23d31c | -7.59672 | -43.91159 | 2025-09-24 12:17:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 0340cdd3-4285-3022-bdab-f4bcaac47e15 | -9.55974 | -47.55827 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 366455ee-cded-38fe-b284-3f10b6043d4f | -11.98714 | -46.62693 | 2025-09-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 81d3997a-2ae2-337c-826e-8fc17078752c | -11.52625 | -43.66902 | 2025-09-24 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| dc5364e7-fbf6-32e0-97f0-5d6360105210 | -18.30978 | -43.93719 | 2025-09-24 12:19:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 3eb4cc95-672c-37b4-8209-d7b315fd8bae | -13.90811 | -40.38968 | 2025-09-24 12:19:00 | TERRA_M-T | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 8e18f42d-cb19-3d0a-827d-69c9c9f1543a | -11.62929 | -44.37296 | 2025-09-24 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 4b190e2a-e116-3006-955b-0782750a4600 | -11.66822 | -44.39024 | 2025-09-24 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 8ba96cf4-eeee-333d-a392-a0218132ff3d | -11.84474 | -45.12583 | 2025-09-24 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 13e4edd9-deb6-3a30-90a4-5ea012db5a40 | -18.11154 | -47.12592 | 2025-09-24 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 227c1008-4a6d-3999-b11d-2658b36422d0 | -18.11291 | -47.11573 | 2025-09-24 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| dd5ba53e-142e-3994-9841-eb59a7fef058 | -13.01298 | -42.40308 | 2025-09-24 12:19:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 6f17107c-aed5-3c33-96b4-fae3e8c2dbad | -14.31212 | -42.68904 | 2025-09-24 12:19:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 45cd56f3-2000-39c1-9bf4-d7eb95f48614 | -11.51729 | -43.65436 | 2025-09-24 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 17777ca9-b09e-3d2b-b157-00042b16c6ee | -17.95626 | -55.86152 | 2025-09-24 12:19:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.9 |
| da13e9c5-62af-3f1a-aacc-8204b320c0ec | -14.56731 | -41.95378 | 2025-09-24 12:19:00 | TERRA_M-T | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 53.8 |
| f1f125b3-b485-3562-b9e7-0fc14e907430 | -13.28037 | -43.28366 | 2025-09-24 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 81bdd39a-a24b-3aee-8663-329dcb197538 | -17.95704 | -55.85475 | 2025-09-24 12:19:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 08c35f46-4080-3eca-bf29-b4ac6149af07 | -11.40749 | -44.95957 | 2025-09-24 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7e090d1d-4ecd-3fb0-8b2e-7333f2926f9d | -20.98244 | -47.04552 | 2025-09-24 12:19:00 | TERRA_M-T | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 41b2504c-6edc-3ef7-a775-cc20ec91d035 | -11.64258 | -44.35033 | 2025-09-24 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |


[Clique aqui para ver as próximas entradas](README22.md)
