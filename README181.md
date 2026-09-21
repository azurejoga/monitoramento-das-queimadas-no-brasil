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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f854a41d-876c-3a8c-9580-0825244f6df2 | -11.4353 | -45.3459 | 2026-09-21 17:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| c630a7e5-038c-3597-af8e-bfe51c1dc97d | -6.7863 | -58.8995 | 2026-09-21 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5c0196cf-d7c8-36ec-bcc1-d86e155c6aab | -10.4285 | -50.3518 | 2026-09-21 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 12bdaa46-cf2b-3b26-974d-23cd9d6306cb | -6.5761 | -45.5194 | 2026-09-21 17:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 2f5066a3-dcdb-3656-be0c-b97df8567049 | -6.9223 | -42.9323 | 2026-09-21 17:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 185.3 |
| 86248e5c-ea99-3c14-b2c5-6345dfb2c869 | -7.5661 | -61.3239 | 2026-09-21 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 0adafe73-8341-3569-af7c-6f872ccd6055 | -6.3434 | -55.8442 | 2026-09-21 17:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e038ec72-a5b0-33dd-a40a-a21611665500 | -11.0237 | -49.7304 | 2026-09-21 17:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 8e7d0c49-46d7-3663-becf-da2401750556 | -5.8596 | -53.4993 | 2026-09-21 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 0906a37c-5270-3cc9-bfca-dc364bfe8a38 | -7.8789 | -44.8348 | 2026-09-21 17:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| ffd78a7c-ed6a-3630-ace8-1e00e17906fc | -5.5848 | -45.5478 | 2026-09-21 17:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 1099cae4-e2b2-3bf9-8045-d38abe653123 | -7.5891 | -57.6561 | 2026-09-21 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 213.5 |
| 2294bd6b-2880-323c-b461-a9ad010940f3 | -6.295 | -57.735 | 2026-09-21 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 105b0f25-bd57-3149-89ef-dfad5d9dcfaa | -10.6883 | -50.7084 | 2026-09-21 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 97277989-55f1-3056-be19-f53742f8a5af | -10.67 | -50.6678 | 2026-09-21 17:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2e1c2947-fc2c-3f40-a74f-826ec424054f | -12.4567 | -48.2438 | 2026-09-21 17:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e960d30e-08a0-3207-9e2a-78259a864570 | -9.8686 | -48.447 | 2026-09-21 17:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d068f5b1-10c8-3496-82c4-1f9df6a9cd60 | -11.4353 | -45.3459 | 2026-09-21 17:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 43421783-aef5-3547-b5df-33197ae2c6ed | -7.3444 | -55.6142 | 2026-09-21 17:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 98f0732b-2cf9-37dc-8003-5854cd927040 | -10.7061 | -50.7915 | 2026-09-21 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| ef34caf1-9710-3678-9e1a-940570744dbd | -5.9333 | -53.5362 | 2026-09-21 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 6e1a50a2-98a6-3260-bd5a-3a1b634f6b47 | -7.822 | -61.8084 | 2026-09-21 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 8d72d7de-d163-330d-831f-d67414e79c57 | -2.8791 | -57.8184 | 2026-09-21 17:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 169.8 |
| e15a1788-ccc3-3063-803f-408a96de0e13 | -10.911 | -53.984 | 2026-09-21 17:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2d16c36c-b1db-3c7b-bb92-1adf9cc20bde | -1.6766 | -54.9327 | 2026-09-21 17:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| dad9093b-4913-3bfe-b1a5-13ae6b60e09e | -8.1681 | -54.8239 | 2026-09-21 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 89d70fdd-3974-39c0-94af-aa727ee0ee3c | -5.9335 | -59.9515 | 2026-09-21 17:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 84c75441-f45d-343c-bde9-fb573419e520 | -7.9152 | -72.9324 | 2026-09-21 17:50:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 86.9 |
| e1532654-2d00-3d8c-aae4-c2cfb9f82947 | -6.8796 | -41.6995 | 2026-09-21 17:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 470.3 |
| 15976b8d-3bfa-324b-a774-7c3830c2ec51 | -2.8791 | -57.799 | 2026-09-21 17:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 827c3a16-e796-333a-a945-83e3e2f59e52 | -3.3 | -57.8681 | 2026-09-21 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 174.6 |
| dc091f72-873e-3ad5-be6d-403e47f212fb | -3.6398 | -60.5656 | 2026-09-21 17:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f19a1c53-cbe8-3347-aad9-a0c08f50fe04 | -8.7381 | -45.4526 | 2026-09-21 17:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 50a8b12a-87b8-32ef-b1cb-52ba9dd9956e | -10.1814 | -68.4175 | 2026-09-21 17:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 8ce6df34-ef6d-38ad-be80-f17ff6bf92de | -7.4184 | -73.5177 | 2026-09-21 17:50:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 29310020-00da-38d3-9976-dffb8d422400 | -2.9157 | -57.8177 | 2026-09-21 17:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e5d26b7c-9ef1-3490-b01f-e4362cea2c40 | -11.3996 | -44.0995 | 2026-09-21 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 37b9539e-f246-3bbc-8304-e4d417785aad | -9.2793 | -45.9369 | 2026-09-21 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 4e5b1f8c-6b44-3319-afdd-5a2eb08245ff | -3.3183 | -57.8677 | 2026-09-21 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| fb4995fb-c638-3944-9501-3a6d0ebb4f02 | -8.7729 | -44.2568 | 2026-09-21 17:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 7b5b4433-d865-386b-a954-ddaef624dd7f | -9.1999 | -60.7738 | 2026-09-21 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 90824273-1179-304d-9612-9170fa0ad7b0 | -9.807 | -46.0797 | 2026-09-21 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b44d573b-ffbf-38e4-9175-2e921f913ed8 | -3.1514 | -58.644 | 2026-09-21 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 87af1ada-a919-3f86-9d7f-a15cc0eede1b | -7.5478 | -61.3056 | 2026-09-21 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ab9ff883-7c85-30be-b82a-6e1cf8f86726 | -5.7504 | -43.7091 | 2026-09-21 17:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| dfb16f22-3a60-3b6b-a826-c718920f148a | -0.803 | -48.6611 | 2026-09-21 17:50:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 44a91ef7-36a1-3643-9ea5-cdcadece8f77 | -3.1698 | -58.5859 | 2026-09-21 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 0594dbd0-630f-31fd-bf1e-b3dc2b9c0b03 | -3.4461 | -58.0199 | 2026-09-21 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 41e3d40b-127d-37f0-b291-222785efe6ef | 1.5282 | -56.0424 | 2026-09-21 17:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 93d33807-33de-34cb-a187-dbb532821f8f | -10.8921 | -53.9857 | 2026-09-21 17:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 37a067da-b1ff-3fc8-9e4e-b7662bebb490 | -6.3656 | -58.2966 | 2026-09-21 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 776e1c18-bff4-32c3-8cfd-9066371f5bfd | 1.2794 | -50.8718 | 2026-09-21 17:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 12783614-9611-3226-a115-edf8a4bc76c0 | -9.1057 | -60.9511 | 2026-09-21 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.4 |
| edbab60f-c17d-3464-9cc9-fd26f82b960e | -6.7093 | -59.4623 | 2026-09-21 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9b4b48c0-1332-34ad-b057-e4a6c79aa1e9 | -6.2946 | -47.6493 | 2026-09-21 17:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f1187a7f-60a6-3857-95fe-90a790203ba9 | -8.6606 | -68.692 | 2026-09-21 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ec61a683-3298-3280-bb2c-b3785379e827 | -3.6449 | -58.8647 | 2026-09-21 17:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 675625f4-2308-3f16-bc9c-07bc1a0c346d | -2.9157 | -57.7983 | 2026-09-21 17:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| f3aa3cbc-42d3-363c-96c8-323e4c89aecd | -6.2766 | -57.7358 | 2026-09-21 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| efc63171-7ac3-3e0e-a6bd-0c6456bc8626 | -6.513 | -58.3099 | 2026-09-21 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 9f396e5f-1d5f-331e-9742-fa34fcdf6efc | -7.5703 | -57.6962 | 2026-09-21 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 450.0 |
| bffb4eeb-ea77-3179-9398-69f193deb532 | -3.4215 | -60.1896 | 2026-09-21 17:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 30df0637-b480-3bca-8724-2de1fb7ce837 | -5.6221 | -43.3934 | 2026-09-21 17:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 242.9 |
| f8d1dcc4-0f18-3fd3-8370-c15a93058e74 | -9.8404 | -46.3911 | 2026-09-21 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| ae8ecd90-a003-3c8f-83ad-93767c5f1d8d | -6.8985 | -41.6976 | 2026-09-21 17:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 600.9 |
| a1810067-25bb-38f8-8f2c-80291648980c | -5.8225 | -53.5214 | 2026-09-21 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 5516d224-f699-3449-bdd7-fb120eb501aa | -7.7707 | -70.8714 | 2026-09-21 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 92c36134-38ea-3739-8f9c-77dd83e9dfa1 | -11.0048 | -49.7325 | 2026-09-21 17:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 474b170d-2af8-3f87-a27f-aa7f712ab7e1 | -6.7123 | -58.9412 | 2026-09-21 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d0068cfe-ed43-3d52-b9b7-a801099baae9 | -8.4922 | -47.0257 | 2026-09-21 17:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 1f29019c-9b24-3f50-a266-1067fc3bf445 | -8.8758 | -71.4806 | 2026-09-21 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c571eab6-704a-324e-a61d-e5f4e953f78e | 1.0844 | -60.6741 | 2026-09-21 17:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e0850ef8-d69b-340b-b0a9-d2c29fafc1de | -3.331 | -59.8292 | 2026-09-21 17:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2e5a20db-cb3c-35dd-b2d0-c8f14faf7bf9 | -8.3167 | -45.9934 | 2026-09-21 17:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ea5a3b2f-3056-3ab9-9bcd-f7a36d2da79b | -3.6264 | -58.9228 | 2026-09-21 17:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 360e3fbf-d3b7-39ab-9db2-6cfacf959346 | -10.6878 | -50.751 | 2026-09-21 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 05d7fd33-9926-322a-bc2d-73de62a1c212 | 1.2978 | -50.8715 | 2026-09-21 17:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 56.1 |
| fbd666c3-ed3d-3fa3-80a0-59317c247545 | -10.8735 | -53.9668 | 2026-09-21 17:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f6c00c1a-1449-304f-b4a7-6d28774df2f5 | -3.7313 | -60.5638 | 2026-09-21 17:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7b614738-dc18-3de1-9eb3-07227953f6c5 | -3.7364 | -58.8626 | 2026-09-21 17:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 3cfa73f1-d019-3084-bc17-cd6edb16b23d | -7.4186 | -73.1537 | 2026-09-21 17:50:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f931fdf3-44fc-3749-823d-10c039343dab | -6.7517 | -55.6256 | 2026-09-21 17:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| db6822b9-cdea-30ae-8528-93c9b5b8db7f | -3.3322 | -59.3894 | 2026-09-21 17:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| cab9cd2c-2893-3d0d-b22d-e3bf7f23ee29 | -8.6755 | -70.0345 | 2026-09-21 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 028640d8-d91b-3fc9-b612-ec8a8a6b3e3a | -8.3164 | -46.016 | 2026-09-21 17:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f6ee3cf5-011d-3963-b7ef-53d286612bb2 | -7.9537 | -71.5089 | 2026-09-21 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 2cfcc2ef-830c-387f-adfc-a1d486e1cb9b | -7.5477 | -61.3247 | 2026-09-21 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| b0aaaf4a-2e8d-30ef-919a-9db05a01210c | -5.3955 | -45.8746 | 2026-09-21 17:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| ad83b77f-fc84-37db-8070-7ad5345c1be7 | -10.4764 | -69.2073 | 2026-09-21 17:50:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b67af8e1-c705-34c5-8594-53992bbb9420 | -10.6697 | -50.6891 | 2026-09-21 17:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 133cd920-4689-39e8-a250-3c08115c0cbb | -8.1872 | -54.7622 | 2026-09-21 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 0515969b-d0c0-36d2-a28c-c9338a83bbcc | -10.8282 | -50.1601 | 2026-09-21 17:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 557e8024-8e90-3615-be4c-06ca4f46c598 | -9.2796 | -45.9143 | 2026-09-21 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| d40205ca-31e2-3002-8d8b-8c59c7d1f548 | -6.9223 | -42.9323 | 2026-09-21 17:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 212.8 |
| d4fe000c-bd8b-398e-a4e5-8b015aab8785 | -3.8264 | -59.3407 | 2026-09-21 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| a9346ff7-e8a0-3e2d-a21e-8e7e17bf23ce | -6.5451 | -44.8643 | 2026-09-21 17:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| cd49e806-7091-3fb9-b959-a1aecc581172 | -2.9528 | -57.623 | 2026-09-21 17:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 630facc0-3af0-3037-bcac-58849e1b4dfc | -3.4974 | -59.1944 | 2026-09-21 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| f355b658-2bda-3226-9ecf-9d4580bf5df5 | -2.9525 | -57.7394 | 2026-09-21 17:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| bf61fbd1-b865-37be-bff4-176b739f9477 | -6.3436 | -55.8243 | 2026-09-21 17:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |


[Clique aqui para ver as próximas entradas](README182.md)
