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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 221e50f4-dbc1-31a2-9023-2de9963e2454 | -6.70059 | -48.71201 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 640b1e9d-749d-3a27-9d78-05990eb9d792 | -7.55193 | -42.63902 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3dea2d17-2716-3971-a48d-9b53f41928e0 | -11.53305 | -43.55181 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fc7bf4b-cdf6-37c2-8c5e-a8649dae9c15 | -10.99802 | -46.58782 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f993b23-68d3-390c-bac6-527ef2f17634 | -7.55477 | -42.40464 | 2025-10-02 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3c022443-504d-3ba9-a7f4-a0aebf9fdc93 | -9.85665 | -46.87994 | 2025-10-02 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73d8b2fd-50f0-3047-a2ab-7df8470662f2 | -11.90679 | -47.8862 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23e0ce51-2f0d-394a-9b8e-2642e529b911 | -9.45094 | -45.47243 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8520003b-ab89-33cd-a068-ab6a57b9e66c | -7.72722 | -46.21922 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fb4be82-39eb-327a-982d-da3eb1aa57aa | -9.3271 | -45.67687 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a770e84f-13b6-3dd8-aea3-bd1bd5dc840f | -7.77774 | -42.52573 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6f473464-9164-342f-b023-42521d222448 | -6.96379 | -45.34482 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8f472fb-8fcb-3bee-9d7e-b44cd3cda44b | -13.32587 | -43.10074 | 2025-10-02 04:02:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b04d783f-48c2-3c6b-a8f5-5a1fe22849c3 | -11.17672 | -47.27483 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2af68f15-d248-33a0-87af-3b0a52774e8c | -7.46415 | -46.45898 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8136144e-c6d4-3df3-997d-8bead232576f | -6.6695 | -42.79443 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8909156f-cacd-3c05-b18b-74a4ed4b3a9f | -10.83177 | -46.63385 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bf5d15e-d71d-37b4-924a-7bd375633eeb | -11.42936 | -43.49847 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6d21750-0e3a-384b-bee4-6166ad7ac08f | -9.77174 | -46.2266 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 616f945c-4a7c-3c20-bdc1-f754c3534c1b | -12.28213 | -45.377 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b521cf25-d4dd-32d0-aedb-8a903b87ab11 | -10.86738 | -47.82277 | 2025-10-02 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5be7fd5-864a-3093-b1e0-ab44470cf993 | -9.9403 | -43.75726 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0e3e1f66-d8b6-3d2a-95b3-6f1f9afa9876 | -6.96657 | -45.33022 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8fc037e-5adc-34d3-bcf2-eab5130d4274 | -7.72916 | -46.2079 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53c8fee3-dece-394f-b024-2311def10c02 | -10.64652 | -48.51016 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d73fa1b0-245b-37b8-98fd-50a5bc875b73 | -11.4824 | -45.11699 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1da4a1dc-f1ff-3cf8-b2e6-8932a109ebca | -9.94476 | -43.7076 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ade4a586-24cd-39ac-9485-8a2dd9c66e37 | -11.00214 | -46.58861 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c5e240a-d193-3511-8bdd-509d3b1b21f5 | -6.32715 | -43.04892 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 765838dc-abec-37a7-8c87-12be798beb1e | -11.13569 | -43.3825 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b30fb739-3050-35e4-968e-a7f1753495ba | -5.83087 | -42.86394 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 37699d8b-9304-3f9e-8617-6662c2d412ac | -12.26141 | -47.80617 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da732287-382b-32b4-b55a-de569ff3be08 | -11.26864 | -47.80479 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f1f6e0a-194b-34c9-8068-19265ad8c0fa | -11.4259 | -43.49789 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee70a71a-dc37-37b8-b312-79a3923827c3 | -6.30105 | -43.81021 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6827d7d6-e6f8-30fe-8dc9-d51d20b9f452 | -9.94188 | -43.70291 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2b5c1a2-fa6f-3b71-afda-8c00ffabc5c8 | -9.84424 | -49.95588 | 2025-10-02 04:02:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9480aaac-55cf-3476-b791-76d31892e82d | -11.80301 | -47.58435 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f754224e-08e2-30a7-aa42-281bcf42892f | -9.80258 | -45.95489 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03ffc40e-eb23-3434-a520-e4e16b3846d4 | -5.83153 | -42.85983 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4223cbbc-f3e7-37c2-82f6-96a5ceafb04c | -10.53018 | -43.63912 | 2025-10-02 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fa668d2-2234-3b93-8644-14d7c656e182 | -10.84456 | -45.38837 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9962197b-6da8-3e61-b539-b034cfa76fa2 | -13.01417 | -45.22076 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee006c7e-caeb-3d95-91da-bd54c6ba4abe | -10.10982 | -45.7009 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bc08d11-2a04-3cb3-9aba-a11581e4d597 | -9.94339 | -43.58275 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba4be267-6b92-30a5-be09-4dc408d31d8f | -12.95914 | -46.37319 | 2025-10-02 04:02:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d3e2940-c1bd-35aa-8d77-c5a368212d3d | -11.2734 | -47.82957 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8066ccaa-1fa1-386c-910d-4d66eebbbfe5 | -6.08283 | -42.42574 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf908f03-2d73-37fb-8ec3-b7d8b999fe81 | -10.28064 | -36.34077 | 2025-10-02 04:02:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 27554100-05cb-32ad-9a52-3d8012bd42d5 | -8.70675 | -44.82302 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48bed8ec-62f0-3b55-973c-4c21acb2ffe9 | -7.02739 | -44.47202 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 950c8d30-394c-355b-a642-f71d6e4895ba | -11.82449 | -45.03062 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1bc5a33-5521-367b-b873-924990a8df4c | -10.83647 | -46.6069 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff545b34-61c3-3b9a-8bdc-f1e553d348b3 | -11.91646 | -47.88328 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00d07f29-4bbe-3b7b-82f8-6d043bac004e | -13.32702 | -43.10437 | 2025-10-02 04:02:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1b4b0d5-594d-3322-a98d-3ff43fedae6a | -7.7765 | -42.53331 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| fdb9b259-d362-3380-9a43-3e3e3108b966 | -12.85505 | -47.03947 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28ec1cb9-590e-3b4c-bf7c-db7fc3ca6e23 | -9.90021 | -45.94283 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29c5435c-a2be-3675-b233-97e2a5913114 | -7.77995 | -42.53387 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 50937abb-3422-3131-baa5-4d613a9884dc | -12.65819 | -46.94426 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3100f68-8e03-3df5-814d-cc14271eb6af | -10.26338 | -50.32462 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ccb041be-6ba3-3bd9-8d29-f98e30f589b4 | -11.35959 | -44.96387 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 79761b46-4ed8-36a4-8746-f10bc7c6b3a9 | -11.47066 | -45.11182 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7dca41b-ec20-34ed-9ba4-4e0f8a2e2d94 | -9.03868 | -46.68175 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ba527fc-b523-37c6-9405-0d6cde53b56b | -5.51033 | -45.1601 | 2025-10-02 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 656b4254-ab98-3635-9187-d6709a6bd200 | -5.82862 | -42.85514 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9ed9129f-82db-3d46-8ff7-9839fc06a7db | -12.2619 | -47.82864 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dc82519-9c43-37fa-927e-c6389ba9fe8e | -8.51436 | -47.82598 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c2a98ae-91a2-38ba-a0f5-33bb83e6eba7 | -5.94087 | -45.88438 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ea2949e-fc78-3364-8c43-96c9d3cd7c23 | -11.87047 | -45.0295 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5397afc4-4f76-3a5f-a4d1-50d1d48c8250 | -12.27916 | -45.37172 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 610b3083-b90f-3365-baf7-da6e7a93f743 | -12.87076 | -47.02255 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f60de3d-def3-30e6-b2a3-448200f4cb40 | -12.47416 | -47.27324 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a432c4b-9cc4-3de9-8a07-fd305c432753 | -7.0447 | -43.32387 | 2025-10-02 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 37367784-8157-31da-96ce-7bd82aa980b6 | -12.15216 | -46.67581 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b084becb-1c1e-3f58-adf7-319473644226 | -11.18765 | -47.18728 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 885f3061-984e-384c-ab4b-0055f5465b67 | -9.93037 | -43.61785 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e565ed53-b760-39ac-9037-09c628912032 | -11.18342 | -47.18624 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0ae662a-cd02-3278-937a-a71f95de5d89 | -6.96813 | -45.34546 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b0f37f0-1ffc-3b61-aacd-341d4823985d | -6.10214 | -43.44137 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4a66354d-c92e-3510-9218-3175eddbfc7a | -13.17824 | -47.8342 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 832e679b-0f00-3a9e-9b09-310ca1260da0 | -14.21966 | -44.93792 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1398bac4-c446-3900-86c0-cce90ac665e8 | -14.31242 | -45.9787 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0616c9ca-58b5-31c0-b481-ecc00423f622 | -14.61253 | -48.20066 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e644329-7af5-3114-9498-b9d2d01d3218 | -14.90057 | -47.1787 | 2025-10-02 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58a39aab-186d-35ce-be83-f8a0774024b9 | -13.86715 | -43.6015 | 2025-10-02 04:04:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46cfba49-c6c5-30e3-aa7c-c0c1d9ee4e4b | -13.2081 | -47.33623 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a45fe2a-b244-3bee-a61e-ef04394465c0 | -14.91243 | -47.23371 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e876f51d-a2a0-3d35-a0b1-1e4f236abfeb | -13.86944 | -47.94629 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbf6db8f-a561-3422-b36f-50ea0bfa1418 | -13.81251 | -47.53911 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 54ca30e4-162e-3a2e-9ad5-aa61143819d8 | -16.04733 | -50.85493 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 514b29a6-9ed4-32d7-81c9-8332ea46a382 | -13.68951 | -48.64846 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95c59f05-3caa-351d-9ff0-cd1f4ef7b9e3 | -19.89475 | -42.62359 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 07a428e9-9c99-383b-a978-82b47c0e86ce | -13.08675 | -47.08135 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7d23979-b0ce-3e8d-ad58-444ad3d26fbe | -13.23218 | -48.506 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f783abb-bf3e-34be-835f-00e99e4f1c71 | -16.02 | -50.86169 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf6a9a66-5e93-3274-9536-9db174a76de9 | -19.46654 | -43.87443 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c27f1b57-70f1-3306-9c9b-c20306033ef7 | -14.86842 | -48.39261 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9373003-b641-3c60-9802-71d62a95fbba | -16.06729 | -51.01215 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13546f4b-0cb5-3fa5-87c3-d530e37f67c6 | -13.86789 | -47.95485 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README38.md)
