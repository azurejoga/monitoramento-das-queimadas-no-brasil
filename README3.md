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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df3c2418-2e99-32de-aed2-d82dfd0ee8e4 | -20.71704 | -48.63277 | 2025-01-13 04:18:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 353d0577-5fc5-3758-a2c2-5bf495ba6438 | -23.38804 | -47.3283 | 2025-01-13 04:18:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7116410f-e4eb-3184-8f62-0ea9a6009d55 | -22.20497 | -47.70243 | 2025-01-13 04:18:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1479c3e9-2fcd-356f-905e-039acaf5d9fa | -20.71295 | -48.63605 | 2025-01-13 04:18:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1618e916-cfd7-34fd-ad47-139b2fd6abbf | -22.20436 | -47.70615 | 2025-01-13 04:18:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8118e0be-2b6a-34f6-bca2-402bea82d1d1 | -21.44546 | -48.61185 | 2025-01-13 04:18:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c563f20-4555-3ed2-aaf7-0ab2f426d3c9 | -20.76435 | -46.76963 | 2025-01-13 04:18:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 220db487-fe84-3d21-9f1e-7d7be61a3d0d | -19.81846 | -53.83654 | 2025-01-13 04:18:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecaf7762-de7f-37ce-aa60-477ad41d1282 | -28.7599 | -55.6114 | 2025-01-13 04:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 149.9 |
| 0a83cd03-52fa-32ba-9136-22ae89b094eb | -28.7367 | -55.6396 | 2025-01-13 04:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 75.5 |
| 9d11bf32-3319-3894-9e30-a6ae3505dcb1 | -28.7592 | -55.6345 | 2025-01-13 04:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 214.8 |
| b4109298-3bde-3fad-810e-1219298a805f | -23.98494 | -48.91784 | 2025-01-13 04:21:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e433ead-1ba3-34f2-b395-a6d41054e0e4 | -21.97346 | -55.35454 | 2025-01-13 04:21:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e43eb212-22b6-3781-bde4-cab993cfd47d | -29.46484 | -55.93907 | 2025-01-13 04:21:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| dc958948-d47e-3b47-b4ff-dee8c60bdb11 | -28.76044 | -55.62743 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 107.5 |
| dc04b0d3-9a54-33ac-b36a-11f6b0f2ef26 | -28.75844 | -55.63686 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 81.3 |
| 43fd52bb-37d6-3e72-be6e-969a2beada83 | -23.59516 | -47.43916 | 2025-01-13 04:21:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4470ba9f-c48e-3470-8188-b1de9f5641b1 | -28.75813 | -55.61694 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 19.9 |
| 56baa582-6347-3b77-80b2-7e42cbd4c26b | -28.75514 | -55.63104 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.3 |
| 29aa35c6-4cf5-3c8a-a5f4-d4ceb01d7b7f | -28.75184 | -55.62519 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.3 |
| d89dcac9-9bfa-331d-aa82-2510642f4d08 | -28.74688 | -55.64861 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| e976011e-60e2-36ed-bdd8-bacd4515aaf4 | -25.19311 | -49.32898 | 2025-01-13 04:21:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad2e5361-4769-3623-87e9-786b6f942b0f | -28.76112 | -55.60278 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.1 |
| 2bebd1a6-847a-310c-bd03-b4b77745a6f3 | -28.74657 | -55.6287 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 2f6a4498-23f5-3b07-89c0-ddab66a0045c | -28.75414 | -55.63575 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.4 |
| c55cd655-94c9-3d93-917d-a5237fb7f570 | -28.75085 | -55.62988 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.3 |
| 751180da-6ad7-36b3-bab1-f11344b74f62 | -28.7634 | -55.61338 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.1 |
| c0747008-b7d7-3a73-a515-5d37f9571ffc | -28.74986 | -55.63455 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.4 |
| e97af2f2-a7ab-30f6-8664-f476d5d17d10 | -28.75483 | -55.6111 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 45.6 |
| b730b06a-6249-3eff-a067-9a1570fe468f | -28.75613 | -55.62634 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.3 |
| 7f6294cf-ac66-3e78-b372-ad87a08a0996 | -28.75944 | -55.63214 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 107.5 |
| c0b9bcca-5abf-3963-845f-7c1d1fdcd1be | -28.75912 | -55.61224 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 45.6 |
| acf9195e-5ce0-37a7-b08c-431775118e94 | -28.76012 | -55.60751 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 45.6 |
| ab1f8eb4-9bcd-357f-922d-224f21f0222f | -30.12955 | -51.96658 | 2025-01-13 04:21:00 | NOAA-21 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 60842c38-e27d-331a-bff1-0bd392eb17c2 | -28.74788 | -55.64389 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| 84e76ae7-8d6e-392b-b4cc-c3f3bf14beaf | -28.74887 | -55.63922 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.4 |
| cdc1b13d-0c1d-3d7b-938f-9b9d126d3e4e | -28.75315 | -55.64043 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.4 |
| 6d8b4b12-0033-3667-a734-d4e8f3baae33 | -28.76212 | -55.59808 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.1 |
| 05fce8c0-3bd0-358a-857d-64c5362f368b | -28.76143 | -55.62273 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 77.2 |
| 3e94d610-8d57-33b7-ba06-50ccedf3170a | -28.76241 | -55.61806 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 77.2 |
| 6adebfef-8e4f-38a8-8093-bfd3c6dffa81 | -28.75744 | -55.64157 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 81.3 |
| 443f6021-fb59-382b-b91d-153c84ec02d6 | -28.75384 | -55.6158 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 19.9 |
| 66df9bc6-0027-396c-b4ad-0faaa8e1ddff | -28.75284 | -55.62051 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 19.9 |
| d5c470a6-b7d3-3229-85e7-c238b0a1d46e | -28.75713 | -55.62163 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 19.9 |
| dab74a17-5021-3a72-afd9-06593a809d4a | -28.7644 | -55.60868 | 2025-01-13 04:21:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.1 |
| 3a556160-5660-3cde-bd4d-ae0b7d7901ac | -24.30886 | -53.09996 | 2025-01-13 04:21:00 | NOAA-21 | QUARTO CENTENÁRIO | PARANÁ | Brasil | 4120655 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3570d5a1-8d2a-32f0-95e7-9040ce195f0d | -28.7592 | -55.6345 | 2025-01-13 04:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 94.7 |
| 634e0f3e-8e53-39d5-9c22-5163c23313b2 | -28.7599 | -55.6114 | 2025-01-13 04:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 124.4 |
| a3c02d73-c174-37c6-b928-c3c4ac3c786d | -2.01297 | -52.07429 | 2025-01-13 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fe00f57-5a21-36a5-8b21-76356e6750fa | -2.60533 | -47.53369 | 2025-01-13 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42a6fff5-8e00-36e5-8dad-7f70adbce550 | -3.34955 | -53.25082 | 2025-01-13 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c22634ff-96ca-35ad-b8c8-0ffef39e997e | 1.1742 | -60.50003 | 2025-01-13 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c769f82-0395-35d3-9520-679a38481745 | 2.45663 | -60.12352 | 2025-01-13 04:38:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba7ea5d1-6537-3153-81dd-bea8b3699548 | -5.21418 | -43.29838 | 2025-01-13 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01d11271-87c7-32f4-baf3-989ee07f7b1b | -2.4712 | -54.26223 | 2025-01-13 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9344bac-a76e-315e-98b6-5c77d9282aba | -2.60196 | -47.53316 | 2025-01-13 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 720b9ea2-6203-3e23-8a90-064579ef7709 | -5.20924 | -43.30177 | 2025-01-13 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 89099871-7fc6-39b4-a5b9-b29ef40f4f29 | 0.55683 | -59.69429 | 2025-01-13 04:38:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31256e08-ee0e-307d-b465-329524cccfdf | -2.60588 | -47.53014 | 2025-01-13 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e7e0c79-c50d-3dda-8baa-b5716f7e358b | -2.60251 | -47.52961 | 2025-01-13 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2048e0d9-f476-3a8e-82c5-35ef0fe64d02 | -1.46837 | -45.71465 | 2025-01-13 04:38:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 703f4e11-2290-3bd4-8b3d-96069f70e59b | -1.469 | -45.71064 | 2025-01-13 04:38:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29ea9461-9124-3a32-b066-4d666bc53920 | -5.21851 | -43.29909 | 2025-01-13 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bdc223c-55d9-36dd-88b0-4fb0be260d22 | -2.6407 | -48.64426 | 2025-01-13 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74e708d8-3df3-3a69-b3bb-908390b75240 | -2.42519 | -48.05682 | 2025-01-13 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4c5e24e-0b3b-395c-9099-b870316647cc | 2.44996 | -60.12452 | 2025-01-13 04:38:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6cc3f11-fb51-3302-a356-2bb7ffa12407 | -5.21357 | -43.30249 | 2025-01-13 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 90e58d1c-4093-3428-9bf4-b7506121f8d5 | -2.42853 | -48.05734 | 2025-01-13 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b3015ff-26d3-3e0b-8788-b2207767e41e | -2.42574 | -48.05334 | 2025-01-13 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b547d009-3b3b-36f9-b639-49baee5002ec | -3.86853 | -54.23296 | 2025-01-13 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e67ed5aa-c99e-3df0-90c3-c2750f98e2ad | -2.42907 | -48.05386 | 2025-01-13 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c6b2c97-b796-31ef-aa50-972773e1b502 | -3.87165 | -54.23312 | 2025-01-13 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61c4d621-90be-373c-8a6a-57985080ae2a | -5.20491 | -43.30104 | 2025-01-13 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7523e97f-6af0-31ab-9a93-afe635ff5296 | 0.56235 | -59.68829 | 2025-01-13 04:38:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d436f5d-1b13-327c-a53a-3b3eda2d7fab | -1.87824 | -48.71551 | 2025-01-13 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aff5aa12-6a16-30a1-8b1f-e33dbc6f1d86 | -1.41447 | -55.01236 | 2025-01-13 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1415f146-5285-31f5-969c-8818dc8df2df | 1.18089 | -60.49898 | 2025-01-13 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae32f10-5e36-355e-9b74-429e55aa88b5 | -3.87262 | -54.23364 | 2025-01-13 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a275aed5-b1c1-38c1-91b6-f1d46f0c6f90 | -28.7599 | -55.6114 | 2025-01-13 04:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 81.9 |
| 446c1b95-2cec-39c4-bd77-9b59aae5058c | -28.7592 | -55.6345 | 2025-01-13 04:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 68.2 |
| 32e4382f-d38f-3e98-ac22-cf744ef04f33 | -19.81825 | -53.83218 | 2025-01-13 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3eb6da6-031b-31dd-ac14-5c98cd7c59e5 | -24.30888 | -53.0982 | 2025-01-13 04:44:00 | NPP-375D | QUARTO CENTENÁRIO | PARANÁ | Brasil | 4120655 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc93173c-22cf-3ab1-91c4-a83635bcfa44 | -19.75115 | -45.50338 | 2025-01-13 04:44:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3bf9254-b3d2-3608-b647-d7eecff572a5 | -24.03197 | -52.38793 | 2025-01-13 04:44:00 | NPP-375D | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7b1dc36-e07e-37d6-8e6d-a43370a2cc87 | -21.97074 | -55.35575 | 2025-01-13 04:44:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ae6df96-298a-3ce8-823a-e16c87f1485b | -19.62241 | -54.15114 | 2025-01-13 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66244cc6-2a1e-30e7-83b4-2e8a3c2f6050 | -21.97142 | -55.35174 | 2025-01-13 04:44:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07aa4a72-1ec2-381f-9e42-eadf84850b89 | -20.7133 | -48.63498 | 2025-01-13 04:44:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8b927b3-af73-352a-88f7-1440598fd2cb | -21.44485 | -48.60631 | 2025-01-13 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| dd9681d1-a0a3-3116-b8e5-bfe9a1602512 | -23.59207 | -47.4398 | 2025-01-13 04:44:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe8ed053-bb98-3fde-9efe-b967c24b8796 | -21.44419 | -48.61136 | 2025-01-13 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c11c6d3-bca1-3c49-9a97-7771e5d88fe6 | -23.98557 | -48.91684 | 2025-01-13 04:44:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ff1e702-4b5a-3e8c-a9c3-3a7f6f2d0d0a | -22.21945 | -47.69993 | 2025-01-13 04:44:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d595f10-613a-317e-a4e6-e16e623c20fa | -28.7633 | -55.59943 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 11.2 |
| 939599f7-dae0-30ab-9ed3-ec9fe7e5c168 | -28.76138 | -55.61135 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.5 |
| e27417cd-e48e-352f-a4d5-d765628d836f | -28.76074 | -55.61532 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.5 |
| e40093dc-b3d8-329b-9a83-a575ea341bce | -28.75021 | -55.63776 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 808a19c3-9afa-35e6-b7dd-e739729f4107 | -28.74751 | -55.63309 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.8 |
| 10802ccc-def2-3d36-9825-a708077530a9 | -29.46365 | -55.93687 | 2025-01-13 04:46:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 0463fc71-90a7-3515-bff6-4eddef070181 | -28.7601 | -55.61929 | 2025-01-13 04:46:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.9 |


[Clique aqui para ver as próximas entradas](README4.md)
