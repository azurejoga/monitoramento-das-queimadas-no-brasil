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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9c614b1-5217-3606-8cfd-1aec2d20ca4e | -12.64883 | -47.9416 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 541de66e-e73e-3a0f-ba5a-80d9d76249a6 | -10.6352 | -44.21157 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 984039c1-8a44-3044-a413-aa215f7622c1 | -12.6405 | -47.92878 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f589bf60-73a7-3efa-b1ca-dad5400bd87e | -10.03023 | -45.29976 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98877a07-9865-356b-bb59-1a74d182c8d0 | -17.40626 | -42.51867 | 2025-09-15 04:21:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d4ba4a9-b197-3d2b-8684-9f598a835fc6 | -14.48873 | -47.34693 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2e5bb94-d2e5-397e-97b5-894efad2b3ba | -13.87988 | -48.12762 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a476932f-430d-3d61-ab88-a2a2642bd1d4 | -13.88335 | -48.30461 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00fb436a-a847-3361-b536-7d3d0c3f1d96 | -11.08169 | -49.71148 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ff50fc8-94de-3992-b1fe-52c378f58be2 | -11.86616 | -50.52458 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 4abcd542-d2d9-3ad5-988c-4594a077c166 | -10.75087 | -44.70286 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6228baba-4ddd-3378-980b-07442b7887a2 | -11.45613 | -43.56665 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b1853b9-e5bd-3478-b400-42afc50d094a | -11.33862 | -43.49406 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90398a83-6137-3a37-9a4d-5eba09dc12cb | -11.06899 | -49.71861 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c82eea5f-a0f9-3474-b82e-db3c00ed3369 | -12.59258 | -45.70606 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a97dddcc-6ddd-39c6-baca-f7d35e65a3ed | -9.11805 | -46.9337 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d8fcd67-88fb-31ef-a6cc-6aa0cd0f438b | -11.47121 | -43.585 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f5495a7-2480-3995-b231-c17eff9473c2 | -12.67647 | -47.73031 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c7195bf5-dfad-3965-a67a-7648ceefee0d | -14.93203 | -46.56426 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac6a2687-94ba-3c0d-87bf-5ead5e119b06 | -12.51171 | -44.76493 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c6de46a-6fee-31a2-b733-984098b6cb14 | -10.63237 | -44.20738 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19b92af1-d487-3bb5-b3d1-b93599f8eb83 | -11.80946 | -50.43921 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6361c82d-ffac-3028-a572-ee8ddc57922e | -10.93447 | -45.49793 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6224bc47-083f-31a4-b18a-a4b2f12ef09e | -10.89221 | -45.5521 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c183615-0fb6-38f5-951f-a200e1abedc4 | -12.78044 | -47.97399 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e14fd01-cb12-3139-a8f2-2e4ccf655dec | -11.08311 | -49.7257 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf8a0f35-6334-396f-8005-eaaf43643f29 | -11.47178 | -43.58109 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 400eb322-63f6-3f5d-90e4-029b37cb156d | -12.0113 | -46.65955 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b85a9d5-cce7-3057-ac78-818a7c93c8e9 | -11.43381 | -43.53583 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec49ab94-b6c0-3e24-9f2d-0dd822545a8d | -11.4596 | -43.56719 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5260ea5f-6771-3a5e-8ac4-5569821ad121 | -14.43504 | -53.36331 | 2025-09-15 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dc7b8bce-3755-3706-a3ed-2cbb369952da | -16.28658 | -45.67917 | 2025-09-15 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e499ecf-b3fb-3be1-8e2f-a8ef2f345d92 | -10.91808 | -45.55981 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5cf9c73-3adb-3bc2-afe1-87c89a5838f6 | -11.45753 | -43.56739 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b84c1265-04ed-37c6-8025-b24cbfad763a | -10.90135 | -45.4497 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ff3933e-2598-3077-9b6e-8efc49789127 | -12.59811 | -45.71418 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf3ccb8d-9211-3032-a15a-b8c5797b54b3 | -22.17537 | -49.61587 | 2025-09-15 04:23:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42154df7-43ba-31d4-8825-f95dfaca72e5 | -20.10312 | -43.19716 | 2025-09-15 04:23:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b0413d86-1c19-35f3-8c9a-1b432a508073 | -18.47704 | -46.94321 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5259a6d3-5357-3ea1-810b-9ab53b6222f6 | -17.91496 | -44.4472 | 2025-09-15 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8b26dfb-65da-3315-ba8b-0e4a72040da6 | -21.92467 | -46.56476 | 2025-09-15 04:23:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8881767f-e0fe-3cec-8934-69e6e81e3fe9 | -17.14626 | -48.51855 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64cc8e72-fa8f-315f-9122-e328a1b26b30 | -20.76046 | -56.94172 | 2025-09-15 04:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6237828b-1640-387e-b78a-434677916efe | -21.11982 | -45.95388 | 2025-09-15 04:23:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1ec7d5d8-eb14-34e4-b428-fef2de423ee8 | -15.79822 | -53.50759 | 2025-09-15 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9574d77d-6a3e-343c-9089-4211e93a599a | -18.62 | -50.39814 | 2025-09-15 04:23:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9d42a4c4-368f-3879-80d7-aee89abc71ab | -22.21012 | -48.35269 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb4c11ad-82df-37d0-9d43-37378322b322 | -22.29906 | -47.95204 | 2025-09-15 04:23:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8320dbc8-b906-3e6b-b494-b7e568e3b754 | -20.04743 | -46.16046 | 2025-09-15 04:23:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adc0311e-8fc6-3f54-a2fe-b2ec4483b35c | -19.25234 | -45.99729 | 2025-09-15 04:23:00 | NOAA-21 | MATUTINA | MINAS GERAIS | Brasil | 3141207 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 784bace4-22d7-3db8-9e1b-cad7a5592011 | -18.71581 | -44.27398 | 2025-09-15 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81247481-07c8-3e9d-9395-3c05f0f17086 | -18.47373 | -46.94267 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71dd12a9-7f61-37d5-b3d9-1dccfc6f50be | -20.93843 | -47.01588 | 2025-09-15 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 901ba1ba-0296-330c-90fd-c51421e2e8a3 | -17.14686 | -48.51488 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78f38e52-fe11-3952-9293-338343b03e3b | -16.66775 | -49.77251 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5d04560-a6a1-3fdc-b2b3-1b33863ec167 | -21.26346 | -47.0068 | 2025-09-15 04:23:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c527ca64-0ee9-300e-b665-e5f3c130a22e | -17.29801 | -46.1123 | 2025-09-15 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30a5a49f-3305-3fc9-818c-bca642c7568f | -18.58096 | -48.15185 | 2025-09-15 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ab03f5f-af61-393c-8848-8c0874f03e4c | -19.72091 | -45.44199 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e64a657-0933-3f68-817f-574f8f38f759 | -18.61649 | -50.39749 | 2025-09-15 04:23:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7ed98425-f139-3169-b2c3-71f21f86d31e | -17.06649 | -49.67709 | 2025-09-15 04:23:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae361b6a-f4dc-3588-9a69-c01712af16f8 | -15.79762 | -53.50777 | 2025-09-15 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44f0d44b-72ff-30e2-b8a9-8e9c7657f097 | -20.74229 | -56.74905 | 2025-09-15 04:23:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd086022-caeb-3e36-88b1-559dedfe6f05 | -18.26676 | -49.46643 | 2025-09-15 04:23:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cadad660-83c5-39ea-b6b2-76ce3b0b9fb5 | -16.70656 | -54.94713 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f0cc0e8-592a-3282-a219-e88085c21f85 | -18.62835 | -47.3304 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a77b7d8d-b1c1-3814-bddf-c1eed58b53ee | -22.77848 | -47.1242 | 2025-09-15 04:23:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7fab1ff-5fa9-374f-89ff-72fce280783f | -20.08901 | -46.884 | 2025-09-15 04:23:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ab856cd-8685-3932-8409-8fd1d7d7bb12 | -17.3511 | -46.66092 | 2025-09-15 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b129076-8e9b-3715-9b1d-02389024089f | -20.51352 | -55.63655 | 2025-09-15 04:23:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fbbc80d-27e7-3dcf-9a33-735a19c28995 | -17.24565 | -49.47055 | 2025-09-15 04:23:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25aeabc7-1119-395a-9a1d-bc2102077e16 | -20.76071 | -49.68135 | 2025-09-15 04:23:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32b50685-196e-3e20-a5a4-e98c16560b1a | -16.71118 | -54.94855 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50a46388-2435-3c1c-8278-9d6121cfdbca | -19.71686 | -45.44545 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d156ef1a-a067-30c3-9a8f-33f2c8a8554e | -16.67397 | -49.77829 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 135dbf37-376a-385a-ad9b-a945e995d0d9 | -17.73114 | -47.95266 | 2025-09-15 04:23:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac117512-c51f-3c30-9e7d-170fd9f93ae2 | -18.1391 | -49.19601 | 2025-09-15 04:23:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3f41db62-42d5-33e3-ae5e-a1fb9675173a | -18.59716 | -47.20188 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23f0b8f4-6266-3a79-8b1a-80f8d55d03ad | -18.48368 | -46.94433 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2788d84-bce7-3feb-b1de-5d3bec9b9e39 | -19.71628 | -45.44949 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13204e12-59d5-3f23-8562-81a986122e96 | -17.76427 | -44.51474 | 2025-09-15 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d4a5271-4b67-3fdc-b5f3-9b339026aaf2 | -20.52618 | -47.47797 | 2025-09-15 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5452b62b-e13b-3f2f-9e11-303e660aa5f3 | -19.72496 | -45.43854 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7f85768-c52b-35aa-90ee-919c631c5a61 | -20.93604 | -47.01565 | 2025-09-15 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d027cc38-2d82-306f-b9db-37699febca9b | -18.59329 | -47.20495 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b26f9256-c436-318c-80d3-dd8435140454 | -16.66845 | -49.76834 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3cdc8bd0-67d0-393c-a96d-f98b6a11bf4d | -21.9258 | -46.5569 | 2025-09-15 04:23:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d677c541-f301-3c22-ba67-32f76fe699c1 | -18.71519 | -44.27839 | 2025-09-15 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f038513-dab8-3267-bb39-2b8e130c6fbb | -22.20624 | -48.35581 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9565e3bf-f7a8-3dc8-9ac7-090445d3ccbd | -18.96305 | -48.21044 | 2025-09-15 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03072daa-9b0b-33a6-a030-0df3b47ccf5d | -18.79106 | -48.54097 | 2025-09-15 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7eb3d9e7-4ec3-3e50-90fc-1400e28efdf1 | -22.19963 | -48.35462 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 535756c0-41be-3c87-8f4a-2f51ff7fd237 | -20.53002 | -46.86295 | 2025-09-15 04:23:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b618c13-b350-33df-a2ba-62f81f20a86b | -22.21615 | -48.35759 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04569668-db59-3c83-9f9f-3e07211ffe4f | -16.71591 | -54.94941 | 2025-09-15 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbffa443-56fd-3467-9255-7432701c3ac7 | -18.03882 | -46.96392 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f6ac953-4fde-3b1b-8534-94e82acb732d | -20.23698 | -46.18199 | 2025-09-15 04:23:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21dceae8-61bd-3223-98c0-8d561e69fd20 | -20.32582 | -43.67948 | 2025-09-15 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9a895779-d589-3e02-8d2c-43fea9f06e99 | -18.16214 | -49.2039 | 2025-09-15 04:23:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ae34358d-4e58-36fc-971a-21a7704bfdd7 | -20.32743 | -58.08652 | 2025-09-15 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README35.md)
