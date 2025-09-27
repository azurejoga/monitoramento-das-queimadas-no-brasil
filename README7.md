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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 219f3506-b66d-3426-a51e-39ccb2c88515 | -14.8253 | -45.6282 | 2025-09-27 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fd7c54a7-5722-3dc0-8083-e8f0587f3622 | -5.4748 | -43.1009 | 2025-09-27 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e94c8101-554b-3f76-abd5-e11ce5786b9a | -10.2412 | -50.2429 | 2025-09-27 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 44d894bd-4a38-36d9-bbb4-a01e2ff8bbe8 | -8.822 | -46.2564 | 2025-09-27 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2b72e5d5-7699-3225-be2f-d6af4891207c | -14.8644 | -45.621 | 2025-09-27 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 0ed34344-1937-3dbb-b849-b202103083ae | -5.7961 | -42.8182 | 2025-09-27 00:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 18ca9108-8103-3071-8b12-133ab2339482 | -14.8258 | -45.6049 | 2025-09-27 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 8bce7041-cd7e-332b-a646-01927147d5f7 | -6.5368 | -43.831 | 2025-09-27 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5e687273-29df-3241-97ef-6fb831964250 | -5.5056 | -43.866 | 2025-09-27 00:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| f605fd82-ba10-3096-8057-9b275c128539 | -4.7844 | -42.7972 | 2025-09-27 00:30:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 79bb8ef8-2b17-3ebf-992e-f845fdcf0e38 | -14.8649 | -45.5977 | 2025-09-27 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| aac63bce-717a-3cc5-953f-1ff1ab9c64f9 | -22.5792 | -48.5986 | 2025-09-27 00:30:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 548.7 |
| 157ca2f4-3dac-355e-92d8-ac7a0bfe4f69 | -14.8448 | -45.6246 | 2025-09-27 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 8f10640c-4b64-37e4-8fea-096596b5cb7d | -10.222 | -50.2662 | 2025-09-27 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| bad5792e-230b-3e24-a99d-ff3c357699b3 | -22.6009 | -48.5698 | 2025-09-27 00:30:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.5 |
| ba0a03b0-c690-341e-bc3f-f0f87dc4dc0e | -11.3646 | -45.0108 | 2025-09-27 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8a64ec9f-85f0-3420-8a0f-e5c96774cd92 | -15.0267 | -47.1307 | 2025-09-27 00:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 2f8a38cc-9bcf-3150-afd0-76948f0c9e95 | -14.8454 | -45.6013 | 2025-09-27 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 43c19614-b10d-3419-b53b-efb2e3f971c3 | -11.3455 | -45.0135 | 2025-09-27 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0815cc9e-349e-3e79-9f7c-d370413d22b6 | -5.4935 | -43.0995 | 2025-09-27 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 3f62e665-411a-3347-a035-5385deb8ca00 | -22.6001 | -48.5934 | 2025-09-27 00:30:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.0 |
| a3211c90-82e2-3b0f-9928-604717b7bcd7 | -5.4935 | -43.0995 | 2025-09-27 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 16147c0b-c195-3f54-b18a-a37c114d421f | -5.4937 | -43.0761 | 2025-09-27 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 66f365c9-b405-3f3f-ae3c-0dff972d459c | -10.2409 | -50.2643 | 2025-09-27 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| ebb53745-8a76-3b8f-a8c4-fbdada3b95c9 | -5.475 | -43.0774 | 2025-09-27 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 599.8 |
| 0e683df3-78e7-3693-8471-441402d2709e | -5.5056 | -43.866 | 2025-09-27 00:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 6892fd0f-9d8e-3cc2-80a4-c7a77ae15368 | -10.2412 | -50.2429 | 2025-09-27 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fb4fdf43-153a-3c55-8fca-54e3c3c432c1 | -15.0462 | -47.1274 | 2025-09-27 00:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 2585a594-f2b8-3abb-864d-3339c4d59f30 | -5.4752 | -43.054 | 2025-09-27 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 327.2 |
| 33fc23fc-1004-30b3-ad90-7476e26e7365 | -3.45 | -44.1238 | 2025-09-27 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 887fe111-d93a-3675-82bc-a258463b3d18 | -11.3455 | -45.0135 | 2025-09-27 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| ce56b09e-6232-3b21-aebe-1b562f075140 | -5.4562 | -43.0788 | 2025-09-27 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| fd3654fa-fcb3-3db3-ab82-bec3a9a14beb | -5.4748 | -43.1009 | 2025-09-27 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| eff39f1b-9369-3aa4-9bbc-f1407151341f | -11.3646 | -45.0108 | 2025-09-27 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 65fb8292-87d6-3b66-8f06-9c019877c576 | -5.0676 | -44.8581 | 2025-09-27 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 919ea6d4-c3fe-3a53-82d6-e8c13636e41e | -22.5785 | -48.6222 | 2025-09-27 00:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 0d70996c-56e6-30db-a6d7-60e020f64716 | -5.494 | -43.0526 | 2025-09-27 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| bd9aecd5-796a-39be-b6f9-e3a08a2674b0 | -22.5582 | -48.6038 | 2025-09-27 00:40:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |
| 7deeec00-4d03-3ee1-9d09-fe0415d9fa7d | -11.3459 | -44.9904 | 2025-09-27 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4d184929-6df0-3f35-bd48-33d5376ace81 | -22.6001 | -48.5934 | 2025-09-27 00:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 1035bd8d-ea9a-3723-951c-c11ee641eca1 | -5.4565 | -43.0554 | 2025-09-27 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9b606190-529d-3e7c-ab68-66c006e1ca64 | -22.5792 | -48.5986 | 2025-09-27 00:40:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 303.4 |
| 02972493-4dd8-357a-9d16-701f3e36cc19 | -15.0262 | -47.1536 | 2025-09-27 00:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d98df9be-1665-3f77-a402-db886fe81b10 | -22.6009 | -48.5698 | 2025-09-27 00:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.5 |
| ed291d01-4e1d-3444-85e2-06153a21985e | -11.365 | -44.9876 | 2025-09-27 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4cb18214-3677-3007-bb13-c2ddc5be481b | -5.0862 | -44.857 | 2025-09-27 00:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3a725ba2-0dbf-38fa-b74f-81163e57dea9 | -15.0267 | -47.1307 | 2025-09-27 00:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| bcb501a7-91cf-3687-b03f-f30cfde8b61c | -15.0457 | -47.1502 | 2025-09-27 00:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 19d27500-cbce-3825-9f3f-6d25b5a045df | -22.5799 | -48.575 | 2025-09-27 00:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.5 |
| 77ef9cca-8f17-3423-8f57-ac2051705f7d | -5.7961 | -42.8182 | 2025-09-27 00:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| a1c79b13-985c-355b-bca0-876f73012b48 | -5.5243 | -43.8647 | 2025-09-27 00:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 56116307-8e08-3ba0-a9e4-ead0688d061e | -14.8448 | -45.6246 | 2025-09-27 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 18ad8980-e5d2-342c-9e45-c0005d2de439 | -5.7961 | -42.8182 | 2025-09-27 00:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| da25d137-20be-34dd-969d-12c2ef80eef0 | -22.5792 | -48.5986 | 2025-09-27 00:50:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 290.4 |
| 86c9fa9e-4994-3461-a3d5-16e26017a6db | -12.2834 | -44.0332 | 2025-09-27 00:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f386902e-15cd-32c9-a0e9-7a7e782dd16c | -22.7271 | -51.3948 | 2025-09-27 00:50:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.7 |
| fcb07a57-572b-39fd-a71a-134a5f635af2 | -6.9042 | -35.0916 | 2025-09-27 00:50:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| 0e269e0e-d7db-3773-ab92-dde3494a302e | -5.5243 | -43.8647 | 2025-09-27 00:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 7ffe6382-7fe9-33c4-a5c8-61484f93762b | -5.4748 | -43.1009 | 2025-09-27 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 7ccbd660-43e3-3f43-b701-2a034a32d84c | -5.5056 | -43.866 | 2025-09-27 00:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 63b586df-3dd3-3a3f-ac06-40eb4dd8391d | -12.2641 | -44.0363 | 2025-09-27 00:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| dbb38acc-0188-3cf8-b2fe-d123498abbc7 | -12.2829 | -44.0568 | 2025-09-27 00:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 43c25307-7adf-380f-8864-41d2fef0e127 | -11.3646 | -45.0108 | 2025-09-27 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0a93de35-a017-39d0-a39b-3c825779ddee | -14.8448 | -45.6246 | 2025-09-27 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 83a9c926-52f0-3601-bed9-402816c195d1 | -6.9045 | -35.0641 | 2025-09-27 00:50:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| dc878aaf-7183-3f16-b41c-48deef5f6f16 | -3.45 | -44.1238 | 2025-09-27 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| b74ce9bf-fe5f-3a99-b56b-d8561ebc02e3 | -5.0676 | -44.8581 | 2025-09-27 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 1f2c437d-039c-3e1e-9589-262e390fb813 | -22.5575 | -48.6273 | 2025-09-27 00:50:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.3 |
| c92ee14f-72a2-31b4-addd-b5fb0ea3df7b | -12.2636 | -44.0599 | 2025-09-27 00:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 89d1cf86-e1f1-347e-87c8-8520c773b0f1 | -10.2412 | -50.2429 | 2025-09-27 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a15a0a8c-74d9-350e-abbe-d67222c4851c | -5.0862 | -44.857 | 2025-09-27 00:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 41a4b182-e5dd-39f0-9cbe-d3ca43b9e75f | -5.4935 | -43.0995 | 2025-09-27 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 06dcc905-5fc4-3255-be94-526b20ae2b60 | -22.5785 | -48.6222 | 2025-09-27 00:50:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 9287fc96-283d-37f5-8ac9-380763afe6dd | -11.385 | -44.9386 | 2025-09-27 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 08eab423-1351-3a53-bc90-614c54acaf25 | -22.5799 | -48.575 | 2025-09-27 00:50:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.9 |
| d5193993-1c94-3027-93f7-3446123fa38b | -22.5582 | -48.6038 | 2025-09-27 00:50:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 340.9 |
| a3e8ef67-8002-381d-8791-e37ea24b2c3b | -22.5589 | -48.5802 | 2025-09-27 00:50:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| 548e514f-7247-351e-acce-dcce3e3ee58f | -10.2409 | -50.2643 | 2025-09-27 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b215847a-db7e-3a99-8f2b-929f711ec688 | -5.5241 | -43.8878 | 2025-09-27 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| e6cc8ef6-b834-3215-a289-465e51a4d187 | -9.3705 | -47.5781 | 2025-09-27 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d1318a94-ab8f-364a-9981-d01418788a9e | -10.2412 | -50.2429 | 2025-09-27 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 6a627074-282f-38d1-bc2d-4ad0debaf774 | -5.5056 | -43.866 | 2025-09-27 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 21579523-b5ec-31f6-a19e-b0bab5a7350a | -5.0862 | -44.857 | 2025-09-27 01:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 02d712f5-d402-36bd-a4c9-4a69d4298af2 | -14.8454 | -45.6013 | 2025-09-27 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0666005e-3ae4-3852-82c0-621f192484df | -5.4748 | -43.1009 | 2025-09-27 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| a24c6704-8998-3904-bcc7-916b9efd33f6 | -5.494 | -43.0526 | 2025-09-27 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 58498ac2-85ba-3988-baed-a57b6ce87dd6 | -15.0462 | -47.1274 | 2025-09-27 01:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f7c4c6b4-8a2c-3e00-a12f-6c138c902ab0 | -22.5792 | -48.5986 | 2025-09-27 01:00:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 231.2 |
| 4dc40b4b-7e9e-38b3-98b8-2a7fa208a908 | -6.9042 | -35.0916 | 2025-09-27 01:00:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 96.6 |
| f00d5363-693a-3060-ad56-25d36906a186 | -6.8854 | -35.0666 | 2025-09-27 01:00:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 845649af-a294-3fad-ae27-f8851b798c23 | -5.5243 | -43.8647 | 2025-09-27 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3bdaad28-1793-3374-a2fa-ba211ea82c0a | -5.4937 | -43.0761 | 2025-09-27 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 2dbd3d3b-e035-3aec-a303-56d624bb2d87 | -22.5799 | -48.575 | 2025-09-27 01:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| 9279f732-c54f-3a99-a634-0ad87990ee25 | -6.9045 | -35.0641 | 2025-09-27 01:00:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 141.3 |
| 2027f593-1b45-3583-be72-81d33b31a089 | -5.4565 | -43.0554 | 2025-09-27 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 74038109-43b7-3999-a1ba-86d661a5a059 | -14.8253 | -45.6282 | 2025-09-27 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 04a631f7-1838-3f17-b292-486cb656bda8 | -5.4752 | -43.054 | 2025-09-27 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 269f397d-bed1-328c-8b85-7a174877ac64 | -22.5785 | -48.6222 | 2025-09-27 01:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 9d821d01-170d-3220-b1cb-9a75520a26b2 | -18.39 | -51.7528 | 2025-09-27 01:00:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 82a00da2-10d3-3919-b947-92752a8a8784 | -14.8448 | -45.6246 | 2025-09-27 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |


[Clique aqui para ver as próximas entradas](README8.md)
