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
| bf1858c1-f82b-3a30-a283-7ea7cf308239 | -9.48549 | -40.33911 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 08467ab7-03d9-3dd7-a5a3-46215acb433c | -9.46799 | -40.33674 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 0094e0a4-1402-3621-854f-c1f2f8ba0956 | -9.47137 | -40.3373 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6df8b1f0-39d4-3d13-bb8b-cc41ed166366 | -9.47183 | -40.35597 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 339a8f7d-888a-3b0f-8964-85c9cd793d43 | -12.26196 | -50.74 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3bff7e7-7747-3af9-8a4f-7d7c19f8900a | -8.34446 | -44.15215 | 2026-09-26 04:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90a04026-26ec-3981-8061-a02596841543 | -7.41 | -42.63087 | 2026-09-26 04:08:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 20c349ad-3ddc-375c-9c22-07d8d5faceb9 | -12.41237 | -40.92036 | 2026-09-26 04:08:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 64e958d6-1ffa-39a2-9628-daab36fa6003 | -9.48209 | -40.33534 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6afeda80-90c1-35e0-b61b-a50bfcabfd34 | -7.35515 | -42.08863 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6d114570-b7a7-38f5-8000-de1fe54d6e11 | -9.48268 | -40.33172 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c293047f-6219-377d-8b83-b2f115ee8855 | -11.87853 | -50.56971 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eef58737-563c-38a4-be43-e6c0ed80df92 | -9.47124 | -40.35959 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 2f901934-6ed3-3367-aa6b-47593dcac10b | -9.46299 | -40.32476 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 2b1fb012-fcff-34cd-a289-2960e7590cf3 | -12.26557 | -50.72235 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 96f37fdc-4208-36c1-b47a-9a350edd516f | -12.07276 | -42.21822 | 2026-09-26 04:08:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| daf6ebeb-1996-32d8-9feb-1ed4f7412e4a | -9.46741 | -40.34036 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32128dd2-2a52-3a47-8120-bb667ad3b448 | -7.24399 | -45.26244 | 2026-09-26 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 951a9fb3-4bd1-3156-b1e7-3322482191c0 | -7.4007 | -39.79102 | 2026-09-26 04:08:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0625d345-0d21-378c-b253-05287937e352 | -9.48668 | -40.33186 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58580da4-3c82-3ae5-b806-38804de662b6 | -11.93141 | -38.29817 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 0d275a98-69c2-3a34-8452-46a3095064a6 | -11.85504 | -50.54844 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92cfe054-9a95-3e25-9d97-8fb6e14efe77 | -7.40237 | -42.62963 | 2026-09-26 04:08:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 100051dd-cad4-388e-996f-aa00d212a518 | -9.47521 | -40.35652 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 2c544087-6bc4-389f-b90a-e7d6071f25df | -12.13578 | -50.30595 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56b969d6-5f6e-31b5-9372-dc227ec451f7 | -8.34859 | -44.15287 | 2026-09-26 04:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cbc4383-3436-3bb0-aa5f-daad611f030e | -11.90633 | -50.58472 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef3c2057-1d1a-38e4-888e-f847b41af27e | -12.34842 | -48.19516 | 2026-09-26 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 454de349-03ff-3275-b841-0fe0b3a3dbd1 | -7.34926 | -42.08948 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e70f07fa-83e9-3743-b024-7c6c9ffba8db | -7.23764 | -37.74911 | 2026-09-26 04:08:00 | NPP-375D | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 286a1ec0-e86d-3cf9-ac54-98020f8ca98e | -8.75876 | -44.90009 | 2026-09-26 04:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45abde15-6b04-3f7a-8bd7-f36d08882790 | -6.83695 | -43.50776 | 2026-09-26 04:08:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cca9f94d-fb98-3de6-9c5c-eb7977f26865 | -8.51734 | -40.23096 | 2026-09-26 04:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ebd20f38-cb23-37bf-95bd-630d4e381756 | -11.89538 | -50.57784 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6906ca12-be33-3bea-ac74-7f11693adbd3 | -11.76143 | -50.63721 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0350730-dad0-3b27-ac08-de3a78b7a3ac | -8.11641 | -40.7476 | 2026-09-26 04:08:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e92604a9-b1d6-31c6-9958-653dc13a18f6 | -11.76878 | -50.64029 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77b3c0ec-f156-3575-b5bf-b925a91abbee | -7.40128 | -39.78742 | 2026-09-26 04:08:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 09bf3d2a-5d85-3cc4-9931-e9c6820a0aa1 | -7.36626 | -42.09047 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 760ddf3a-b7c6-38df-b3dd-26add76d1c40 | -9.47241 | -40.35234 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fdbd5e6e-b05f-3cb4-b7b0-8d8748310f19 | -11.94268 | -38.29247 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4650776d-3b2c-3b15-b4ee-fe4c2d1e3ee6 | -12.26501 | -50.7428 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1ee305f-f760-3478-80e4-efe8b4220021 | -11.75778 | -50.63336 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e21da36-fcf0-320c-8ba9-f27d321f21a7 | -11.85418 | -50.55279 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0f08f89-e260-3c58-b842-a7561a8ff2a4 | -11.9359 | -50.59098 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9af37f3c-8321-3681-a359-5d5953685193 | -6.98343 | -45.06289 | 2026-09-26 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbda4c15-c28d-3e6f-8a5f-a02db5f4dfb3 | -9.47988 | -40.32755 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 59dc1125-fa06-30ad-a092-78d906ec482f | -7.71106 | -34.90687 | 2026-09-26 04:08:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 91146718-fcfe-3c53-b9a8-8b6b5db87786 | -12.26789 | -50.74124 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77b056b3-6684-3f32-9a19-806825141db0 | -12.26344 | -50.7194 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e20be3ad-8443-3fd1-9f3c-d18474635ec0 | -7.36996 | -42.09108 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99c3ba17-ebbc-37ed-8fd0-2192eb553298 | -12.64956 | -43.16391 | 2026-09-26 04:08:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35265c18-f7cd-306a-bc26-ed0a0a73de04 | -11.91049 | -50.59473 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 434ed297-4bc1-39b0-90bf-d88fcc5d8b12 | -9.47312 | -40.32643 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 193.4 |
| 5986ea74-8877-3888-b18b-3978c90653df | -11.92494 | -50.58409 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5a90dd0-ebf5-3ab9-a5fa-9412b9fa0b5a | -11.8945 | -50.58221 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26623259-8e0e-3f4b-bcab-a09b66e710e6 | -9.4793 | -40.33116 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4ce669db-cc2e-305b-a73d-b7334dbe73d7 | -11.85253 | -50.54607 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2140b7f-c029-3205-a415-85b185ab7bd3 | -11.7908 | -50.65419 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a2e5423-dbaf-313f-ae94-d37f4582bddc | -12.13659 | -50.30179 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3921cae-32a6-3ed0-94d1-479d80f6cfbd | -9.48608 | -40.33548 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a9782b9-afb4-3541-819b-70e93648f0c2 | -7.3559 | -42.08424 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 66634af0-8269-3d24-8022-3ef611f369a5 | -11.84827 | -50.55154 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f9d020f-f004-3289-8fca-caa218ab1013 | -9.4624 | -40.32838 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| e0968ad4-f040-32b9-a380-31c6de159144 | -13.06684 | -43.2811 | 2026-09-26 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8b78be2a-4dfd-3acc-9853-041dfa61c498 | -12.02464 | -50.65269 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3b0fd16-e362-309e-8d47-0ef630e0f615 | -9.46461 | -40.33618 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| cd7a12be-9beb-3174-8033-120e65e7df56 | -11.93479 | -38.2987 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 99cf5ec8-0093-3d30-995a-c6e87cae5437 | -11.92232 | -50.59724 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30a924b1-a239-3c51-be53-98b61dea8b30 | -9.46916 | -40.32949 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 193.4 |
| 1c981ee2-7c6e-38bd-b0aa-0d4cf2ede990 | -11.85933 | -50.54294 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e4c61b3-c391-3732-8bca-4380372d5d84 | -12.03649 | -50.65522 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 177f3bdb-a226-3ee0-8924-9762c4b152d2 | -8.15143 | -44.44407 | 2026-09-26 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e2f97c3-a042-38c6-bb3e-ec79ed8a256b | -12.26488 | -50.34463 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7d62af4-a871-3a23-a026-3b435d730265 | -11.95001 | -38.28987 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| becca3e2-9465-3788-b821-7053107577df | -9.4652 | -40.33256 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| ffe5811b-296a-3a28-b9eb-1a1bb668a620 | -8.15077 | -44.44795 | 2026-09-26 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aee1398b-b46e-38d5-9608-44348d67bb16 | -11.93535 | -38.29506 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 470d00c7-e7ff-35ea-99da-0a78a069e29f | -13.40598 | -43.89505 | 2026-09-26 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1e32182-e239-359c-ba7d-fec7976f93ce | -9.47358 | -40.34509 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 82e2f5c6-93bb-3143-b0be-560b3b0b17ef | -9.473 | -40.34872 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c2dc2651-6849-3cd9-a0aa-63fdf5b311fb | -9.46578 | -40.32894 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 9791eff2-30e5-34a5-9043-e9421843e394 | -8.11987 | -40.74813 | 2026-09-26 04:08:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 976eddb1-2b6a-3e5a-ad31-df619ed58713 | -12.26762 | -50.72952 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f170c3ab-4143-308d-a0f2-a484acb23a4c | -11.85747 | -50.859 | 2026-09-26 04:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fafa6b5-4f0d-3a7c-ab64-ba088f1b11e2 | -6.84161 | -43.50491 | 2026-09-26 04:08:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65655313-1e16-3826-b6f8-c9f2363ec9f2 | -12.26647 | -50.71793 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 242307f4-c166-3ebf-9790-2902a28a888d | -13.21567 | -42.36152 | 2026-09-26 04:08:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ac2de2b-b12c-3d65-a230-9e953b7207af | -12.13622 | -50.30004 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 609be34e-c591-3e06-b149-d9ea7ccaf6e9 | -9.46858 | -40.33312 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 7fef95a7-8ed8-36a0-b8a1-b1248a0c2554 | -6.31869 | -45.80745 | 2026-09-26 04:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48bd98ae-9ac9-33c7-a4eb-60d7d7747865 | -13.46747 | -41.6049 | 2026-09-26 04:08:00 | NPP-375D | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 41c15d80-40ed-302f-9813-2477ff362e3f | -11.93986 | -38.2883 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2f9f85a7-53e7-3846-844a-af40a1e5d0fc | -9.4843 | -40.34314 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b85fe091-c07c-337a-9b7a-aea37547494e | -14.8708 | -47.1349 | 2026-09-26 04:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 69b119c2-6e74-3791-962f-3f062385b586 | -12.9457 | -51.0695 | 2026-09-26 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c4074505-43fc-3b51-ab42-d2c6a5733a71 | -14.83379 | -43.30532 | 2026-09-26 04:10:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7987166-421f-39f0-a34c-5c7e33b4b5d8 | -15.24297 | -43.27507 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 4657f9aa-e94c-31cd-b723-48bf7f67df13 | -15.23726 | -43.26549 | 2026-09-26 04:10:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| edf775a7-c8e4-3be0-84d0-bf1ff5063628 | -12.94063 | -51.06413 | 2026-09-26 04:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README11.md)
