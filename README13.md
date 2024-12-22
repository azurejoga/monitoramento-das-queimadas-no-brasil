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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffd5f4f9-5d56-35a9-8de4-8b454c5dee4e | -4.55711 | -43.30186 | 2024-12-22 04:50:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 679746bc-019a-3def-a2bd-7b874a1e8c0f | -4.72857 | -43.25303 | 2024-12-22 04:50:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7a2de9f-ad1e-3c81-a9a8-e39fe5ca7e8f | -2.41599 | -53.73768 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61290adc-5888-3766-a255-a8a4f1be7fe1 | -2.58373 | -49.46726 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ebed61d-d40d-3043-8280-089897c6eb4f | -3.01335 | -46.99524 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8384825f-4a06-32d3-a9cf-f333db80a03b | -3.97574 | -47.2618 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a4b43ed-644f-3d19-af67-20b133968a0c | -2.6018 | -47.00072 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c03de2a-2faf-3ae7-939f-3591250ce286 | -4.56244 | -43.30262 | 2024-12-22 04:50:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aee60433-e01c-32a1-ad3b-122f51e740c1 | -2.568 | -49.453 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a1395c9-c579-3898-b3d2-8b0c67f65d88 | 0.98059 | -59.53267 | 2024-12-22 04:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 54dc49c3-2682-3851-9c51-b84ccd558836 | -2.56511 | -49.46939 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 371c8195-bf68-385e-b9cb-00c54cbcc8b0 | -2.56161 | -49.46886 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e06d2d0-58fe-3885-94f5-9f0f37db8352 | -4.51512 | -48.06882 | 2024-12-22 04:50:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d49122de-8bf2-3326-8f42-7f6d5ed76acd | -4.82013 | -44.41053 | 2024-12-22 04:50:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 052308de-e2aa-3c4c-b071-94f4acd079d2 | -2.09241 | -53.3119 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cc29c2d-ba88-303b-b691-783700c21da9 | -1.2942 | -53.12613 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ace105b4-3c77-3554-8bbd-d5c5b3770ee2 | -1.36972 | -53.70432 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 476408ba-1dd1-3a89-b382-488e571c1638 | -2.76432 | -54.04784 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15ed493a-430a-38a4-994c-e685780f470b | -3.9251 | -46.90834 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a560741d-8f6a-3fc2-8383-4250c26e0f15 | -3.18316 | -50.39806 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 763bbb91-c39c-37dd-b2ea-5ca2aae2befe | -4.09783 | -45.30524 | 2024-12-22 04:50:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c94ff1d-91ec-3948-ae42-8044091a191f | -2.76827 | -47.39443 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 278d1fca-8a0d-326e-8b63-359fdcae4994 | -2.53368 | -53.95882 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94b26384-18c6-3bd8-a21e-2e3a77b0ca0f | -1.15034 | -46.75526 | 2024-12-22 04:50:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db28f73f-a410-3851-a863-a6de0f6a3545 | -1.55037 | -54.24477 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e553de6-f443-3767-9a1b-e786084a0136 | -3.17365 | -46.25693 | 2024-12-22 04:50:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c67e0a9-1fcb-3449-8ece-fbb5bfce4ffe | -2.68526 | -54.84414 | 2024-12-22 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ca8346e-ec52-3530-ba8a-521c9fb9f2e1 | -2.55809 | -46.8833 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 678ca00a-b6d1-3644-a5da-c5eb9ad875c9 | -3.75774 | -47.19738 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1f6266e-2339-3bde-923b-d40daa92f422 | -2.51665 | -48.37274 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b535bd29-4e02-39c4-91dd-ef26d57bbaa6 | -3.75478 | -47.18983 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74505720-b7f9-3280-82c0-cc7bf20b8195 | -2.07984 | -52.04786 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afd5378e-bcb6-3ead-9af3-6017735fc7cf | -1.8943 | -54.57292 | 2024-12-22 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 728aa0da-5664-31c7-a547-037aa7fc6326 | -4.56021 | -43.30175 | 2024-12-22 04:50:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| af2185ce-68ac-3c9d-83d4-8ff6018de246 | -3.83664 | -46.68429 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c26c81a-5748-3dd4-9525-35a5c44ce503 | -1.78908 | -52.75628 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 064dd7e0-7a20-3745-bafa-d31b3904da61 | -2.77407 | -54.35116 | 2024-12-22 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 713c608e-9a07-3d80-8e1b-76467802f776 | -2.8243 | -52.85984 | 2024-12-22 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f30fc88-33ff-303d-8d78-4a23902a5520 | -3.22084 | -45.93865 | 2024-12-22 04:50:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c85934b-a988-3770-8231-5fb429e84ad1 | -1.25588 | -53.48051 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e91fcbe-8400-3b52-9779-022c289c39e0 | -4.01839 | -46.9037 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0b33cf4-d61d-3dbe-b959-6baab8e2426d | -1.36648 | -53.68027 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30e9ef8c-81a8-34b6-b862-087554455145 | -1.71665 | -52.57135 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1134a5a-f35c-349e-a766-70160a7b6017 | -2.57673 | -49.46618 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ad7cbc1-ff02-301f-a416-81698b2462a7 | -3.50114 | -47.19706 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05eb182e-f52a-309c-8548-7ea1ac327f26 | -1.17902 | -52.5489 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c533672-f5da-3f18-a14d-703d6452cdca | 0.64367 | -60.30762 | 2024-12-22 04:50:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0ea3289d-821e-357b-bfb2-25c9bcdf2c1d | -3.06726 | -47.76458 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05949e56-a33e-37dd-a6bf-d062044a25ad | -2.82846 | -51.7866 | 2024-12-22 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9583499-89dc-35ec-a1ba-32dc6313e06b | -2.65063 | -46.10799 | 2024-12-22 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a019ade6-0cd3-3126-a5cb-52437459e0a7 | -1.19019 | -52.54342 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3bf7b51-2316-35e9-a7fc-94ec5a019085 | -2.50205 | -49.06706 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 951e1cec-8f00-3726-b497-fa077b46a48f | -2.80625 | -46.75003 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c6a8ae7-9951-3010-b57e-14a2fe713b7f | -3.83709 | -46.8877 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49d576d7-9c8f-3efe-8e7a-a0c182d28fda | -1.37033 | -53.70051 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| da1a31e5-5245-33ec-b7d3-fefae360de4c | -3.74725 | -47.1852 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d608afa-a9b9-346d-8027-a305cf6d8da4 | -1.37379 | -53.70106 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4745a7dd-33cd-3e15-97b3-6318e9cb416f | -1.36687 | -53.69997 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2a1e05fc-609a-30e8-aca6-3e4962c98797 | -2.22559 | -53.81173 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bc7fa80-5e42-3596-8c0a-6b47bbf63d32 | -2.04674 | -52.10644 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 909cc8c5-dc4a-3179-8a73-cb4115e3e40b | -2.68886 | -54.84472 | 2024-12-22 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38b63f3f-4866-33be-beef-58d3b94a8e39 | -2.69245 | -54.84528 | 2024-12-22 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df5796cc-0e22-3fe7-ada6-68a57bc67f99 | -2.19634 | -48.42504 | 2024-12-22 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0abb5913-160f-3f76-9bba-b9a381dd1549 | -1.26381 | -53.51985 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 174188b6-d77a-335a-a720-4c015cdf899b | -2.56564 | -49.46844 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d1eb659-ff5c-3b42-b3d9-59865628130c | -2.56391 | -49.45632 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1a68c34-7a5b-388a-bbc0-0b5680097d7d | -1.4117 | -52.03552 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cb20d45-99f9-3db7-85f8-95901e55b5ea | -3.78781 | -47.10788 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24b73fbc-0061-340f-a751-b2f65207b0b9 | -3.22519 | -45.9393 | 2024-12-22 04:50:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8453f51c-884b-3518-b0cd-361fb9b2197d | -2.24718 | -48.31443 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d9a2e2c-5ebc-35a4-9e63-311a26e97cd2 | -2.22799 | -53.79671 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1246fb96-c335-3a4a-a5b3-e24eee6adc5a | -4.01545 | -47.05874 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 364a490c-1973-302f-a915-ee1e4d58c819 | -3.04004 | -52.71383 | 2024-12-22 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f7b7804-71f2-3358-8934-19b98f4dcbdd | 0.0031 | -51.67575 | 2024-12-22 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 209879ae-6d52-3d15-bda7-596337d84504 | -1.25931 | -53.48109 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02a5bdef-0091-3a76-a272-b95a0716cafb | -2.6177 | -47.46468 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 928c27a8-a35d-3cce-9486-ac9d49b17baa | -2.63028 | -48.02887 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca2fb374-3339-358b-b907-25b7748fbedd | -1.69258 | -54.4815 | 2024-12-22 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b98ee988-3ae9-3b1d-92df-cbb02d21e3af | -4.54109 | -45.87852 | 2024-12-22 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f45ffe63-d428-3cfd-8a74-9154c4e6fb58 | -2.55512 | -46.87563 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ded09e7f-175b-3e13-8c81-3ec49d88789c | -4.08183 | -46.80272 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b23e85b-0883-36ec-80c6-b3f9a7a378bd | -2.67083 | -46.93384 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db5179d2-a7c3-303a-a152-f022fbd80eeb | -4.32661 | -47.78232 | 2024-12-22 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc830acc-7b88-33ab-bbc6-43344362a000 | -3.75827 | -47.19388 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62d2445c-d6fe-3c42-928d-4478d1407bae | -3.76633 | -47.19504 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb334d16-27a2-3549-aca6-99b109193e7b | -2.19044 | -49.6049 | 2024-12-22 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81839596-d9ba-3a47-9ea1-115222e79683 | -2.49829 | -48.06169 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4164d42e-7e58-3d4f-8f28-ff08e600c2a3 | -4.0225 | -46.90434 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d5582fb3-5b27-3eaf-8179-667b79c7a0b9 | -1.85172 | -45.62445 | 2024-12-22 04:50:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69f0af32-4c90-38b7-87c2-654bf7797065 | -4.01428 | -46.90304 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e72c6c4-313a-34d0-9efb-d4fe79ada118 | -4.05787 | -44.04874 | 2024-12-22 04:50:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c453049f-63a1-3f06-a243-dbb84a742ae2 | -1.36872 | -53.6884 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 542214b3-acf0-36c5-84bd-6ae131c10f7a | -2.97672 | -48.08416 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 495e8ddc-644c-3b01-a54e-477a91545ba8 | -2.51894 | -54.22992 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a7a84d3-47f2-349f-90fe-a100311db603 | -3.98186 | -48.39151 | 2024-12-22 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f455941-b31d-3ef9-ae44-6730eb50675f | -2.19104 | -49.60112 | 2024-12-22 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51e89d06-6e6c-30b9-bf7c-4979d08c3e3c | -2.67135 | -46.9304 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a74cd2-8bf4-3f5a-92c1-cf829a81acd9 | -1.15514 | -46.75078 | 2024-12-22 04:50:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c34977c-3d5e-35ab-9953-bd70dbafc30b | -1.41115 | -52.03898 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3812f40d-ec43-3936-b589-11a031daa642 | -2.56504 | -49.4723 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README14.md)
