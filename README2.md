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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8475d088-edf1-30fa-803b-d6c26c2f54d1 | -7.23282 | -44.79393 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6e18c19b-6b44-3c73-8b44-4945c293a671 | -9.50581 | -40.32447 | 2025-06-12 00:20:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.8 |
| f883084e-288c-31d3-9e07-af026c2559ab | -11.83983 | -43.79733 | 2025-06-12 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 08ac863c-6d36-3117-abbe-4df64b7611d7 | -6.94368 | -44.56579 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 0fc52ef2-2fb6-313c-bf50-02e3bb6c9ecb | -8.96486 | -47.9814 | 2025-06-12 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 73a05e4c-a695-320a-8687-ed6c7b2fa239 | -8.31516 | -47.91905 | 2025-06-12 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 90945eb9-f2fe-359b-9158-5caa57b9c327 | -13.04117 | -42.01006 | 2025-06-12 00:20:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 98884177-0ff3-3c28-a149-f11d18a96d12 | -12.76754 | -44.401 | 2025-06-12 00:20:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7e34f369-37ac-3e05-bdcf-32c77bcff6a1 | -10.69594 | -49.52456 | 2025-06-12 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 149399af-9743-3fc7-bda4-1cc56335df5f | -12.38545 | -45.7711 | 2025-06-12 00:20:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 03ee3888-7c06-3e2b-898c-a9878ca1b498 | -10.89781 | -42.24435 | 2025-06-12 00:20:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bfe93a09-1aa6-3bc4-be2d-131d163ba7b1 | -12.76886 | -44.41093 | 2025-06-12 00:20:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 92a58705-d69e-39c4-9671-222674a7e6f0 | -10.6942 | -49.51926 | 2025-06-12 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 1231a9fe-8566-39b8-a9c7-799db3f26f21 | -12.23911 | -44.16744 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 39b9a447-de84-394a-8888-1858019d4a41 | -13.90044 | -48.7431 | 2025-06-12 00:20:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| c20abb83-a1aa-3eb0-9e72-0e6f1eba18d9 | -7.46046 | -45.52605 | 2025-06-12 00:20:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 426bb56c-0a42-3449-b65a-551400c25cb7 | -12.05307 | -48.07922 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c6a0d169-2bab-3d36-85c2-e1809a835920 | -10.64698 | -49.44729 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5ac2994c-30fb-3c44-84b9-a2495522667d | -6.94725 | -42.80483 | 2025-06-12 00:20:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1a1beac0-74e7-32ad-a69b-03ea115e7f8a | -11.61302 | -46.995 | 2025-06-12 00:20:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b1af2cc3-31f1-37db-aa53-31df68e335ca | -8.66342 | -47.13764 | 2025-06-12 00:20:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 448b440b-6333-3791-bce6-f40ea5326055 | -10.6574 | -49.42547 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 1fa8f5ba-3658-37c6-be61-e386a022a7b3 | -8.963 | -47.96667 | 2025-06-12 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e1e788ce-44ea-3c54-83eb-075d4425e8ea | -6.60715 | -44.2578 | 2025-06-12 00:20:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b2fc1ed6-83be-3bfd-9787-18e7f01bf46e | -6.68663 | -43.9703 | 2025-06-12 00:20:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b47dd03e-abde-3a3c-b8b4-4ec09566f51c | -7.19243 | -47.4247 | 2025-06-12 00:20:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e3ccd700-2eb5-38ce-ba0d-8018dcaddfa1 | -15.92154 | -43.98494 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41a147df-54ad-3d26-97d0-f78bb8a69f21 | -7.23158 | -44.78476 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9562c47b-a76a-357a-bf14-54cc1e396e40 | -12.40355 | -40.90724 | 2025-06-12 00:20:00 | TERRA_M-M | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1ea22e88-cd96-33b7-aec2-d248752d5677 | -7.46971 | -45.52478 | 2025-06-12 00:20:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 96a994f6-b6d9-323c-b76b-0785aa6ed656 | -11.28119 | -44.6456 | 2025-06-12 00:20:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c3a05a2b-b275-331b-ae43-3e79f80e56e5 | -12.20605 | -49.63132 | 2025-06-12 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 5a8cde8e-527b-3754-8a11-1ab3174ee2ef | -6.958 | -42.80622 | 2025-06-12 00:20:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a0e5fd28-c276-30b4-b840-f2e8385a4aa2 | -11.33738 | -45.22404 | 2025-06-12 00:20:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ee4c0464-a9b2-38fe-8ef9-473b52cd4e2d | -10.66463 | -49.37813 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f1603b8c-e2e1-314c-93ea-88ff89ae85c7 | -11.57671 | -47.43808 | 2025-06-12 00:20:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 34530169-55ed-3c55-8fe1-bfdfe38de590 | -10.69338 | -49.50404 | 2025-06-12 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| ddc8cac8-5bce-300e-b216-513fc0adc927 | -13.0399 | -42.00105 | 2025-06-12 00:20:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0c4326de-59cd-3ea0-a748-1e5d8fa16e6b | -14.47214 | -48.6185 | 2025-06-12 00:20:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e5e27678-c89c-3d21-b39e-4af6b56504fe | -10.65645 | -49.42014 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1393e771-300a-3124-b9e5-988ccf20ec7b | -7.2393 | -43.10949 | 2025-06-12 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 7c6325d3-59cc-3121-bf57-55ba4f6c98ca | -11.84108 | -43.80661 | 2025-06-12 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8aca8a93-8ac6-3c82-beab-bff2d90730f7 | -13.5694 | -44.27613 | 2025-06-12 00:20:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3b619c80-8c1d-3f16-9b53-093caacf419b | -10.13743 | -46.76841 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f7054d5f-0a1b-33c3-9ef4-d91c6640e98c | -12.25114 | -41.38454 | 2025-06-12 00:20:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f8354e1f-6590-344e-9ebf-c08050b48c91 | -7.19405 | -47.43684 | 2025-06-12 00:20:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 374717d6-5304-3bfa-bab3-e75e00d1af78 | -13.4666 | -41.3095 | 2025-06-12 00:20:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 10f33da4-6c51-383e-8abc-0b5c0c50b0a5 | -6.75272 | -44.9911 | 2025-06-12 00:20:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e8287bf-57a5-3f79-a466-2eeb296b54e3 | -10.66229 | -49.35801 | 2025-06-12 00:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 4e1f855a-3e8b-37de-80a5-0773f0e571bf | -10.70719 | -49.5176 | 2025-06-12 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 11090bf5-1b2f-3246-aef0-35e1249bb7fb | -6.94491 | -44.57478 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 87cf07c3-08b0-33bb-80a8-83693c518119 | -13.54303 | -44.14747 | 2025-06-12 00:20:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| abfc4861-e653-3a8a-9248-b070f975bc56 | -10.2461 | -46.98109 | 2025-06-12 00:20:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5783ff09-7752-3d43-b82c-d905d5e09a0c | -5.64833 | -43.60058 | 2025-06-12 00:22:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c1bf5a2c-facf-359d-b9bf-cb9a0353b4a2 | -5.63951 | -43.60183 | 2025-06-12 00:22:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7ff01215-f2e2-3b6d-b442-730669af89da | -5.92356 | -43.46209 | 2025-06-12 00:22:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fd50614a-ac6e-39f9-bcbf-3e7fb53a867e | -4.55208 | -48.00642 | 2025-06-12 00:22:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 31bce644-14b4-3ed8-91be-f59bb9443774 | -4.55543 | -48.03165 | 2025-06-12 00:22:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 2839bd8f-4e15-3f80-adfa-18ec320e2b9a | -5.64956 | -43.60941 | 2025-06-12 00:22:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 6b14d114-6c1a-3d91-b44f-c3d1702a5747 | -5.90467 | -43.45576 | 2025-06-12 00:22:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 12a51f31-125d-3430-9923-9da0477009f1 | -5.78193 | -43.62336 | 2025-06-12 00:22:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e0d360de-76c4-3385-b892-381fd94cabed | -5.89584 | -43.45702 | 2025-06-12 00:22:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e0a1b5c4-b862-3859-817e-dada16f71db5 | -4.55375 | -48.01902 | 2025-06-12 00:22:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a891b1fa-d2a2-3145-a012-087cb76a5800 | -5.91473 | -43.46334 | 2025-06-12 00:22:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4a805681-4615-372a-9a5c-5bd676845fcf | -5.9135 | -43.45449 | 2025-06-12 00:22:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b65897ea-1d9d-31bf-afaf-6154ce454c5c | -5.7807 | -43.61454 | 2025-06-12 00:22:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7dac1847-3ce6-3f67-846b-5d7ca74a29d3 | -6.54719 | -47.81188 | 2025-06-12 00:22:00 | TERRA_M-M | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fd84cb1d-dbec-34d8-9421-75a329c6751d | -5.06803 | -43.72869 | 2025-06-12 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 281c8235-c528-3973-97a4-2935f7f77a39 | -5.0668 | -43.71987 | 2025-06-12 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 09986fdc-0f15-37d8-9d44-62f52b646167 | -4.88992 | -47.99426 | 2025-06-12 00:22:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 654a1d87-6478-3682-a841-bf6c99a4f380 | -7.4572 | -45.5342 | 2025-06-12 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 6c0c8a6e-320e-34f7-a968-90259af259e5 | -12.7169 | -58.0242 | 2025-06-12 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 65066f64-078e-35e4-9280-424a22224db0 | -13.8864 | -54.6519 | 2025-06-12 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| e9f8721e-4f8c-3865-80c6-40bbdf0168e3 | -13.9056 | -54.6498 | 2025-06-12 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8b0d1976-65a6-3cfd-8a29-259eb3c9b2b2 | -13.2798 | -57.0751 | 2025-06-12 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| af690c95-095e-32b5-95f1-711d6fc10f98 | -12.0063 | -57.2061 | 2025-06-12 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d39e12c2-64f3-33c7-a201-f5b7b687c0f0 | -10.8832 | -54.742 | 2025-06-12 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 86dfd970-2da6-30b8-a969-38560509ef05 | -10.883 | -54.7624 | 2025-06-12 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a26b9576-13bf-31ff-8dc4-508acc6e38e4 | -10.669 | -49.3597 | 2025-06-12 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a76858d0-6bfe-3896-aa76-16168ffad707 | -20.5619 | -50.1175 | 2025-06-12 00:30:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.5 |
| 506b4aa1-0a9e-3e70-816f-33096f0ce8ca | -7.4575 | -45.5116 | 2025-06-12 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 14f9c61b-a99c-3646-bd4d-5cc06b7bce72 | -10.7048 | -49.507 | 2025-06-12 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 93454a1f-4085-313f-9042-7f8abf7bb519 | -11.9278 | -57.4717 | 2025-06-12 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 40c8da8b-91a5-3263-9b5d-536af18959a3 | -13.2989 | -57.0734 | 2025-06-12 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 689b40c9-d92e-3d29-afdd-1ecaebb3d050 | -13.8867 | -54.6312 | 2025-06-12 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ed881c33-1be4-367f-aebc-578e7387ac18 | -5.0764 | -43.7339 | 2025-06-12 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 9f9011c7-0835-3c82-8ab2-08916bede3e5 | -5.6577 | -43.6001 | 2025-06-12 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d9feaa85-d746-32b8-b0b5-758cd03a6510 | -13.2986 | -57.0935 | 2025-06-12 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 193abeae-53ba-3171-9749-0e2effc6ba6b | -11.9874 | -57.2076 | 2025-06-12 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| dd9cfc17-271f-39d6-9390-c373b80e737d | -13.2796 | -57.0952 | 2025-06-12 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 70f83c4d-bf62-37a0-b69a-4612110ab7f2 | -20.5625 | -50.0948 | 2025-06-12 00:30:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.0 |
| 13961bd3-54bb-3f78-89f2-d0e3e97a9287 | -7.4763 | -45.5099 | 2025-06-12 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 9220587a-bcff-3809-9e63-e2039fda2029 | -5.639 | -43.6015 | 2025-06-12 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6ca18184-61bf-32df-94da-a1e2fc09fb4e | -7.2403 | -43.1134 | 2025-06-12 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| c1168a3e-0117-3117-8015-62ee6d981f22 | -13.2798 | -57.0751 | 2025-06-12 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| adb52fc3-0f3c-30fb-b215-1825bed21559 | -13.2989 | -57.0734 | 2025-06-12 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 160.9 |
| d2e37b08-fbff-38f5-946f-5c9bd4e6d612 | -12.6979 | -58.0257 | 2025-06-12 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 91655446-e491-31fe-889f-6307d9908ff6 | -13.9056 | -54.6498 | 2025-06-12 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3ac709a9-51df-3ce9-a6bd-063b50e51bbd | -10.669 | -49.3597 | 2025-06-12 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 03457f32-af33-3736-819b-786b5ec93a6f | -5.6577 | -43.6001 | 2025-06-12 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |


[Clique aqui para ver as próximas entradas](README3.md)
