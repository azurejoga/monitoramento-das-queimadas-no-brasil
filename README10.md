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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3faf52df-2872-3087-9d00-d6419c4fdcd8 | -11.2316 | -54.85347 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0719f48-e729-3c1e-81b3-ce334174dc60 | -6.5429 | -55.16807 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be937b17-2e63-3feb-8709-7da8236cf32d | -11.24695 | -54.83593 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1023e70-4a23-3af0-890d-850437222196 | -11.12232 | -50.4011 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b8be517-b461-36b4-9388-7d6544cb2369 | -11.23728 | -54.8548 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94e88781-1eaf-3873-83f0-607e2041d428 | -9.93242 | -53.33121 | 2026-08-04 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8753952-9a1a-3b21-8715-c60d637e1450 | -8.72766 | -48.32425 | 2026-08-04 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7f6ca3c-9b5d-3856-8e38-7dcdb6bcc741 | -11.20205 | -54.8782 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 340df1df-cd35-365e-b644-baf7901d9f7b | -8.34707 | -45.98564 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdb8e3ef-942d-3a9b-9235-7052ae9a493d | -6.56075 | -55.15835 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db38f22f-fe62-3b91-ae46-13cd14bfe9c4 | -11.21214 | -54.86172 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29b241b1-7130-37a2-b879-e4132f3ca354 | -9.07697 | -46.04815 | 2026-08-04 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 709bebca-9859-3337-9c78-1621fd030fae | -9.4722 | -48.87081 | 2026-08-04 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a72549d4-f7d4-3ae4-8751-8e3b02666d56 | -11.20365 | -54.86994 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b82ba9f3-0bd3-3288-b412-eab827a51cbe | -12.43716 | -44.3172 | 2026-08-04 04:19:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c291662-507b-3d53-bd71-1edf44e50970 | -11.21293 | -54.85773 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66021ee5-03b2-34c5-a6f9-ecb013e1e281 | -7.39201 | -45.05772 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80749997-3a65-3ae8-b510-a56dd51903d3 | -6.5483 | -55.1743 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28d848a6-3083-3a90-a16f-64a8c41fea60 | -13.33536 | -44.67344 | 2026-08-04 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9d540c9f-36e9-33c9-9389-fd6e2c3a2eae | -7.91667 | -44.9199 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b681b35-a8a8-30cf-a919-33dc10f43782 | -10.64152 | -46.76925 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 69ad5e82-8011-346d-bb99-3c004789640a | -12.03705 | -47.65852 | 2026-08-04 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b017acc2-37bd-3e5e-8c3e-de99eb085e99 | -6.5525 | -55.16762 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18524f6a-f87e-37b1-a75f-8f55040438fe | -6.55787 | -55.17384 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cd4ec04-1822-3807-a792-17a9560bd0b5 | -7.83101 | -47.1058 | 2026-08-04 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f280efc-3614-37ea-be3f-465af1ba4fb8 | -6.57142 | -55.17108 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff192156-09bc-3295-86b8-e36d08399886 | -11.69924 | -50.31164 | 2026-08-04 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ebd01d3-7797-3552-8c40-98a8eaa14388 | -11.20522 | -54.8618 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd18c081-5584-3425-886f-6a5da2fec564 | -6.89184 | -42.84121 | 2026-08-04 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3fc81e22-10a9-389a-bde7-7acf3e10654b | -6.5472 | -55.16113 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2624e985-f901-3655-9953-aca52c89f0f7 | -11.20409 | -54.83689 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54cada05-e7c6-3789-a7ad-367cbe642828 | -8.354 | -45.98678 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b4b0c970-ce28-3582-9263-a694c97a065d | -11.75716 | -50.28128 | 2026-08-04 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 389942d1-1b17-39a2-ae72-ebd29cfb4e86 | -11.25342 | -54.8332 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fb2dd20-c7fe-3149-bd61-c2786c0874a2 | -12.44047 | -44.31774 | 2026-08-04 04:19:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9280c674-6867-3f09-a9e5-9ab5eca8108b | -8.92626 | -45.21114 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c60e781-38e6-3d83-8ce1-51a22c11339c | -6.55551 | -55.1704 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51548b8f-380e-316c-8b18-561d4817f04e | -8.27815 | -47.54952 | 2026-08-04 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e188cd4-1932-3a1e-af4a-29f4beb431a6 | -8.34991 | -45.99006 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dd52be1-3715-33b5-a0c3-c824efdae104 | -6.55882 | -55.1687 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57a9b105-d53d-34be-be48-498f290864f5 | -7.91216 | -44.92653 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d78191fe-3fb9-3443-adab-45ebe75fec97 | -6.9616 | -52.82494 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 726be473-0593-312f-888a-91598026fd17 | -6.57428 | -55.15562 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6d825d8-b848-3a94-bf6b-b46412e17ba0 | -9.47308 | -48.86567 | 2026-08-04 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22e99c75-ebdd-3778-80ae-ca0e814c13ff | -6.5637 | -55.16106 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efaa8b87-42c9-3af8-a3bb-d254df158bb4 | -11.19948 | -54.86077 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e4168e1-7a9f-385a-b426-5574856e6e21 | -8.35626 | -45.98674 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 93fc3c93-9509-3f0d-94cb-992478cb30c6 | -8.3544 | -45.9897 | 2026-08-04 04:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 80ca4217-1fec-335e-ba4d-6b2609154112 | -11.2213 | -54.855 | 2026-08-04 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1f9e28de-c6ff-3fee-aed1-4a387bf0b358 | -8.3546 | -45.9671 | 2026-08-04 04:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| b4e22489-914b-32f1-9fd2-391368192ff9 | -17.98176 | -47.16218 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84251451-5a29-305c-a44f-8d89070568c0 | -17.95688 | -47.15398 | 2026-08-04 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dbb100f9-638a-3d22-9dc0-5895ea6202d9 | -17.95896 | -47.15422 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4f5e5759-2bb7-3cb8-a344-88a3cdbfb136 | -17.96472 | -47.14017 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01f5914f-47cf-3b1b-ba1b-1fd9b678274b | -21.41863 | -44.0909 | 2026-08-04 04:21:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c1553526-98dc-3199-a2e6-490d55d846bf | -19.58014 | -43.95868 | 2026-08-04 04:21:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 418c3c28-714d-3565-927d-633130947ad7 | -17.97841 | -47.16157 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47cfd891-f0f3-38dc-b50c-e022d5d6d171 | -17.98389 | -47.1701 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a8231cf-c76b-3277-a16c-ba159dca6a0f | -14.26524 | -45.25845 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8f46237-0263-3dc7-8e26-dad132fc8b08 | -14.25807 | -45.26088 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 493fbf16-5a3a-33ee-91ff-0e3d49b20b69 | -17.95748 | -47.15031 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ea407bc-7684-3839-86df-5ac11acb52ec | -17.97568 | -47.15728 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d9f5258-9c57-3fb7-be74-ec61edd5c55f | -14.71861 | -47.14565 | 2026-08-04 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 367c783c-5070-3e7d-9862-b2ac969d7c49 | -14.26081 | -45.26498 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b8e6e1b-76d8-361b-b307-394624057ad3 | -16.22526 | -45.49389 | 2026-08-04 04:21:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cc7c530-aa04-3f60-b4b5-bcf73c484d4f | -17.97507 | -47.16094 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f9363b9-563a-3541-89dc-104ca41a6158 | -14.2575 | -45.26443 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b67ce973-6c42-3794-9992-c8a377bddf24 | -14.26194 | -45.2579 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0847d7b4-cf19-347a-aaae-b95486cf4e0f | -21.0708 | -49.21931 | 2026-08-04 04:21:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 709ab5be-e1e5-3b15-b07e-4386b8886685 | -16.52836 | -49.2207 | 2026-08-04 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| af2de0d9-6121-3651-a93c-e8f3c599ce3c | -19.17017 | -46.58585 | 2026-08-04 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07e60122-d787-323e-9863-adc42c4e6338 | -20.52909 | -43.2869 | 2026-08-04 04:21:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a444e018-5ec2-342b-a377-1bab1f6dd74c | -16.72158 | -49.40256 | 2026-08-04 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e0a5b77-6da1-3dfa-a1f1-2bf89a06e622 | -16.53201 | -49.2214 | 2026-08-04 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a6fd429-2bea-3220-b56d-c598f33b8ef8 | -19.49727 | -44.80643 | 2026-08-04 04:21:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e61a881b-cf08-3dcf-bf09-d89ba395b533 | -15.65857 | -43.32043 | 2026-08-04 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ebb0cd6a-4d6f-36a1-ae67-a7ceb9c3f4b8 | -21.23485 | -43.83506 | 2026-08-04 04:21:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 93bb7bb5-71ba-32d3-b181-ee9bf9179fd2 | -21.67311 | -43.60758 | 2026-08-04 04:21:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73e25246-a2d4-33e8-bf21-8666b090d31b | -14.25863 | -45.25734 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04017bf7-3483-3576-8b8d-41468740bd59 | -14.26412 | -45.26553 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 207ad939-fba0-379f-a78e-faa2377472e7 | -21.03456 | -45.51471 | 2026-08-04 04:21:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b1301da-4217-3bb7-839e-9239cd35d23b | -14.26355 | -45.26908 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e30f4ec-1672-387c-9d5c-c9e66287e09b | -20.99153 | -42.83712 | 2026-08-04 04:21:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 840f086a-aea5-3814-a125-e8aefe957b2c | -19.52675 | -46.90364 | 2026-08-04 04:21:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 226346b5-759e-3f25-9ad4-4b14625f82a4 | -21.67372 | -43.60315 | 2026-08-04 04:21:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bae669f2-e910-320f-a5d2-980f65866885 | -15.04428 | -41.99275 | 2026-08-04 04:21:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0528038c-895d-372f-8a3d-195024dcf9da | -16.22195 | -45.49333 | 2026-08-04 04:21:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5c795ee-a3ad-3aa6-ad6a-9df25aaa17c5 | -20.31644 | -42.00517 | 2026-08-04 04:21:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 997757ae-6df6-31bc-acc2-af6044f7a0ea | -20.99006 | -42.83436 | 2026-08-04 04:21:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0b992309-302f-3660-aac4-bc8b890f9840 | -17.95808 | -47.14664 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e8b4527-711d-38b5-94ce-721fbda682a5 | -15.658 | -43.3243 | 2026-08-04 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24cef396-2ef6-3b0e-9a35-7ed979d8ae6d | -17.95868 | -47.14299 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c27d06c1-c4ba-3d4e-a431-e09b14bc2de8 | -17.99455 | -47.16817 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3107bcf0-78b6-3a06-ae56-9aad12b0c4ca | -18.95643 | -43.17402 | 2026-08-04 04:21:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6ce13917-c8cb-3656-ba50-2fb224b76485 | -17.95957 | -47.15053 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d331deb7-f092-31d6-8dd7-87698603b6da | -20.98781 | -42.83656 | 2026-08-04 04:21:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36b5be91-7857-3006-8128-47490307a979 | -14.26468 | -45.26199 | 2026-08-04 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c207c87-2971-39ba-8ddf-b60c861d27a1 | -17.87222 | -40.05349 | 2026-08-04 04:21:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b1f9dfdb-6f6a-3db9-afdb-1fd5d61651f5 | -20.50774 | -41.67046 | 2026-08-04 04:21:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6c8eaac2-0338-3510-942a-7dcf812aa120 | -17.98055 | -47.16952 | 2026-08-04 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README11.md)
