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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7edf0628-c182-3e5b-a33b-a0b3a4517124 | -12.5347 | -53.11843 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 790190a4-1f1b-3f09-90ee-5efe29d114a5 | -12.53136 | -53.10812 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6587992-f1d4-30fd-8e2f-d00682f0dc09 | -12.53007 | -53.11781 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7cf1b14-15cb-39ac-b87a-9da0d2a2f425 | -12.49914 | -53.13842 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 190f5144-3b21-3ec8-8537-e2a2940bcf65 | -12.49849 | -53.14339 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aaa32788-e32a-33aa-b223-624d6bc824ab | -12.49452 | -53.13778 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 426975ee-4ab2-313f-a8d2-0c77813579c5 | -12.49388 | -53.14276 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f14a9794-6a4c-37df-a472-5c13a4a76d53 | -10.52602 | -54.59597 | 2024-10-03 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74d8a8ca-8bb8-3fbf-9675-26f79097900d | -10.52194 | -54.59544 | 2024-10-03 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e994c08-9785-348c-8c48-e6d0902a431e | -10.52185 | -54.59501 | 2024-10-03 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2b79126-8374-3db9-83d0-0e1a1d0efee9 | -10.52142 | -54.59904 | 2024-10-03 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ce32d76-ae43-3fd5-ade8-6b6dc25466d5 | -10.52136 | -54.5986 | 2024-10-03 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05a9973e-b0a4-3497-ba76-c12ad38c30ab | -10.44885 | -54.70248 | 2024-10-03 05:16:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39599a00-ac41-35c1-b91f-eccd809601c3 | -9.6352 | -53.57964 | 2024-10-03 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 513e2363-5276-3452-a27d-9f10cb117ef0 | -9.58637 | -54.63768 | 2024-10-03 05:16:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 350eab72-95d5-37b7-a25f-175ac0d752cb | -12.31976 | -54.11217 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fce5173-1f46-3648-b0ff-c505fb770e2a | -12.31783 | -54.10936 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0d4bae0-d3df-3327-a501-acdb3bc85b3b | -12.15106 | -54.26919 | 2024-10-03 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53fb92ef-0620-3521-8a8a-6f71d1d8c25f | -12.1505 | -54.27328 | 2024-10-03 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe9822b9-97ba-380e-839d-0ae2d6f7da39 | -12.14737 | -54.26449 | 2024-10-03 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 776d4150-05ec-3365-8d1d-64052363fd1c | -12.14681 | -54.26859 | 2024-10-03 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af75d451-b7a3-310c-9c40-17355e4ef938 | -12.14625 | -54.27267 | 2024-10-03 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 508727f1-0b37-3afa-b8e8-0edf1ef7fb4f | -11.10188 | -54.22081 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0405d746-a0c2-3e97-bcb8-cbb06d579ee3 | -11.10134 | -54.2247 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc8fa041-a160-35e3-bd58-2972bbf6af06 | -11.10079 | -54.22857 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1d6f9bb-6531-311a-bfd7-02afbcfab287 | -11.09769 | -54.22014 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1bd7f9b-3666-302d-a07b-0a4bd58e3c9e | -11.09715 | -54.22402 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2410f022-6a66-3b87-95d4-34be3cd86c9f | -11.0966 | -54.2279 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 329160be-4fb2-369b-a82f-a5b4ee478da8 | -11.09606 | -54.23179 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6c84222-9efc-3b68-958d-47b0eb422ec7 | -11.03061 | -53.99257 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5925534-6dd7-3dfd-898d-abd6a7395da0 | -7.61472 | -55.16556 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e887b43-15e2-3559-b8ac-cb9db4776da8 | -7.44986 | -55.41484 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ebef974-0598-3b08-bb8d-0cbd325db861 | -7.44615 | -55.41426 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce015071-0432-39be-9827-394404782452 | -7.4419 | -55.46801 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ed7ba7-8ea9-3153-bd36-56d88bfd2e6d | -7.4382 | -55.46748 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cb4c724-154e-3a3f-8bd3-5e717f8497c1 | -7.40576 | -55.43096 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba7d24db-ee7e-3b60-ad6b-364c75450d8f | -7.40271 | -55.42595 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c456f2c3-f37a-3472-a67a-9229a68a0585 | -7.4014 | -55.43483 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a40fb29-bd07-3259-91e3-cc1be9b073f8 | -7.37564 | -55.50745 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f1c6c90-2e01-30d8-b24e-659109db7a62 | -7.37499 | -55.51184 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83948307-981d-328f-ad4a-600648969e0a | -7.3373 | -55.08184 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a635da1-cd9d-3992-9653-b349e4466835 | -7.33352 | -55.0813 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 936f8132-459c-3ce8-bdc5-58d1841bb1a4 | -7.32974 | -55.08075 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4949cc75-c4f4-38c8-8450-a190e2632b0e | -7.32908 | -55.08527 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3da8f6f4-4bd4-3f40-b0ee-3a944cbe42c5 | -7.31164 | -55.30971 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a76f30df-0c67-3507-b27e-6e33170fed71 | -7.30791 | -55.30914 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acc04dfb-a7bf-3954-a2cd-89d0b97319c1 | -6.99836 | -55.12668 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d8c7d80-b1b7-3090-a110-1ee1a804b306 | -6.90087 | -55.054 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0208ac52-2f12-3bfa-88e9-9165e3ed69fe | -6.86708 | -55.1204 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d19a1fb2-9dfd-3494-9152-ada88d8aafab | -6.86639 | -55.12493 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c6a00d3-a7b4-3517-a59c-461a2220dada | -7.91385 | -54.75076 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cafc972a-b631-3629-9d72-4627c2694fa8 | -7.91316 | -54.74942 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebad5594-fb64-317a-a67e-b9d9e98d2649 | -7.91315 | -54.75568 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 143f7429-be2b-303f-ab1e-55edab840827 | -7.91243 | -54.75434 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d4998b2-fedc-3e00-a303-befa4743fc8c | -7.91067 | -54.74527 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b25683b-34ab-3232-80ee-a7ec85e7d82f | -7.90996 | -54.7502 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fc71ac6-37ff-3aeb-bd21-e5e5aed59878 | -7.90928 | -54.74887 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00355c0b-147e-35a1-86e7-532d78978526 | -7.90926 | -54.75513 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5cd240a-086e-3cf5-ae2f-7b8e8079e34f | -7.90854 | -54.75379 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35946854-6fde-3edf-9b20-d545a07379ef | -7.90608 | -54.74964 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e1b68e7-1ce1-3745-8e3c-c26c035c69bd | -7.90467 | -54.7595 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b21d7fc8-2ccd-35ce-8fe4-76e1262e2eae | -7.90465 | -54.75325 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1096ddab-b3c7-3bba-a599-29d87be7a03d | -7.90392 | -54.75816 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e04ceae-1a3b-3135-86a4-7bf619ab3645 | -7.90149 | -54.75401 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 055f068a-7169-34f8-a1ce-29caf78abb5a | -7.90079 | -54.75893 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 163adc75-bace-33c5-92fa-61bab2ca9f63 | -7.90077 | -54.75267 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5448ac9e-c339-30c4-8f73-6069d104edf8 | -7.90004 | -54.75759 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 184c7c2f-ac89-3342-87ab-b1cd600c2130 | -7.89689 | -54.75211 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efff5179-a773-35ad-83dc-1a5c8226f518 | -7.89616 | -54.75701 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af162a4d-5020-3033-ae58-5014d6c62fdb | -7.71893 | -54.82262 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ec33599-b0ff-3c46-91cf-c3ef7c92c76b | -7.71647 | -54.81239 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df636875-d2b1-3aed-a7c8-82dacf2d43e7 | -8.49984 | -54.90295 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1954370-b3b4-302c-bff3-7ee5c05af0b5 | -8.48461 | -54.97993 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20557bd3-bd1f-3e4b-bdf3-57c25ac3d2e8 | -8.44984 | -55.456 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc87fa71-2a05-39ea-9385-d31c1dfca2c9 | -8.44872 | -55.45804 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ecda237-7c06-34bf-8e0c-c90814766b60 | -8.44294 | -55.47103 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50f10600-ea7e-3cc2-9fde-cf94fcd458cc | -8.44226 | -55.47557 | 2024-10-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce986f96-e884-37b2-9c4b-e95a0d95d943 | -8.30878 | -55.09398 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e3fd2e5-39b9-3d9a-8da8-bf1c3da8c822 | -8.2975 | -55.09977 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3f07fb1-f0aa-305d-8599-58564c988134 | -8.17139 | -55.16305 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e71000f-a53a-30f6-b467-53ff0266d0aa | -8.16842 | -55.15994 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11036e99-bfe6-3588-9229-a6cde218adff | -8.16758 | -55.16252 | 2024-10-03 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 792a1d34-581d-3f5a-a251-f123648871e2 | -9.57746 | -56.02127 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64e0b580-2453-3ee2-81b6-bf9c6ab44d0e | -9.57682 | -56.02571 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c2bcaa3-d0ea-3eee-811f-014345ece3cd | -11.92335 | -56.96117 | 2024-10-03 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6cac03d-bbaa-3fe4-964d-af9e761d369a | -11.92095 | -56.95217 | 2024-10-03 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c737603-6d7e-3f06-8bd6-2e6f8c50b857 | -11.92034 | -56.95641 | 2024-10-03 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdbc28e9-571d-34d0-9203-1db9d779b8fe | -11.91936 | -56.95418 | 2024-10-03 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c628b03-3846-3ff0-a3e1-76cd3f180c84 | -11.91874 | -56.9584 | 2024-10-03 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5df50cfa-177e-3da4-8023-007d2f174786 | -11.91674 | -56.95589 | 2024-10-03 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce1e9a92-1484-3e79-8e2e-54fa3fd4743a | -11.91513 | -56.95789 | 2024-10-03 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57086c21-c045-3a45-8c0e-1b81ad36f756 | -12.61536 | -56.48375 | 2024-10-03 05:16:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bd6ba4a-440b-3c60-851b-22392361e0e9 | -12.61163 | -56.48321 | 2024-10-03 05:16:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1578d07d-10fb-37bb-960d-eb38da291368 | -12.61098 | -56.48774 | 2024-10-03 05:16:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce2ddba6-eabb-367f-871a-372365fa32bb | -6.56309 | -56.02343 | 2024-10-03 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9457fab9-d233-3d9d-bb63-95578f9036b1 | -6.55953 | -56.02291 | 2024-10-03 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50dfef29-254f-337c-bf12-94efafa94282 | -6.55536 | -56.02645 | 2024-10-03 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c742b28a-ab2d-320f-980c-df92c28d7180 | -8.09333 | -57.67892 | 2024-10-03 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 652db3c9-c9b3-3f44-b108-e6f6e23dc0b9 | -8.08994 | -57.6784 | 2024-10-03 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1018f0d2-ca18-3c7e-a7dd-f7c53c9ac496 | -8.08656 | -57.67788 | 2024-10-03 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README163.md)
