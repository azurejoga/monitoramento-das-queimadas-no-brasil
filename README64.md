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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c7ba857-9fc8-3143-a89d-3c733e5a9890 | -3.03979 | -53.24674 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff61dcf1-ecb1-3574-9ce5-a2b645dd6b06 | -3.03922 | -53.25031 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6db4c7a5-3573-3f87-91d9-4d38d35c5799 | -3.00647 | -52.18494 | 2024-10-15 04:49:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 775eb001-6a27-3c71-8457-272963fc93d2 | -2.98602 | -53.21623 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f2a6ec3-62ed-33b5-9047-222edeae11ac | -2.9846 | -52.90765 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9a3ba66-6cc6-30f4-9308-9ca23e51f815 | -3.62593 | -52.69694 | 2024-10-15 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5b0e21f7-cd31-3eee-a053-86094b4d017c | -3.49275 | -52.80767 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff954a06-965b-35cc-b66e-24cf853950e3 | -3.47446 | -52.88 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2162a30-d09e-3f17-81bf-9a94645d7f1e | -3.42378 | -52.72903 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9581acde-c12e-3afc-8546-f32001578050 | -3.41991 | -52.73199 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90da11c0-873a-3842-b760-37c699f3c947 | -3.41936 | -52.73549 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7807d481-53d7-39e9-8e0a-6363905e5255 | -3.29069 | -53.12144 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f09c7c74-9009-3f70-a0fb-45c48a64995d | -3.27606 | -52.58869 | 2024-10-15 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5395709d-74e9-36c2-a6bb-08254245cffb | -2.86645 | -52.47066 | 2024-10-15 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eae9651c-d2a2-376a-92ea-16c65ccc7b9e | -2.86312 | -52.47075 | 2024-10-15 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 867803fc-2daf-3f34-abc5-209eab7762d2 | -2.8598 | -52.47023 | 2024-10-15 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f652a2aa-075c-354b-b66c-3b3fa263425b | -2.85926 | -52.47369 | 2024-10-15 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 604f7af0-75ca-3b02-95c1-f4d5c0ea566c | -2.84649 | -53.32313 | 2024-10-15 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb815e73-a705-30ef-945e-a59f9544d125 | -3.89925 | -53.39878 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13528f45-a666-3d0d-acb0-11c58a0f08bb | -3.89869 | -53.40236 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62f701fa-7831-3db3-920a-c13d0297c923 | -3.89804 | -53.4941 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be8ca303-a206-328e-ab8a-b46357bf6a2c | -3.82518 | -52.40219 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c95e630-1990-368d-a1d9-7943bf726ff7 | -3.82296 | -52.39478 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b47cea84-09d7-336a-9020-cf49ad61eb56 | -3.82241 | -52.39823 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c0c14a-b58c-314d-98a3-4247e5ac4888 | -3.82187 | -52.40168 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 745d816d-f30f-3bd8-9ceb-4e8793be2ed7 | -3.81911 | -52.39771 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d82b63d0-894c-3b52-8184-37fa2dd7abd0 | -3.81856 | -52.40117 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2ae6d71-41f3-3983-b694-4097765553c8 | -3.73659 | -52.31779 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7716e6-9311-3116-a00d-fdde948b4710 | -3.73329 | -52.31728 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 250f8127-c7fb-30ac-9744-3dbadb4e2247 | -4.32745 | -53.86533 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ba037a9-6a92-3727-939d-1a10449c3b5b | -4.21523 | -53.50747 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27bf72f1-0839-3f35-b6d7-7a14dd4e4449 | -4.16974 | -53.53331 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c682f4e5-292c-34b1-9554-cb014d309a74 | -4.16917 | -53.53689 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04636879-def2-3ba5-a026-1cccc621891a | -4.14567 | -53.88223 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 011b563f-9df3-3786-aba6-071e159c764c | -4.14227 | -53.88171 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f744993-2c61-3163-b4cc-0fdf3e8581a4 | -6.09809 | -53.22206 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecdadb6e-c7a7-3b60-a4ba-7883a9d12ee0 | -6.04216 | -52.75874 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db91abbe-6a90-360d-8cbc-9b9e28f5d7d5 | -6.0051 | -53.35761 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 722b7e9c-7b38-359c-af55-3701bede68b0 | -6.00233 | -53.35359 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 946eb538-00d5-3c2c-9919-77a27b441fcf | -5.91351 | -53.31451 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a8aea49-ea43-3172-a79a-3c1b458ee82d | -5.91018 | -53.31398 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b3e0cd-784d-31e2-9013-ebad51fe279e | -5.63721 | -53.87742 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef0b964d-ae7c-3bb1-9225-f11e11e9bd10 | -7.81171 | -54.11623 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a47d978d-91f6-3039-be8c-a0f5918bd4aa | -9.00844 | -54.51341 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 783737d3-7cde-3b36-9d9a-b23ddb4ca05a | -9.00681 | -54.50209 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 4a22ee44-5abd-3f74-8128-5ca38b4fdb96 | -9.00623 | -54.50569 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e3f45f92-bbf5-3aca-9227-3767919db6ae | -9.00566 | -54.50928 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| de440bc7-3447-314f-9374-bc3646136e6a | -9.00346 | -54.50155 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e0e9895-fc7e-3161-8675-08625791b98a | -9.00288 | -54.50515 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 553b92ad-8fd4-359b-aae7-c751d0073a13 | -8.98955 | -54.58792 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fec9a22-f7bb-3fc4-b1ca-ac5a784922fa | -8.98897 | -54.59154 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8a731ce-afd5-3ccc-ad1d-7a3b3dc2a786 | -8.98676 | -54.58378 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dee3d7f6-2919-30a6-89da-d93b62309929 | -8.98618 | -54.58738 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 059075c2-36da-3d32-8f5d-8890fa1dce93 | -8.9856 | -54.591 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c48703ed-6289-35b8-8aa6-95793cecf3f4 | -8.98282 | -54.58685 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e340b633-8e22-3c1e-bce8-9b8c6132ea31 | -8.98224 | -54.59046 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e0eb2625-89d7-3278-a6f9-d9d4e09491bc | -8.97945 | -54.58631 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f26831e0-daa5-36ee-bd17-ff58aeeb2725 | -8.97887 | -54.58992 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6d135b1c-902f-3658-bd8d-4453bfc23a63 | -8.53502 | -54.77314 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| feaa2019-31b5-3c03-a63a-139e31f157ad | -10.03947 | -54.33644 | 2024-10-15 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cd72196-6cd4-3556-b32a-8a5cce51b8a1 | -10.03891 | -54.33998 | 2024-10-15 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2cf9d059-cec8-3b43-89f1-e5e82cc7cfce | -10.03614 | -54.3359 | 2024-10-15 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0f1e489c-284b-39bc-9a99-38d8573a8c6e | -10.03558 | -54.33944 | 2024-10-15 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1fcd4552-6d2f-3b26-ae04-77f6e9a0d7c7 | -10.03502 | -54.34297 | 2024-10-15 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 97c020c3-ee41-3e40-893b-86ec717c2829 | -10.03225 | -54.33889 | 2024-10-15 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 98c9535f-1c4f-33c5-ba28-7751ebdaf22b | -10.03169 | -54.34242 | 2024-10-15 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a7d65643-f9c0-3f12-b7b3-e352b9a31751 | -10.02836 | -54.34187 | 2024-10-15 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f650617-fb45-324b-96cf-1715759c6269 | -3.60147 | -53.95328 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75691d2e-6538-3fda-b9b4-32ab9928b676 | -3.59011 | -54.66994 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dde27e0e-066c-37d5-b73f-48ef5a293d05 | -3.58658 | -54.66938 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 295b7a8d-0970-33ad-a1e0-5b88e7e6db67 | -3.50449 | -54.6846 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8b7c0d9-0c95-3087-9766-5d38f498b410 | -3.49444 | -54.451 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 149cb353-dba5-3318-a8d0-e42757d7ec66 | -3.49383 | -54.45488 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 597b781f-2077-3e25-b216-6eba8f611060 | -3.48971 | -54.45821 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9f37b36-8112-38b1-9b1e-a7a732852e1a | -3.42779 | -54.66538 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40fd42c9-9e94-36f6-8436-b3c7d46c3a08 | -3.42715 | -54.66937 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc6be752-0f64-37ad-b12c-4bbaeee293e0 | -3.4265 | -54.6734 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0ba0d0a-adfc-316e-9d16-00ea72aa5793 | -3.42425 | -54.66485 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81da9a8c-7e54-3cb4-a9c9-1c0c33ee3a32 | -3.42361 | -54.66883 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab90bc22-8496-3cd3-9940-8212bea4f64e | -3.42297 | -54.67285 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7d8acb4-9896-3443-ad9a-810b297c8f20 | -3.41943 | -54.67231 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bc5ac04-44ab-3787-aefd-946fa96a72c5 | -3.41878 | -54.67634 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5fe093d-c7bd-3acb-9944-9d8a301e1542 | -3.35463 | -54.71644 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58ffd920-8b33-3fd1-ad57-4f7076c2cc76 | -3.35419 | -54.81146 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d96c061-7905-38a5-8fe1-8ecb3310c3cb | -3.35064 | -54.81087 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 729c2724-b898-3287-ab94-f2c51cec571a | -3.29831 | -53.85317 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efcc6a3e-4941-3604-bbbb-37b2316e5b8c | -3.29828 | -53.85272 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2856dadd-583b-349d-ba6d-f53f55cc97fc | -3.29772 | -53.85688 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41673dcf-46b9-3636-bd6e-9b8a77dd2bc7 | -3.29768 | -53.85642 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85c3a992-87b8-3f94-be8e-b4a4c818fb72 | -3.29547 | -53.84892 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b83aace-9260-37cf-b0f9-18edcc0875c5 | -3.29488 | -53.85263 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b343264f-b60f-3ca1-aca7-c4b64a6fcb91 | -3.27605 | -53.706 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac6a2889-635a-3653-960f-71436b22da5a | -3.27039 | -54.17977 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc9b963b-5c9d-3016-b1a1-055c5b1c2918 | -3.26632 | -54.18299 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67f85a65-200b-334f-bf03-01d451f6c850 | -2.83257 | -54.60565 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3e03704-de16-33c2-91c8-b3774af0a075 | -2.83194 | -54.60962 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55c129c7-141c-356f-95de-3687eefb50a0 | -2.82635 | -54.04623 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95459ed9-958e-391d-9142-1b6e6d1f7d71 | -2.8111 | -53.98558 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 032e751e-2a41-334f-99b7-d268b4edeb89 | -2.80592 | -54.0859 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b56487d-b881-3ae8-af72-4ad980124bd3 | -2.77537 | -53.98773 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README65.md)
