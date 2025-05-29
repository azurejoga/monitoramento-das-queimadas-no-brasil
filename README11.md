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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b688c4e3-5f93-3ead-9f60-1670a8e6832f | -11.81982 | -44.26654 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d7f33034-5905-37f6-a2b6-c95c575efbd4 | -9.38946 | -48.41693 | 2025-05-29 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e0f4e94-c16d-3286-891d-5db08b062061 | -12.32066 | -49.995 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c56a5ce-d946-3cf7-aaea-b399cad714b0 | -11.96542 | -44.00895 | 2025-05-29 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63c63bd9-6a1d-3d11-a2d1-ebfb213be40e | -14.6208 | -47.94089 | 2025-05-29 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeb2158c-22f9-3d82-a41a-428597188cd9 | -12.91174 | -48.07415 | 2025-05-29 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f132e672-2f37-3b38-abcd-04fe29c979e5 | -12.10351 | -44.74878 | 2025-05-29 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2424a0aa-6110-3a81-b535-35059001b3a2 | -10.66888 | -44.41425 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 981719a2-9298-399c-b265-7a266d5df94e | -10.28132 | -46.48293 | 2025-05-29 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46f98cdf-6c33-3401-be97-84777b378559 | -12.60133 | -48.36871 | 2025-05-29 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 704c6645-e06f-3efe-a30f-cb18567177b1 | -14.61809 | -47.94146 | 2025-05-29 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18cf5783-7e57-3605-af1b-d9b088938d75 | -11.7896 | -54.78189 | 2025-05-29 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c345eb65-aa29-36e3-9045-7cc6be570eed | -8.75256 | -49.76715 | 2025-05-29 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 086c49fc-10a6-3cc9-aa67-b323aa69e430 | -14.67431 | -45.09283 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c38ab64b-0511-333f-8c64-e1775a413f84 | -11.91057 | -54.42039 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 519962ca-5135-30e6-b978-3702b921355c | -9.11202 | -49.63511 | 2025-05-29 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05ed0d7a-2ab4-38f2-b42b-ebb9905d2d31 | -10.73247 | -49.28526 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02b2f4d1-5118-3c14-9510-43f91f05e5fd | -11.77841 | -47.3183 | 2025-05-29 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 923d2ae5-e5f9-3741-b261-65f39f4bf92b | -12.32617 | -49.98812 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b1e8b2e-588a-3067-9eb2-e9a7e8cd7ba8 | -10.95156 | -48.15516 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdf1a36f-3ac1-376a-a7dd-6ed4c688178e | -10.81978 | -54.03291 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbcbcfdf-78bf-3333-bd42-1f82a16bcf66 | -11.13883 | -53.91203 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2278f7ee-7eb4-354c-ac5b-609fb1538dbe | -11.91686 | -54.41787 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adc25fea-c3ad-32ee-a906-a474d647aad3 | -11.14445 | -53.94387 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b706eef-8ad6-341d-ae3a-3fb662a31cc8 | -10.95235 | -48.15052 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14114b6a-13a9-3317-848f-bf15477ecde6 | -13.08528 | -45.28135 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbc6617e-4852-3f4c-92fd-ff156b4a7a9b | -12.27867 | -49.53025 | 2025-05-29 04:14:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3058484-93a6-32aa-b685-a8bf4304483b | -12.38461 | -49.9713 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bfb76a1-7236-3895-82dd-6fbef4757451 | -11.05359 | -48.85331 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ceab49-0280-38f7-9462-318f25bafd7c | -13.66682 | -45.4249 | 2025-05-29 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8cd274c-56a1-3014-a748-5e32c6250a35 | -13.08917 | -45.27834 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03247e80-02e2-3586-9a97-0c8ea757998c | -12.25881 | -44.60441 | 2025-05-29 04:14:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c6a723b-145c-3b07-a416-5d1ebcf98ef8 | -15.80492 | -43.56638 | 2025-05-29 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47cbff06-f698-30ec-95bf-2fca55a01976 | -13.07863 | -45.28024 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48fa9743-c848-3330-8504-db03fab14b15 | -10.46715 | -47.94226 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1760646-b2e0-3ce2-bfc9-b1f36fb52b6f | -11.79864 | -55.07079 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7309beaa-a748-339f-ad16-d9250faac97f | -10.81424 | -54.03181 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb82187e-f158-3640-bf92-569687bedd30 | -11.81927 | -44.27006 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 847ad53a-b28c-3714-b7f9-a4df33194b5f | -10.73459 | -49.29705 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 743f3118-cbd6-3739-a5bc-147a8345e364 | -13.08803 | -45.28546 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a47ef781-e4f4-3b49-84a7-9a098c3923a7 | -13.07806 | -45.28379 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 703ecd0c-ffe9-3971-a731-4915d3ebda1d | -11.90794 | -54.40455 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaa40bd3-2565-318e-aff4-5f5cd8c37b4e | -10.95314 | -48.1459 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d6d7113-3e04-3b68-8206-65f3115f8917 | -14.67156 | -45.08872 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c09f90b-98af-3d3f-b0ba-1ef9a1a59347 | -16.48251 | -43.3826 | 2025-05-29 04:14:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35a53b9b-d8df-35b4-bae9-6abfa12f5152 | -13.65961 | -45.42735 | 2025-05-29 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 377ad584-d0ea-319e-b9ed-0acc3caa3784 | -10.63974 | -48.80286 | 2025-05-29 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2e0a577d-7000-37f0-9684-e1569b820c72 | -9.2987 | -50.43156 | 2025-05-29 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2916453-ab56-337c-a5a0-5b1e1735e516 | -11.90168 | -54.79205 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54183f54-d738-3c6e-a82f-215e4694a69e | -9.20887 | -49.474 | 2025-05-29 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ed5ef3e6-59e5-3302-862c-e1c4bce8674a | -11.13848 | -53.91627 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03fb15a1-6dd4-3b49-adc9-6ac3bc9bdb5e | -10.65661 | -44.49135 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79103dd3-bc33-37f2-b149-2283cedd26ae | -10.6555 | -44.49837 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 548063d1-de5e-3aa1-a4fb-465229a78c5f | -12.32204 | -49.98737 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5182cb85-4d93-3bb2-bec4-c566d74cc9fe | -10.67274 | -44.41129 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a35e9560-7afd-3bd2-aeb2-a5be68be8204 | -11.96597 | -44.00543 | 2025-05-29 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b81edd05-35d8-3937-ae52-1f450c48f849 | -11.58926 | -47.84612 | 2025-05-29 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73332376-5550-3732-9314-dd9de9849406 | -14.66825 | -45.08817 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e118719-598f-3494-97e5-b84c173039ee | -10.73183 | -49.28891 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a3564e0-d5e3-30ba-8e7d-efff37fb840a | -11.28041 | -46.43566 | 2025-05-29 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 25c231e6-8a80-30a0-b6d8-28e3a5db6727 | -10.65218 | -44.49783 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ce7d0ec-5a1c-3bbd-b15e-e5db67c5cfec | -13.67072 | -45.42189 | 2025-05-29 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b0cd6e4a-a1cf-35e1-9423-c10f185df84e | -10.73118 | -49.29261 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 122c6a77-3595-3f99-8e3d-7e17ddc1fbb5 | -11.81707 | -44.26249 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fc5b3341-2059-3e47-a2ab-bb0a952e664a | -12.32135 | -49.99118 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5265894-858e-36b5-a8a1-d8075c92858a | -10.66281 | -44.40966 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccad31aa-9686-325c-a46d-92163378026d | -11.13815 | -53.91562 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f353ed26-46ae-316b-97c6-9c8430b23ada | -9.09937 | -49.65779 | 2025-05-29 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d0b25ac-40e3-38f3-97cb-7c4a4283c901 | -9.40038 | -48.42398 | 2025-05-29 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad29b899-7f5c-332b-af3f-f7d0f9ad1c26 | -12.4217 | -53.33167 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33ce3902-c87b-3877-99ff-c71dfd0ecb14 | -14.53073 | -42.28859 | 2025-05-29 04:14:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7586aedb-b044-3950-8332-f517125f1067 | -11.1368 | -53.9228 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13532e8a-8488-3a4d-8155-9a38b2020368 | -12.36156 | -53.28368 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf717812-9880-3666-9d84-941b71a98b7b | -12.94097 | -42.48933 | 2025-05-29 04:14:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4cbb30e2-fcea-3f36-83b2-f848af74e371 | -11.77772 | -47.32245 | 2025-05-29 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 587f7793-d41c-3f29-9308-b85c28a41262 | -10.95533 | -48.15585 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3f209e6c-5651-3bcd-b99c-561109bd66ae | -12.42683 | -53.33271 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d5e7be2-16a9-3bcc-b1cb-5e4803efd9f7 | -9.81111 | -54.71891 | 2025-05-29 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1b106e1-565f-339d-becd-fab42ec0fd4e | -11.82314 | -44.26708 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a1abcc9-673e-3be8-9fc7-20dfb7b228f9 | -12.35905 | -53.22992 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3817abc-00dc-33bb-9b3b-c3a75a3a59fc | -13.23769 | -47.26396 | 2025-05-29 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad6cfec3-7b38-3b0f-b208-273877b39fb6 | -11.13612 | -53.92643 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e2f3b1a-641c-35e9-a035-fd84fe3a7cd7 | -14.67762 | -45.09338 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26d4ca56-07c6-3c77-8fe2-aeefec214860 | -11.80359 | -55.07628 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80814f12-d47a-3526-9e9b-3c6f7d88456a | -12.3637 | -53.24525 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1133aae8-4873-37a1-a055-cf0f517fa5f6 | -12.30833 | -47.26881 | 2025-05-29 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c9d8383-4fc2-3e8a-a841-4832e6865d04 | -13.08746 | -45.28902 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d877371-a55b-33f5-b9ed-594f09025c58 | -10.65548 | -49.44188 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5df7e419-19d4-33a0-a166-a1134c9375b4 | -11.28668 | -46.44069 | 2025-05-29 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a1698fa9-6371-3ba6-aac3-dc28e248c1ee | -10.78982 | -48.65599 | 2025-05-29 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba5961b7-e783-3ee0-8912-58ccb68a4eaa | -15.56873 | -47.8534 | 2025-05-29 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f8702d4-bf19-39fe-9d62-6981cbb042ec | -10.65606 | -44.49486 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44dfc080-62e4-346a-af49-795b135d96f0 | -12.26212 | -44.60495 | 2025-05-29 04:14:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd4e19c5-fdab-34ea-9706-266bf9961260 | -9.96259 | -49.80738 | 2025-05-29 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a2918ae-620a-331a-bffe-9ba7ed646114 | -13.68505 | -47.68296 | 2025-05-29 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb75dca2-6ee9-3b7d-8947-72c35fe234fb | -12.30401 | -50.08713 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc5949bd-7609-3669-aad4-8039b4dc9646 | -15.48097 | -41.89748 | 2025-05-29 04:14:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54eb5375-8c94-3d7d-b270-e915182e94a4 | -10.52715 | -47.58347 | 2025-05-29 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4d8c855-fae8-30ff-865e-064dad22eefc | -14.53528 | -48.34419 | 2025-05-29 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2269ea3f-b642-3a19-b84a-de47a3a9fe1f | -11.13748 | -53.9192 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
