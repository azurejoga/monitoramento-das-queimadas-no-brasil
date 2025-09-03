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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dacc46c4-a28f-3fa9-b533-da5a0dc32939 | -13.34801 | -51.73647 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0924f732-9297-303e-adad-134060b937f4 | -15.0269 | -50.04319 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9dd09d4-67d7-3e94-bcc2-63471352891a | -13.69956 | -46.93604 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eb1e7b3-fb78-35d3-9f70-bc1a507526d7 | -11.85129 | -51.41723 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 023fd242-e359-37a7-a505-bf6ca13843f7 | -12.93466 | -56.95706 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ab9a59b-159c-3373-a21c-64b36bfb3558 | -11.96449 | -51.34296 | 2025-09-03 04:49:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e276095b-8b26-3915-abe5-b2fd0f2cdfc8 | -13.49866 | -47.02372 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6373d34e-a63a-3d98-bd28-f0e974fa7df1 | -11.83767 | -51.55026 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e17e351d-8856-343d-9a7d-85ce0b496cbc | -13.48167 | -46.82639 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f3b65dd-64e4-31c8-9c9f-cf7615e2c5d4 | -12.60781 | -57.00061 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| daae7210-7a70-3f3b-8b56-080b12317cc1 | -12.62953 | -56.98947 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdb52cc1-4b4f-3ac9-9fd9-adc3030416b1 | -13.49137 | -46.81879 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a35aae4-987a-3a06-aea1-e0e9c3f5e644 | -14.7622 | -48.13641 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57a7f51a-8a7b-338b-9b1f-b8dd93b7450f | -12.9024 | -48.1009 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 810a5e1f-5580-3a5b-ada6-5c32c4493c3a | -13.10274 | -57.13936 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ee7295b-76ec-300a-80dd-b6517d583aea | -11.86989 | -52.41778 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d55522b2-8c71-33f0-a89e-b0d6a2376f11 | -11.67382 | -57.35147 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f5f57445-3bbc-3c88-ad41-a645db258672 | -17.92502 | -47.20887 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0934464f-3c0d-35bb-a2bd-fc53bb903e89 | -13.70863 | -51.937 | 2025-09-03 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 965119c3-2596-378d-afc2-d82440d06877 | -13.72306 | -46.9216 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7e310d1-3ba2-3372-a153-fed76be550fb | -12.49162 | -53.83659 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2084939-800d-3adc-b3c0-898977d7e988 | -12.99702 | -48.11809 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba2572ee-dc37-3702-b1a5-9cdd3db05cdd | -15.14772 | -52.34747 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ad6884a-c066-3302-abe0-d4ee0bc5b328 | -18.06917 | -45.99424 | 2025-09-03 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 573a8509-4f2b-35a1-a0b0-b3cb6c2957ad | -18.19452 | -48.12685 | 2025-09-03 04:49:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbdd98c2-a878-3751-8d55-25ccb7da836d | -14.77274 | -48.14869 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36d4ed1e-b435-3945-be05-be4f366bd7ce | -14.99942 | -50.0563 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d5b5429-e258-33ca-862a-de8304433e31 | -12.93625 | -56.95393 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 451cef52-06a3-3b8a-bd00-a70335946e38 | -13.40125 | -47.07455 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90c5cebb-308d-3dee-830c-182398b092a9 | -13.71227 | -46.93797 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2eb8d2b4-55a9-3cf2-9060-5479e86a97e8 | -15.56224 | -48.40849 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8269a9c-445f-398d-aa80-c48c395f0efc | -15.71953 | -53.63586 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72a7c1c6-1d63-38c5-85b4-0cb9e0acb735 | -11.41827 | -55.18941 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cc4e4b6-df57-38ee-8c2a-fd88acd6aae5 | -13.89884 | -48.10422 | 2025-09-03 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 612de832-21f9-385f-81e5-0de23f84160f | -15.6015 | -52.66806 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 899e00d6-093d-3f9d-b551-9599fecb8f3e | -13.51656 | -47.01804 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc79c765-8bf0-3f86-8770-e954276dc8d0 | -13.00813 | -48.09467 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98afaad8-cfb8-30bb-972c-edae1b6e8ac3 | -15.90202 | -48.17208 | 2025-09-03 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6f2aa28c-d9c5-3393-aeff-d73395f4881b | -13.01139 | -48.1 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 38dc41f1-f9cb-3061-98a8-cfae77402ba4 | -13.20916 | -51.80337 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2823056-4a68-3d3c-adbe-04f857cf249e | -12.83787 | -48.05036 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6794b78-7233-3906-99e5-29a41457c991 | -13.10189 | -57.14427 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba2e40aa-a2f2-3d20-951a-04985a2e72e4 | -13.01045 | -48.10251 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b7c9664-24e3-36bf-b39e-dc6c0d5eb060 | -15.55576 | -48.39692 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 880e6c65-a583-3241-b2ff-656c979aae82 | -13.70379 | -46.93668 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f32a8d50-6aea-3649-a15e-8a8a23f83f0d | -14.56288 | -53.05338 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 505b9b26-5217-3cef-b884-693d455ba755 | -16.81918 | -52.14094 | 2025-09-03 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 768f140c-b6fe-36cd-ad86-484e79c7bc72 | -14.60448 | -54.58473 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca6df8bd-84d7-3d6a-a5bc-83f1df3293bb | -17.94879 | -47.23462 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04ba78ad-db75-39da-8b83-a8f7b8dbd298 | -15.00187 | -50.04927 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0177644-1f09-3a66-b8f7-66d638b99bdf | -13.70241 | -46.87988 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6417b2a6-bfa1-3bd5-a25c-37a60767aada | -18.03163 | -51.5891 | 2025-09-03 04:49:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31e7225e-3723-364b-9e4e-cc2a12c1c5f9 | -13.49918 | -47.01976 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 843dbaa9-c731-3514-b334-6f329e637224 | -15.74415 | -53.69495 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f2a3bdee-d2f5-3a4a-a838-f00a124c4d2d | -15.55505 | -48.40207 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7026a0b4-f0b0-393f-82b1-61172eab8ee7 | -11.85145 | -51.50505 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a99c165-2631-3c7d-a89b-7d075aebb3b3 | -12.90381 | -48.09739 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58f9a6c0-eafd-30c5-bbea-924b0f3e29d1 | -12.96243 | -48.076 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbf57828-0839-30b1-b41a-45a3ec5bf730 | -13.30974 | -46.85366 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5883e252-f280-320b-9303-5ef446cca550 | -18.03509 | -51.58966 | 2025-09-03 04:49:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cc3f9dd-2e59-31e1-af3e-33872942ac31 | -15.173 | -48.01284 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee387dbf-dca1-31f7-adcf-2f0cc94a840a | -11.47759 | -54.61783 | 2025-09-03 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd512cee-c729-3370-a681-8506ca94b12b | -12.94567 | -56.98388 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9aafa975-4f9f-3ab2-847d-b3824a0bae73 | -11.85803 | -51.46227 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adef8045-109b-378f-a67d-63a6da209864 | -12.1742 | -60.74264 | 2025-09-03 04:49:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f980c51-7025-384d-a3d3-f3b04ca060f1 | -15.55182 | -48.39619 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b932292f-9e81-3caa-9193-55684c3f5319 | -12.9393 | -56.99774 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e223e09-93fa-3f16-aa49-347ffa7676c0 | -11.84518 | -51.41254 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef80107b-dad5-35c0-bd27-5aafb8c2d27b | -14.97723 | -50.21479 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b53f302-b864-3669-9cbc-3d7f2c7aae5e | -12.99313 | -48.11749 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41307b99-5bd0-3f89-a3d8-5599aa6339ad | -14.26596 | -51.21732 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a964e2d9-fa00-3c1e-86c0-e6a38c95b141 | -14.30064 | -53.09739 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95e12fcc-053d-3e50-93b4-8799d535163e | -13.00355 | -48.09918 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07b6f69c-28ec-3ff5-9d1b-5ee8f8a56af5 | -12.93888 | -56.97775 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce091da8-36db-3c94-8ee6-14bd5a1f79bd | -11.4225 | -55.18591 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 317e01b8-a496-3cc5-8429-4985f25bf7b9 | -14.78323 | -48.16125 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38cb6f01-d942-3851-a56e-18aa12854319 | -13.7033 | -46.94049 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6b37f2c-2a82-3712-924d-bca301e4d6ce | -11.42182 | -55.19 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f81ea87c-a2e8-3c1b-88bd-ab151a1c654d | -15.09536 | -48.12739 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1da0298f-200f-3d4c-a37a-2de1d5a0311d | -12.86914 | -48.0261 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8890caa3-2865-32df-9bb2-dfaacbd9b1cb | -13.3041 | -46.92957 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed76213-8683-3a01-b63c-0781e4ca8a21 | -14.98014 | -50.19403 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 56f5d091-6651-3064-af63-5e1253443a6d | -14.83649 | -46.69701 | 2025-09-03 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ed7e986c-2e57-3d00-aabd-04d9dbb084e6 | -13.69604 | -46.96344 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c9f95f8-fe04-3823-a24d-5f9d40fbe939 | -13.99327 | -49.55442 | 2025-09-03 04:49:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 489ffd96-d314-3f76-9cb7-8f2e1d77deb5 | -12.90574 | -56.94872 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 593113a3-0532-3e83-9afc-0949cf94b2b8 | -13.28671 | -46.83129 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2d09636f-199f-3d3a-9ef5-cd0501086713 | -13.71087 | -51.94469 | 2025-09-03 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bbcec8c-8eac-3650-9c4a-7b46253bc9bb | -12.52468 | -53.82354 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5364f907-a6be-3da8-ac61-d3d0b860700f | -15.09584 | -48.12381 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9dff3824-f9b8-3a8e-aabc-fd16efdc7b03 | -12.49439 | -53.84077 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06a5a48b-e9c2-357b-b618-4647a411febb | -14.99827 | -48.13726 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f05c1fed-83d3-3cb3-b570-07d7a2acd6b4 | -14.26823 | -51.22537 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f7bd07d-aaf1-35e5-b61b-fa58a0c29cac | -12.94058 | -56.96807 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d026dae2-e78f-36e6-9c24-bfb2442c14a7 | -17.53918 | -47.58192 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 63c4a924-1b20-3e2c-9671-9b7c590ba2f6 | -15.09985 | -48.12431 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70395214-7a99-3c75-a55a-d43fafc60ae8 | -14.34766 | -52.79633 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0ef015d-71ab-336e-b17f-0c1baaf08a31 | -13.2075 | -51.81417 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15f42ced-8541-3e3f-8803-7e7ef44ae2b6 | -15.74535 | -53.66583 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f10a61ca-72de-3600-8271-b1a7f24cd6b1 | -11.66862 | -57.3577 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README72.md)
