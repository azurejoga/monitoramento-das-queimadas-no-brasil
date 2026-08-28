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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7a06cbc-1f0e-3978-8703-c43f16f27f16 | -8.76202 | -49.63494 | 2026-08-28 18:49:00 | AQUA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bd5cd2aa-6b22-3866-8b73-c56f63409af1 | -11.22262 | -45.04211 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a48b882e-1015-348b-be68-3f57ed28c63c | -11.38507 | -45.13433 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cc63ed53-0bda-3e33-8cf4-43608c1033fc | -11.35516 | -48.39561 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 9e422265-4bf8-33bf-b453-28f291096b7c | -11.24617 | -45.06997 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c27ede88-1c77-3b29-96d1-09153cfc121b | -8.02716 | -48.00596 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 211394d1-fd18-3970-a469-80fbb25e4be9 | -11.37013 | -45.15507 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a80d9b3d-878e-3d2a-9299-368d7b29db8b | -9.696 | -45.70619 | 2026-08-28 18:49:00 | AQUA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f5de435b-b534-3ab7-bb51-b43088655fc0 | -11.15625 | -45.58315 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2c5f7562-5256-3aec-894b-8cdfa51da741 | -9.79886 | -43.57742 | 2026-08-28 18:49:00 | AQUA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 6c4d7e0d-1945-3feb-aea5-902fd65b561d | -11.94217 | -47.50204 | 2026-08-28 18:49:00 | AQUA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4dc6be68-fd61-36f1-9ec3-930cda285edc | -10.45088 | -46.19073 | 2026-08-28 18:49:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| c59ddf72-7201-38ca-a324-3aa85515ba7d | -11.21855 | -51.27523 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 740b8d02-f30f-37a7-8dbb-3176aaa6f226 | -8.31661 | -45.68906 | 2026-08-28 18:49:00 | AQUA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 70880706-2bb6-3569-8fab-402defe60826 | -11.27597 | -54.03183 | 2026-08-28 18:49:00 | AQUA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 360.1 |
| a2f55780-1a98-3a32-8945-503a0b87311e | -9.46234 | -45.63222 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d8ebe487-2901-3aec-abe8-eca33b6c1886 | -8.31796 | -45.69809 | 2026-08-28 18:49:00 | AQUA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 1c7c7e0b-05cd-33c8-a990-9ed36dda94fc | -8.53252 | -55.27271 | 2026-08-28 18:49:00 | AQUA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 88c26978-21e6-369b-9d7d-d64b5b6147ac | -9.48612 | -45.65946 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 454.6 |
| 239fe10d-b24c-3d50-952d-f0fcf9cfa533 | -9.47381 | -45.64875 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 312.8 |
| d0f463f8-985c-36d2-8377-5f3f40a8a1b8 | -11.69999 | -47.81492 | 2026-08-28 18:49:00 | AQUA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fdd5606d-734e-3283-b033-66efcbbbfcbe | -9.47249 | -45.63983 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1057.5 |
| 5733309a-cd21-3051-9886-91cdd8df7c21 | -8.85742 | -48.51574 | 2026-08-28 18:49:00 | AQUA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 12.4 |
| aa4c5b40-582e-370f-b42b-8ff5fffc5da7 | -12.27103 | -43.14289 | 2026-08-28 18:49:00 | AQUA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| aec9def0-dcdf-3aea-aa94-2dfc59437b82 | -9.43111 | -50.46358 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 135e1ee0-72a8-39fb-a789-29955b772ece | -8.01952 | -48.01648 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2fa0c443-eb0a-3d29-a25b-a52559b1e7e6 | -8.5335 | -55.29572 | 2026-08-28 18:49:00 | AQUA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| afb388be-995c-336b-b6b1-a39306fdbd16 | -6.6723 | -38.85033 | 2026-08-28 18:49:00 | AQUA_M-T | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 49.4 |
| d25f2138-2732-3627-af39-e0bfd1897822 | -11.18974 | -43.72771 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 429e267a-edc0-391f-9031-da735d9356f3 | -9.41688 | -50.43882 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 00445a37-22e6-3c32-bedf-825594e5e4a6 | -10.01994 | -46.405 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 589a9206-931a-3012-a24f-97fd4311d804 | -10.45218 | -46.19958 | 2026-08-28 18:49:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 357.4 |
| 6dc06bcf-0ce5-37c2-b250-569e227f1f01 | -7.77996 | -47.63604 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c7e39475-0e62-3d11-9c99-268e7807bc65 | -10.32334 | -49.98484 | 2026-08-28 18:49:00 | AQUA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| aa1c6e04-9bf0-39a0-9524-553fbc4b4ac8 | -13.35098 | -46.90231 | 2026-08-28 18:49:00 | AQUA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d5204046-f955-373d-8483-8859f788ead4 | -12.76802 | -44.81524 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e3c63e2d-2d09-3780-a15e-95f01196a4c1 | -13.31772 | -46.92672 | 2026-08-28 18:49:00 | AQUA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 37288275-37eb-3b9b-87d0-81e6abd7137e | -9.42157 | -50.43287 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 10323628-81c0-3bcf-bfc0-da1e2c59a1ff | -8.42577 | -44.81694 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 45048173-571e-32f9-96ce-a47f9320682e | -8.96338 | -50.80367 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| facdcf61-29d6-316b-bc02-13e38fef0b51 | -8.95151 | -45.73288 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ae70fa65-99d7-3f5d-95bb-e620f78514f1 | -7.38375 | -46.51326 | 2026-08-28 18:49:00 | AQUA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8a3ca732-c9c5-33d6-b4bc-84906f7b6969 | -9.42331 | -50.44595 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| f93ba64e-6680-37eb-a459-b82898fe3dbe | -11.22192 | -39.98251 | 2026-08-28 18:49:00 | AQUA_M-T | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 432fd6f4-b34f-35f1-aaa7-693cc46cac1c | -9.6937 | -46.57835 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 2b2ba79c-24cd-3df8-96f9-f557cfacedb8 | -13.02115 | -47.1161 | 2026-08-28 18:49:00 | AQUA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 61c68fae-5c0e-3744-b1bf-e19f5999c960 | -9.15734 | -49.9762 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 209.3 |
| a234a44a-f090-3ef0-9271-dd2d5cef3d64 | -11.78865 | -44.92942 | 2026-08-28 18:49:00 | AQUA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 8b49834d-b96f-36bc-bff2-74d939a7d5bc | -11.35082 | -43.51091 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 92a57578-0a12-32c5-983f-1211269d2672 | -11.6086 | -50.21612 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5bd79d5c-2638-3cc0-8202-ab7a84527972 | -8.58888 | -54.78137 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 417.6 |
| 1190ebc4-e6ef-3269-820a-1973e1bfea12 | -8.09587 | -47.5888 | 2026-08-28 18:49:00 | AQUA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bb9743ad-ebba-3f70-8f4b-b437f8ffe5f0 | -11.80074 | -47.67348 | 2026-08-28 18:49:00 | AQUA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 0f7e5a85-b848-3aa3-9c6b-cc2e2d0838ac | -11.01868 | -49.68657 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f769623c-b6c6-3fd5-90be-86d55ef256a6 | -8.07268 | -45.85567 | 2026-08-28 18:49:00 | AQUA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 896fada1-1615-32cc-b48f-86d72a5a8d2d | -9.79558 | -43.55602 | 2026-08-28 18:49:00 | AQUA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 5cbffe6a-d960-32ec-982a-a6598b823fab | -9.48344 | -45.64159 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 291.7 |
| f53b7c98-bc82-361b-b3b4-f849349c4172 | -8.05502 | -45.85833 | 2026-08-28 18:49:00 | AQUA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5ec8fc30-ba3f-3fac-9713-079fcdae90f0 | -9.43997 | -51.70094 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 84610ed0-64b5-387a-84e7-88ed21406e9d | -11.69966 | -47.61563 | 2026-08-28 18:49:00 | AQUA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d96d85b2-e33a-3afb-ae11-93365572c341 | -13.87994 | -53.24374 | 2026-08-28 18:49:00 | AQUA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 2aa8aac2-ca8c-3c59-b574-452422f4752d | -7.31367 | -42.96503 | 2026-08-28 18:49:00 | AQUA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| fc203f5d-cea1-3912-b8e0-8d46a945e4ee | -9.83946 | -46.16716 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb4d0ae6-6d1e-37f6-ab64-9f0361ee0dc3 | -11.96601 | -45.4929 | 2026-08-28 18:49:00 | AQUA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 00bcc400-f289-38ba-8c4d-36ce581656cd | -10.313 | -49.98628 | 2026-08-28 18:49:00 | AQUA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 44116d02-7514-3768-90ba-28bbb9f3f1d7 | -11.4928 | -46.94253 | 2026-08-28 18:49:00 | AQUA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 108445b6-4eca-36b7-b320-ccc389fd2580 | -10.07264 | -48.69269 | 2026-08-28 18:49:00 | AQUA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5c248162-ffdc-3f99-a68f-b9e9f8a9a1f8 | -12.35562 | -50.58168 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 313.8 |
| 6e9000f8-cff2-3835-b3f9-93119ffca9f9 | -9.722 | -45.82049 | 2026-08-28 18:49:00 | AQUA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 08b78436-c6b4-3476-a2ab-53c95f59d710 | -12.75979 | -44.26255 | 2026-08-28 18:49:00 | AQUA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 562a2454-566e-39f1-9dfc-d6a20e6ffa25 | -8.76889 | -50.49272 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ef9745db-3670-3f5e-9726-f4dbc374d6f8 | -9.42741 | -50.43732 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| cedad866-e94a-3987-8a6c-1c851f790931 | -10.08213 | -48.69152 | 2026-08-28 18:49:00 | AQUA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 8b1d919a-f180-3698-8eeb-45161c2181be | -9.95135 | -45.99983 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fc4e79d0-4380-366a-bd9d-0a65ce961bf5 | -11.20485 | -51.26059 | 2026-08-28 18:49:00 | AQUA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 4ca1bdee-ecba-39d3-a733-e6beb323797d | -9.68134 | -47.89099 | 2026-08-28 18:49:00 | AQUA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0b8e6aa7-9c19-3caf-8246-1ce3cbde4cd0 | -10.02646 | -45.81845 | 2026-08-28 18:49:00 | AQUA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 21c67b08-8ff4-31e4-a2ab-af3b995f74da | -11.21644 | -51.25903 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 292.9 |
| 84d5c5fe-7d73-31bd-8cda-1b1d72798154 | -11.95725 | -45.49426 | 2026-08-28 18:49:00 | AQUA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 52da244d-c226-3c51-9084-4df4166182d1 | -10.32842 | -45.36361 | 2026-08-28 18:49:00 | AQUA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fd27c87c-160c-39cb-8e92-fc8066524c32 | -6.81818 | -43.87937 | 2026-08-28 18:49:00 | AQUA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 88aafea2-4c25-33c0-8928-cbe542ca2860 | -8.95083 | -50.79205 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 0b9d6a99-a1ec-3818-a433-890385696b9d | -8.82114 | -49.62649 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 68348b06-8c42-32a7-a13d-f62067dae0bc | -11.60368 | -50.20834 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 9018c2ea-1f19-3506-b82f-bec6468ac09a | -8.05369 | -45.84939 | 2026-08-28 18:49:00 | AQUA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 47806ca1-0141-300b-800d-2a2084f031e0 | -11.80881 | -47.21816 | 2026-08-28 18:49:00 | AQUA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 09f6c8cb-7934-377b-b535-c2a061e95811 | -13.31906 | -46.93621 | 2026-08-28 18:49:00 | AQUA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 37fca18a-d1ab-3df1-b669-f9a4d600d073 | -8.32545 | -45.68768 | 2026-08-28 18:49:00 | AQUA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9419a9bf-e195-3e75-b2f9-12dbe7ddfa5a | -8.02085 | -48.02571 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8bfbad6a-0f24-35db-b2f5-50c937bb2114 | -10.32506 | -49.99746 | 2026-08-28 18:49:00 | AQUA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 81e30e3e-d6c5-30f9-81bf-786658f96702 | -8.46763 | -47.66641 | 2026-08-28 18:49:00 | AQUA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ed550f68-1b6b-3eaa-a802-ee3c65224809 | -8.87118 | -46.01216 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7eb1fc4a-2258-346c-a7dd-13690b208321 | -10.64018 | -40.50913 | 2026-08-28 18:49:00 | AQUA_M-T | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 3e05997e-eaaf-3a8e-bde7-7c1248e55b3e | -10.03032 | -40.17897 | 2026-08-28 18:49:00 | AQUA_M-T | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 439b3b46-fc61-38c9-aaba-765b448afcd1 | -10.45834 | -46.18055 | 2026-08-28 18:49:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| cf15ecf9-68a6-344f-a0e6-84e0bc970c21 | -9.41505 | -50.42578 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ab1a01a4-42e3-389e-9dfa-ea75f32268d1 | -11.35242 | -43.52129 | 2026-08-28 18:49:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| df5a1e54-b6d3-31d1-9a09-c79fa9f25957 | -11.16203 | -45.06092 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5c9ad925-b4ad-3717-ba25-666c2d25c933 | -8.66741 | -49.53968 | 2026-08-28 18:49:00 | AQUA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d43228cc-8e9e-347f-b804-466d38dbf5a6 | -5.98105 | -44.97689 | 2026-08-28 18:49:00 | AQUA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README165.md)
