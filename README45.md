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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffda47c3-abd1-3a4e-b92a-216f8920bdd0 | -8.98852 | -54.58584 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 639de5d7-b17f-3ec4-b8c1-cfe2ef3e9b6a | -8.98634 | -54.58391 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a20e5c2d-d3d3-3be1-9213-550ce976628c | -8.98539 | -54.58931 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f25e828-2a04-3ef7-abbe-12d55c057bcc | -8.98364 | -54.58502 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35b01712-5132-31f5-a9a2-d83dc824f193 | -8.98265 | -54.59042 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de22d6b3-beb1-3d3c-92d4-dae0b7d35ba2 | -8.98051 | -54.58849 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8d5d6d1e-dccc-3d41-9a0f-32f04dd777da | -8.97956 | -54.59386 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 28f88f37-f884-3969-a870-db6d171dbeb4 | -8.53767 | -54.77259 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b113f233-5e61-3342-b955-909d1ed192c5 | -8.53272 | -54.77291 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3fbfd52-7be1-361f-a285-b3fe86a6b10e | -8.5327 | -54.77168 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e687e80-c29e-3c3d-bf7a-c31410e8692c | -10.03995 | -54.33989 | 2024-10-15 04:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd0f7589-a32d-3c90-8187-91bd22d217d0 | -10.03617 | -54.33397 | 2024-10-15 04:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52a9c722-8b6e-38f2-81e7-70826096da16 | -10.03526 | -54.33897 | 2024-10-15 04:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3f6d5b9f-bcb2-3e98-b433-0b69e708ddd6 | -10.03437 | -54.34386 | 2024-10-15 04:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e5d74a22-8d50-361e-af7e-d0ffc87f8243 | -10.03057 | -54.33805 | 2024-10-15 04:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6f657525-c5a3-3db1-9ea8-1aef6c129f55 | -10.02967 | -54.34294 | 2024-10-15 04:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9eca3007-8b29-30e1-9bbb-65bef7f9751d | -10.81144 | -53.89421 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8835be2-aeb1-374a-87f8-0226eaad34d4 | -10.80695 | -53.89333 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38c42076-693a-3c9c-9451-8e47db8dc7aa | -10.80613 | -53.89792 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c80f932-30d5-371d-a639-04bf4b8cddcc | -11.3147 | -54.33204 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 157f2e5d-1504-346e-84a0-159229f4cbb9 | -11.31011 | -54.33116 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09229fc2-6c93-3548-9488-26cb821293dd | -10.94441 | -54.09645 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a42bbdd1-a007-3a56-a798-8ed2bce39c89 | -10.94354 | -54.10119 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4811ad8d-05fc-3c18-a11f-8fbfc443a246 | -10.93985 | -54.0956 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f24e899-a1f7-3455-b967-6bbb758332cb | -10.93898 | -54.10036 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eaa1347e-aae8-3e93-b4ad-7fcadf4826ad | -10.93812 | -54.10511 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1bff92cb-6759-3ad5-aea0-9632c152ee9f | -10.93444 | -54.09948 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 472085bb-a69e-3063-a30c-c03dc776b7c1 | -10.93357 | -54.10423 | 2024-10-15 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db77d854-6eb3-3182-9c5c-e247e7f0c4f3 | -4.44999 | -55.08411 | 2024-10-15 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27a1c645-7144-3ffc-8c97-077b553f10ec | -4.44396 | -55.08664 | 2024-10-15 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cca564f-8da1-398b-986d-f2f9ad3db143 | -4.35628 | -55.13499 | 2024-10-15 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7651e6af-0ef9-3142-8b31-7f76453de75c | -4.35569 | -55.13852 | 2024-10-15 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6acd942-de72-3782-8723-ac0d7891d1b2 | -4.33186 | -55.21267 | 2024-10-15 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b6e5ff9-7e58-326a-9dae-7f94ff783e5a | -4.33125 | -55.21629 | 2024-10-15 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cf9d576-0e0b-37bc-bd3d-b7ba291f9b39 | -11.43783 | -55.68066 | 2024-10-15 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b0f52a2-524e-3aaa-b79d-70623011c060 | -11.43281 | -55.67972 | 2024-10-15 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7385a0ed-84be-30e7-b253-619341a8ade0 | -3.87443 | -55.77383 | 2024-10-15 04:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd482a03-a4dd-313e-983c-2f18a8f25735 | -3.86868 | -55.77287 | 2024-10-15 04:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c46eb04c-b189-3728-a8cc-49a91fec9d03 | -10.37712 | -61.19178 | 2024-10-15 04:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d266ebbe-dc49-381d-90ed-ffe7642b5800 | -10.3757 | -61.19872 | 2024-10-15 04:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7ab8eaa5-8815-306a-8d77-c26d22b8b232 | -10.37143 | -61.18322 | 2024-10-15 04:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9470ea6f-15a1-37de-97ed-cfc51d035d02 | -10.37001 | -61.19015 | 2024-10-15 04:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6ef4c24b-6e83-3b20-9607-499bbfab556d | -10.36858 | -61.19715 | 2024-10-15 04:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 8e58873a-d216-354f-966a-ab34f680eaf5 | -10.36432 | -61.18161 | 2024-10-15 04:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7af20cb2-fde7-329b-b635-e2bde8d6f74e | -10.36288 | -61.1886 | 2024-10-15 04:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a753bb78-8550-3884-a0b3-a70e56b61fc6 | -10.36142 | -61.19569 | 2024-10-15 04:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 62f09693-6b6a-3eed-b1da-8adbe6e521fc | -9.43662 | -44.16573 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61f1f8ff-b1c7-3071-92e1-76e702385ac7 | -13.27726 | -41.94395 | 2024-10-15 04:25:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 046375b3-e336-39b5-8e20-d75c26a731e6 | -13.27677 | -41.94234 | 2024-10-15 04:25:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a29745cf-4442-31d7-93c8-3397d6fbe743 | -13.27626 | -41.94627 | 2024-10-15 04:25:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d8777ab-2813-3f7c-b1fc-c3d1be860b5b | -7.04966 | -42.08909 | 2024-10-15 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 88f08011-769a-34e2-b318-c64ba7dab8c3 | -7.04512 | -42.09324 | 2024-10-15 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0cb302d6-8f37-317f-8cd8-07d5d9a1481c | -10.48364 | -42.44101 | 2024-10-15 04:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 254c9639-0602-3781-8c2f-e3743b4b8d79 | -10.4797 | -42.4404 | 2024-10-15 04:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 87be44c0-a8d0-3a07-9a61-766fe57eea5c | -9.45788 | -44.14447 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbc57af4-7725-36de-baf7-d7de567d293f | -9.45669 | -44.15248 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d92a3f16-a5df-36b1-9e1d-2611830c4674 | -9.45663 | -44.17712 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ac2ed81-1505-3849-82a7-372d52b99608 | -9.45604 | -44.18112 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9f668f8-57c1-38b0-8192-5afbbed13f95 | -9.89829 | -44.59306 | 2024-10-15 04:25:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27a56985-c239-34ae-81ec-ce0914dd57b2 | -9.83565 | -45.05961 | 2024-10-15 04:25:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ce14556-0bdb-39a6-ae83-66148946c92a | -9.83222 | -45.05906 | 2024-10-15 04:25:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbab0516-e97f-3582-abb5-65f2c39470c2 | -9.45816 | -45.50381 | 2024-10-15 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30142bbd-485c-3138-a119-92a8c8edab99 | -9.4576 | -45.50742 | 2024-10-15 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d3b902f-f4de-3612-9b87-2c9e5072906e | -10.07976 | -44.24393 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b98fb0ff-d189-3e54-928a-96f4de981d9a | -10.07919 | -44.19857 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32a962eb-2f61-3359-ab14-16f240e34a41 | -10.07683 | -44.18989 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5388ef5a-0e21-3745-9b55-1fd5d82df225 | -10.07623 | -44.19396 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7dc6157e-627a-3d12-a007-bce77d5f58be | -10.06554 | -44.24189 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ce5b8d3-2971-3324-8dcb-03f4f95dcfc7 | -10.06258 | -44.23737 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbfccca1-b7bb-3884-86cd-8152b0b90f9a | -10.06199 | -44.24139 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7d767e8-2838-39a8-9f2e-9f1ad5bae07a | -8.16579 | -43.92865 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1397d0b3-6e20-3be9-bf68-8a9954f13f64 | -8.59289 | -44.03328 | 2024-10-15 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bdeb5833-dd54-36c1-b843-dc1714a80008 | -8.34016 | -44.92294 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe98e0a2-0705-347c-89c3-6f2ddec9aa2f | -8.33676 | -44.9224 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b292d3c-085e-37ae-aaba-232faac0d282 | -8.28857 | -44.85152 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a3ffbcc-3816-30f3-ad2d-5ef4cacd955f | -7.95036 | -44.53513 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8538e37-ae0f-392f-8d46-b04b75094477 | -7.94927 | -44.51941 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56e73392-1467-3a0a-a7df-c2d386a57994 | -7.75832 | -44.89563 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e04fe3fb-e276-3cfc-8b27-d525f45d734b | -7.75776 | -44.89928 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 004ac70e-370a-39df-9d25-6dfaf81268ae | -7.75729 | -44.53687 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37ebc285-2abd-3a66-9b85-206c191188ee | -10.67616 | -44.32523 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8054eeb-3a48-3c56-af12-0f9e560b6f4f | -10.57577 | -44.22793 | 2024-10-15 04:25:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 817e4b9f-cfc5-307b-b64b-50f3b4aefeb8 | -10.51157 | -44.19297 | 2024-10-15 04:25:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8a13f21-5c46-3f92-9d32-25a8ab9d529a | -10.47343 | -44.06629 | 2024-10-15 04:25:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe1cd8ef-5922-3d2f-98c0-42ae4daa82a3 | -6.90283 | -43.96967 | 2024-10-15 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 338b49d9-f55b-3534-95c4-acd7d44d6832 | -6.89994 | -43.96529 | 2024-10-15 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d80fd852-092b-3d09-a13d-e3994b811bec | -6.89935 | -43.96914 | 2024-10-15 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21eb622d-c314-3afb-8a54-d0014c127e1d | -10.70864 | -44.9761 | 2024-10-15 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c06b2e31-917d-39a7-a40c-33165e110843 | -10.70517 | -44.97556 | 2024-10-15 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 905352ea-064b-3b0c-b294-7690f56e0bbf | -10.65618 | -45.17112 | 2024-10-15 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1b1c38c-e3c8-3d47-bc7d-11475b874803 | -6.55305 | -43.66599 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37f86ec4-5366-3718-8e99-7c33bb8ae5b4 | -6.54542 | -43.66878 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08268cd3-8ae6-348c-a6ae-ae5ea125b44e | -5.97889 | -43.90483 | 2024-10-15 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abf41722-14ee-339d-90d9-392d5680e620 | -6.82245 | -43.6918 | 2024-10-15 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 19a322cf-0c87-3442-828e-0c1e6c4ce576 | -6.68954 | -43.64382 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac30b9a7-48e7-3c55-bb58-f00708a4753b | -6.68836 | -43.65171 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e4e72b1-2192-3f0d-b459-33f894d3462f | -6.68601 | -43.6433 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7aa7869f-3344-3e62-86ee-34234e9de9fe | -6.60265 | -43.8588 | 2024-10-15 04:25:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b2030deb-e805-3c45-84b3-25f2dfa2d49a | -10.04089 | -44.19337 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aed6284c-8bbd-394c-8713-453fc1e5ca92 | -5.85337 | -44.87782 | 2024-10-15 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README46.md)
