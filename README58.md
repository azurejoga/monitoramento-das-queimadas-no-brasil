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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb6929a9-74ac-3a10-a420-15f118a85948 | -7.80967 | -45.11835 | 2026-09-18 04:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 796a2bf1-8b2a-3bb9-be1e-4bdb79aba92c | -6.93891 | -43.11493 | 2026-09-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71a7d5ad-bbd3-3093-8e6d-aafb2d7aef8f | -13.25609 | -46.90149 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 502e83a9-01d6-3255-a64a-7440e95db970 | -4.79104 | -56.12012 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff3c7939-e29a-3232-b83d-b6467355ee82 | -7.22727 | -44.21436 | 2026-09-18 04:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b120d74-9470-3186-9986-fdbec80a1563 | -10.16387 | -45.36868 | 2026-09-18 04:57:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ef61f28-5b85-35bc-8d0a-99067a2b27bc | -7.81339 | -44.90684 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46fb8e4a-8785-37f0-a417-22bc7ff746ad | -10.59606 | -46.55183 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 285c50cb-b7c1-3fb0-8621-eeee2a5659dd | -11.27747 | -43.51733 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f252906-613e-3412-ba98-38c411ff55cb | -7.88019 | -54.7234 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63a2466b-9f19-3b18-b66c-fa55af0071d0 | -6.32432 | -55.27449 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b6b4dac-727d-3da3-b256-209b48caa2f2 | -7.03533 | -42.07876 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4c7d092b-25d4-3c0e-a205-406a17158fb8 | -7.34982 | -44.63438 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8edc7221-b32d-3032-8ddd-0fcd57a14994 | -7.82095 | -45.10268 | 2026-09-18 04:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 439cd5ea-7124-35c1-bda6-58995df9f2dc | -7.45715 | -46.84209 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90634a68-3013-3af2-a021-a84ab4f59e9b | -11.2296 | -43.42804 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82d46af8-6bcb-3dd3-98f8-4208a550609b | -4.8817 | -56.06247 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ed37dec-2a48-3cb5-9bac-22d64567f048 | -9.39784 | -46.85689 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 314ee2ae-4649-3ff0-b897-6781b3a436c3 | -8.44515 | -45.7052 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3dbb215c-b311-323f-9f2a-0af8d70a2570 | -9.39533 | -46.85249 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e0ae0f5-1789-3a11-b42e-371e88eadf55 | -7.06254 | -47.48869 | 2026-09-18 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cde9d01b-0a29-3ff1-8bb7-87eb25499a00 | -7.80053 | -44.83761 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4b2ac27-856d-30e0-bfe9-057ba7c446ba | -8.93841 | -44.39661 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0e11e61-7082-338c-be30-fa9aa3a14180 | -5.98226 | -53.58323 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52fdf16f-fc17-3d96-a949-c89600622e88 | -8.88236 | -45.88409 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e36fc707-317f-30da-8b0c-e26506fee211 | -8.53934 | -44.55223 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6f3faa8-5e90-37ef-b3e2-050466828600 | -10.52021 | -46.73023 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a5b2b00-0604-3d5e-a15f-c7883b8dfb78 | -7.79561 | -44.9039 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 121dff26-3a35-3219-b346-2368943cf144 | -10.64955 | -50.24202 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29faa8a4-9e26-3e19-a664-19b700c42b76 | -7.58859 | -44.94516 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 794aeb40-af59-36dd-b22c-d1ed48d6d027 | -10.8324 | -44.96004 | 2026-09-18 04:57:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f92dcf7-899f-3fab-97d6-67fe5cc99cd4 | -7.36826 | -44.46882 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1843eaf-916b-30fe-b8c3-5797f81e60de | -10.83236 | -54.10118 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad37acc7-8906-3903-8418-d81cbeb28835 | -9.10472 | -45.71964 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa3714eb-4258-313c-89be-b923b32be5d2 | -7.45247 | -46.15965 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64b5d999-1d8f-3f9f-a960-bf5d6c681c1c | -6.65843 | -50.91282 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4550364-d2b5-3a36-97a1-09562d58e61c | -8.71326 | -44.87952 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 881dfede-6781-3e6f-ad8d-8fe655f17461 | -12.16615 | -46.99174 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b41a188-4181-30ef-9c87-2e237dc25731 | -12.39414 | -48.46569 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 694cb45a-756b-3f7f-a2e1-6d2a0955a5a7 | -7.8013 | -44.89595 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| babbe77f-c5ac-3e9b-89bb-1b6eaac7c398 | -9.46529 | -45.44852 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da4ae5d3-e946-3cf0-b5db-e21705a38639 | -7.67898 | -46.10609 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0cd9c13-dc04-3102-a4c4-b7a07992aef8 | -12.25594 | -50.74923 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1e55faca-876b-38f9-9bba-bb2100db3f11 | -8.90942 | -45.01035 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3877b9cf-5cd7-3548-96ad-e62ee059fde5 | -10.32881 | -45.31179 | 2026-09-18 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba9bec35-a4f8-35c3-a604-071460139725 | -8.9941 | -50.1679 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574f94db-91a5-3282-b9f2-be0109dac9c9 | -8.71166 | -44.88182 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df7e4bcc-89bc-3112-a95f-0f2346d660a3 | -8.93913 | -44.3914 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26e61846-434b-357e-aa02-22758542c76a | -10.64898 | -50.24575 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6507cd0c-ba5e-377f-a69f-5cd0b78dc008 | -7.19951 | -44.10744 | 2026-09-18 04:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 045e2d34-3d8c-30e7-a36d-58e43a4e4042 | -10.90196 | -53.992 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c569a40-f2cb-3d9f-9b57-4f8205ea6355 | -12.57288 | -47.0929 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbb89ba6-85fa-3ce1-8084-fa896496f252 | -13.24983 | -46.91634 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0eb2c875-e24e-32c3-8ef9-e134751f15dd | -10.66775 | -50.4877 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09085cb6-b111-3229-a023-57695500afc1 | -9.94426 | -45.29038 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8fcbddd-5ea7-35b2-86a2-022318470990 | -7.49559 | -55.01017 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e255115d-65f9-3dde-a6a7-3cde66c2b72f | -9.7769 | -46.09068 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f595c51e-dab2-36d8-8a7a-62864f0b6a81 | -9.68933 | -54.33378 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed15bad7-27c7-35f3-acf5-675da9a77a0e | -12.5349 | -47.09377 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0b9d0a5-fad4-33d3-b333-3f738c085475 | -12.3825 | -48.47138 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4dd7972-9ea6-3e43-bfb1-fdd93c9dcbb6 | -6.33343 | -45.68496 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b709da37-4aab-3702-98b1-edae1910e86b | -5.73721 | -52.23997 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec88d2b0-007d-3635-9d7d-940c5db3b6d3 | -7.08543 | -42.08946 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90da8cf0-abf5-3eb8-99c8-45eb31993b06 | -10.63928 | -50.24041 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03f92540-f255-30af-96b8-1321bde7b338 | -12.31475 | -50.75006 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d130a41c-2e04-3d2c-897b-f5f0f208adcc | -9.75469 | -46.095 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c1c70f0-0e7f-3aa0-80de-5016a9183891 | -10.61503 | -46.08048 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c15d0e84-b8fd-350f-8c5a-5c08d92864dc | -11.24454 | -54.20786 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9cb6982-cd26-3d5e-a7c5-7a50498b935a | -11.88043 | -47.61205 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4de8682-9796-3e8b-b0c8-19ead49d004a | -10.66154 | -50.25536 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ac3e483e-856a-3542-8179-12c06de75749 | -6.02944 | -51.80877 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f4fed72-7819-3d79-afed-518c7c68131e | -10.51457 | -46.74059 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99df9146-869d-33dd-87e8-96b44ed5a185 | -9.78476 | -49.1772 | 2026-09-18 04:57:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb6c4afd-3ab7-3961-be45-8ddeccdf267b | -9.93967 | -46.54564 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7fd83ce-308c-3764-8c2a-c8cbee48f999 | -4.79334 | -56.12386 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ad30b40a-c562-344a-a987-2c5c32e9d1ae | -12.25253 | -50.7487 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 908fb767-ae20-380b-8256-8f285b8fc9ac | -8.9049 | -45.00983 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1ed9d1b-54a9-3ddd-90f3-2969ea871b69 | -9.71799 | -54.81079 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8418173e-15c4-37d0-b564-36d4927e09ce | -9.19073 | -46.74641 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3d5f118-2c90-3118-ac6b-de70952bee55 | -12.3119 | -50.7458 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a9639de-14a0-3985-903e-6e9cca0b42c0 | -9.95259 | -45.28049 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f325789d-ece7-37f4-8e3d-7b64b7a0a925 | -7.0729 | -43.58155 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7212466-7c4d-3fbe-b4db-53c750d09e76 | -6.23388 | -51.71207 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e97cc3b-ac38-3f19-9fb3-00a289251d7d | -10.6467 | -50.23775 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| efaa41e4-be56-3311-b584-fb13e0297511 | -13.24711 | -46.90438 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2c27b4fb-9b00-3341-a194-9843912cdecf | -10.66832 | -50.48402 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 427d848c-0b88-376f-bfdd-567a95b02c12 | -11.29391 | -43.34708 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 694ab230-303a-3e40-be73-0b1b25e75a8a | -10.23936 | -50.91493 | 2026-09-18 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f607e091-b3f2-3836-9ce2-e0615e8b3514 | -12.55548 | -50.72607 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fffd9f40-accd-3600-b92c-be803a3a6c62 | -5.17271 | -56.18219 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be0c8d6c-7841-3e00-92b6-21fb64eef74e | -7.34084 | -44.62577 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41583888-a03d-35a4-a765-455bc732a5ed | -9.71439 | -54.81023 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 87107cff-7eac-38c9-aeeb-8525fcd812a8 | -11.31408 | -47.25523 | 2026-09-18 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b52b99b5-55e4-36c4-bbc6-b6c28255c23f | -12.99776 | -46.94292 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d88ea77-58fd-3858-bd4b-55505cf96a26 | -8.68077 | -45.43639 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 342aa3a0-2aac-3132-9faa-ffa5071a5543 | -8.49187 | -44.5615 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55adeec2-45a5-3133-8692-439fa52e56b1 | -9.74506 | -46.10213 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57285e45-1a49-32ce-8208-88ad628310a0 | -8.90363 | -44.97387 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 353fbde7-2be9-3fa9-be42-4e35160f7863 | -9.48448 | -54.48158 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e4c68af-d592-3cc5-affd-fd65207acc91 | -5.94174 | -52.22792 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README59.md)
