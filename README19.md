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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 294267e4-c7ec-30f9-9a0d-2efc879b82af | -12.8736 | -44.3828 | 2026-06-23 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 67ee26a5-1f61-3376-98d0-068c5d0c77ca | -12.7949 | -44.4661 | 2026-06-23 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 238352f1-baa1-34d3-a88e-25fb252ce014 | -12.8548 | -44.3625 | 2026-06-23 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| e6a59aaf-a1ec-3c60-bef6-2ea0fda4be98 | -12.8741 | -44.3593 | 2026-06-23 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 337.2 |
| 930efb37-4033-3675-b3f1-6ba47f99a372 | -12.7949 | -44.4661 | 2026-06-23 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 347.8 |
| 55dfdbd4-4480-3c35-80b9-8f2408ff1c9f | -12.8736 | -44.3828 | 2026-06-23 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ad653ed1-0ce9-3f82-86d5-64b11809a166 | -12.8548 | -44.3625 | 2026-06-23 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 4ec95331-496e-392d-b87f-fd48500ce3ea | -12.7949 | -44.4661 | 2026-06-23 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 467.3 |
| a96601b9-a529-322a-93d3-664c6a66f95d | -12.8736 | -44.3828 | 2026-06-23 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 5d7ca9c5-c04d-356c-ae5a-4d5cfd27aa93 | -12.8741 | -44.3593 | 2026-06-23 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 354.8 |
| e3264ec6-dde5-31eb-a566-6d2d62e8930d | -12.7949 | -44.4661 | 2026-06-23 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 419.0 |
| e501ec45-8f06-3c34-aa57-94b32d1e4a49 | -12.8741 | -44.3593 | 2026-06-23 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 359.7 |
| ea871717-92b7-30b8-9473-85a3a62e2b99 | -12.8736 | -44.3828 | 2026-06-23 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 207.2 |
| d283f457-27ff-3502-a639-8576a45a0a79 | -11.4892 | -46.6795 | 2026-06-23 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 146.4 |
| af0ce92f-a5a3-3b90-839f-ad516906f3ef | -12.8548 | -44.3625 | 2026-06-23 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 5350d584-dffd-3833-ab79-70c79371da23 | -11.4701 | -46.682 | 2026-06-23 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 9b2d68ce-3b91-3337-9817-1aa6c70783c9 | -11.4892 | -46.6795 | 2026-06-23 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 838462ec-3416-323b-9bb0-d8083895045a | -6.9979 | -42.9016 | 2026-06-23 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 98ee9623-471f-3ad8-b564-8cfd8b9c81c0 | -12.7949 | -44.4661 | 2026-06-23 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 421.5 |
| 198c0708-b543-3376-9963-132349a89f50 | -12.8548 | -44.3625 | 2026-06-23 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| f1ae8978-3577-3b85-87c9-4d4aaa562bbb | -12.8736 | -44.3828 | 2026-06-23 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| bc8992ad-db3b-311b-a886-97f66c732c9a | -12.8741 | -44.3593 | 2026-06-23 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 408.8 |
| 17da4039-7a46-3997-8b06-3c34c7b5b088 | -12.8548 | -44.3625 | 2026-06-23 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| e83479a3-a12f-3cda-a2f6-5f0322e0299c | -12.8741 | -44.3593 | 2026-06-23 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 358.7 |
| 5963b7c6-8edb-3728-8bbd-ebfef5a74e07 | -10.7542 | -50.0395 | 2026-06-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| eb55b058-21a1-3083-9287-d8a55c7cede5 | -6.9979 | -42.9016 | 2026-06-23 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| b9d350c7-f749-3cac-bcef-4bfc0a241ef9 | -12.8736 | -44.3828 | 2026-06-23 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 8b2537da-dd4e-30fd-8b00-a9c3c13670af | -6.4973 | -42.2142 | 2026-06-23 14:10:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 93773e7e-1a3f-37de-8a7b-adc7eb1d699d | -12.7949 | -44.4661 | 2026-06-23 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 314.9 |
| dd717b7e-87d9-3e2e-9b3f-32ee48b3e11b | -6.4973 | -42.2142 | 2026-06-23 14:20:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| f99712ba-68dc-3b6e-8451-a72a91f2b27c | -12.8736 | -44.3828 | 2026-06-23 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |
| cf7b1e1e-77d6-329e-b1ca-6ad0c1432a3b | -12.8741 | -44.3593 | 2026-06-23 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 335.7 |
| 9252af8a-7188-3e8d-b1b6-bdd569322d58 | -10.7542 | -50.0395 | 2026-06-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 68231358-78f8-311e-a633-f5eac5f29d04 | -12.7949 | -44.4661 | 2026-06-23 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 303.5 |
| d5893f01-2db4-3fa9-aa77-345b250d5199 | -9.7442 | -47.8688 | 2026-06-23 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 51baf2f8-7333-3f0d-98db-cd49c8c283b5 | -12.7949 | -44.4661 | 2026-06-23 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 443.3 |
| 8d6eaa58-59f5-3849-a38a-688157a151a1 | -6.4973 | -42.2142 | 2026-06-23 14:30:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 908ed393-0e09-336f-aed0-c38ee37ebf67 | -12.8736 | -44.3828 | 2026-06-23 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 4a39da89-79c2-336f-8e71-a8dbd8ffed51 | -12.8741 | -44.3593 | 2026-06-23 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 413.2 |
| 49f1205a-a301-3eea-bd93-59e75861e2b2 | -6.4973 | -42.2142 | 2026-06-23 14:40:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| d4f89c9e-1fb0-3d3c-90ce-116996fc62de | -12.8741 | -44.3593 | 2026-06-23 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 415.7 |
| f0dbf5c2-04a2-3060-a2d2-50b1c18c7b5b | -12.8736 | -44.3828 | 2026-06-23 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| bda1dcea-39c9-32a6-9e22-e816d2f12971 | -9.7442 | -47.8688 | 2026-06-23 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 445f2965-b3c0-30af-948d-58729f10bb61 | -12.7949 | -44.4661 | 2026-06-23 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 595.5 |
| 41da93a2-3fc8-3f34-abe3-fca6825b7e41 | -6.4973 | -42.2142 | 2026-06-23 14:50:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 036c4746-8ac5-36db-be2a-ec72ef4777b3 | -12.8741 | -44.3593 | 2026-06-23 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 420.6 |
| 0f2d1b29-c6b1-32ad-8a5e-3f789c2dc01e | -12.8736 | -44.3828 | 2026-06-23 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 77a94fb7-d133-3012-ab5e-7c748324b8d8 | -11.4892 | -46.6795 | 2026-06-23 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 113e99a9-8700-396c-afcb-82035c244143 | -6.9979 | -42.9016 | 2026-06-23 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 6bd6d20c-7cfb-37bc-a2a7-62b113ab6491 | -12.7949 | -44.4661 | 2026-06-23 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 489.4 |
| f22461cb-b0eb-3078-9eb8-880262cfb67a | -6.9979 | -42.9016 | 2026-06-23 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| c2727193-3215-3cef-9448-940d7dc76500 | -12.8741 | -44.3593 | 2026-06-23 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 439.2 |
| 029d3672-f8ba-39ec-a7ef-e4df3fae4556 | -6.5161 | -42.2125 | 2026-06-23 15:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| a78ca4da-ad31-34bf-a5dc-8dfe73c9e6d9 | -12.7949 | -44.4661 | 2026-06-23 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 434.2 |
| 2accf2e1-7e8a-3d7d-9ebe-bb03d3265898 | -11.2791 | -43.3405 | 2026-06-23 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 95.4 |
| ed022e10-8fc1-3e05-a9e4-951193e6924d | -12.8736 | -44.3828 | 2026-06-23 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 241.8 |
| a43b5cb2-bd43-3315-8976-450be01850ae | -11.4892 | -46.6795 | 2026-06-23 15:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| dbe45063-0bf5-3db6-b9da-66b17bfe8408 | -12.8736 | -44.3828 | 2026-06-23 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| da24924a-8748-3310-a0fb-b40312d75572 | -10.7542 | -50.0395 | 2026-06-23 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 706028c4-cc19-3f3d-901a-a4480488c570 | -12.7949 | -44.4661 | 2026-06-23 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 366.6 |
| 2504680a-5e76-3c79-b87d-fa2f62e7f5bf | -11.2791 | -43.3405 | 2026-06-23 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 134.4 |
| ec9b0e02-7886-3ac0-8f50-c22a08469114 | -12.8741 | -44.3593 | 2026-06-23 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 332.2 |
| 959e7fce-028b-3db1-9c4c-b6311e2afdef | -6.9979 | -42.9016 | 2026-06-23 15:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| ba6106a1-4866-3bd7-9116-fe94e9bdcc9c | -11.2983 | -43.3376 | 2026-06-23 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 7c011470-6412-35b5-a8a7-70f132ed4427 | -9.7442 | -47.8688 | 2026-06-23 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 43eeccf8-21f4-34a8-8709-caa31d409360 | -11.2791 | -43.3405 | 2026-06-23 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 108.9 |
| f7881172-2806-3aea-975e-09b9e7b6c18e | -12.7949 | -44.4661 | 2026-06-23 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 320.4 |
| c8d8b628-e96f-36ba-95d4-68a13605c03d | -12.8736 | -44.3828 | 2026-06-23 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| d0153df3-4b56-386f-a111-bb312485a858 | -11.2791 | -43.3405 | 2026-06-23 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 142.7 |
| c31da891-e5a5-3cec-8efd-23944b5e230f | -12.7949 | -44.4661 | 2026-06-23 15:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 216.2 |
| ef05bbde-1eff-3b2f-94ee-e1bd761a52f4 | -11.2983 | -43.3376 | 2026-06-23 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| c1bf9d7c-1f86-3b9b-9b38-e25a95b57079 | -6.9979 | -42.9016 | 2026-06-23 15:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 2a366d9d-babd-309f-8d40-85475b7e7e7a | -10.7542 | -50.0395 | 2026-06-23 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 21508bc0-830e-3bef-9be8-bb66d14963b5 | -12.8736 | -44.3828 | 2026-06-23 15:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| a22e515b-d2ff-331c-91ff-841b772973b8 | -6.5161 | -42.2125 | 2026-06-23 15:40:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 822a72b7-b50f-34ee-8573-4c7f8575b1c6 | -12.8736 | -44.3828 | 2026-06-23 15:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| b2c633f7-41e2-3062-ac01-0d36d73faf82 | -12.7949 | -44.4661 | 2026-06-23 15:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 255.9 |
| f3fc86bd-dfc2-3cbe-8cc3-f4b87f823b8b | -11.9108 | -43.4081 | 2026-06-23 15:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 0e13a5d4-6013-3c64-b343-c915beaaaad3 | -6.9979 | -42.9016 | 2026-06-23 15:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| e8d38342-7fc9-3e55-8a97-321f73480083 | -11.2983 | -43.3376 | 2026-06-23 15:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| ca94bc41-59d2-30ab-899c-9f7fb7405e13 | -12.8736 | -44.3828 | 2026-06-23 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| bb5f8945-d66b-30a7-833a-96e84b0205c9 | -6.4973 | -42.2142 | 2026-06-23 15:50:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 2cec4205-c6f2-3ea7-9d4d-3d03ed6e7655 | -12.7949 | -44.4661 | 2026-06-23 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 188.2 |
| f2b48367-7405-3aae-94cb-6b244e7125e8 | -6.9979 | -42.9016 | 2026-06-23 15:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 61eb0b34-ec5d-3e94-9036-84b02ebd351c | -11.2791 | -43.3405 | 2026-06-23 15:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 103.1 |
| ab6aa54e-172e-3107-97fa-52b64d534912 | -6.5161 | -42.2125 | 2026-06-23 16:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| c3d6390e-dd4b-326f-bb3b-7afb89167e28 | -12.8736 | -44.3828 | 2026-06-23 16:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 6a327d15-27d6-311f-82b0-de1e10204eb7 | -11.2983 | -43.3376 | 2026-06-23 16:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 460fc84e-97da-30b1-b352-0e2d54ff2ed6 | -12.7949 | -44.4661 | 2026-06-23 16:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 5434b01a-42af-35ec-a97f-8f3d82632680 | -8.8118 | -47.0606 | 2026-06-23 16:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 34f807c6-6d7d-3f58-931d-f72beb30bc14 | -11.2791 | -43.3405 | 2026-06-23 16:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 466f7817-977b-38fb-81aa-16d76066dda1 | -6.9979 | -42.9016 | 2026-06-23 16:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 30361090-a8ee-3fee-bd2b-bdb5a2d3ccca | -8.8118 | -47.0606 | 2026-06-23 16:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 08888b1f-f2e2-3795-ad8e-7d1c037005bc | -12.8736 | -44.3828 | 2026-06-23 16:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 97b103df-d807-37e8-aaaa-8a9af9d2ec87 | -6.4973 | -42.2142 | 2026-06-23 16:10:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 64f3d0f6-06f5-3d1e-9f91-098a2396b402 | -12.7949 | -44.4661 | 2026-06-23 16:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 47b0d770-2284-33c9-b140-f68d82e25572 | -11.2791 | -43.3405 | 2026-06-23 16:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 4e809a39-d777-3290-9994-014f2048badb | -6.9979 | -42.9016 | 2026-06-23 16:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 90bc4a05-bfd8-3cc4-98f6-6a3e2bc0c869 | -11.2983 | -43.3376 | 2026-06-23 16:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 8bb31f4f-a28a-30a6-9e43-d83beee9acb5 | -8.8115 | -47.0828 | 2026-06-23 16:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |


[Clique aqui para ver as próximas entradas](README20.md)
