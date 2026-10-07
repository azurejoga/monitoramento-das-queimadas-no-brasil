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

## Dados Diários - Página 193

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8c63b89-0ee4-3ff6-91ad-f648d0ff7a8a | -6.14487 | -52.65081 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6bc9d878-7ed4-39a4-b4f6-a2b5696dadce | -9.44583 | -45.83969 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 0173c34a-4fb0-32fb-b578-008465c596b6 | -6.92415 | -41.23624 | 2026-10-07 16:37:00 | NPP-375 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| ddfef367-5df9-3664-95ec-6497ab095cc1 | -4.7841 | -43.33472 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| ada94ae3-19ba-3807-89f5-5bd755bebac7 | -11.09804 | -47.63401 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fb24138d-e323-3dd8-9db4-adaebe1e8f03 | -4.69918 | -40.27319 | 2026-10-07 16:37:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 86a9465a-833d-3ca3-a16a-d294b989082a | -9.13439 | -45.10355 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 1904701f-bb37-3a73-80e9-b4d8752a5a5d | -4.84532 | -40.39759 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| f26baa39-df94-3249-9173-189f7ae491c5 | -11.00067 | -45.42489 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 63b14e3c-9276-3163-9e79-37aa7c7a35ad | -14.20487 | -39.38641 | 2026-10-07 16:37:00 | NPP-375 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 96240956-766e-37e3-8d2b-4e38a37ea1b1 | -10.46262 | -46.84365 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a27d23e5-8a8f-32c8-a98a-7ff3a0a7b336 | -9.31199 | -48.4933 | 2026-10-07 16:37:00 | NPP-375 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fefe1f23-5c32-3ad3-a8e0-3c5330d0f2f4 | -3.80791 | -42.22099 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 71f9dba8-832d-3543-b856-1c0847a04f14 | -3.98717 | -40.91809 | 2026-10-07 16:37:00 | NPP-375 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2c847384-07ef-3dc6-8fd9-e7df5fd31b73 | -9.14829 | -45.82333 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6e0183fe-3514-35aa-8691-169b55a9953a | -3.94295 | -42.32652 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3a3afd39-38c2-3116-96e7-1676370515d7 | -17.032 | -45.92671 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7086339-086e-3f7f-a0aa-440851802873 | -4.12028 | -41.77702 | 2026-10-07 16:37:00 | NPP-375 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| f2aaa138-048c-3cca-9745-a2503707de6c | -9.8227 | -46.24923 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f99510e2-41aa-3cb5-af22-73fa272435b9 | -10.29245 | -47.82499 | 2026-10-07 16:37:00 | NPP-375 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| df27b8a6-47a4-3780-94b8-bd5c865854f6 | -5.99837 | -53.50326 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| adf572af-b54a-3ab2-98c3-b6daf54581f7 | -6.01518 | -53.50459 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ccfed39c-4067-3776-801a-a25d05bcdafb | -8.72491 | -48.07109 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f175f22-a308-3b66-8cf3-3c6612c3f04c | -7.30257 | -37.5458 | 2026-10-07 16:37:00 | NPP-375 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5e213113-fc0b-3c84-9b42-240e1c9ea349 | -5.81398 | -53.83067 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 284fb77a-bb96-381f-8123-73fb3f416bcb | -5.08821 | -56.25637 | 2026-10-07 16:37:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86cfa3a2-0511-3a6f-a9e3-a0b2c3c00b4d | -10.97576 | -45.40092 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6287ca87-a45b-3901-9463-3d51f22e59f5 | -3.50064 | -41.94044 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 11c6c50a-e433-3912-8a0d-d69f9fc55f7d | -5.98514 | -40.93212 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 9cc95b70-d62c-39e6-b39b-e2a5888e0b23 | -3.2905 | -42.27975 | 2026-10-07 16:37:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 10e05f54-8da8-3ac1-9375-3f110bd4a754 | -4.57883 | -40.77582 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 97e4b6ab-856b-36e0-be34-1d3d67e50bf3 | -3.75071 | -41.71166 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| d57bb461-6511-3bff-8479-ed76d7ebbf03 | -6.35542 | -55.14267 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 86d8fdb3-dac6-3ae9-a519-4af4f8377ef2 | -6.44195 | -45.2144 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f5abe3d9-5ba7-3702-ab79-f37a7bcbc4e3 | -7.23442 | -49.38244 | 2026-10-07 16:37:00 | NPP-375 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9beb70c1-1a29-3cba-8b3e-34ad757a10b5 | -11.89402 | -51.67665 | 2026-10-07 16:37:00 | NPP-375 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8aed31cc-4b98-3a6c-9d75-1be4f5fc846e | -5.45364 | -45.59336 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2653660b-a935-3680-898e-27397d57b55b | -7.87485 | -54.96146 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 8e49e8d5-9d79-3793-a2f9-49be300a975f | -7.56454 | -35.33564 | 2026-10-07 16:37:00 | NPP-375 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ca7b64a2-ced3-3c54-972d-7d8beb4696a0 | -6.7248 | -55.06179 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69e37474-234a-373a-9580-99d8ce87d17e | -8.05637 | -45.61174 | 2026-10-07 16:37:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2b74e8b-a456-32fc-ad94-19248732a444 | -15.89547 | -42.85516 | 2026-10-07 16:37:00 | NPP-375 | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| d7a8edab-3230-3d39-9536-0a12d441907d | -9.86406 | -46.30635 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6bb9288f-6878-35c5-9801-fa629d8d62ee | -4.32619 | -48.63306 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 09dceaf6-1f88-31ee-8fe5-45d2b6e641a8 | -5.53132 | -44.96004 | 2026-10-07 16:37:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f676b03-875b-3b34-8a0f-0423e587c997 | -5.4979 | -42.83351 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 9846c052-1ba3-3a06-8861-af2e29c0094c | -4.55595 | -49.34937 | 2026-10-07 16:37:00 | NPP-375 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 161b90ad-db82-3547-bd85-b221838589ed | -6.31877 | -53.30862 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3c4f09c5-9922-334e-a9b7-77ef2d383a02 | -15.3971 | -41.70616 | 2026-10-07 16:37:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c4cd6b94-de18-32af-b8ec-1d78cf11d96a | -6.37935 | -45.05001 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ecb02292-62ed-35e0-8dc2-8a306ef7015f | -15.44807 | -43.9577 | 2026-10-07 16:37:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ef455971-bfa9-3a52-9508-bfe3b4f09fc5 | -5.4227 | -48.31804 | 2026-10-07 16:37:00 | NPP-375 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ded32826-ac30-3410-b167-c0cb525d504e | -5.71643 | -41.67588 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 4a7c6e06-f471-3173-b057-2a6fa2a1759e | -5.37531 | -38.28258 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| a3963c47-d219-30be-b1ad-3ef136666112 | -6.24902 | -53.4554 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 23a4f21e-8517-35ab-8f89-ade7a47cfff3 | -6.22682 | -52.84504 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7b3000b7-673d-3f98-aff9-29f0c62f495c | -7.67995 | -37.59766 | 2026-10-07 16:37:00 | NPP-375 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| fd9c78ee-a82a-3f27-b474-8fd44e2d7897 | -9.87302 | -46.30974 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d9872500-b8b2-3d54-bacd-ef6c25b46a1f | -5.25848 | -47.92688 | 2026-10-07 16:37:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| bc57ef65-c4f2-3afc-b21c-a7bdf13b4042 | -7.53414 | -45.87405 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6fcf7d34-0b2a-30fc-9ec4-8cd024a07e4d | -5.49846 | -42.83711 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 7bcaa6d2-c9ee-3d75-b69b-95eea3144f20 | -4.67911 | -40.82953 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 35.8 |
| 5916511c-164f-366c-b477-62981c594426 | -3.42047 | -41.21917 | 2026-10-07 16:37:00 | NPP-375 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c78d2d3c-b918-396b-b9ea-aecd9ce7e077 | -5.87629 | -45.97031 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c367340c-5756-3810-9252-aaf5ef59a40c | -5.73925 | -41.72851 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 26fcd01d-1fde-3b4d-980e-eef7468a0667 | -5.03401 | -42.7242 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 40b96d13-9c70-3b4e-ad47-e692b9e98081 | -15.63616 | -41.69888 | 2026-10-07 16:37:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 3eea986a-5a32-3eb9-af55-8d14c6fd7eaf | -6.17399 | -55.36326 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 480f6bfa-ce3e-3ae7-b4ac-1a9ece104507 | -8.89345 | -37.96951 | 2026-10-07 16:37:00 | NPP-375 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ecf77a4f-8ce6-334f-82a4-49ca4e9cb63a | -6.59175 | -47.40574 | 2026-10-07 16:37:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 52fb28fb-ec1f-30b1-b4db-7601b2f582f1 | -3.95985 | -42.86584 | 2026-10-07 16:37:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3a9c2a93-9bc9-338a-9fea-7370d569d936 | -11.10272 | -47.58181 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 88f2b0bd-463c-3186-a484-df603f60b129 | -7.19313 | -44.29084 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| daa801b5-c40e-3c98-8a32-aab4e431c926 | -3.92923 | -40.38496 | 2026-10-07 16:37:00 | NPP-375 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| b66b75cc-d4ad-3bcf-9e4d-01df5be36ca1 | -6.05132 | -53.48602 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 918fe77a-8072-38ca-bd5c-f8ec89708928 | -6.48264 | -52.806 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 42baadbb-52bd-31bb-928e-dc2b5efcb74a | -5.58174 | -44.25135 | 2026-10-07 16:37:00 | NPP-375 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 967eec03-dd42-327a-bd18-3656961ff604 | -6.44965 | -37.63153 | 2026-10-07 16:37:00 | NPP-375 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 26fb0c02-e8a8-3ac9-a9ea-cf6c87b56e9b | -6.42037 | -47.7116 | 2026-10-07 16:37:00 | NPP-375 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f33c150b-c843-33b0-9ae2-d826579852a4 | -3.80617 | -40.46571 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 4bded966-413b-37f6-879f-bfa5a0f4e8af | -9.51519 | -46.84298 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3cc75498-292a-3d2f-b9b2-940f4170a314 | -7.74859 | -54.94661 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| fd430384-77d4-3572-97eb-1e2c4a480ec3 | -6.3717 | -42.90726 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d1f97c5f-8ce7-3466-8bde-506ae66c9af7 | -8.55239 | -40.28624 | 2026-10-07 16:37:00 | NPP-375 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 45.3 |
| b76d6b69-3e6e-3874-8208-a27113455873 | -8.53643 | -54.59771 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e454e4a8-ac5d-3da0-bf94-89a2bf9df1c6 | -7.89889 | -54.71982 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 9e925e21-4846-3dcc-ac85-e7e40165f803 | -11.15691 | -46.11442 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 21461751-992c-3d21-8114-c8d107bc3395 | -16.67981 | -41.4743 | 2026-10-07 16:37:00 | NPP-375 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| deca6ae9-a1c2-3c81-a8a0-2c1b84fae439 | -3.77101 | -44.35122 | 2026-10-07 16:37:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 136eddc5-9cf0-3726-9bdc-a3e38322b4c3 | -3.50967 | -41.95145 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| a8217b3e-a9ea-3298-a132-77df10e4a114 | -3.74727 | -44.70141 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 847122c4-5f64-3a78-b50c-d53b895f9d15 | -4.84273 | -45.9854 | 2026-10-07 16:37:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2d8e6f90-36d5-386a-b1f2-4cffaf2cba70 | -6.02732 | -44.11343 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2f7bd469-b1c7-3cf7-9d58-1c66d499c9ce | -15.25141 | -40.99371 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3d96d049-44cd-3820-a351-7919e9a0958d | -8.60124 | -45.08043 | 2026-10-07 16:37:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 259779a0-7cf0-36c7-9926-941722777ce5 | -8.991 | -45.92633 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8183f48c-677f-3f54-bd33-1ec3929d4e5d | -3.49729 | -39.50004 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1d915f07-0838-328a-ac00-2c93617bb6a5 | -10.99593 | -45.49031 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| c9981fdb-2970-3f7d-a242-83190dbadf57 | -3.81372 | -42.21216 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 93e137f5-4f05-324b-901b-f031268ca57a | -6.75023 | -52.93163 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README194.md)
