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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ca22a43-a477-343a-9691-dd200f257225 | -9.18619 | -48.84671 | 2025-07-02 00:24:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0b2330d8-e775-3f0d-a506-27f1b6830ef6 | -5.61679 | -43.65759 | 2025-07-02 00:24:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2de0f267-419a-376b-a1fc-112dad895f45 | -5.65548 | -46.59251 | 2025-07-02 00:24:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 307f1441-98e3-37c6-a76d-21f4984b8c8b | -7.09145 | -44.37299 | 2025-07-02 00:24:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4c82be9e-0580-35e0-a2ae-75233776eccd | -7.09394 | -44.39079 | 2025-07-02 00:24:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f938f423-2cf1-36d6-ad8f-5f0932da5b30 | -6.02539 | -49.22733 | 2025-07-02 00:24:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b9bee354-10f8-375b-8530-68cc947536ac | -3.99992 | -43.24415 | 2025-07-02 00:24:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a1eb50c1-1096-3147-9169-ac4c67ddebac | -9.57425 | -49.11041 | 2025-07-02 00:24:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 07db4225-f399-3d61-a200-163c95f86ad8 | -8.31514 | -46.31767 | 2025-07-02 00:24:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a12e3bcf-8c78-38b6-b855-2895b05c9ac4 | -8.35336 | -48.45367 | 2025-07-02 00:24:00 | TERRA_M-M | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 76954b03-2512-306c-9fea-846059d6d6e3 | -7.20692 | -40.23559 | 2025-07-02 00:24:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| d6971de3-c48d-3c70-9ccf-d6a50755a3b5 | -7.22315 | -43.09162 | 2025-07-02 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 4590da87-b10d-3110-a8d7-f4efa3d79671 | -7.80013 | -44.04028 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1820e8da-77bc-3ba8-b638-c6c405e5007b | -7.79887 | -44.03133 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| e3a4cd3b-e955-3a20-ae46-897fb234bc0e | -7.79635 | -44.0134 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 00eb823a-3a7b-3c81-98e4-28c091ccfeff | -4.37281 | -48.07867 | 2025-07-02 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 955222f2-2fb3-3510-90e1-6295cd8cdcd8 | -7.61386 | -45.76176 | 2025-07-02 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| debecc49-927d-33cd-be82-d69f6460a6a9 | -7.21261 | -43.08335 | 2025-07-02 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.4 |
| ef2bd6d6-b61d-3286-8178-100086652a1f | -7.0927 | -44.3819 | 2025-07-02 00:24:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 69d2ae3b-40d8-3a1b-a28f-7352d66c6ae5 | -7.53971 | -49.68279 | 2025-07-02 00:24:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d5a3a58a-92cf-3edb-837d-d76e40dc42ad | -7.08318 | -49.60537 | 2025-07-02 00:24:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3c8b1b65-3518-3f34-8b99-2e542c2fcc85 | -7.28337 | -45.36728 | 2025-07-02 00:24:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ece2d875-622b-3fc0-9076-57238270dc18 | -7.78999 | -44.0326 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 54f7edc3-f5df-3e0e-a2dd-6098f6c79419 | -4.80782 | -43.225 | 2025-07-02 00:24:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0bf1e52b-05cd-3516-a6d8-488d330c93bc | -7.61012 | -45.73442 | 2025-07-02 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| e57b8db6-9183-3acd-ba88-ab8b6b841a87 | -3.90504 | -49.08498 | 2025-07-02 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2c825c7e-0354-3564-8b81-7f4f44fe378f | -8.8988 | -48.33214 | 2025-07-02 00:24:00 | TERRA_M-M | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aeca643b-3bd6-3f1b-9e67-08e12b358eee | -7.18842 | -45.47776 | 2025-07-02 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4d646d2b-3cbb-300b-ae9c-14dd43234930 | -7.61137 | -45.74352 | 2025-07-02 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 09eb4bbb-9729-39d2-9775-04cd5321df94 | -7.20344 | -43.08471 | 2025-07-02 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.8 |
| 2f377216-78e9-31ec-b3f2-d061866dfe55 | -7.20482 | -43.09429 | 2025-07-02 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 51b47c3c-2c58-3acd-ad86-335108e90fad | -5.62587 | -43.65629 | 2025-07-02 00:24:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 5d3ef361-feef-32b0-9495-7c599b315c95 | -9.85338 | -44.69751 | 2025-07-02 00:24:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1f557fdb-ff22-3491-9d97-3b8ac5fc8a13 | -7.78747 | -44.01469 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b37bfb69-56c4-33c9-a18c-28911d83b96c | -7.62031 | -45.74223 | 2025-07-02 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f3b2aa7-d9f7-37e8-a423-686f76cbba10 | -5.0746 | -43.73422 | 2025-07-02 00:24:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9fda8778-fe4e-3032-b847-204194924c47 | -7.61262 | -45.75264 | 2025-07-02 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| d2739844-1ab5-38f6-9615-42650f0cd012 | -8.86366 | -47.28312 | 2025-07-02 00:24:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 72b6aef9-a82f-373f-8fa5-52da42578bde | -7.08411 | -44.39823 | 2025-07-02 00:24:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| beb1895d-bd88-3084-883f-3a925942bd37 | -7.79761 | -44.02237 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 268.6 |
| df6059d5-0c10-3e58-847d-a97d831bf729 | -7.08128 | -49.5906 | 2025-07-02 00:24:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fc4ec0c7-1778-3a49-ad5f-58d7e7682a7b | -8.44036 | -49.20232 | 2025-07-02 00:24:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bbfbb216-0a59-3a8b-b895-ff64399749f3 | -7.78873 | -44.02365 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 29a978a7-d00a-3a34-89d0-9f3459cefccf | -6.25355 | -44.8429 | 2025-07-02 00:24:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9fe91df-7f3b-3e42-a39f-81b5fc06e467 | -4.53511 | -48.0181 | 2025-07-02 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 6bfa508e-5a04-3548-8902-132d37aa4a4c | -6.95729 | -42.90202 | 2025-07-02 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b557feaa-f2e5-3a82-9700-3cc6043bee9a | -8.86225 | -47.27221 | 2025-07-02 00:24:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a682e94f-f9c3-30cb-ba30-e4951344c421 | -7.08287 | -44.38934 | 2025-07-02 00:24:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2ca2432a-ae3b-3a65-8fa4-453f1f2ea60e | -7.20903 | -40.24986 | 2025-07-02 00:24:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 25.6 |
| ca3740c1-c1ba-3d54-b580-e1e8a5a83406 | -7.29347 | -45.37496 | 2025-07-02 00:24:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d12d43d-c47d-3695-9464-884428293b62 | -5.87952 | -44.80353 | 2025-07-02 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 0e538ee3-6c67-3154-81d7-d0ad4a30cb32 | -9.85461 | -44.70647 | 2025-07-02 00:24:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5df202a1-1992-35eb-aeaa-487c579c1b42 | -6.71141 | -51.40657 | 2025-07-02 00:24:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8415c3a0-1b9b-35c7-b1ff-c7d89f101919 | -8.35505 | -48.4665 | 2025-07-02 00:24:00 | TERRA_M-M | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c4bea308-00ca-364c-bf38-bd00492386ed | -4.37425 | -48.08948 | 2025-07-02 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fbbe3819-77c9-34d8-9b77-45b7996ee535 | -4.37012 | -48.0854 | 2025-07-02 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2e318ae9-efc5-3c9b-9993-fbbde7815d57 | -7.60242 | -45.7448 | 2025-07-02 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d87c112b-c667-3607-8ad2-9421cc591699 | -4.32043 | -48.08139 | 2025-07-02 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| a633bf2c-4899-35d0-acd9-cfff3aea72da | -7.21398 | -43.09295 | 2025-07-02 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 354.2 |
| 943ffdb6-2528-3b6b-b18f-ee6dd6010c65 | -7.60367 | -45.75391 | 2025-07-02 00:24:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 1939d713-f7f6-3860-8d91-ebf120a1d9bb | -7.21535 | -43.10253 | 2025-07-02 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| c52f5eb5-27dd-312a-953e-cc371d9f26f0 | -5.62719 | -43.66559 | 2025-07-02 00:24:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 011b4c81-b403-38f2-928e-6506cb0f49f6 | -7.80774 | -44.03005 | 2025-07-02 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| bc618acd-6863-37ec-b376-78110d45405d | -7.88031 | -47.88881 | 2025-07-02 00:24:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8759946e-b9bb-3ce6-9bfc-63a3e26cdef9 | -6.89888 | -44.78014 | 2025-07-02 00:24:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e02745bf-66e3-33d5-960c-63ecfe460cc9 | -6.29271 | -43.67943 | 2025-07-02 00:24:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 55434179-fe27-3de1-8cd4-b7030a5659e5 | -8.54011 | -46.34324 | 2025-07-02 00:24:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4106a6bd-6fc4-3e04-b97d-c61ef68e7dfb | -6.71403 | -51.42675 | 2025-07-02 00:24:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| d7936b56-6180-3337-a270-c49a4266d45d | -4.53657 | -48.02864 | 2025-07-02 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8f2e77a3-6953-397f-91ac-1d943e350406 | -9.23032 | -50.03211 | 2025-07-02 00:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 175bc886-6b6e-33e0-a49a-342968d06b89 | -9.23244 | -50.04947 | 2025-07-02 00:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 372c2c41-a1bc-3384-8656-ea94be6e23a0 | -3.03158 | -49.42765 | 2025-07-02 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 57bf49ef-f973-31c5-9394-1ab81878fb4d | -3.03496 | -49.45256 | 2025-07-02 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0a682a54-11ec-3131-b29b-2dd0ea22f980 | -3.04365 | -49.43866 | 2025-07-02 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| a0c5d8cb-7615-3a7e-8190-5293058d480f | -3.03326 | -49.44007 | 2025-07-02 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 263735f4-130d-3ca1-b2d1-1a05c862186c | -7.2031 | -43.0701 | 2025-07-02 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 8a962d84-6145-369f-93b9-28cc491a8429 | -10.9018 | -56.4552 | 2025-07-02 00:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e288410a-af71-32de-8854-1975761cf5d6 | -7.2217 | -43.0917 | 2025-07-02 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 266.9 |
| 46e8e0b8-ed2b-3e12-9dbd-045449ede95e | -3.0355 | -49.4476 | 2025-07-02 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 46025ae0-4d4a-391b-ae00-a8483c02d539 | -7.0943 | -44.3819 | 2025-07-02 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 8a65dbd9-d040-3211-881e-743692955aed | -7.7947 | -44.0145 | 2025-07-02 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 301.1 |
| 3fefeff2-ac12-3bd3-a155-8431f32926e5 | -3.0356 | -49.4264 | 2025-07-02 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 69ccdd54-7b20-3006-92a5-e89e6549fa93 | -7.2219 | -43.0682 | 2025-07-02 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 0dd96f54-6827-3057-ab39-894b8923c045 | -7.8135 | -44.0126 | 2025-07-02 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| e9cea1e3-c0f2-3ff7-8dfd-13e308944e50 | -7.8133 | -44.0358 | 2025-07-02 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| e80876cc-fd9a-304c-bb53-57fc0528394b | -7.2028 | -43.0936 | 2025-07-02 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.4 |
| 12185b13-a08a-3441-ac15-9e3bd0aea580 | -7.7944 | -44.0377 | 2025-07-02 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 152.3 |
| d8748538-2424-3ad9-98b5-765fc85e4906 | -10.883 | -56.4567 | 2025-07-02 00:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| fa11b098-c4a0-3196-8103-61169367bed4 | -7.7758 | -44.0164 | 2025-07-02 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2c4ec61b-3fe3-31c1-b5b5-6359e03d5451 | -3.0355 | -49.4476 | 2025-07-02 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 205f8a13-fd40-3679-8a3e-7f017329b99a | -7.0943 | -44.3819 | 2025-07-02 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5d501aeb-b527-3c31-87f9-8e364af141de | -7.8135 | -44.0126 | 2025-07-02 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 2aee65f7-71f6-3beb-9795-a85dc9261189 | -7.6051 | -45.7464 | 2025-07-02 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 6b0db1a7-f677-3c6d-bea8-ce71147fe56d | -7.2028 | -43.0936 | 2025-07-02 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 222.4 |
| 5480012b-2400-30b0-abe1-94b910df2c6d | -7.2031 | -43.0701 | 2025-07-02 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 126d8ce6-ce2e-32a2-9634-d732b9869e4e | -3.0356 | -49.4264 | 2025-07-02 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0f45ea31-ba8e-3a73-aa64-73725efebd87 | -7.8133 | -44.0358 | 2025-07-02 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 775bd988-592f-3dfa-9d0d-c548aa6357ec | -7.7947 | -44.0145 | 2025-07-02 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 259.6 |
| 63483678-6f75-3460-af47-d194140c851e | -7.7944 | -44.0377 | 2025-07-02 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 56812486-564c-302a-8df8-b2d1fbed5093 | -7.7758 | -44.0164 | 2025-07-02 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |


[Clique aqui para ver as próximas entradas](README3.md)
