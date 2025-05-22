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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da50e573-d176-3386-ab80-4f799429b092 | -13.78348 | -54.31361 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e37e4a31-bda5-3823-bb93-474f8b2db0fa | -13.784 | -54.30909 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e245ac96-754a-3771-8708-826dfba2bcaf | -12.29004 | -52.50009 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2cb00008-c7a7-309b-8d68-63efb03cbfe0 | -12.28942 | -52.50581 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4d047084-9423-382d-8cae-6dd70a95e761 | -12.29067 | -52.50699 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dea53a47-3c66-3e25-b444-ed26fd0eff3a | -13.77801 | -54.30825 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2442e0ca-edc2-3d80-8c14-91edf57ac448 | -16.28535 | -58.66664 | 2025-05-22 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 06bc3ed0-39b6-320b-a696-e132262c09f6 | -12.29922 | -52.49065 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2315be1-9804-3f60-8321-b85bac69e2ca | -12.66798 | -58.2156 | 2025-05-22 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f79e231c-8bd9-3fc1-9999-f2207bee10e2 | -12.29198 | -52.49558 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7b2c2a7e-3047-3cbe-ba45-b22736e8ef08 | -12.29725 | -52.50782 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e563211e-f0a7-3936-a22c-b7e8c2b9a4dd | -10.05307 | -64.99826 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2cb747d-9b03-3e58-a9bf-a39d618c0ae3 | -12.67194 | -58.22092 | 2025-05-22 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d9717a6-7c30-3e19-9200-a18b02fca469 | -13.71384 | -57.48127 | 2025-05-22 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c49bebef-05d8-3b11-925b-63f2828bfc15 | -12.27878 | -57.26958 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04f311b2-8d4a-3ee8-b9fa-e62ffdc1da78 | -12.13158 | -54.6622 | 2025-05-22 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9f2ac96-ff2b-3331-9c2a-2016e9dee3c0 | -14.03556 | -53.38236 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7de1b904-59e2-35cb-b75e-8c16cc8e7838 | -12.02227 | -63.79159 | 2025-05-22 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0effaff6-fb3d-38a5-b8a9-a5390b0fe8c6 | -13.47538 | -52.28019 | 2025-05-22 05:38:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60f3085c-1509-37d8-81f3-2e657f088829 | -12.028 | -57.09824 | 2025-05-22 05:38:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd4cd1b8-75a9-38e3-b69a-97c41cc14a46 | -12.29988 | -52.48487 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd4e260d-7189-323a-b231-088eab7aea39 | -11.67515 | -54.94215 | 2025-05-22 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 167a6aeb-5d3e-3892-b8f9-635974bd40be | -12.13206 | -54.65802 | 2025-05-22 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 720b1c7f-73a3-3688-b093-d8b3684ede4a | -12.29065 | -52.49437 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 61a33470-c085-389a-9ec0-1b0bdac41c82 | -13.7807 | -54.30741 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d196597-07f3-3957-a535-4e8d83edd242 | -17.6164 | -54.17344 | 2025-05-22 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3c7b1438-412b-3658-90e7-79eb833d39c6 | -13.78022 | -54.31193 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec0c4879-609a-35a2-81c6-32c7efcd6424 | -11.67355 | -54.94305 | 2025-05-22 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e6e7c4c-9d4e-3f0d-a468-0333c56e44d1 | -12.10418 | -64.05779 | 2025-05-22 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42a92e44-452b-332f-95ee-19e808dad45b | -14.03167 | -55.14021 | 2025-05-22 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7bfffd5-7162-31fc-8547-07b2520784b6 | -12.67147 | -58.21802 | 2025-05-22 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d8124d4-83a2-35e6-a151-1c7187e15268 | -12.27946 | -57.26419 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5cfb36ef-4646-3653-964c-e108128a20f8 | -12.13569 | -54.66341 | 2025-05-22 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7952291f-8b68-3be6-8a34-92ac70703e90 | -14.02073 | -55.13453 | 2025-05-22 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ede526f-99fa-38fa-9f5e-8eaca77881f0 | -16.28476 | -58.67163 | 2025-05-22 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d5782113-9637-33fc-aa96-fee506c78873 | -13.66476 | -53.93428 | 2025-05-22 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79c1b163-a90d-3285-816d-693953e31ae2 | -10.0415 | -64.98567 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 059b6b05-6a1d-310c-92d3-b939f30a3ef3 | -10.02499 | -65.00451 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6156289-5c87-38f2-aab1-90a39fc48625 | -12.30444 | -52.4903 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc3a49f6-8d44-3060-ad79-f7a7d6077fc2 | -12.1362 | -54.65923 | 2025-05-22 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8dfc048-f5f4-3a76-8c8e-547c582c42cf | -12.2979 | -52.50212 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 05606c52-f385-3e60-b83f-d5251d08d546 | -12.66692 | -58.21743 | 2025-05-22 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a4806d0-3553-3552-9856-195e27004a24 | -11.66954 | -54.94153 | 2025-05-22 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea4b684a-e833-346a-b9db-272f1b86fea7 | -12.29786 | -52.48945 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b572bacf-bb46-3097-a882-d535c97c4871 | -11.91812 | -54.41045 | 2025-05-22 05:38:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 563f54db-36f5-3afe-adf8-d88672a5975c | -12.29657 | -59.83376 | 2025-05-22 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6416d43-0cad-3a9e-9c32-ceedcaa7a29a | -12.296 | -52.50666 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cf9d3c08-34da-34b2-b61e-fb68f7e62797 | -11.91761 | -54.41469 | 2025-05-22 05:38:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 956d2890-1d74-351c-b8cb-26d09748956f | -12.48903 | -57.18406 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d723a44-870d-3c14-8bc7-a874a5e0fc0f | -13.78452 | -54.30452 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 38204932-8b6d-392a-97c0-9611a0fc8968 | -12.29662 | -52.50096 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 25c7c3b7-65c5-38a4-9467-140d13361c87 | -14.02027 | -55.13865 | 2025-05-22 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19a31352-7ce5-3404-ac42-bf95ac92a21a | -17.62267 | -54.17473 | 2025-05-22 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b70f6b8-8573-3bf7-acc0-75270290555b | -12.28361 | -57.27026 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d3ce6d6-d313-335e-a766-4530ec5addd9 | -10.98962 | -59.16012 | 2025-05-22 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 228d995f-3639-39c2-9ca1-d99ed45a8c2c | -12.28409 | -52.50615 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bf164dd5-5454-392b-b2b5-39cabeb07bfe | -14.02118 | -55.13043 | 2025-05-22 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2969800e-33c7-3b42-ac66-786999fb53c3 | -13.71543 | -57.47968 | 2025-05-22 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee5944ce-7422-3c63-93ee-f1af00167fd5 | -14.03122 | -55.14426 | 2025-05-22 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2bc9f3a-7679-3397-92e6-2cbe34335fc8 | -12.29132 | -52.50129 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dc523229-a45c-323e-9340-f3d0e71de849 | -12.48348 | -57.1889 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3a15bbe-6556-387e-ad2f-53ec5e52cd5e | -13.67036 | -53.93983 | 2025-05-22 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d688c6c9-c0c0-39bf-9775-5b109c7b167f | -10.02168 | -65.00397 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51acb6fa-d881-3718-824d-cc072f97f3a8 | -11.57372 | -54.57203 | 2025-05-22 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ce04c1a-a35d-3c30-85c1-3c9dcc248b25 | -13.77974 | -54.31636 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3720b959-c377-3a4c-8593-668a64a18d68 | -12.29127 | -52.4886 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31eec626-67cb-31e5-8004-3227a95567b6 | -12.29263 | -52.48983 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 47e92305-dc47-3b26-bd17-eb514afa88c6 | -12.28429 | -57.26488 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22d8ad6b-753a-3705-b519-ef7eec22267d | -12.3032 | -52.50179 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c6ed49ed-be65-377b-8aa3-c3bea3e393b6 | -12.66738 | -58.22035 | 2025-05-22 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 924e6fcc-3e04-3f7b-b5da-34c44cbc823c | -12.66629 | -58.22216 | 2025-05-22 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13604a4c-a8c2-3db3-8547-5de11fb040b5 | -17.61332 | -54.17282 | 2025-05-22 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e85cee1d-178e-3d45-9052-e7b38bb79952 | -11.5528 | -47.4546 | 2025-05-22 05:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ca85eaef-b120-3ab3-abfe-493d68097e7e | -11.5719 | -47.4521 | 2025-05-22 05:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f29b61cd-72e1-3f23-ac63-a70cf450f6a0 | -19.05846 | -53.46104 | 2025-05-22 05:40:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e254bc3f-6837-34fb-b2d0-0ccac5d2d481 | -20.94586 | -56.59223 | 2025-05-22 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b126258d-5bbb-3783-97d2-bf09885e2908 | -19.05894 | -53.45522 | 2025-05-22 05:40:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f49e68e0-e269-3a65-b56d-9214f59affc3 | -20.94869 | -56.591 | 2025-05-22 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0148af25-793f-305f-b4f9-c0eaebb57fb0 | -19.11331 | -52.69687 | 2025-05-22 05:40:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2bd4a6b5-8a91-34c9-9209-dca2728de255 | -20.94622 | -56.58821 | 2025-05-22 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b75da4a1-529c-395c-9fa4-f60fbd20494c | -20.94908 | -56.58693 | 2025-05-22 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 9f3b65fc-5d34-3794-8137-10eb84c854f3 | -20.9483 | -56.59506 | 2025-05-22 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 078f194a-8722-329d-84b8-15e861dbb0de | -20.95189 | -56.58863 | 2025-05-22 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8a6cf1ea-c4f9-38a5-88a4-8ae76f72d9f2 | -19.06514 | -53.46177 | 2025-05-22 05:40:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d898466-000c-3831-86e6-5ba06556a3d9 | -20.94658 | -56.58418 | 2025-05-22 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8b7bd454-10ec-3804-bd9c-50dbd2cc98f2 | -19.06563 | -53.45596 | 2025-05-22 05:40:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17f6b1cc-4288-3fbb-be6a-f40c01fc105b | -19.73031 | -54.51115 | 2025-05-22 05:40:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2b8b547-0401-3d47-8822-982ac94b5ee0 | -20.95152 | -56.59274 | 2025-05-22 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1e2b811c-bb74-3ed6-9525-b1ef1d7b0679 | -19.73665 | -54.51177 | 2025-05-22 05:40:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2427cea3-2490-3ca6-8c1a-a6cc4bf0953b | -11.5719 | -47.4521 | 2025-05-22 05:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f9ad1981-30a0-36ec-89f9-866d38c55e4b | -11.5528 | -47.4546 | 2025-05-22 05:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 84d541c1-efc0-3293-8422-79530620c2fa | -11.5528 | -47.4546 | 2025-05-22 06:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 08c6ec03-4487-348b-bc6f-335a6697231c | -11.5719 | -47.4521 | 2025-05-22 06:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| dd5f24cc-347b-35bb-b4ed-126e60e5a55d | -8.17063 | -61.47461 | 2025-05-22 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d70bcd7-153e-331a-ac59-1ce86818fbdb | -8.16486 | -61.47711 | 2025-05-22 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a49696f-d966-36c4-b67d-a20fd9c41461 | -12.27748 | -57.27128 | 2025-05-22 06:03:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6eff26d3-c5d6-3177-8ac1-47192817b847 | -12.28555 | -57.26485 | 2025-05-22 06:03:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76fd38c5-78b3-3bde-850f-194559b83272 | -12.0203 | -63.79042 | 2025-05-22 06:03:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 184e8f81-357a-3ca3-abd8-49708b39e654 | -12.0251 | -63.79105 | 2025-05-22 06:03:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3af5998e-ccf6-38f9-9e6d-969d0d8a6b8d | -10.68296 | -57.59933 | 2025-05-22 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README22.md)
