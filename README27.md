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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fba1c360-ae41-346e-bf9c-d9753c614d6f | -20.18543 | -44.24203 | 2025-09-06 03:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 93ef025b-4171-309e-a0c8-5c5917cda7ba | -13.56527 | -48.11805 | 2025-09-06 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| baa55f49-d877-30c3-8772-00b3fec6df60 | -14.90165 | -49.45531 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| c54d8b11-56d5-3f1f-964d-e618dc119e99 | -20.30288 | -43.7094 | 2025-09-06 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9e9764e4-7e7f-37e6-9930-84f603daa8ac | -14.58215 | -48.08202 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d280fcaf-5c11-33da-b27a-ee2b3eea471b | -14.5917 | -48.09047 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ebf8cf0-a011-3ab8-b3c1-e404e8eb9b21 | -17.6939 | -44.50959 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92cc061a-1c19-384e-8f0e-601e768fd715 | -18.26736 | -43.02115 | 2025-09-06 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b7650bd6-37b1-399e-a420-7ac0d5b6359e | -15.54343 | -49.8192 | 2025-09-06 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0816bfc7-b3d5-392b-bed3-bf848abd6db8 | -18.13166 | -42.71819 | 2025-09-06 03:51:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9aef833b-337d-38da-82db-f145d7b58c16 | -13.8508 | -46.29447 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bdeb644-735b-31cd-9356-612f6845ac1b | -14.11285 | -51.717 | 2025-09-06 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18077e5c-1d0a-385d-87fa-c4b8f5d362fc | -13.85274 | -46.2645 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d275fab9-680e-357d-a336-2407dc9daa9f | -14.79783 | -48.11928 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9c1d52a-af22-3ad0-8214-4416bb53048c | -19.07053 | -41.13723 | 2025-09-06 03:51:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b12d510c-68b6-37b1-b039-c34eb134068a | -18.56355 | -43.82278 | 2025-09-06 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6eb03fac-7ca0-3165-af71-b126ad562c30 | -19.99301 | -50.46077 | 2025-09-06 03:51:00 | NOAA-21 | POPULINA | SÃO PAULO | Brasil | 3540408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c82bed81-1e9e-3be7-9a29-1faac7e2d592 | -15.70667 | -53.58797 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d1812b4a-5197-381d-bd9e-ef487f536766 | -16.73867 | -43.02026 | 2025-09-06 03:51:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8683f2a-dbfd-396c-8fcd-75e9a55f2b0d | -14.80422 | -48.11438 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1a5255f-00f4-3ab4-b3c2-98e01b09602a | -16.60351 | -48.94806 | 2025-09-06 03:51:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40a7200d-bdf0-3eb3-8e0c-2657797cf4a2 | -21.49343 | -46.19103 | 2025-09-06 03:51:00 | NOAA-21 | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3377703-03bd-36b6-ad33-c1245f2b4072 | -16.29894 | -45.68843 | 2025-09-06 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b2b3699-aa7a-3720-8d9d-da3a215d8a43 | -14.8315 | -48.19488 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3df78c5a-e5be-3c43-a3fd-3a55c71f8344 | -17.96834 | -46.90063 | 2025-09-06 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a3e5013-387f-3b8e-9bde-306631ec5612 | -14.26104 | -52.19233 | 2025-09-06 03:51:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49dfe07e-c481-3391-bc1c-392a1e5bb533 | -15.58386 | -52.91455 | 2025-09-06 03:51:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d7943c39-5365-3242-891e-9f872ede2241 | -15.63877 | -41.86029 | 2025-09-06 03:51:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 93fcd7b7-5d76-39f0-8ad9-37dd7037f12d | -14.79914 | -48.11261 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e9a11e9-cb6d-3e05-948c-9686ac10ac06 | -17.76329 | -42.51437 | 2025-09-06 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1fc4cbdb-43ac-3785-afbb-1790f7788936 | -15.07498 | -48.11892 | 2025-09-06 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39911992-1801-3227-8363-919aca018565 | -14.56317 | -48.01397 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be321f5f-b534-3705-8cb8-16f172628594 | -15.71518 | -53.58326 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1126b84-f1b6-3108-a531-517102af77ab | -20.53086 | -46.47086 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ec2e93a-d546-351b-a5ef-e97041899bd1 | -14.57499 | -49.13026 | 2025-09-06 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d847fed1-b3d5-3a9e-8a24-be5dc066acae | -19.40799 | -44.3138 | 2025-09-06 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f2cb915-92de-369e-8c14-1aba31ec7bbf | -18.4436 | -45.93729 | 2025-09-06 03:51:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81f630c8-dfee-3573-92f3-d5f8a70d53d0 | -18.26658 | -43.02554 | 2025-09-06 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7eaf6391-35d2-3a75-aa3e-b8757222e5dd | -20.46861 | -48.7861 | 2025-09-06 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fe221ee2-18ad-3e13-a9ee-e9e432ae42df | -13.87547 | -48.02903 | 2025-09-06 03:51:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5614ae2-cd8b-3ca5-b4a4-dc08bc8c6a85 | -15.36129 | -46.41253 | 2025-09-06 03:51:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f10734c5-aaa7-3aa1-a9a4-6b88bbe1c17f | -16.91936 | -45.75055 | 2025-09-06 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 038b91ca-a2df-3e68-bc1c-432aeb0d0bae | -20.53255 | -46.46208 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d84ce09-1234-3f6a-983d-bf9541e22bf4 | -21.44011 | -45.26107 | 2025-09-06 03:51:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a5c35e00-6dbd-3d46-8106-771986afa0e6 | -21.37107 | -46.80861 | 2025-09-06 03:51:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 51445704-0c0b-3765-8b11-9c4f30c9c162 | -18.0897 | -45.80205 | 2025-09-06 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5f89223-10af-3058-8212-4c4177d05744 | -15.35757 | -46.40669 | 2025-09-06 03:51:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81c8825b-ddfc-3a7a-88e8-e194016a6666 | -14.83292 | -48.18778 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f59f2530-8b3e-3b12-8ce8-eebf61cad1fb | -15.63948 | -41.85618 | 2025-09-06 03:51:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5ecd45f9-f7fd-328d-b03f-1f099f9524af | -20.09932 | -43.81635 | 2025-09-06 03:51:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6be6e224-96bf-3fb4-a982-dc5986d15b62 | -17.60856 | -50.55927 | 2025-09-06 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82f3ada9-f749-3c32-9299-d09662e0a16d | -17.96658 | -44.41271 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c22d54c-aa42-3eb2-b65e-3c734f913086 | -13.55456 | -48.11592 | 2025-09-06 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 307ee461-e0c2-3dfa-9bb1-de364558df02 | -20.91951 | -44.01336 | 2025-09-06 03:51:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c98538f4-0b0f-3192-905d-baa48164677c | -15.67101 | -45.8911 | 2025-09-06 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2446ff74-63ee-3159-a6a0-6907e8696e07 | -19.41084 | -44.31979 | 2025-09-06 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ec1fda4-ccc4-3c1a-bb6b-429feceffc31 | -15.62735 | -42.40079 | 2025-09-06 03:51:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9660ed68-d253-3da6-b28b-3fb2b0ff9e1b | -15.98462 | -42.38493 | 2025-09-06 03:51:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4a1d6fcc-d638-3757-8aa9-c8c88e96197a | -18.26518 | -43.02633 | 2025-09-06 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 47f7f427-902e-3990-94ae-188d763190fe | -19.78163 | -45.21159 | 2025-09-06 03:51:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3bfe6a4-1707-39ca-aa8d-106a29422215 | -14.82752 | -48.18745 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e3647b2-dc82-328e-a472-0ab0e9e78b17 | -20.53668 | -46.46349 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a00ec8f-a914-35a5-ba8e-b426d753bd86 | -14.5695 | -49.12857 | 2025-09-06 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51eec3d1-8c5a-349b-bbc1-bd3c97ee9077 | -20.5317 | -46.46647 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44da0a76-4ce1-300d-996b-2205b7abd092 | -14.83893 | -48.18504 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f849a0d-245c-3bf4-b077-4a562721b9d2 | -19.95969 | -41.77932 | 2025-09-06 03:51:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1a4a23d6-c9ff-3e6e-b7db-fa9d22a36a1b | -19.62532 | -46.01842 | 2025-09-06 03:51:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81e20a5a-b626-3938-bc04-90f223b55b77 | -15.71363 | -46.24794 | 2025-09-06 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52c25d45-d368-357c-ab3b-fb72f1df37ed | -14.57261 | -48.02115 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aec95b4d-e292-3ac2-9012-8812772a8f5e | -15.72353 | -53.56259 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97a6ce89-e85c-3f15-adcf-c0581a44068e | -20.46251 | -48.79074 | 2025-09-06 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e1e948d5-b8d3-39fc-8b2f-59e2208182a9 | -15.07113 | -48.11106 | 2025-09-06 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f4fad03-e604-3761-8f46-1f507df1ee57 | -15.54916 | -49.82044 | 2025-09-06 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0d42c4af-4f43-30c4-a330-c19679e5def4 | -14.18903 | -53.06789 | 2025-09-06 03:51:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 962f388b-d121-329b-a842-cbfe82e05e55 | -17.23646 | -46.71225 | 2025-09-06 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 609d137f-8e0c-3afb-a02c-9c5864e4612a | -17.7089 | -44.49459 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17442487-6447-3ca7-8cae-a736fc22c8fa | -20.10013 | -43.81183 | 2025-09-06 03:51:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 86fe3bde-686d-32ee-9df8-dc4ac665fc59 | -20.14515 | -41.9964 | 2025-09-06 03:51:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d2fce3d9-1de1-395e-9855-dd7d49d3d3b1 | -14.58783 | -48.08232 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20630521-e7f3-3b27-a45e-07dce68c712b | -13.88616 | -48.03059 | 2025-09-06 03:51:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de77dda6-3617-32e7-a917-dc4181948e00 | -16.0903 | -39.40845 | 2025-09-06 03:51:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c3dbc3a0-97ee-3086-9891-7ad3c7e49d96 | -16.3068 | -45.69455 | 2025-09-06 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cfde58e-744b-318b-9115-6a579f1acfb3 | -13.84603 | -46.27393 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95bfa325-68ab-3322-81d9-c55421f8ff1d | -19.46698 | -46.27461 | 2025-09-06 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f513285-3d55-337f-8ae5-c28aaf78348b | -14.89435 | -49.46195 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a911bbaf-bdbe-3449-8152-48a24c0012f2 | -17.75974 | -42.51376 | 2025-09-06 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5817a700-6761-31fb-aabc-af59d35cfcd5 | -16.92367 | -45.75142 | 2025-09-06 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3cda0a2-d0b1-3b94-a57f-d1781f2ef5c2 | -15.36356 | -46.41671 | 2025-09-06 03:51:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2be102d0-bc0f-3c5c-8698-443cb5df9ec2 | -13.54772 | -48.12243 | 2025-09-06 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09c50d9e-b775-3830-8572-b136776cdabd | -16.29459 | -45.6876 | 2025-09-06 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2756fb22-6614-3649-a024-43aa4b7146bf | -20.75931 | -46.0272 | 2025-09-06 03:51:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f982bc20-43f4-3aff-850d-1b153c86abfa | -14.57145 | -48.02703 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 706f890f-b4e6-3590-b309-2b2284d3490d | -18.53743 | -47.41474 | 2025-09-06 03:51:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 699e7313-46a4-3646-8dd5-5bc11bce3c2b | -16.30329 | -45.68925 | 2025-09-06 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06295a09-f77b-333f-8d73-36758a18aa84 | -18.59262 | -43.64649 | 2025-09-06 03:51:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ee7df129-4795-306e-b688-a57f3166582e | -15.7239 | -53.57757 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f97e3897-63d0-3bd7-900e-84d091e0c9c7 | -18.26593 | -43.02194 | 2025-09-06 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| da162860-56d2-3bc5-b779-3b4a64d78732 | -17.241 | -46.71329 | 2025-09-06 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff7bae73-e706-3aa2-9af5-7caa95052597 | -13.84622 | -46.26638 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2ee1d94f-ea5e-328d-a9b4-d03e22bc3b70 | -14.56444 | -48.09055 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README28.md)
