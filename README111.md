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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c3f8b9c-b175-33fa-9b38-cb0b625d69e8 | -12.39174 | -48.18971 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 887dacd3-a7f2-3cbf-8ee9-a01b9973a68e | -14.17952 | -48.76363 | 2026-08-28 17:26:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8ecab6dd-6471-3788-9c53-f7c2ec6c89b2 | -16.42844 | -49.00535 | 2026-08-28 17:26:00 | NPP-375 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bcd92234-2d5b-3ce7-954b-4922984bb333 | -13.32736 | -46.93135 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8aa139ea-ad2f-3279-93c1-5632cd6c3af6 | -13.40988 | -51.86721 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a38aec0b-f35a-3711-89bb-84e8d64821c8 | -12.62114 | -44.63094 | 2026-08-28 17:26:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 34ea5d82-c74f-37cd-8a16-d22debb45639 | -12.79669 | -46.45215 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3552d634-bb1c-3460-9c95-e6f4b75cb919 | -11.20689 | -55.09885 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8ae4b053-0143-3bc4-8fdd-c16e4825ef8e | -11.56674 | -50.66209 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56202da7-b128-3c1a-8476-0bf7a811ecf2 | -16.16017 | -58.59182 | 2026-08-28 17:26:00 | NPP-375 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d4d07dda-34f7-3285-aed9-6b3b3d60ab67 | -14.49185 | -53.40302 | 2026-08-28 17:26:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 10909f25-f65e-31f7-a9ac-cf2f5eba975b | -14.92289 | -56.31626 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cb8c2a42-c8bc-3ee5-a085-88de4f9156af | -13.86909 | -54.11754 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 15c27d6b-f159-339a-ad7d-effb8b8fbff8 | -14.60882 | -53.14939 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c656df0e-2d9c-3d80-86be-d371629cf4ef | -13.42252 | -51.77095 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a225a2d7-4050-3510-9d41-07418509b0c5 | -9.86984 | -45.87332 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e046399-179a-300f-9d32-39df3728631d | -13.40467 | -51.76763 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2898fddb-5a43-3f28-a9e8-3133305efe55 | -14.90279 | -56.32358 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 67d00b30-ab04-34d3-9e14-fd4e3ffcb5c4 | -13.32624 | -46.92556 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| de512a08-40a1-36f2-8e37-1fd94565bb68 | -11.84146 | -47.22265 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00d61e7d-1848-35e8-8c1d-00a7c90297eb | -15.73924 | -51.17966 | 2026-08-28 17:26:00 | NPP-375 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 5a230ae4-f2cd-35ac-9fbc-46e7f13fbcdd | -14.45924 | -58.52014 | 2026-08-28 17:26:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 261d213c-e915-3fa9-a307-14a169e38a9c | -10.46915 | -46.17825 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 000c3f67-bea7-3e0b-b4b7-94c12acc3e42 | -14.19185 | -52.84572 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 19df5c6c-d3d4-30db-a2a4-301d428ac0b2 | -13.41867 | -51.7604 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| be4ae769-0f5e-3ab0-a61b-52ef483a6a82 | -12.79724 | -46.45496 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b915a3b4-7c7b-33f6-aa0d-24f5eee81c79 | -10.76962 | -50.62757 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a498b0c4-9b53-32bf-9295-1bf2610847e4 | -15.3572 | -52.83956 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d386416c-9d76-317e-b2eb-68f2084d771d | -14.88183 | -52.62657 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 6ee8f6f9-45b2-3f49-8c19-ad62038a9148 | -10.75859 | -50.6371 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b439801b-d5bd-32fe-bacf-64dd6963dc80 | -13.41652 | -51.79322 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| afc07729-048f-34a9-8f21-fbc67981d283 | -13.40835 | -51.76694 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7345459e-9f17-3f62-baf8-aabb35a61868 | -11.3797 | -50.23183 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8fc9920-b3b5-348c-a166-f0e8738f4dcd | -11.83189 | -50.07162 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2bdec85-b4d5-31fa-96a9-a62e71f54973 | -12.03504 | -47.18709 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b6c741d-cc29-365c-a9a9-03fbc424bc15 | -13.34801 | -46.90347 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ddb15e01-c7ba-3ce4-a006-a708c2f11cd6 | -13.5999 | -45.77682 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 04435ce8-391b-3d32-aabf-90c58e817240 | -14.8707 | -52.62446 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dfe4855b-dd43-3a57-a3fc-17ace1688ef7 | -11.19018 | -55.07962 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7c6724b8-a1f8-3829-bd88-11fba354ae54 | -13.87245 | -54.11698 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 826daea7-9555-30d5-98db-73e19abff977 | -12.35903 | -44.39347 | 2026-08-28 17:26:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b7b9be95-4450-3270-852b-bc0fb8a4b32c | -14.16788 | -48.77434 | 2026-08-28 17:26:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 22996a5c-5828-36dc-8743-8250b472a7b0 | -9.86737 | -45.85647 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| c4cd98d0-de55-32e7-9783-986d310c2e80 | -11.53806 | -45.51178 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb82ca11-d5fa-3e80-b2cb-e5d5b53b9a48 | -12.06847 | -47.15367 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0371814-16f1-303f-b17e-8890754c3460 | -9.69148 | -46.56092 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 07d34b16-4d41-3d93-8908-d5a012617404 | -11.85799 | -49.79794 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecdd580b-2791-3ad9-824f-ac7aad90ba46 | -14.58704 | -58.64933 | 2026-08-28 17:26:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4f1716e7-19c3-3564-aa48-02a35cc541d6 | -11.6525 | -55.68624 | 2026-08-28 17:26:00 | NPP-375 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| e67cf221-f9ae-3f45-b926-1d08e6e40157 | -13.83673 | -54.04408 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8fdda0be-638a-35aa-9dd1-ce443fb8022c | -11.34618 | -48.38055 | 2026-08-28 17:26:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1d5442c3-cc39-3b06-94f4-50118504c5bf | -14.24043 | -51.76596 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bd0c2e04-2f8d-3f82-9950-36018e8a2369 | -14.43187 | -52.59196 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e310fc8-1494-3be2-89c7-6d234524ddf3 | -10.08901 | -46.98554 | 2026-08-28 17:26:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a05ce5a1-0374-3b36-8553-c0fa3204e9d3 | -12.19446 | -50.56197 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d9b937f1-b1d5-33ae-b832-d025490ad37f | -13.32808 | -46.9283 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 907fa7dd-51b3-3018-befb-3bd7cd99c3fc | -12.04962 | -47.18119 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 37a18e35-b65c-3fa5-b969-ceb36a3ebead | -9.69212 | -46.56445 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e178090b-f7da-3176-948d-f91f314ebdc7 | -14.19533 | -52.84512 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 72768de7-2a31-3d39-babf-ecf14967787a | -15.48075 | -53.96081 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e38a95ef-a2b8-3149-8a8a-38de9594268c | -11.15885 | -45.5867 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb8ac5ac-ffa2-329c-85bb-e0e5dca32964 | -12.65001 | -46.75431 | 2026-08-28 17:26:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 67db42c8-cc68-36d0-b9b5-e463b8c6ee69 | -13.32283 | -46.90796 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17e4e258-5955-3c5c-a8ea-174c68ec5e65 | -15.35938 | -52.83122 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 796535ea-8cb8-361b-9b08-ce4604b754be | -11.96253 | -45.50318 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0a1fe7f2-466c-30ab-9e9e-25618bca5f6c | -11.22326 | -45.05066 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bc08250c-3249-313a-8d9c-8d2676dc9b84 | -15.60676 | -56.4003 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7ae59327-a885-3d0a-b092-caa66f8fcad8 | -10.831 | -50.52902 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ce2688d5-99a6-3f15-ab2d-a993ca1d0294 | -9.68722 | -46.56918 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4c5d4163-758f-3e56-8c9c-d372041de744 | -9.8697 | -45.84074 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31e3bd5c-87ed-3b98-8b4c-b0b0105a9052 | -9.69084 | -46.55739 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| fb7c8752-8ddd-3422-8b3c-de26fbcdba0f | -14.87549 | -52.6317 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| ab692fff-113d-3976-aa55-dad83e5f3c68 | -12.57257 | -48.48233 | 2026-08-28 17:26:00 | NPP-375 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| c19c18d6-cb24-3249-961f-6fa67cabe5b2 | -14.17227 | -48.77358 | 2026-08-28 17:26:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ff32265e-db6d-3cf3-91b6-d28203d90d5a | -10.47351 | -46.17713 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c037cd25-7c25-37ba-a270-32f1376b1b66 | -10.30809 | -49.97112 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 8ab8dfec-3e33-32ce-bb55-ac829b6968d3 | -11.20021 | -55.09993 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 12ff156e-ccaa-3b38-8144-6287534f6bbf | -11.60962 | -50.18644 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 93a3ab78-e439-36f7-a605-ee595935ffac | -11.02647 | -49.67928 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| a33be311-ebc4-3658-8a05-81d6d0dbec61 | -15.6073 | -56.40407 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 24daa048-3187-3356-95e4-98da32c06768 | -11.19392 | -53.99609 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d9c79de4-1d0a-3213-80b6-04dada7ee883 | -9.503 | -45.66396 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 37d8c686-5b06-3258-9b7b-778c4c1f0864 | -14.83427 | -45.52648 | 2026-08-28 17:26:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| cea2f4cc-73d6-3f13-9b5e-1df1c05218dd | -10.83479 | -50.51237 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a63a48fe-0f59-3f8c-97a7-c38a86b680ce | -11.24183 | -53.99196 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1addad72-59b1-3de6-ad1d-eaa1b7a5d3eb | -14.91219 | -56.31413 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| b37e50bd-a38c-39ad-ae5a-b2aa7ca289e3 | -12.09429 | -47.17943 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| beb1be69-4689-38ec-9fd2-074c878986d7 | -11.24869 | -45.06841 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4da0f557-f35d-35cb-b35d-370019c65bd5 | -11.19519 | -55.08978 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fc9e1350-2a12-385e-8795-546df8f5066d | -14.80926 | -48.80477 | 2026-08-28 17:26:00 | NPP-375 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d8daa3eb-2ab0-3c56-a30c-926eca513e36 | -14.51934 | -56.50834 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e8497d03-8821-3cf9-9e17-824afe66800c | -13.40173 | -51.77279 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4b042dbb-dfee-3a63-b920-2a9af67fa551 | -14.20677 | -45.2831 | 2026-08-28 17:26:00 | NPP-375 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f0cc7648-9980-37e1-9873-b9978f289922 | -12.19166 | -50.56982 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6d74000b-39fc-3f29-9dce-f8eeb24e8efe | -11.24604 | -45.055 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8e352030-8068-3820-a1d1-2bd02d532345 | -8.96645 | -42.69939 | 2026-08-28 17:26:00 | NPP-375 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| b7d81485-da46-3e3d-be86-f22ee29a8208 | -16.31069 | -47.85168 | 2026-08-28 17:26:00 | NPP-375 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b30baf8f-68bd-3117-b084-8fd62830e699 | -9.50481 | -45.64814 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 49672f96-1eaf-3f5a-b65d-367e3693f259 | -11.71592 | -54.53535 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| a59649a6-af06-3f74-9eff-3cd097d229c6 | -11.6797 | -46.72986 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README112.md)
