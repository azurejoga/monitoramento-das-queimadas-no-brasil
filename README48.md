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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a1897b0-ff7e-3237-9dc2-de097c504cdb | -21.43458 | -54.14135 | 2025-10-15 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e29279d-7f1e-330e-968f-6ab70c1c43fa | -19.48555 | -54.93355 | 2025-10-15 05:01:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39e324d7-a714-3aac-b59b-926f4f8eb7b2 | -20.56067 | -54.65775 | 2025-10-15 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca94c581-3d74-30fb-8387-69f36713743c | -27.75175 | -50.40169 | 2025-10-15 05:04:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| b0b1cc79-9339-3a91-a4fe-072c7ad2eb88 | -27.75115 | -50.408 | 2025-10-15 05:04:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 486455e2-57af-326b-9b10-40fab3894cf0 | -27.75287 | -50.40134 | 2025-10-15 05:04:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e7d73c33-043f-3ea1-bcfe-6e9cc17eba4b | -27.74735 | -50.40728 | 2025-10-15 05:04:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4edc2316-47cf-31d8-bdc6-58323a0f0814 | -30.61399 | -52.39149 | 2025-10-15 05:04:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| e724c656-f91e-3f29-ab29-8d7a69fd4dcd | -27.7479 | -50.401 | 2025-10-15 05:04:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8026c696-da63-3044-83a0-827962870272 | -27.75232 | -50.40762 | 2025-10-15 05:04:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a8a5e3fa-2fe8-3ce0-8ff6-4d0e4518f3a8 | -2.8147 | -49.1993 | 2025-10-15 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 8a2ce690-4ebf-3533-8fd4-21633fd2f651 | 1.85547 | -55.73361 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 403dbade-41a6-33e2-81f8-cb43d5334d4c | 1.3089 | -50.71876 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf654101-429b-32fc-a3e3-0fb7abe37778 | 1.77965 | -55.76652 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00453c77-6c00-3054-a10b-bd5433f8b784 | 1.7583 | -55.7812 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af5a28ef-819a-3c5a-9201-bd18c918b1a9 | 1.86112 | -55.69911 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09f1b6a6-0a6e-3198-88a0-d00ef80f872e | 1.87617 | -55.67305 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0822ceac-c7a7-302a-9186-cfdb903a3240 | 1.07811 | -51.21778 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da848be0-2b04-3d16-9ca0-365b27c44ee2 | 1.33487 | -50.72043 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c446f6e9-abcc-3219-948c-51061c80c002 | 1.0096 | -51.08606 | 2025-10-15 05:23:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 997c911e-fa2f-387e-9a9e-b0d7f9615b84 | 1.85854 | -55.70107 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a94dd5c1-f313-35b3-9bdd-ab1e48ae0b22 | 1.75137 | -55.80732 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9ba2312-aca4-3aaa-8d84-aa40ab9720f3 | 1.85611 | -55.7377 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e685702-1e39-32e1-9091-03f25ae151ac | 1.30983 | -50.72449 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5f0eb3fd-74d3-3f74-848d-dfd8b430fc29 | 1.81067 | -55.75323 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 335f6c94-fc02-3141-83bf-64e475e322e7 | 2.04805 | -55.83895 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72ff85dc-9370-3ea3-95cb-cdddf384255c | 1.07882 | -51.03451 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51ae677e-a52d-3682-8e25-bbf57761b47a | 1.81618 | -55.85658 | 2025-10-15 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6679acb7-e5d7-3cf1-bdc4-b24a5545ebcc | -0.90179 | -47.55467 | 2025-10-15 05:23:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 00b4fc7c-8ba5-3946-b3f1-a69973c14164 | 1.78617 | -55.76127 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933d65d6-6de2-3e67-ac79-2f9689e39999 | 1.32986 | -50.72125 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 096d6370-7bf4-38f2-a4bf-1878901ae483 | 1.33671 | -50.73186 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9448bd0-c26e-3281-a00f-49cae75afe24 | 1.86176 | -55.70321 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 662bef0a-685b-3b18-8306-94bd9cc4b53e | 1.00638 | -51.0854 | 2025-10-15 05:23:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b207be0-be18-3103-85b3-7253ae623c07 | 1.85842 | -55.72893 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d07ea49-c3cc-3d71-ad81-7f0a6a0ff7d0 | 1.8628 | -55.7046 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67c28000-c9b9-32d4-93b6-7226118c4e6f | 1.00875 | -51.08064 | 2025-10-15 05:23:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6c9fd92-d723-32b9-8b1c-ad8b831cdc6b | 1.33763 | -50.73756 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6391c427-988d-3647-bc52-cc2348e0310d | 1.29833 | -51.25073 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bb5afb5-4cd7-31c9-b6cc-4113ad5b81f0 | 1.88272 | -55.66781 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44ac9c56-6cb7-3849-a153-386bc0d0eb71 | 1.87684 | -55.67717 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a640e4c-e157-3fea-83d6-c0ab1adc44c7 | 1.81198 | -55.7614 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6b03651-6b9b-3f74-b62e-eee8f0a0aa9f | 1.07896 | -51.2231 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 991d26b9-6105-3ad8-9721-48384974f083 | -0.89623 | -47.54848 | 2025-10-15 05:23:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6487b3ee-8804-3f62-add2-3e680b5bc538 | 1.8588 | -55.70788 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8b1e298-c9f6-35dc-8ea6-bba8b4eb4569 | 1.0797 | -51.04 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d86298e-30af-3e46-ac0a-9d2a77378b0f | 1.8597 | -55.73711 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51610b60-dfe7-3db3-81c5-e805e81866e0 | 1.8592 | -55.70516 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ca6ef2e-6ea1-307d-9ef5-f764dbd24ac5 | 1.08288 | -51.02823 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10863674-257d-3cb3-a4c3-9cdc3b36d3a6 | 1.81133 | -55.75731 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bed8507-8da5-35f1-b6b2-2fb20c667c52 | 1.07478 | -51.04078 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d524d101-aae0-32e1-a6ef-903a4c4706ae | 1.87323 | -55.67773 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34347c85-07c4-380c-b0b3-32fd51435ad0 | 1.08113 | -51.01727 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bed1d9aa-8b9c-318b-8cd4-1986a58b409b | 1.85713 | -55.72075 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaaf5a26-c1a6-3777-9457-6e156be5c479 | 1.7754 | -55.76301 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4af2987e-15c5-3f75-916d-17be686da256 | 1.06985 | -51.04155 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79c294ef-2ffb-3781-8987-9d8f3afcd049 | 1.81683 | -55.86062 | 2025-10-15 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 956eb9fd-86c5-3191-ab14-e24a158a1826 | 1.87096 | -55.68651 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 450f25de-f273-394e-9ac4-b5730f941a46 | 1.77181 | -55.7636 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b60ea97-bcae-3c3a-a68d-5b1ed332e552 | 1.8576 | -55.71801 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfc04610-81cc-3ef4-b9f8-d398544485e1 | 1.01128 | -51.08456 | 2025-10-15 05:23:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c53ca6f2-8676-3147-a689-70d3fd0700c7 | 1.89879 | -55.65272 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52d3506c-5f02-349b-b07e-b2bc9cd5de63 | 1.85987 | -55.70925 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4158bbd-58c9-36d1-aff9-afaa753f902b | 1.86026 | -55.73435 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 135c7251-9b31-3883-9641-da39b421a449 | -0.9026 | -47.54955 | 2025-10-15 05:23:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ae98c7b7-e55b-3318-aa18-11d950926b21 | 1.79042 | -55.76479 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c985b22-84be-3936-8cb0-0af437759e16 | 1.77606 | -55.7671 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2d18640-dfe5-396b-a513-ef7d0fcafa60 | 1.08606 | -51.01645 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a422e6b8-2c79-3183-af49-8f1c620dd831 | 1.86735 | -55.68707 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31ead154-5806-3d58-951e-9186c908ce82 | 1.88982 | -55.88231 | 2025-10-15 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c906219a-5759-3777-9d77-888921b15bbc | 1.86214 | -55.7005 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32beea73-2521-3d5a-b6f1-47de838ddfe0 | 1.76008 | -55.78217 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a242a2e4-abed-3b37-8764-503ae34f4d5d | 1.85649 | -55.71665 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dab0dfd5-b636-389a-aa0c-0b1ae651a441 | 1.74779 | -55.80788 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8e8df63-4ce1-30fd-9c50-c7e1371ff019 | 1.88497 | -55.87464 | 2025-10-15 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b23bfecd-cbae-3851-8b70-e96f66b389a3 | 1.87912 | -55.66837 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 242eb577-bf48-370a-a22f-b64710fdf60a | -0.89541 | -47.55372 | 2025-10-15 05:23:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3c1dacc0-612c-36e5-b0ac-3b9efab46b44 | 1.8856 | -55.8787 | 2025-10-15 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c4684f-b81c-3781-bc7b-56a161d04fee | 1.80218 | -55.7462 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d959d205-6f7e-37c1-a332-5f6a0f1a7175 | 1.8869 | -55.87574 | 2025-10-15 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54bb4d4d-094f-30e0-82e3-4121f7cca3c2 | 1.75894 | -55.78527 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea30ecb7-dda5-3c6c-a9c6-297fe3cb8e26 | 1.89584 | -55.65735 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f642d79d-0c69-36b3-bc60-70eea6a43c02 | 1.29749 | -51.24554 | 2025-10-15 05:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16c7ce5f-8027-30b8-9f00-45c0fe9bcb57 | 1.85906 | -55.73302 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a049d57-589d-3739-af78-4f7d186b1cca | -0.89704 | -47.54332 | 2025-10-15 05:23:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60d5fb03-39c0-3a74-b94c-217a2013c593 | 1.85816 | -55.70378 | 2025-10-15 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca0415d7-9021-3f49-a427-8fc9c7304806 | -4.28167 | -48.58659 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3359e5e5-88ad-31a9-9b42-6378701f82d7 | -3.78384 | -49.42822 | 2025-10-15 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5759897e-8fd9-3cdb-b3c1-4df274d0926d | -3.42618 | -50.25657 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 219ba12f-257a-360a-9d0f-0d07a0456a46 | -2.93022 | -48.30294 | 2025-10-15 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c707b21b-26d9-3fdc-a98b-a22a1f0896d4 | -4.42393 | -47.75813 | 2025-10-15 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d0a4ed49-e6a2-3163-962f-505ecc876e79 | -3.62155 | -48.91639 | 2025-10-15 05:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cf14746-95a1-3c59-a3a8-c6e3fffe729e | -3.78321 | -49.43249 | 2025-10-15 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a027a3f7-2d18-35d8-ae24-852645a6350e | -2.87746 | -50.72947 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888dbadd-6f86-3317-9b18-87a8b23c9336 | -4.91153 | -46.7131 | 2025-10-15 05:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78aacef9-7799-3638-aef1-5423137416b8 | -2.88229 | -50.73364 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a816f49-3750-38f8-a03b-ddd4d48d0848 | -3.07571 | -49.5037 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c132f820-d95a-3881-a1ab-7ff4b43784c6 | -3.09377 | -50.37727 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c96e621-233b-3eaa-b085-e4df6a57c3dc | -2.24893 | -47.87906 | 2025-10-15 05:25:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e23718f9-0aa3-3ce7-9468-1bbabc43b677 | -2.87593 | -50.73949 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README49.md)
