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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb74490b-7eb2-3e5f-bcd5-570419416034 | -11.88043 | -45.82235 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a81dad7-8205-3e57-bfbb-465d3d8e32c8 | -11.49504 | -50.32746 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55409524-883b-3a02-92c4-7539cb9ff2d1 | -7.9729 | -44.28019 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaac64db-1824-3df1-a81a-d993926d7559 | -12.08927 | -44.98006 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18100a96-2b10-35e6-a09e-33ae93363b09 | -7.3445 | -55.18748 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b78b646a-45af-3772-9d8c-62e2afc9eed5 | -7.35116 | -55.18576 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1ad51c9-be09-321e-b1cc-bcd04be45888 | -7.0402 | -42.19796 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 580bf1b8-b4cd-340c-9564-c2ce4b83e5e9 | -8.74721 | -46.45324 | 2026-08-31 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b37d3321-d319-3dff-9cb1-f392689d879f | -7.92137 | -44.24832 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b98185c-3cec-352d-8621-f18f5ae9148d | -11.20084 | -43.37654 | 2026-08-31 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 094630ff-6a73-3fa3-bff9-c70229c3c480 | -9.18685 | -51.55524 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 411eb0f8-483f-3bd3-906a-6f45ea5c4fc9 | -10.15455 | -45.73952 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a65a8e46-be13-3400-a0aa-c8d4fc01238e | -7.2173 | -42.74872 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 633bc8c6-134c-34cd-b91c-3c67a6e1d3e6 | -7.11579 | -42.19224 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 241b3539-5ceb-344b-b645-7e5abbe5cc43 | -12.09801 | -45.05534 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 553882b3-ebd6-30d3-b551-d572b4337874 | -10.15544 | -45.72113 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47adcaf1-a692-30cf-8e11-3e16a7d77b0d | -7.91604 | -44.2591 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4141bf90-944e-38b7-9333-d63cf9d08e33 | -9.43061 | -45.67819 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2cb0c85-82e0-301d-86b0-2abc5e6cb273 | -11.36547 | -45.19435 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 235a101d-1582-3e82-a244-11a7939093bf | -8.087 | -45.46071 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fab497f-abd4-3857-8c22-2b6b8121139d | -7.78585 | -44.0713 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9685ece5-c1d6-3ad1-807e-c274d6cd1436 | -10.77572 | -50.85303 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 221a5fc7-8b4c-3e84-a42c-36da57ae58b9 | -9.41978 | -45.67613 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63ee3e5a-819d-3a15-baf1-49d8f7c50cc2 | -7.92772 | -44.29595 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d96443a-07a7-3c81-a396-5081e103a089 | -10.79871 | -50.65131 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 569a17dc-8b25-37c9-9798-a9055684aebe | -11.21042 | -45.11835 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2b04f5e-47f4-3428-856e-13e3dc410208 | -6.30321 | -44.61123 | 2026-08-31 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71ab3c5f-5a6b-3318-b360-9db37198972c | -11.68114 | -47.60381 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa65d882-1fbe-3eaf-a13b-2644e9f261b0 | -11.19423 | -45.04417 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3569925b-cd2c-385a-a949-4022b92a97b5 | -12.11261 | -45.03085 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b23a2fb-6b9a-38b4-8ba5-fda63a67da7c | -10.99194 | -49.69195 | 2026-08-31 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31f0dfab-d203-36f0-a386-428f74391f01 | -7.3115 | -43.00989 | 2026-08-31 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0197944a-df81-3200-87b9-edb4c13a83c4 | -10.73351 | -47.96583 | 2026-08-31 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8fd50af-0af9-300b-a698-0f163a1175b4 | -11.21426 | -45.09507 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ebff96da-fff1-3e6a-8772-3fb31d2c101d | -10.81605 | -50.6659 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5837c4a5-e23f-3a12-a96e-a1603bc28ec6 | -11.34706 | -45.21898 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58f04d4f-cd44-3620-b2a0-fa0d9a2c17df | -11.33112 | -45.19696 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0bbf64f-a504-3d60-b657-fe3f03aeb1aa | -10.85272 | -45.37348 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 390aa623-8d33-3f9c-8f87-f1e94690f5f2 | -6.38267 | -45.45964 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1a5cbc0-6d7c-30be-82d6-f775e9635c2b | -11.91553 | -45.05216 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7479999b-8904-3756-8bf2-d13df689b294 | -8.3771 | -45.00007 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb3ede32-5608-37b0-9785-041c5a5c7b79 | -10.57153 | -50.36494 | 2026-08-31 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba73e188-8e53-3017-99bc-b532e72d543c | -10.74468 | -54.04197 | 2026-08-31 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 024fb8ef-a11e-3c17-b8cd-13b376237f5b | -6.77589 | -55.64368 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| baad7a2a-e0f4-3c0a-8902-c4875754a201 | -7.92012 | -44.25589 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15f5ac2c-b065-382c-b5d2-381884e19d60 | -11.78755 | -47.66336 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2654cd32-6263-3e67-8ec9-8062e2fb15e6 | -6.30256 | -44.61528 | 2026-08-31 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6312114-d1aa-3247-a89c-a85abe9c7b82 | -10.15381 | -45.74405 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38b8b25e-3991-3973-a33f-3c493b4ca77e | -11.33293 | -45.19679 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64e939d7-014c-3a5e-8d77-3f5554f04cfd | -6.77465 | -55.6504 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5cf4d45-fab9-30d6-a66e-a85a918d8d5e | -9.80373 | -46.45144 | 2026-08-31 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc4bc726-e8ef-35b4-a77e-d7120640a9fa | -12.21513 | -38.73719 | 2026-08-31 04:14:00 | NOAA-20 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3f4c7484-299f-3d10-961a-cebc642711ed | -9.43636 | -45.66618 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8280da08-ee01-3c01-be00-3bfa408f19d6 | -7.09482 | -45.77682 | 2026-08-31 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88835375-3ca4-317a-a58c-09ae54800cf6 | -7.93173 | -44.25002 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4c2a529-438a-39e3-8a36-61a8d6ac72a7 | -11.37396 | -45.20765 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da328076-379b-38fb-ba76-f5da185ca0fa | -10.1507 | -45.69566 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 501de115-cefc-3176-8d63-d81ee0b2bae3 | -10.73697 | -47.97008 | 2026-08-31 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 378e0d94-d1fe-3464-b663-f94b1520a503 | -9.5797 | -47.60606 | 2026-08-31 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0da4669-39b2-3bab-87fb-f91af5653cbd | -6.43142 | -41.53728 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ad45a53-0fa0-3e42-8ded-17a2c5409156 | -5.60544 | -43.99877 | 2026-08-31 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f9650a4-6230-313b-b259-0ae2a91ee621 | -11.34206 | -45.20622 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a930dc77-7e20-3f68-84ec-cec4a9c38396 | -7.22283 | -42.75681 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43c085d2-1195-38ef-bc6a-dfc37f4b30eb | -10.54477 | -46.20932 | 2026-08-31 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d21434e-b3bd-320d-bfa4-b16bcf5a3811 | -9.6678 | -47.93536 | 2026-08-31 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa2f4fdb-5bea-39cd-9cd0-37c0b5dd4817 | -6.87159 | -41.65311 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28373381-cec0-37e4-ab1e-cc801176099d | -10.73876 | -47.9597 | 2026-08-31 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ac6948e-aa86-35c6-ace0-a30e26b55cd8 | -11.68891 | -47.6055 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de921add-7b78-3276-9899-4c5e42177938 | -11.19077 | -45.04361 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f6fcb3f-879d-3da4-a942-df4fb941d689 | -11.21929 | -45.10774 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d740d58-447f-3209-ae78-443ec6729e12 | -7.11864 | -48.0616 | 2026-08-31 04:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6fbfca2-3c88-3035-94fb-907af590151c | -12.09396 | -45.05847 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c75e64c-29df-3f99-8668-d85436fc926a | -11.35811 | -45.217 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9381471c-ca25-3fca-90aa-5dc2fa0dddca | -10.13924 | -45.72024 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42befa66-a286-3fbb-8ce2-35408e827a29 | -11.51376 | -46.94667 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75db8715-27c7-35d6-b3ad-95d551a23bee | -7.21392 | -42.7698 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6396ad5b-d220-303b-99d9-1cb9415db27f | -7.92019 | -44.29856 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4028b846-e12c-38a0-9a7f-0539e85edd8d | -11.36635 | -45.21043 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6a11b0f-9fd1-3782-8d2f-7f78efdf2048 | -11.22101 | -45.36366 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2023540-f0a1-3872-9d76-2362a6c5b6b7 | -11.88428 | -45.81799 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8854d9d0-b51f-3ef1-970e-c4034e0b63ea | -10.81222 | -50.65954 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eecc9c93-9fcf-3f5b-a7ea-d6240f5de08c | -8.15216 | -45.47458 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a075275d-d4a4-3b26-8f1e-b828ba83871e | -10.75009 | -44.88426 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 855939fa-2621-37d7-86db-51912d975037 | -10.15473 | -45.72532 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c704c49e-0674-35da-8714-3b857e1d533c | -11.37331 | -45.21152 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bb1c17d-79a6-34a1-850f-a3660ad33de0 | -7.16753 | -44.68731 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49194da9-6e5c-3b2e-a74c-cdc41f06a8b2 | -12.39415 | -46.45266 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f799cc4c-9af8-35b4-a4dd-af0d3a665da3 | -9.58375 | -47.60678 | 2026-08-31 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96a5dcf7-9929-323f-bfae-04d384410dbe | -10.1471 | -45.69506 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd30f1dc-df47-3e05-8a3b-8321b5630d92 | -8.13318 | -45.49819 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9623cc0c-8169-3e5d-9880-73e3c3f54d65 | -5.73069 | -49.13381 | 2026-08-31 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e9751f4-c678-340f-9ba5-38922c3c2c9f | -11.19386 | -45.06784 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fa43512-c36f-3f29-bd8a-4f9b134b0f48 | -11.3364 | -45.19741 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fecfa59-37ea-3f74-ac79-512aedd64da5 | -11.36093 | -45.22147 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd00e552-0396-37b2-9ef8-6fe6f71b8775 | -11.2259 | -45.08919 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 004d536c-a0ac-3ac3-b09c-35e9244d0394 | -7.10895 | -42.76705 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fd8856a8-cbe2-3c81-9a3f-8142f7651fda | -11.33238 | -45.1893 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81efda81-f834-3f2c-ac22-381c1f9e4fe1 | -7.28782 | -44.52592 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1abcb2f5-3a09-38eb-b821-324dad069720 | -11.88005 | -45.82143 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f032afd-9705-3628-bd3d-4651c43998ae | -11.36789 | -45.22258 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README31.md)
