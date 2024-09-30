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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47eefcc7-bb91-30be-9fe1-337613d60d1a | -2.14565 | -53.67469 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad6ba359-1def-32cc-8f29-640570ff3a6a | -2.14336 | -53.65991 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3136d0f1-85ae-3330-8560-fca31b554549 | -2.1426 | -53.66461 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd942eb8-2d57-3f5d-a545-ea642edad5cd | -2.14183 | -53.66928 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43f176ae-a880-37c2-aba5-fc8ab1b86e47 | -2.13801 | -53.66396 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e423103c-f5d4-3e44-b41a-573dca9cdb67 | -2.13648 | -53.64465 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76c34576-8033-3fed-aaf5-2926e2ca469a | -1.29291 | -54.55396 | 2024-09-30 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3824d61c-9654-39a1-b008-aad6fe776e01 | -0.91927 | -53.71734 | 2024-09-30 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 119b3bf8-6731-3b18-8152-29947de455f2 | -0.91669 | -53.7176 | 2024-09-30 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b2ddd2c-f193-3d9a-b69d-e34c36c5defe | -2.43731 | -54.10987 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 834a28cf-ab09-30a3-815d-9bab0793f364 | -2.43651 | -54.11487 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d73649a-fe21-3dca-88d0-0e1b81cd8bd1 | -2.4357 | -54.1199 | 2024-09-30 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92332209-04b1-348d-9b64-72dff08f0888 | -1.42682 | -55.34387 | 2024-09-30 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58926643-eac9-377e-975a-beeb5e597896 | -1.42631 | -55.34699 | 2024-09-30 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92e8dab2-35d6-38bd-87cc-ac4a692da37c | -1.41298 | -55.49432 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bcc1b68-2ff2-32b5-bb3f-f539a67e30a1 | -1.41245 | -55.49753 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebc3163c-d1ce-3c35-ad02-e8e1c9a01f4d | -1.36511 | -55.68763 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 180930ea-c5f6-3ca3-a8b5-fbf68d5329d0 | -1.36097 | -55.68938 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32913ce3-d367-3bfc-8a57-af46b6fc5a3b | -1.35978 | -55.68677 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7425117b-a35d-3109-8871-e08c7a627fdb | -1.35923 | -55.69013 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 230bae8c-4b9e-369c-b00b-059ca3ba011b | -1.35617 | -55.68517 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9abac08-d034-3819-a6d5-34a4b4f5ffdc | -1.35565 | -55.68849 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5127c89-d1b8-3a9c-ae17-89e957560c70 | -1.35446 | -55.68594 | 2024-09-30 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b40c8f16-7155-3378-b2a1-4f03cf7e064b | -7.47723 | -34.94111 | 2024-09-30 04:29:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b44f3c7a-dd2b-3ce9-90f6-0b1ddb5ea123 | -7.47647 | -34.94726 | 2024-09-30 04:29:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 814acf99-3e31-3f3d-8e10-ae26546b018c | -7.88793 | -39.32848 | 2024-09-30 04:29:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2e972282-42c5-32c1-a083-f4698c6b11eb | -7.88752 | -39.33162 | 2024-09-30 04:29:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f30f6577-5513-3967-a18e-7f888dca288b | -7.88697 | -39.32778 | 2024-09-30 04:29:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3451f14-8f66-3f87-96ec-4ce572611442 | -7.88653 | -39.33093 | 2024-09-30 04:29:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 481ff41a-3b28-3300-adde-e17867f0a936 | -6.79013 | -40.13824 | 2024-09-30 04:29:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c04e262-5053-347b-96a0-fae9fc3f41f1 | -6.78935 | -40.14365 | 2024-09-30 04:29:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ffeb48d4-196c-3171-973b-12c9f507c3a6 | -6.78911 | -40.13898 | 2024-09-30 04:29:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 73367113-864e-3785-ba0c-83c8f172e881 | -8.12717 | -39.53196 | 2024-09-30 04:29:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d3668d1d-dfd0-3e40-983d-5197752614e1 | -7.95959 | -41.38013 | 2024-09-30 04:29:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| acd44b16-c345-3477-8ba0-be713e67605c | -3.95889 | -41.4901 | 2024-09-30 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 24d9c35e-5d3a-3889-a7ca-a0665feb2643 | -6.42562 | -42.93796 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9090b2ed-419a-3a44-8143-38cc37fcd0d8 | -6.31336 | -43.15725 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ca95141-bf5e-3ea1-b491-de6a4bc37e10 | -7.92133 | -42.76522 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 997956c0-ed7f-325c-bcc6-b767b10a3d4b | -7.92077 | -42.76901 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7065630d-bbd6-337e-aaef-3cac2f925609 | -7.92022 | -42.77277 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0bac07e7-dfe4-306c-b44a-3a3d02af14ec | -7.91723 | -42.76462 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f3f6aa3-cffb-38de-bd42-7bd28532d957 | -7.91667 | -42.76841 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a2b8b60-3468-3885-8b56-98d45dff9639 | -7.91612 | -42.77216 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b2713bb1-cf32-3717-ac23-56d1770ba942 | -7.91367 | -42.76023 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 951b1b1e-b560-3d91-9413-165873811a92 | -7.91312 | -42.76401 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 559d0db4-e627-3043-9f85-af70001c80b4 | -7.91257 | -42.76781 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5f826c36-11e7-3611-82e0-949c6bb15f06 | -7.90956 | -42.75967 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05ffc3a5-4170-37a8-af2a-de1f3ec81521 | -7.90901 | -42.76344 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 05df162f-16b9-3a92-9628-ea21901ed2cb | -7.90846 | -42.76722 | 2024-09-30 04:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 27a65efa-5737-3ec5-845f-2d159d07a922 | -7.886 | -42.66085 | 2024-09-30 04:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 858e3b4d-cc21-31a8-95ec-49d91f8939ab | -7.88546 | -42.66465 | 2024-09-30 04:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| df63f723-c9ea-39ad-8be8-433f6fb6074b | -7.75856 | -43.75906 | 2024-09-30 04:29:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d56ceb88-d362-30af-b5d9-b4c803ae8c8d | -7.66492 | -42.42904 | 2024-09-30 04:29:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2aaf1c89-4d05-300a-b7ba-19dc66256a74 | -7.28808 | -42.25572 | 2024-09-30 04:29:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f5957e30-b5ab-33b6-ac2d-1351cf6c7607 | -7.28753 | -42.25957 | 2024-09-30 04:29:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c55ffa05-c680-3c35-afec-78441e57875c | -7.28698 | -42.26342 | 2024-09-30 04:29:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c28c3238-1de4-3be7-aebe-7f6bcd887266 | -7.28443 | -42.25118 | 2024-09-30 04:29:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e7354cb-c5d8-3c1e-9530-fb1f682d6edc | -7.28388 | -42.25506 | 2024-09-30 04:29:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 63e33370-3b4d-3a8e-aaaa-b55557cfe423 | -7.24976 | -42.25064 | 2024-09-30 04:29:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b3bcbbc-99f4-30e9-a02d-da64d7294acd | -7.24556 | -42.25 | 2024-09-30 04:29:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c347fef5-40b5-3029-8ce0-6d8949dec320 | -6.96708 | -42.41467 | 2024-09-30 04:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f4cf5457-e44a-3f64-8a86-191ff7d6cc67 | -6.96239 | -42.41784 | 2024-09-30 04:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7def0120-c500-396c-b539-14857966eae5 | -6.64218 | -42.09632 | 2024-09-30 04:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b721ddda-85bf-3ea5-a28b-47e3bae92bce | -7.31776 | -43.32592 | 2024-09-30 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71dc869e-2ec3-3f41-b716-6481cd9e5b24 | -7.31756 | -43.32906 | 2024-09-30 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a114293-f0b5-36de-bdb0-8a61457d4b9b | -7.2937 | -43.38143 | 2024-09-30 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5db4e19-ac82-3373-9f7e-eaf49525afea | -7.28904 | -43.38586 | 2024-09-30 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d484033-613b-3a17-88bc-ad70998547fb | -6.82885 | -43.1098 | 2024-09-30 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fae9c11-e4cb-3bba-a583-18051ce01a65 | -8.08169 | -42.88896 | 2024-09-30 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4eed14df-7948-3def-b7d4-8ab01bbbb51c | -6.39151 | -44.78148 | 2024-09-30 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9c0fa22-3e16-34e4-8ffb-065c75cbca74 | -6.39089 | -44.78558 | 2024-09-30 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7634cda4-5d24-39c6-808d-e1ae1247505b | -6.39028 | -44.78967 | 2024-09-30 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 892f966e-f59d-3419-b5f5-8c7589de3af1 | -6.38856 | -44.77683 | 2024-09-30 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3ba7ba79-5933-3f1b-9d95-39912ddf4bb7 | -6.38794 | -44.78094 | 2024-09-30 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14baeb32-5d03-3738-a867-66f5bdf95de0 | -6.38562 | -44.77214 | 2024-09-30 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f6c951d-e2ea-3dab-9573-6d1b6fc79a8c | -6.38499 | -44.77627 | 2024-09-30 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e73db3aa-0630-3b66-bd02-8558e7e4a323 | -7.56915 | -45.02489 | 2024-09-30 04:29:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53a6aad4-e849-33b9-9b26-e5b640c4021b | -7.51163 | -44.91914 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d24305e-41fe-31d3-81fb-2d0099b473e5 | -7.50971 | -44.92029 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21eda372-15ec-3c25-b23d-ef523a616873 | -7.50314 | -44.97676 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 517b09e9-f37d-3b7a-9dad-e70211c8bb66 | -7.50157 | -44.97362 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6b72dc1-f362-3d1e-a2ac-7403a9af98aa | -7.50094 | -44.97769 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a977e01-561a-37ee-8904-1feb95bb1d54 | -7.49956 | -44.97618 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d4473b0-e5e7-3afa-9018-1861d3d187d9 | -7.49896 | -44.98027 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 502873d3-c828-34b5-bfbc-cf1dc8c51d73 | -7.49737 | -44.97712 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fac2e19-3f3d-315a-a687-29194ca2ae61 | -7.49674 | -44.9812 | 2024-09-30 04:29:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a83e651a-1405-33f4-bdf9-e45e442b6e61 | -7.59339 | -43.85468 | 2024-09-30 04:29:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0a4bee4-a9c7-3256-af5e-fa081870c8e9 | -7.59272 | -43.85928 | 2024-09-30 04:29:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddb6a457-c2de-3a72-823f-62fbba77cccf | -7.5775 | -43.85683 | 2024-09-30 04:29:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c34928e-0384-3fd6-8f7c-bd6d14e89af4 | -7.56702 | -44.34448 | 2024-09-30 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70777de6-6e14-322a-8005-ca5f93b401bf | -7.48447 | -43.85904 | 2024-09-30 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eccf558d-57f6-37ef-baa1-4953e3da8885 | -7.48378 | -43.86375 | 2024-09-30 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3503e2a-98ca-3fdf-84c8-d6b0e173b997 | -7.48134 | -43.85383 | 2024-09-30 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 038b3170-55d4-37bc-9c7d-ec3702fd9bae | -7.48065 | -43.85854 | 2024-09-30 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7b6db00-46e1-3107-be85-c034a03ebd5f | -7.31966 | -43.82578 | 2024-09-30 04:29:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37e1e5f1-a52d-3a71-aca8-0c3a27f6eacd | -7.27517 | -43.99466 | 2024-09-30 04:29:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4695ddd-0454-3758-958c-acb3e5c0aa35 | -7.27449 | -43.99922 | 2024-09-30 04:29:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea0b4958-dc5e-3b68-aa1f-9cc651228d3a | -7.25005 | -44.18909 | 2024-09-30 04:29:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2197f309-cd0c-3008-b440-a0ea61706218 | -7.20281 | -44.27727 | 2024-09-30 04:29:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29d7a18d-a868-300d-afdd-af842d9f01c5 | -7.19707 | -44.21313 | 2024-09-30 04:29:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README27.md)
