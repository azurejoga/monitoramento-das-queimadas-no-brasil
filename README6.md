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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fea367ee-aec6-3732-af4c-1a4066866b31 | -12.55135 | -57.17752 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fcd8336-6db9-39fc-ad19-349354478d2c | -12.53587 | -57.18943 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06becf95-4ba6-320d-ba07-8f1246e28f9d | -11.39933 | -57.5418 | 2026-05-24 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7feb8f28-520a-3bd7-9b6a-e6bc56c3db94 | -11.54105 | -56.95148 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02da95c8-5e3c-3303-99e7-7779b3c07d57 | -12.53915 | -54.61355 | 2026-05-24 05:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02666b0b-5d6c-38d4-a1af-bc35917f7f27 | -12.54085 | -57.17941 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23203e30-cf48-3a69-9004-aedfc78b52e9 | -12.8967 | -58.18069 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eea0aab7-31e9-3441-98f2-0e43387a3e1d | -11.43904 | -52.92611 | 2026-05-24 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd54c089-26ba-3b2f-9e6f-4715dffbfa31 | -11.54547 | -56.945 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1a05dda-b5a8-3884-969a-5d2290f0a438 | -8.44475 | -51.5373 | 2026-05-24 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5186b9f5-0671-3318-a042-9352b4524559 | -11.4431 | -54.09344 | 2026-05-24 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a04a3cd4-8669-3df4-9159-55ed30d209cc | -11.78154 | -59.32404 | 2026-05-24 05:08:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b668a127-9bce-3b66-8012-1dbeea7b1998 | -8.85885 | -46.93689 | 2026-05-24 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1addd9c1-8a27-3832-8719-d2f7f569370f | -11.17976 | -55.91832 | 2026-05-24 05:08:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 110cf777-887d-345e-918a-0a409e00fe4d | -11.9119 | -57.03329 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73f3f5d-7040-3677-b739-8b6183040c0b | -11.94445 | -57.04222 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e02dbdf5-c2b6-3512-8765-5200060a2962 | -12.55027 | -57.16288 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f0902a5-0b04-3f4f-a8c8-6c99045b80cd | -12.5464 | -57.16587 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7a263fb-105d-3d09-bfdd-7223d85841c5 | -11.51526 | -56.12067 | 2026-05-24 05:08:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c15b0796-1028-34e6-8396-192edae0b9a5 | -12.55079 | -57.18104 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79a18ac3-9ef0-3077-8e65-e438cba4a4e4 | -10.72208 | -51.5905 | 2026-05-24 05:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 727caf07-662f-3919-8c6d-09d3be475dd4 | -12.88844 | -58.16822 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e0adcd2a-f11a-38d7-b9a6-79aaf38f6fe0 | -11.54767 | -56.95256 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6491809a-bd4b-3c92-b09b-11e27924c912 | -12.88188 | -58.19286 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 321bfcc1-9710-30ad-aa5b-3a1e43f9d95f | -11.78995 | -57.3524 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93db8a93-9e7f-37ca-bfd7-0cd64ee6c53c | -11.60861 | -55.33308 | 2026-05-24 05:08:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e50acf4e-907a-31b3-8b18-10face0620e9 | -12.53643 | -57.18591 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 775c6589-26f9-3cf3-a13f-97618bea0935 | -12.89453 | -58.17293 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd77ffba-db81-3500-b043-b0b577ba7917 | -11.54934 | -56.94204 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97c39f42-9826-3aed-92dd-6fb1cde00fb4 | -11.90803 | -57.03627 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb930e5b-a28d-33a3-a1e6-42c14788d17f | -12.5381 | -57.17535 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e92c10c0-fd96-37fd-981c-86d7b193a5d2 | -12.88592 | -58.16768 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20d6ec06-452e-3ddf-9e0f-97d5b9384e1a | -12.55358 | -57.16343 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eefa807a-1ed8-357c-9ed7-d46ef059a1d9 | -11.54492 | -56.94851 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19de267d-579f-3d57-a693-a858610cdf7a | -11.50321 | -57.16848 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac4d5b2a-3ac9-3a06-a3a4-cfdc436c6876 | -12.88535 | -58.17127 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30eaefe1-518d-3113-bb2e-cedd88eb6fab | -11.27333 | -53.96847 | 2026-05-24 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e55434-e2f3-3cca-ad57-1db8dfbe50a3 | -12.54034 | -54.6056 | 2026-05-24 05:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed666145-8d7f-32f0-8e08-e6a83150af93 | -12.89003 | -58.17957 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c19303a1-a3c6-3973-b8af-596731cc8a0c | -12.54915 | -57.16993 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45aff234-8f72-3599-be2a-e1d86e5bdb80 | -11.79382 | -57.34942 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b246d213-b943-306c-b249-a983ca5395c1 | -12.53698 | -57.18239 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98019723-193a-3a70-a2c7-ed2b5f1014a3 | -11.90747 | -57.03978 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fb1cd24-df2c-3514-b36c-079dec00752f | -11.4502 | -54.09451 | 2026-05-24 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5e57a20-e501-35d7-8a65-c904d5ea03e3 | -12.89336 | -58.18012 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dc5e5b5-2ab1-3e05-9449-c114669cedfe | -12.53918 | -57.18997 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66bb392b-82a1-3262-a6fb-619faae2b713 | -11.27393 | -53.96441 | 2026-05-24 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86bc014e-7b99-3963-a093-b5811cfa620a | -11.55432 | -56.32642 | 2026-05-24 05:08:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce64fe16-4abe-399d-99ad-7160819ce6fc | -12.53862 | -57.19349 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 746093c3-4896-37c9-aa57-c3bef2202991 | -11.5416 | -56.94797 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2d817fe-68bb-319f-9ac0-1537b580df6d | -11.53994 | -56.9585 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb464775-f1f4-32c1-b3ec-f11464964a76 | -11.94114 | -57.04167 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc5789e4-cc77-319d-a918-b16da9bcaf09 | -12.54205 | -54.61808 | 2026-05-24 05:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10ba7641-ca87-3295-b19c-112b9962dcce | -11.54216 | -56.94446 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 029aff49-72d6-3af3-a8e3-a6a4f3cafdbb | -11.44957 | -55.11153 | 2026-05-24 05:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5239bced-d8cc-3737-8c75-c0796787878e | -11.55596 | -56.94311 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a45611b-4b23-36c8-90fc-580bbde0a4ca | -12.89178 | -58.16877 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83d1d7c2-347e-3fda-847f-fb57b81d5843 | -11.04809 | -49.60021 | 2026-05-24 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38696b0c-c885-384d-b6a3-0317088fe6b3 | -12.56248 | -54.75368 | 2026-05-24 05:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04f610ff-36a7-3828-90d0-a1406dccfdf6 | -12.53974 | -54.60958 | 2026-05-24 05:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e6fb3fc-6c36-3141-a74b-868d2cd02db3 | -12.89378 | -58.19864 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb852f84-dae5-320d-b46f-41667e3a9ff3 | -11.54823 | -56.94905 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3744406-4283-32a6-acdd-0634faf6af97 | -12.5519 | -57.174 | 2026-05-24 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b400eac0-d6a7-3c37-8fbf-2374b08746fa | -12.88727 | -58.1754 | 2026-05-24 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca72a3b7-42e2-35b5-b69b-f72d8d720e84 | -11.54436 | -56.95202 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ed96ed6-937f-36ef-861f-d212a098b9f6 | -11.44371 | -54.08939 | 2026-05-24 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 627e86b7-3c92-3e11-8397-33ebdf3010c3 | -9.57352 | -63.49895 | 2026-05-24 05:08:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9553241-ffcf-3c50-a0e0-a567994b1406 | -11.54325 | -56.95904 | 2026-05-24 05:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7be3b160-78be-3ddf-a53a-59a0103df3c7 | -6.89838 | -52.19122 | 2026-05-24 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05db3382-f18c-3c24-8ffc-48ffc1ff6b78 | -12.55508 | -52.24648 | 2026-05-24 05:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 009c6173-0af9-3146-88b6-7c2459fb2ec7 | -11.18365 | -55.91529 | 2026-05-24 05:08:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d41a8929-3b1c-3718-a4ee-28b85e28efc8 | -8.71076 | -47.91646 | 2026-05-24 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e851e31-9087-36da-94f2-7c1fa0bf3834 | -11.40265 | -57.54234 | 2026-05-24 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b1591e7-d9ec-3487-94ac-b758fd71981d | -14.02039 | -53.36367 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e92862f4-31f0-3c89-93f8-394680c1c1c9 | -15.10543 | -57.62676 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ff0163e-3ed9-365f-ba4f-b8924877800a | -14.73361 | -52.69327 | 2026-05-24 05:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fd3b029-2a1c-327f-96d1-b271d913ffb7 | -14.02419 | -53.36425 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e04ac502-4d28-392d-a3e5-4addcb51bc8a | -15.08386 | -57.63412 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 611c2b9e-d583-34c3-bc27-5ed1978f7b69 | -16.86956 | -52.43856 | 2026-05-24 05:10:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1998ef94-1902-301a-a7c9-25e9bbba8b13 | -13.83567 | -56.4964 | 2026-05-24 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd09de45-2daf-3414-8bce-db406216f951 | -20.91718 | -46.78684 | 2026-05-24 05:10:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 06849331-bd71-36fb-9223-8313a9f185b6 | -13.95152 | -53.97353 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e3866793-1550-3be6-9fd2-afe8c9a8f884 | -14.77363 | -52.66875 | 2026-05-24 05:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbd4e742-b710-362b-8a6e-e5e25d1a63b5 | -14.0166 | -53.36312 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 748b87ab-07cd-3ee0-b233-af4e36b96f70 | -13.9828 | -53.88179 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93892040-1dcc-3a0e-b150-8c112900451a | -14.01727 | -53.35837 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9cd43caf-f940-3c1f-b0c2-46a0bd6dd989 | -15.08442 | -57.63057 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f2fc2aa-a2b4-3108-b481-d6da44850eae | -15.08661 | -57.63824 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2404176-2fe1-3031-a7f1-1dcbd1a78d05 | -14.01482 | -53.3483 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86706079-54fe-39fe-9480-96bd7d4e47bc | -13.29643 | -60.90967 | 2026-05-24 05:10:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f6b3650-bd39-30fe-b2e0-e4e8b1a2d929 | -15.09161 | -57.62811 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52d4f465-f3ca-3e0f-b81a-9b35ae8c9441 | -14.01415 | -53.35306 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e5b533b-d908-3408-8f8c-815051d3ab15 | -15.09436 | -57.63223 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70a69bf4-0c7e-3fcd-a7f5-7e83e0f4ccbe | -15.09049 | -57.63524 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35d630ca-7fe3-3c70-809b-475953b97293 | -13.29583 | -60.90802 | 2026-05-24 05:10:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4c2bf8e-b893-3fa7-9a28-14920b6a111a | -14.01795 | -53.35361 | 2026-05-24 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed656a29-30bb-3263-b9f4-647564474b7c | -14.77764 | -52.66926 | 2026-05-24 05:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e4a8de6-c051-3669-8e3c-baf2844fb4e6 | -15.09936 | -57.62209 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 217a8ff3-901a-30dc-a416-fa467504d14a | -18.65139 | -48.87417 | 2026-05-24 05:10:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27c7b2ad-7128-330f-9624-06087e31e168 | -15.09549 | -57.6251 | 2026-05-24 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README7.md)
