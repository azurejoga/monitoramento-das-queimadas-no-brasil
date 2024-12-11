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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e79f130-a1fc-31f1-a46b-404dbd439032 | -3.11236 | -54.07949 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88d7b089-0973-3551-b6e2-f029edb93acb | -3.22333 | -53.13746 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f584b47b-e941-3116-b5e3-b15265188aaa | -5.29862 | -43.28122 | 2024-12-11 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b266e49-579d-3420-8831-825450a4e693 | -2.881 | -54.0221 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f9465f-7c79-3832-91f3-d5f2c47bad7c | -2.45858 | -53.63677 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60794b58-eb1b-344b-8fb7-29fcea100c00 | -2.78341 | -52.86311 | 2024-12-11 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edf05f39-0063-372d-9dc1-4e284de4154f | -3.24326 | -53.91589 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c311fa35-f47e-3a6c-a169-5e302faae4dc | -2.78953 | -52.8676 | 2024-12-11 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6786f16b-1552-3477-a675-f8bc8d545806 | -2.46445 | -53.63752 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7a33886-d16c-3c20-aa0f-b21b974c024e | -3.11291 | -54.07602 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1de19914-baac-34ca-a29b-659e894d0d50 | -2.53662 | -53.9965 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4eba98f-72a1-37f0-9cb1-a64fa6cdbf20 | -2.37545 | -53.83994 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5704ed7-0110-3157-974a-3af20da3781e | -3.07764 | -40.04847 | 2024-12-11 04:55:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5ca5c06f-5810-3044-9fc7-89f9f3d7f300 | -2.4639 | -53.64098 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dec0a37b-8d03-3dc8-8878-f8e707f06cff | -2.70074 | -54.2406 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04944d05-41ee-3a7a-9931-9db8a205adb5 | -2.8085 | -53.06556 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c273e8ec-8213-343a-b94a-2a9c5214f5de | 3.22821 | -61.19149 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e30aef6-df67-3a35-8625-ee8d53c098e1 | 3.23233 | -61.19699 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 31f1ed95-94b1-3aee-bf71-ac16f905c5a9 | -3.11792 | -54.08749 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a451626-9ed6-3946-95b7-8cf7a08f2bae | -2.41049 | -53.66111 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab4570ad-ccc5-3f18-a4e2-3f60352cb897 | -2.81509 | -53.04533 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe9133c9-2b80-303d-8085-0be246cf61b1 | -2.82899 | -53.06521 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7dd5004-81a4-3545-96c2-d6ef0528a4fc | -3.60163 | -53.72382 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1058c63-19d4-3b84-9c65-923bbd74b011 | -2.95591 | -53.12094 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 809d4df5-14b5-30c3-a792-b4693289ad7e | -1.41235 | -55.13675 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4af6e1d2-6bbd-3e21-a7ed-8a5fb6a57d80 | -3.12071 | -54.09148 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b13354a-5591-3fc7-bd64-b35082962ea1 | -3.48485 | -53.82241 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b17cde23-b7ae-3243-ad9c-2e6876018c8f | -2.25909 | -53.8467 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c0dff25-5030-3d28-ba25-112ed71c1444 | -2.82458 | -53.0716 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c48d3b0e-476e-3c7b-9924-fc53aa015081 | -6.94561 | -42.99963 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8fb3e7f1-86e2-3738-ae5a-dbd95eabd9c8 | -11.11067 | -54.62767 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb704f46-2e6f-3cab-8b9e-f3dbecd7495d | -6.96066 | -42.99082 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 1bee1210-1e3e-3381-bea8-a7f74b48748a | -11.10623 | -54.63424 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91aec02d-d75e-3e13-a8fe-5dbb91921de3 | -12.19459 | -46.71907 | 2024-12-11 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4812358e-c7c3-3108-8f0b-7119ef9643ab | -6.96481 | -42.99772 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| cedafc6c-6d66-3ba3-9545-bd90b9042255 | -6.8362 | -44.38745 | 2024-12-11 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 449b4ecc-f696-3e4c-8245-c54accbffd8a | -6.97844 | -42.9902 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 8102785b-b324-3ad0-92c6-c049ef106a2f | -11.1012 | -54.62253 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5b8af7c-d339-3f74-9141-16ff16b999cb | -11.10175 | -54.61898 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc4909b3-a177-396e-ad81-e81157e11367 | -12.05696 | -46.88638 | 2024-12-11 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3891e96-ab06-3d4b-af97-a64fec268fe7 | -12.41591 | -43.79739 | 2024-12-11 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 369c19a8-251a-3f71-a82e-df9f0891afd1 | -11.11794 | -54.64699 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8023ee2b-a3a2-3503-93a4-655eec35899a | -11.1157 | -54.63937 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e6923395-e5de-39a2-a137-9f84f053ee68 | -6.97717 | -42.99974 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 6b23a7e0-9473-3782-ab25-60baec801715 | -11.11848 | -54.64345 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d52b6627-72c7-33fe-b95e-683d9a81d620 | -9.82939 | -63.09952 | 2024-12-11 04:57:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e427f2b9-31a8-359a-aaa8-4eecaa4e1949 | -6.83052 | -44.38683 | 2024-12-11 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bd1e708-20d1-369c-8dec-38368086c5ef | -6.9518 | -43.00057 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 02c82d3f-0dd2-331f-8707-68dd4509ccbc | -11.95288 | -47.84189 | 2024-12-11 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37193d6a-6836-3239-abe8-b2672d36edac | -11.11903 | -54.63991 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5072cbca-6095-3fcd-9e77-1f1bf91bd6fa | -11.10234 | -54.63726 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c5b20db-18a5-38b7-8215-c72caa110dca | -6.6572 | -54.9426 | 2024-12-11 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 534e025b-8ac1-36e4-b085-295a9e4483c5 | -12.19401 | -46.7191 | 2024-12-11 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54afa46c-55e8-35bf-8ec1-3e26f4b63700 | -11.11515 | -54.64292 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6fa5a768-6365-3320-838e-6f496796bde6 | -11.11291 | -54.6353 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5bf14c6-85c9-3586-92bc-604df19cb383 | -6.90772 | -43.51869 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3e87683c-9c68-3b58-9ec4-b74a44859971 | -12.66612 | -45.67031 | 2024-12-11 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 44b02481-4764-323c-b086-a48a00911de9 | -6.94624 | -42.9949 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 343aaa90-eb22-3e84-823e-13da654c4aed | -6.11986 | -42.53603 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 856936d2-e2ec-32da-9087-7c0918cd9448 | -9.25603 | -63.26224 | 2024-12-11 04:57:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 38b1d3e2-9add-34b5-9a1b-183f71b7e0e4 | -10.83765 | -56.63132 | 2024-12-11 04:57:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de3ee368-b4a4-3993-a2ca-f9133a8176d7 | -6.90948 | -43.50555 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 12616fd3-83a8-3034-8c20-e554dcce0efd | -9.48181 | -61.86354 | 2024-12-11 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f6d9ab-799e-35ba-a512-dddf0793610c | -6.95862 | -42.99673 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| dfc0defb-e084-3119-a7d1-9ec6201e6da0 | -11.49415 | -48.19819 | 2024-12-11 04:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaf6d20a-72e1-36da-bbd2-2b25ff04f880 | -11.48948 | -48.19751 | 2024-12-11 04:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a201df9-099d-3d0b-9bf8-660b28d7e8d6 | -6.95315 | -42.99942 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 85849ac0-dff8-3d5c-9829-4578c520852f | -12.19498 | -46.71585 | 2024-12-11 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94c7d7ba-eafa-3426-9c6b-f4bfb5ebbe4d | -6.90407 | -43.50031 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4f46e6ab-ab87-3fbd-8478-ebc0dcea21e6 | -11.12127 | -54.64752 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7926bcb-11cc-3141-ba93-fec05a08dbac | -11.87669 | -43.71845 | 2024-12-11 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d919459a-f9ce-3461-bd26-40a27b1053da | -6.96132 | -42.98605 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6970d0ce-a0c2-31a7-92ef-0ea176e2c1a6 | -10.02853 | -53.74827 | 2024-12-11 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc7fdb5e-7f74-304e-8370-a5dbeeb6741e | -12.19442 | -46.71589 | 2024-12-11 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ad1a790-4754-3409-b966-5a9841738be7 | -6.12124 | -42.52602 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6747aa6e-4b31-3301-8acb-3ed4729da659 | -12.85134 | -43.81829 | 2024-12-11 04:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22bef7ce-633d-3ca3-8685-9a2d0f5bf204 | -6.12687 | -42.53183 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c9404714-f6c6-3d9d-aef6-f5c50447e955 | -11.10678 | -54.6307 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9647ec3-1b35-3667-96bb-eb958a31502c | -12.67175 | -45.67099 | 2024-12-11 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e28048e7-d4f6-3b72-b96b-46c71e6d339a | -6.97098 | -42.99876 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 3d2a3ad5-32b0-3a62-917a-afa66545bcae | -6.89633 | -43.51251 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0993acb4-0f77-347d-87ae-cd4d79f46b01 | -6.90348 | -43.50471 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8ca47fb1-375f-3dcd-a7fa-0f54a4d72c27 | -6.96 | -42.99557 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 8fece2e4-bf71-3a61-b608-dbc692c73f6b | -6.97655 | -43.0044 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8585bd71-e85f-31b4-8c98-c47e78f9d341 | -6.9089 | -43.5099 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 15ec6b92-bc64-3864-9759-b94a7b3b0ea4 | -12.05563 | -46.88616 | 2024-12-11 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70f19bba-e41e-3755-b1cb-4f0a89ca19b9 | -6.90173 | -43.51783 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c9d69995-5bb3-3d36-8e61-3b1713c2c193 | -6.94631 | -43.0032 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fc373b34-77bd-384b-a374-f861c755f293 | -11.10957 | -54.63477 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75bc88f1-0ba0-380b-bdb6-30c3613cd507 | -12.67221 | -45.66715 | 2024-12-11 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 33378127-bdd8-32ab-bb28-90b0f837ebcf | -6.91068 | -43.49667 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 61a7d1fd-06f6-319f-b952-1180e0dadd4e | -9.71352 | -54.89241 | 2024-12-11 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4036f98-6133-35e3-948b-1bc64a1e954a | -6.91008 | -43.50112 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a8793dc6-756c-3ada-93a0-3d7657fbca70 | -6.91128 | -43.4922 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 663dc66c-4ab5-39e6-b028-988d90ff0049 | -6.90831 | -43.51427 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 75b58f11-fbb2-35cd-b2f6-235c0cfd8421 | -6.66109 | -54.93964 | 2024-12-11 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05eaa9e6-60e7-3f02-94fc-5e5e00fd9172 | -9.47724 | -61.86272 | 2024-12-11 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e22536ac-b1d3-3ee3-b129-92c4fbe5ea59 | -12.41535 | -43.80249 | 2024-12-11 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d86cfb6f-c19a-3617-9746-a556b7429053 | -11.09398 | -54.62501 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bac1b214-8a26-3f74-9764-f3e10ab4c8c0 | -12.41379 | -43.79655 | 2024-12-11 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
