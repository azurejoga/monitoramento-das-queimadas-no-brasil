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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96e667c9-3091-31f0-af16-9e12e260bdd1 | -9.60949 | -55.01831 | 2025-09-07 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af9e1122-2a49-328b-b50b-bcdac17a6f29 | -11.58611 | -47.17601 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd0383ac-1c9a-3540-9c68-f04147281899 | -9.68766 | -51.07317 | 2025-09-07 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f4e91f4-b99c-34c0-a775-f90c82ede71c | -12.95128 | -54.79103 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5174efe6-c44c-357e-a53a-cab37eae882e | -8.68647 | -45.31382 | 2025-09-07 05:12:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| edff3356-fce5-33e6-bf74-1c041abb010f | -9.68706 | -51.07765 | 2025-09-07 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af46cea6-7223-3683-b8e9-c1ec66968d55 | -9.93514 | -60.10645 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d691586b-132e-35c5-9aa4-d4f9cb0b0b1a | -10.0747 | -49.29808 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a0f91717-4815-353d-bd92-876b40ecea13 | -8.68945 | -45.3153 | 2025-09-07 05:12:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fbfe4392-9530-36b6-b4e0-183fd6955f19 | -12.79459 | -48.01925 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 689dd28a-2c7f-36d7-b3be-4c682ada4143 | -8.93841 | -48.6533 | 2025-09-07 05:12:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9d862e0-5e32-384f-b003-728ccf221136 | -10.58468 | -48.47704 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| afd91b9d-a422-32f1-8e8a-9dbe159024db | -9.09361 | -46.99346 | 2025-09-07 05:12:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 373d2ad9-f178-3ff1-8ed2-c1953f3607a1 | -8.07056 | -52.38151 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd17f940-8250-3224-9fb0-d70bedf7f8d5 | -12.88221 | -47.99307 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e6b0b95-59d6-3869-a2e4-fd911adfe192 | -13.65843 | -47.91188 | 2025-09-07 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de4181ba-c411-3d5c-83cc-1fffdbab5ccf | -13.82694 | -46.28404 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 70926f18-3f2d-3bed-8214-d3dbca24c0a0 | -12.93037 | -54.7732 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| fed7efd6-b3ea-3af2-8490-9918850fc8ef | -13.03005 | -48.08147 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd3fc604-3008-3a30-8580-6e1b2f382410 | -8.06961 | -52.38801 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ee42313a-6911-3c87-9495-3fe65152b314 | -8.06436 | -52.33665 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b4e86220-b926-3a8f-8af3-7e1b4f048277 | -11.13492 | -48.38177 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b33fcd55-3656-3711-9f4e-eeb795c341b6 | -13.29649 | -51.74409 | 2025-09-07 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90ca002e-676f-3e4f-9b21-6285872e143d | -12.77953 | -52.95647 | 2025-09-07 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d0ad0799-122a-3378-9fe8-9214e3263fb6 | -11.15611 | -48.39739 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9965e62c-1485-36bd-98c3-c34fec17642c | -10.3357 | -46.39729 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a0af05e-46ef-3503-88be-7a4de50d68ee | -11.61295 | -47.16133 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1af489ea-8c7d-3ed1-95e0-d0fb909b0407 | -12.62009 | -56.98225 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f492e2b8-a4b6-3059-b33e-7db182ec290c | -13.02643 | -48.08239 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d5257ab-8c5c-3854-9cb7-923bacaac4b8 | -13.55321 | -48.11655 | 2025-09-07 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c6e379ba-7b35-325a-b4b0-c499e42f4396 | -10.37763 | -44.96746 | 2025-09-07 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8b733a8-408c-3f27-a9dc-ed5fb974109a | -11.05313 | -54.17126 | 2025-09-07 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bb3b4e50-4158-3de0-a703-6b6c4622721c | -9.70746 | -49.48694 | 2025-09-07 05:12:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fd83ab6-6ee2-3296-bf84-4b1b30969a9e | -12.94116 | -54.77977 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2327097e-03e2-3b5d-b5e9-0d3d88c571e8 | -13.06147 | -48.07027 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00807793-5905-307e-b8a7-ecf6e809ae10 | -13.91936 | -48.03719 | 2025-09-07 05:12:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adc68e91-9c27-374f-8305-8ee342b62924 | -11.22937 | -55.01426 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55eced1e-7b10-3cc6-bb34-1158e6388405 | -12.80647 | -48.02099 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d205c372-6b18-3857-8c2c-572c52ac2849 | -11.98182 | -50.40265 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48dcfe04-295a-39bc-80dd-40d51797719b | -10.57958 | -48.47218 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d394ed3-198a-3162-82bb-c10593568c4a | -10.16396 | -46.22306 | 2025-09-07 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d20582d-adad-38bc-be76-f7349f14589c | -11.15698 | -48.39043 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b3a8ba1-2212-3d16-a5e8-314852b4a43b | -10.72262 | -48.58916 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a400bbb-545b-312f-bc51-e349a234ff6c | -13.83427 | -46.27848 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1bd03e3-75a4-32a5-bd37-1e80c7a16379 | -11.21398 | -55.01659 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 26c69bd3-83e1-3f8d-bff1-1c7aba2a05c2 | -11.11305 | -52.02218 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0aec62c-aaeb-3bea-a47e-7fefef648b67 | -13.00715 | -54.80893 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9416762a-a157-335e-bef8-e58187a62146 | -11.32295 | -55.21826 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95e83a2d-047a-3c2f-9771-44417d546360 | -13.0112 | -45.22166 | 2025-09-07 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9e9baa2-ed82-3df9-9b3f-5a029eac29a9 | -12.80973 | -48.01688 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fbebfe62-9fab-33fe-8f59-995b7ddf4519 | -13.55424 | -48.10765 | 2025-09-07 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 97df6d2e-29e9-3dd7-9f87-be9a5d84c91e | -10.57764 | -61.25329 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce624499-b8bd-36e9-97a4-b889bd3f5cb7 | -12.84336 | -48.01537 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf932ca5-6bf1-3de2-ad2a-46463468ea0b | -13.06194 | -48.06609 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| faf0fb53-4e75-3c24-9f3e-a2d61ca719b4 | -12.84622 | -47.99022 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44bdefa4-4326-3f1f-88c6-2c724fbed6a7 | -13.01213 | -48.07992 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e78a468-af71-3741-bb03-eef4f0346e0f | -13.77764 | -52.76659 | 2025-09-07 05:12:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0cab4154-8ef7-3872-bd6f-17f6dc1201ef | -11.15392 | -48.36848 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2afbaa3-94ce-33c7-95d6-40808b0e78c1 | -10.72743 | -48.59594 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f371439-7caf-3689-8037-e7e9e3d25548 | -12.63719 | -56.98492 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3615c791-ba1f-35df-98f4-b6c8e32b27c8 | -12.81879 | -48.01886 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5350eb90-45dd-3146-8344-7ba4db9b72b1 | -12.12198 | -59.83773 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba99e74a-1866-3187-8137-cce47deb5678 | -13.05643 | -48.06138 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16b8eea9-c7a2-3588-9d5b-8445903459d7 | -8.34665 | -48.27314 | 2025-09-07 05:12:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc9a40aa-86fc-3e11-8bcd-3957c9b81168 | -10.58185 | -61.24976 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c21adb2-750d-3b8e-ba57-ce9337fcca1e | -8.34493 | -52.55234 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d0f0ecb-4f83-3667-acaa-23b8d5b25d29 | -13.83612 | -46.25984 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2a650057-2865-3b51-9f9c-6048df82f09d | -10.15754 | -46.22203 | 2025-09-07 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1d82ea8-7a9d-344c-a027-b387ed46a4f9 | -11.32175 | -46.54816 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3e5cd5b-b066-3efc-a5f1-bcc0dcc64ac2 | -8.68715 | -45.30817 | 2025-09-07 05:12:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f3ce2f63-6024-3767-bac5-5b1522da0322 | -10.72149 | -48.58868 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bd8461e3-7043-3d24-a223-6df4382cff20 | -12.95246 | -54.81063 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb9d7acb-988f-3315-a6ae-40a2f476f2d5 | -8.69843 | -54.67823 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c3cfb24-c20b-3b99-9daa-7d1f824babb1 | -12.94629 | -54.77073 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 2df2fa3c-4040-3cec-bf5b-35854cf34a0d | -8.30947 | -55.09885 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59b22ce8-3f04-3b9d-b7b7-364fd73e2846 | -11.31988 | -46.56453 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 916fe08e-1e5f-3414-9a73-bdc9e82f892e | -9.93573 | -60.10275 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99faecce-cefc-3f60-beb7-11376b242248 | -12.828 | -48.01571 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d934f33-af25-334f-a6a6-57854c0aa916 | -13.04767 | -47.12701 | 2025-09-07 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 162b307c-0b76-30b6-9c4e-d020575c9ddf | -11.21702 | -55.02155 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce6f59aa-de2c-3ee2-8223-d4f530a25eb3 | -12.93558 | -48.03213 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8390f3be-ee27-39ca-b77c-019bf2fde2bf | -13.82857 | -46.26762 | 2025-09-07 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 538c368c-6785-3ceb-9a9b-8c193c0f0540 | -8.34019 | -48.27959 | 2025-09-07 05:12:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93830a94-2d29-3ad4-85bd-c2127d07f936 | -10.17927 | -46.24744 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2278efad-5b49-3938-94be-b103a9e83f61 | -11.62525 | -47.15467 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e53b593-8193-3b5e-a814-80efe7afcb8f | -13.30116 | -51.74475 | 2025-09-07 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86a47516-d8be-37b0-99c9-e89ca30877bc | -11.69802 | -60.16397 | 2025-09-07 05:12:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72c0e5dc-092a-3f6b-8a72-7c04e4f3f118 | -12.63775 | -56.98111 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 106d2e37-4fcd-3309-9ddd-d0686a3af50e | -9.93632 | -60.09906 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b053b54-8b55-391f-b24f-d6042300fe72 | -11.8255 | -46.76852 | 2025-09-07 05:12:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c8e3e67-c204-3a8b-a190-15301a5151f9 | -11.31022 | -46.53522 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6051415e-2ede-333d-9edc-8d3efade9c3c | -12.63433 | -56.98059 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd2c6b59-dec5-3ac8-8d2b-5c85f9ae166e | -12.47564 | -53.85725 | 2025-09-07 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7843323a-93ba-3747-9f14-c8fe883ed82b | -13.85083 | -46.24852 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48ad9c61-9c64-3670-be41-9fc764834a0d | -13.55084 | -48.11201 | 2025-09-07 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3c0ede09-008c-3908-b53d-5d8e5bdc6ed1 | -9.60886 | -55.02253 | 2025-09-07 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cf1caa8-2954-3a98-b6f3-160eab8ae24b | -11.21093 | -55.01161 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ad04c041-945e-3032-b55c-04e9890a632c | -10.57408 | -61.25288 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b13bfe43-b920-38e7-9959-d9dcd2f18b81 | -11.21029 | -55.01603 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6ac00c06-d313-350f-a46f-8204b617dfbd | -11.16139 | -48.37403 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README71.md)
