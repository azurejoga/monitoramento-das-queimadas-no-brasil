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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f2f3333-74b7-3b8d-9ac9-1616edce59f4 | -5.9993 | -57.8833 | 2026-08-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 53cd61b7-e130-3997-9bf6-81fb222addd8 | -14.4554 | -45.6251 | 2026-08-19 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ca8add1d-4fed-3beb-a437-3053ab2bbcac | -14.4934 | -45.6647 | 2026-08-19 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 12a1c214-fb01-3b13-9510-073713c23992 | -7.5487 | -55.5829 | 2026-08-19 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| a86da52d-b661-3236-8d62-3c8bbd650856 | -7.5301 | -55.5839 | 2026-08-19 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| a5050e7e-502e-35b6-a35e-21d1c0e305c6 | -5.4317 | -48.4212 | 2026-08-19 00:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ea68bd2e-61f1-3d20-a7d9-1a8699969136 | -6.8593 | -59.0318 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 9527a88c-9eb7-39a5-86d3-2923df7e8ff7 | -6.0912 | -57.9187 | 2026-08-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| d2265939-b895-3bb7-9152-26dba5dc253b | -19.7639 | -57.9607 | 2026-08-19 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 210.3 |
| 2af6f3bc-52a6-3f6a-b217-804c658c45e3 | -6.0179 | -57.8437 | 2026-08-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 703f7bf4-a5a9-3b41-9aa0-a0c97606625b | -5.9198 | -43.6264 | 2026-08-19 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 524ca492-ee37-37ec-87b1-149e0ab62e0d | -8.9973 | -60.5147 | 2026-08-19 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3ac8b07a-68b2-3cbe-845f-231a937da351 | -9.3873 | -60.5721 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 933251ed-9c46-3fe3-8881-3145a465ce50 | -6.0728 | -57.9194 | 2026-08-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3c907446-d967-3180-af67-ba7d4f3c1e55 | -19.7442 | -57.9425 | 2026-08-19 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 289.6 |
| 0a86f075-60ff-3931-b5a3-e079d009f535 | -9.406 | -60.5711 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 69c9e5c8-4cb5-3b0a-94e5-9221f959f0d5 | -6.6938 | -58.942 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 34ada012-ea04-36f5-babf-953feab42281 | -6.6937 | -58.9613 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 016f7213-f3b5-3533-97a5-2e944f318b99 | -9.4061 | -60.5518 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 8f382373-2eaa-3e88-a1b5-07b38813eb95 | -7.0577 | -59.8331 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d90b372f-fe5b-3153-abe3-0c670d30c551 | -5.9995 | -57.8444 | 2026-08-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| e19956e9-cb7a-388b-b5df-fd03a1bd95f6 | -3.5239 | -44.2351 | 2026-08-19 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9b8ae6b2-ee19-3631-ab15-487e5cf8050d | -8.5792 | -54.6758 | 2026-08-19 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4f4085c6-c6c5-3f97-b387-96643274d59b | -7.0576 | -59.8523 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ec07e9ca-8afa-3b06-89b8-d384e53e8e9b | -6.8777 | -59.0504 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 7fc99cc6-2b65-36fe-aaee-09e7b22fece2 | -6.3496 | -54.9068 | 2026-08-19 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 13b001fd-547e-3613-90d1-df7854f5c6b3 | -9.4257 | -60.416 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 01368016-fe20-34b2-bb2d-5f080f986518 | -9.0158 | -60.5138 | 2026-08-19 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4c7355ca-8b8c-3a31-86ee-1dc453b14dc6 | -6.8778 | -59.031 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| f0a395b4-45f6-39a3-ab6d-3f7b8f9b34a0 | -6.8594 | -59.0125 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 651c581e-9009-36a1-a5e1-d2e43fe27d67 | -5.9994 | -57.8639 | 2026-08-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 216.2 |
| a8bd8cb6-1582-3af2-9292-7fbf266e3d41 | -9.3875 | -60.5528 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 3e4d239d-0a14-37de-bf34-aa25a56ae9a6 | -19.7643 | -57.9399 | 2026-08-19 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 205.0 |
| e276054a-8a41-3797-b666-8f9e8dfb7025 | -7.5488 | -55.5629 | 2026-08-19 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c72fb9ff-eebd-37ef-a5e0-3c7395ae338e | -5.92 | -43.6032 | 2026-08-19 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0e868b0f-7f54-33da-80d9-7d6d64d4be77 | -6.7123 | -58.9412 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 67936634-4685-34a5-9414-b2ef1758ec40 | -9.4069 | -60.4362 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| d7c8ba35-834e-3eff-9ea5-3031462ffd78 | -5.9011 | -43.6279 | 2026-08-19 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 3f39dc08-d3ce-3364-acd4-aa13343f9840 | -6.8962 | -59.0303 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6f04a0cd-0679-3c5a-b0e5-a2540fe602b8 | -6.7486 | -59.0364 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 32ffbec6-ab47-3e35-ae30-fa2790a3082e | -9.4256 | -60.4353 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| c312dd0c-6fbd-385f-99ef-a9e2eebb6a7d | -9.0865 | -50.7979 | 2026-08-19 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| bfa0c404-f3ad-3fb8-8a6f-49d81f0ff1dc | -6.8961 | -59.0496 | 2026-08-19 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| ef4deff3-859b-3d57-bb15-a8ee9ae28599 | -6.0913 | -57.8992 | 2026-08-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| fc482397-173a-3288-afc5-7cb7ed820ca2 | -9.4254 | -60.4545 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8f395a6e-3fb3-3c60-b3ac-a6c1717a4ef8 | -6.0178 | -57.8631 | 2026-08-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 0ff68868-e70a-3b6f-8dec-9e634a1f3590 | -9.4058 | -60.5904 | 2026-08-19 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 38fcd42c-ae71-3acb-abc5-cbcdaf8920a9 | -19.7438 | -57.9633 | 2026-08-19 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 226.5 |
| dd08e6c0-ff5e-3a39-996c-fe329b7f09fe | -23.75936 | -46.80879 | 2026-08-19 00:05:00 | TERRA_M-M | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| dced6692-af06-3f6c-998b-7f8fa60a0c49 | -24.77209 | -49.09497 | 2026-08-19 00:05:00 | TERRA_M-M | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 465e7ea6-cd68-321b-af30-87ab6604e5ed | -23.75799 | -46.79912 | 2026-08-19 00:05:00 | TERRA_M-M | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 397850fe-d391-33c5-8600-7c95326c3149 | -21.19554 | -48.52604 | 2026-08-19 00:07:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b299fdc0-3226-3d4b-a18a-c872d12b32cc | -19.75141 | -57.92149 | 2026-08-19 00:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 985d1e21-eb3d-3d17-9b62-fd17bb97cf32 | -19.7706 | -57.95514 | 2026-08-19 00:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 56c7566a-2c73-3864-84bb-c6ffb6988bdf | -19.81301 | -43.08392 | 2026-08-19 00:07:00 | TERRA_M-M | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 090c58b5-a415-36a1-b9a1-da31919f0ecf | -18.58696 | -41.32708 | 2026-08-19 00:07:00 | TERRA_M-M | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| 4c3f20a4-41e7-3780-85ed-878274c297ea | -19.48502 | -45.97908 | 2026-08-19 00:07:00 | TERRA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ecaa4a82-0ab9-3c30-b741-8ac5aaa5077d | -20.58579 | -45.93095 | 2026-08-19 00:07:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 962477ef-9230-3431-87fb-701c46899378 | -18.84657 | -47.14327 | 2026-08-19 00:07:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 05d36c94-fec3-358f-871b-011af227f26f | -21.20568 | -48.53415 | 2026-08-19 00:07:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| f5dcb602-beee-324c-aa7d-a179bd63b17e | -19.76567 | -57.98488 | 2026-08-19 00:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.6 |
| e7360836-2da9-3611-a06a-499d4e752774 | -16.58416 | -46.75391 | 2026-08-19 00:07:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f644249-4b78-3222-8fa9-0a108dc25759 | -19.75449 | -57.95666 | 2026-08-19 00:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 550.2 |
| cded9321-42db-316a-861a-31c8bcb96666 | -17.50518 | -49.96877 | 2026-08-19 00:07:00 | TERRA_M-M | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 00b54cd4-4b08-3e79-bcce-096b2f9cc39b | -19.76279 | -57.94949 | 2026-08-19 00:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| ee6bc13a-2f91-3920-af6d-0a3084288a83 | -20.41926 | -44.09464 | 2026-08-19 00:07:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 41c8faee-9fdc-3adb-83ff-f4eb5f0e6b7d | -20.58729 | -45.9408 | 2026-08-19 00:07:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4c29e58a-2541-3315-8b6f-9da2c8afaeab | -21.76194 | -47.54647 | 2026-08-19 00:07:00 | TERRA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 699834de-efa2-35ce-8915-b8922c1cfde2 | -21.04156 | -48.4693 | 2026-08-19 00:07:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 42accf4b-eee4-3610-aa1a-91bb655ab750 | -19.73838 | -57.95818 | 2026-08-19 00:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.8 |
| 33610ece-7d8e-349b-8c44-0f13285f5b4f | -21.45218 | -48.51661 | 2026-08-19 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 773b81bb-6cbe-3fff-897e-bc2b681429ad | -21.52926 | -52.00838 | 2026-08-19 00:07:00 | TERRA_M-M | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| c136662e-2f63-3be3-b72c-35ad9f6846be | -21.40493 | -48.71527 | 2026-08-19 00:07:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d12c91d0-8b4d-3ec8-a375-2b337d2b755c | -16.57672 | -51.62586 | 2026-08-19 00:07:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e65485a2-722f-393a-96ed-4ca67719decf | -19.46613 | -44.18149 | 2026-08-19 00:07:00 | TERRA_M-M | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2024afc5-baca-3fe8-bb3b-593493554ed1 | -22.45534 | -48.58731 | 2026-08-19 00:07:00 | TERRA_M-M | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 7d4db798-b95f-35f7-bb1e-dfff1b1af28c | -20.57653 | -45.93256 | 2026-08-19 00:07:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 3cd990fb-8697-3758-aa40-f3dfa980fe71 | -19.06954 | -57.36412 | 2026-08-19 00:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.5 |
| 7a7993a2-2861-315a-a1b9-a837d864f72f | -20.56927 | -45.92963 | 2026-08-19 00:07:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 295a0b9b-1214-3323-8464-a2433583885f | -22.42286 | -51.73265 | 2026-08-19 00:07:00 | TERRA_M-M | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 5fe98547-d5a5-31d6-9157-e82dc6cbe943 | -19.05424 | -57.36561 | 2026-08-19 00:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.3 |
| 04ff35f3-f4c1-39fa-a740-02e2340795af | -17.45666 | -47.86407 | 2026-08-19 00:07:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 25797442-eef1-3d9a-a6eb-7293918e90fd | -15.60553 | -46.57694 | 2026-08-19 00:07:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 299f8bc1-ec90-39ad-95db-c82759462d6d | -21.04283 | -48.47878 | 2026-08-19 00:07:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c3a32045-42cf-353f-b655-e0203109abbd | -21.45089 | -48.50706 | 2026-08-19 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 390c74da-7b6a-3420-b006-f243368abb74 | -17.61281 | -46.653 | 2026-08-19 00:07:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 49d7e517-d846-387a-97c3-bdd189e35d13 | -21.2044 | -48.52465 | 2026-08-19 00:07:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 9bd84d79-66cf-30d9-8da6-f9c5ed9ca64b | -19.11643 | -44.47948 | 2026-08-19 00:07:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| efbd82f5-cca2-3c15-b015-68cb13b92a13 | -16.57537 | -51.61497 | 2026-08-19 00:07:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 12e6cd0c-efd9-3c33-a1dc-d02d62802246 | -6.89323 | -56.44343 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| c3729e5b-c5f4-32f3-80cd-41ec2bf14e1b | -8.58044 | -54.78125 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| fc6f4910-c6eb-32ab-b5dd-7dcc2722554f | -14.49163 | -45.67066 | 2026-08-19 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| cf0c56b5-f908-32ca-b9a1-2fe056eea6e3 | -11.06349 | -46.52371 | 2026-08-19 00:09:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d628c530-392e-363d-a313-664aaca0f373 | -11.21926 | -55.07217 | 2026-08-19 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| b1dff6dc-e133-3bfe-b2f1-4878472e3ed5 | -6.74659 | -59.03888 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b1a5aecb-9ffa-36c5-bb37-20bc49a75953 | -9.06089 | -50.85518 | 2026-08-19 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 58748221-cc0a-3b48-8185-55f6b18b2f23 | -8.55249 | -54.73152 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ac94c198-063f-3e83-9478-4a04391f134e | -10.8865 | -57.12495 | 2026-08-19 00:09:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 14cd25ae-48de-31ce-80a2-a984e07d1481 | -7.54115 | -55.61 | 2026-08-19 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 57a0da8c-f0b4-3cf5-8447-7be5ec5a296b | -10.63917 | -51.62669 | 2026-08-19 00:09:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |


[Clique aqui para ver as próximas entradas](README2.md)
