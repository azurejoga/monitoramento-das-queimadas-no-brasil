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
| 13a78242-144f-3526-b169-174a3ea005c1 | -6.89208 | -44.67677 | 2024-09-29 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff4e9625-38f1-34b1-830e-73f7b87f27ad | -6.78109 | -44.66608 | 2024-09-29 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8439165a-a8fd-363f-8eee-d83d9ed38d95 | -6.77797 | -44.66058 | 2024-09-29 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67c8e93d-2014-36a8-aca2-656901e3edea | -6.69616 | -44.54685 | 2024-09-29 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2f04636-a9d6-3ae5-8519-79766363452f | -6.61443 | -44.67551 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3434abd6-e3cd-3976-8b7e-2d5f6ac3c209 | -6.58666 | -44.18017 | 2024-09-29 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d65647b-1d0e-3bab-8e88-032ec381f2bf | -6.58286 | -44.17941 | 2024-09-29 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16b3f061-d9c3-311f-9933-2c7a87174287 | -6.58208 | -44.18421 | 2024-09-29 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecd208c1-92da-36fb-9f2b-059078193eb4 | -6.57984 | -44.17392 | 2024-09-29 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da72ca45-dd77-3a65-b5ae-d13b632e8cc4 | -6.57906 | -44.17864 | 2024-09-29 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 484ea461-b597-35b8-a3d0-28b7b3dcf232 | -6.57603 | -44.17323 | 2024-09-29 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d469cfec-55b8-329f-98cb-84130bfab949 | -6.53703 | -44.29052 | 2024-09-29 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84f3938b-7fb7-34d0-ad16-478d90d3cd57 | -6.53478 | -44.28024 | 2024-09-29 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37ed5a4c-dc8a-3ca9-a6fd-4a6f828977cc | -6.53398 | -44.28504 | 2024-09-29 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4062f51a-018c-3741-a1c3-cfacf7169a40 | -7.59469 | -45.07669 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40258761-21d0-3320-b7b1-3cd1990bfe8e | -7.59354 | -45.08352 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65c3cb06-6990-32af-abce-4a409d6ab7d5 | -7.59131 | -45.07252 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb45e505-35f4-307a-bee7-9428ea492b64 | -7.59073 | -45.07594 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c6c13f8-d137-35d1-bcc2-9a319d800dbe | -7.59015 | -45.07936 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d76fc0a8-9ac7-33a6-9147-448e2a392bdc | -7.5886 | -45.04019 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 098601da-c0e9-3e59-a5f2-3f52c1f49996 | -7.5885 | -45.06493 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dca5a769-7c1f-323b-a248-5cef3933f332 | -7.58804 | -45.04353 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 359ab0b0-0a8f-3ef9-ad35-446cc298e1c4 | -7.58792 | -45.06834 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e70f3cd-fd32-37e4-ac09-a1b3d9b30b13 | -7.58735 | -45.07175 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f383e83-6418-37e7-a966-232e04a2cfa8 | -7.58001 | -45.0668 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d24f0ff9-9216-36c3-aea6-b7aa64eb27ba | -7.57942 | -45.07024 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e4a7676-3bcf-3709-abbc-0d2f30968357 | -7.42867 | -45.17106 | 2024-09-29 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a91baa47-2761-3876-ab3c-66610d6d604e | -7.30262 | -44.96945 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 535bb43a-b29c-33c5-8e2e-72f8ae48e673 | -7.30206 | -44.97284 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9edf572e-ec10-383c-87b7-85ed316645a0 | -7.30149 | -44.97624 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb9cd404-634b-381b-b9c0-8f10c42ee96f | -7.29922 | -44.96537 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ca17684-fe6c-3eeb-9ea2-17cad830188a | -7.29866 | -44.96875 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae615235-60b2-3ff3-adb7-fefabc4881f7 | -7.29809 | -44.97214 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6c9ab104-3c5a-3c7f-afc6-79e3e601a488 | -7.29753 | -44.97554 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2c246b72-00b7-3a5a-ae54-d435ecfebbba | -7.29695 | -44.97897 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bc77cf4-5b5b-3f70-9096-13fef7fbb5a6 | -7.29412 | -44.97149 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 68938d64-71bd-3ae5-8394-06d52cb32ca8 | -7.29355 | -44.97491 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d1e7534-b0ee-3440-af51-12eb9a8c6e55 | -7.29014 | -44.9709 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a84e1006-87ef-3454-ac0a-98e95eb552af | -7.28957 | -44.97432 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04e80cf8-9b96-3df6-a1f3-5be68b535955 | -7.28317 | -44.98809 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9aefe7b-78e7-36bc-b7d8-15668b6dfcc5 | -7.28258 | -44.99155 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fe9baf6-3a18-3313-bf35-7820ac7c42d7 | -7.27614 | -44.93294 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ae1da2e0-a6f1-340e-afa7-f31f2624afca | -7.26426 | -44.93094 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9ff00f3-7afa-3b11-a247-b41d8f665e02 | -7.25961 | -45.03067 | 2024-09-29 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a95571bc-5c70-3bb4-bf2c-44696ba98d36 | -7.25798 | -45.0161 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec5fe18f-e7dc-382f-a76b-bf72a87bec42 | -7.2568 | -45.02306 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0ad7ff1-9e8d-30ea-a178-ea73d4cea06e | -7.25621 | -45.02654 | 2024-09-29 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7faf630f-834e-36fd-92cf-5e74ae8b80c0 | -7.2534 | -45.01893 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b2023a1-c55f-3687-b8a0-02bc345234b3 | -7.25281 | -45.02241 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9c0531d-2dcf-36d3-b2b3-1b9c3e4f26c1 | -7.25069 | -44.93887 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4c737b94-a9ff-3938-b802-31710a290f18 | -7.25001 | -45.01477 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f46010c-12b5-3426-95e1-438057a01b56 | -7.24994 | -44.94325 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d1dc1f3-e6ab-3c57-a13a-b785c7663993 | -7.24942 | -45.01825 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de3fda91-6c5c-3f14-b7fd-26f1ea622ca2 | -7.24882 | -45.02174 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcbf56fd-ae49-3401-a1bb-a67c83906a90 | -8.31802 | -44.97077 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b392607-701d-311d-9098-d460cf44376f | -7.24675 | -44.93808 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f649c407-e316-31f7-9c41-97140d968378 | -7.24603 | -45.01408 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 285700d6-071a-3852-be68-c72dc9415c2a | -7.24599 | -44.94247 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15ac07e6-8e37-36bc-9a67-284e7536bf90 | -7.24544 | -45.01757 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 743b15ab-6bfe-3238-b7af-f010f9dd29c0 | -6.95185 | -44.92056 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88cc8e50-a8bf-34fc-a657-317c334eb9bd | -6.921 | -45.05434 | 2024-09-29 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6e14088-840b-35e4-ba29-acc150a7a95d | -6.91645 | -45.05684 | 2024-09-29 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d366253-e77f-3652-af1a-5fea50007ce2 | -6.91305 | -45.05258 | 2024-09-29 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 407a5b4b-5f5e-332a-a27b-a57f4955ce17 | -8.51109 | -44.71216 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c4ad4f2-5b09-3a04-96ae-e68481d326ba | -8.51027 | -44.71698 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2476b9e5-ea73-3fe7-a140-778f44d0f86f | -8.50806 | -44.70673 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4a37d32-b555-3bc7-b579-a633735242f5 | -8.50725 | -44.71152 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74367374-609a-3bee-947d-f85fa53c9fa8 | -8.50643 | -44.71634 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c84b74c1-48ae-3b20-98d3-804b205e74fb | -8.30303 | -45.34271 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb7d6c19-6862-3a99-a17d-541db0149818 | -8.85875 | -45.06047 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b2e0a0f-da47-3935-9f53-f0e832431a7c | -8.80057 | -44.95444 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd2eac60-2a3b-3986-8e83-a000481b48b3 | -8.79926 | -45.1279 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abff4b34-ba35-37c5-a159-7a6688da4458 | -8.79587 | -44.95866 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06666d9d-6986-32a9-8992-93124ddb015f | -8.79534 | -45.12723 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4acecf67-24d8-3d56-a719-3ba6c255bf72 | -8.77059 | -45.15422 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5701be9a-7e3d-3260-b02e-d2aa779ed3a8 | -8.76713 | -45.17451 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5e8ecf60-2c44-3a0f-9ac0-aa0faf7d841a | -8.76579 | -45.15863 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e8b5f20-0522-3c0c-b432-9aeeeb4016e1 | -8.76493 | -45.16369 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fe7acf4-bad5-34ab-9d57-3086cfd84f82 | -8.7632 | -45.17386 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 625f2a97-cbfe-3b11-a7ad-d57628c7f815 | -8.76233 | -45.17895 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 84bedf3b-0ee4-3cc8-94bc-24bcf2098d0e | -8.76013 | -45.16813 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 81456b58-249f-3276-a6c4-ea04dd5b1ff6 | -8.75926 | -45.17321 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b5a20826-d829-31be-ab7f-ccea218a48ed | -8.75839 | -45.1783 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 3a943ffc-bdc7-3255-84e0-f2fd0d19e793 | -8.71664 | -44.8079 | 2024-09-29 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8600def-6589-3f13-bd07-7c654bb57326 | -8.63826 | -45.41282 | 2024-09-29 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9514e44d-b4d7-3b7f-87df-cc0c16794289 | -8.63424 | -45.41219 | 2024-09-29 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc99dd0d-95a1-3d11-8d58-ed3e95786384 | -8.49875 | -44.71507 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 970eb28a-d802-37f8-ae3d-7fbf4b7df65e | -8.48906 | -44.52105 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 49c5962b-e2f0-37f6-b992-bd4456a40d87 | -8.40031 | -44.65302 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a05be14-f833-3569-852e-bb6e2d4e7f3b | -8.18584 | -44.82094 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01dd3307-90f4-36e3-9ae6-0295b4960291 | -8.50561 | -44.72116 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 94634002-445c-3ddd-a296-425bebd928aa | -8.43066 | -44.61307 | 2024-09-29 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7257b576-0c18-3b3a-b8ff-4d9887da18d0 | -8.3175 | -44.97258 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d3e04d4-5cee-3193-b94c-c09b0517fecd | -8.307 | -45.34359 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f160c14b-b902-3a3d-91d3-d6601e849fb7 | -8.30363 | -45.33921 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abfcf9f6-8005-3e30-83eb-095eeb18a333 | -8.3686 | -45.37925 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24a8b450-cc66-3d0d-9917-769ad247a281 | -8.30423 | -45.33567 | 2024-09-29 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b39c82b0-ffcf-3747-8e4f-c87c69f7569b | -10.15789 | -44.91148 | 2024-09-29 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3a7c752-e93e-3e15-bdf0-b7726f9b18fa | -10.1571 | -44.91618 | 2024-09-29 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 912bb552-e14a-351e-aab0-e4492f842851 | -10.15409 | -44.91088 | 2024-09-29 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README23.md)
