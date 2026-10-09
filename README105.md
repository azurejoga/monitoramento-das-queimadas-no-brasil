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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20c00dd7-3651-3931-95ff-8550bdbc0fd6 | -9.58109 | -46.83641 | 2026-10-09 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f96f063-aa0c-35ef-bf44-0ba22c6f1a7c | -5.9649 | -55.36617 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d09ceeb2-e1e2-3a45-80ad-f44fffa1697e | -7.59193 | -46.76532 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ff5e07c-61e5-36df-98d5-db61a7c37cd4 | -10.97924 | -45.39565 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0bf7eb75-7c63-3eee-bab1-4c1f7d5da9ba | -6.38864 | -55.2648 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4d770d2-2df2-39bf-890c-bb9f647a61a8 | -8.67733 | -47.09039 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9a271fd-9a86-32ee-afaf-dff35c9e84a6 | -10.84448 | -47.93888 | 2026-10-09 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9cce96e2-b664-37cf-b31a-d9002e8a6260 | -11.26064 | -45.1777 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b7f653d-ee72-3b7b-9390-23b024c61031 | -11.76843 | -58.2803 | 2026-10-09 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 027854a5-d353-36f6-904c-19a17491ff14 | -13.15523 | -54.34203 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b3a8195-1e46-31dc-bd84-61511acc8963 | -13.18844 | -54.36459 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2ed511e-8d72-3384-8992-e83d56310f49 | -13.19984 | -54.37563 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f75aef8b-4478-3597-92d0-f2ca8d59bb7b | -6.50861 | -55.40952 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f55cfbb4-a04a-386f-9b6f-bf7e5de8eb9e | -11.6406 | -43.69267 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6dec8d4-dc24-3375-99d2-f0be3b44bbf1 | -11.75145 | -61.06046 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3f14f9ce-e488-35e1-8f9a-10b8b0c71696 | -11.66007 | -43.69062 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e33339e-5683-3528-96ee-e16529bd3584 | -8.22334 | -46.37903 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b49c374b-7894-3af3-a88e-28d43c752695 | -12.21812 | -57.1355 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53135f1c-6e0f-3621-a6d0-b97f2928db46 | -7.40228 | -44.74974 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 10e259bb-d51d-3c76-a288-6a87b48116b1 | -12.81639 | -44.65113 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 926532ea-05fe-3718-bbfd-4cf8aad030ff | -11.5999 | -43.70322 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27b6c0e5-4ee8-3a40-8fe1-963cff5c1f31 | -7.29059 | -45.41357 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 934802fd-de03-3723-ae0b-6c638dd9bc61 | -11.75991 | -45.4722 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8132cdbd-e6c0-38ec-b829-f970756b7871 | -9.7422 | -47.80739 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 510b622b-5933-354a-a5e6-07e610535f1f | -9.04857 | -47.73772 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| efffac46-5317-30d0-9374-49a250a73581 | -11.90791 | -46.56305 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddc5e356-afe5-3fdc-8308-4f3ade334a44 | -8.33665 | -49.12412 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e24986c-452f-3ad0-ade6-8d8edb4e6be8 | -9.79488 | -49.01566 | 2026-10-09 04:27:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f167e9b-0a80-32f6-b198-348e73afde41 | -8.34009 | -49.12468 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae495e2c-1c5e-3cdd-a02b-dd58f1fa1d92 | -12.0112 | -43.47487 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb70c6f4-d2c7-3edf-9fcb-5eb0b6c25185 | -13.03161 | -46.81548 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9210f84b-1a95-3362-91fa-6dd48e761050 | -11.20986 | -45.25733 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5c52964-a242-3127-8444-15514e21dace | -12.09454 | -57.15646 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 39b7cd0a-c863-3164-817f-c1d2f1126c8a | -9.30082 | -47.43207 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| f55dd282-d45a-3414-a0e7-591260c9bb77 | -10.93572 | -45.38103 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b807d19c-9c86-3ca2-ac43-696b3c6ef4ee | -6.38804 | -55.26812 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b87938d1-91cb-3751-b193-77997ef26cb5 | -12.2529 | -44.75085 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93ad6c8a-ae38-368e-8ae2-04d0b4cf3a3f | -14.05279 | -43.82705 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6d8d8a3-93ff-3a03-b0cb-484f33c44d8a | -8.17385 | -46.39267 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1169470c-1fd5-34e9-93b2-c9331b7fe93e | -9.08014 | -45.10998 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c544ac91-b8b3-3c16-be79-c7cca1e6679f | -8.72171 | -45.16304 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a2c0b42-ba17-374d-b935-3acec205abf2 | -10.904 | -45.52377 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55777ebe-c460-3354-b554-de1d809d6e76 | -11.22606 | -45.31507 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17849c11-8b52-318b-96f4-ac8cb3e4a719 | -12.00426 | -43.46859 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c7a3ef7-5636-395a-9cea-d92a58b232a5 | -12.20227 | -57.13234 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 967e3c64-b9b8-3144-beb1-960ea314d922 | -13.36825 | -43.88655 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a261e35b-ac78-31f7-b9ef-0327019dc527 | -12.21551 | -57.12745 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8277c516-ebaa-3fae-a825-94f2ec33b553 | -8.1843 | -46.39073 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccec4a97-d9ea-34e3-a5c2-ea7e190bccee | -8.73527 | -45.1424 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5cc4b386-cb59-3d24-a62b-90e4583268b4 | -11.76363 | -46.77424 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3339acd2-6b95-3229-a2bd-36b9f3a46fa7 | -12.58394 | -42.22472 | 2026-10-09 04:27:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7aa1f14-60f0-30f6-9e11-16658347b2ab | -6.51306 | -51.12067 | 2026-10-09 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2558747c-1ae9-31b4-84fd-b2d7d4d8811a | -12.21428 | -57.13401 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ccc259b-052a-3f36-a873-32831f9ecd9f | -11.48577 | -54.61457 | 2026-10-09 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d80f9182-0fab-33aa-964b-0120d5a90093 | -11.05605 | -44.05024 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3f674b4-b065-33d5-be1a-d97d4dbdf646 | -6.57793 | -53.02266 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98f90b6c-ce95-3267-bca6-d26c9b079309 | -7.08856 | -52.6823 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab49385d-5f07-343c-9933-30b95f3533a1 | -7.87094 | -44.14391 | 2026-10-09 04:27:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6edb6b74-1f7a-3a1e-87fb-5d394417150b | -6.12266 | -55.6984 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26882189-9d26-354f-b365-559e96b84ed4 | -11.79967 | -46.7835 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6519f072-3393-3523-beee-75829d98ff87 | -7.96355 | -46.88813 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a3555b4-0836-30c3-a32d-c5e62925da51 | -11.00958 | -45.42767 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bc76fd0-e81a-34f7-bd9c-7361d36d0046 | -11.25436 | -46.29977 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9010a51b-fb4c-30d2-b0f3-4f97523f01fd | -8.91391 | -45.21497 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8248128-9f9f-3d39-9f73-686eb6f465d8 | -11.115 | -45.68576 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02f96c49-3cbd-3eff-baa5-5d9fe898b9d1 | -8.97282 | -45.1707 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0935e9e5-9d7c-3520-9bd3-03c2194fedef | -7.48362 | -42.83364 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 88271d7f-3c95-3a15-ba17-1ff7ffa75b58 | -8.96231 | -47.3777 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78cc584e-ab84-38ea-b749-4dfc56b8ba94 | -8.72567 | -45.15987 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e352c8b7-ab7c-3be3-9f07-a9c92709dc17 | -8.07691 | -45.60405 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adb2355f-7cc1-3ca9-b9a3-292018d24602 | -6.54321 | -56.0491 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bec2803b-ee92-333d-898a-e1637b178364 | -7.37705 | -55.21613 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3550d845-cef6-3045-a571-814fc95926ed | -8.30274 | -45.72956 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fe88aa2-45d6-3b5a-b053-0aa58ca6e28a | -10.00705 | -48.57964 | 2026-10-09 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59199325-da79-333e-be9d-12b69ef3e715 | -11.7878 | -45.58923 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 137d5678-6261-39dd-8d4c-48dea7c96327 | -8.97048 | -45.14002 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70c77d4e-5e2f-318c-a182-953ae3b0eaac | -10.88331 | -49.15148 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 436e87c2-6b1d-3418-98b8-8a0c26d102c1 | -10.50596 | -47.34079 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a1de11a-fb39-38c5-9476-76145419e661 | -11.25872 | -46.27085 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a72ca7b-f484-34f2-9a03-379b1e907f0b | -6.84662 | -59.29965 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c3fce04-5670-37bc-80cc-86334def83e9 | -7.20544 | -46.51616 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5828f78-2958-3c35-ad19-b6e7dc1f1070 | -12.22001 | -57.09775 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| af2c6d36-b836-3f1c-b840-13c0f4d8f3dd | -9.77395 | -44.78244 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 907dc402-2ad3-3939-a3d8-e465a43b17dc | -11.64309 | -43.70231 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 85a77de4-7931-3386-8e27-14af816de1fc | -6.93428 | -46.59322 | 2026-10-09 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f49787d8-c658-3d63-b686-c750cd8ba94c | -13.65073 | -49.40632 | 2026-10-09 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec14def7-cb81-354b-b5cf-5c0138119b04 | -9.27399 | -45.64328 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50824ec4-813b-3dea-bd9c-a0028bb20464 | -5.99633 | -55.37188 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7884f94c-afd5-387f-856f-1d87c69cc942 | -7.59523 | -46.76584 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23cd8a75-0625-3faf-9fc9-d4f177a3dd93 | -11.22261 | -45.31454 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 39f95289-48a0-39f8-a47a-cf615e3cb79a | -10.30858 | -46.5964 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49a5f34c-5575-3134-be4a-219499969ee0 | -8.9716 | -45.13264 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d419a4d8-9b23-346b-af98-4aeaa8cdf82c | -13.15371 | -54.35053 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dcfd0c26-d3f1-3dd5-bb66-8ea52804e201 | -12.01707 | -43.46072 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a082337f-f482-35b5-9afe-4e7769bf6b6d | -5.99229 | -55.36402 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0c04f9b-058a-38b8-9711-5d898b365168 | -10.85139 | -59.1142 | 2026-10-09 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b081146-09ec-3d8f-9027-a9b760e5026c | -11.23715 | -44.87501 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fa9f170-0eea-3648-9d49-82e15003ca60 | -8.08306 | -45.60863 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cd4465c-afb1-3ad6-9a0e-f4cd37aeb69f | -12.53497 | -46.52628 | 2026-10-09 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1307e822-3ff0-3f82-bee0-bb117c2e8b61 | -12.03822 | -43.44928 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README106.md)
