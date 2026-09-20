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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2ec9671-15d4-3410-ae7a-56552020248c | -11.00947 | -48.32099 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad767d73-52cd-34f1-b472-272a7dddfcff | -11.23855 | -48.38368 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fffab01d-63a1-30da-9bbf-3a25ab5dff84 | -11.86108 | -47.67206 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f08ca546-e1a0-3b6c-8cbe-d1c4979c9419 | -11.00812 | -48.31603 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f47d876-9b1a-3163-a26c-2e0f688231de | -11.4529 | -45.37406 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 296c95b2-6733-3283-862c-a4292a8b4ffc | -9.23833 | -46.22801 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4774ee97-d2eb-3fae-bd04-73722600dfc6 | -8.75838 | -48.66715 | 2026-09-20 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76842b57-b7f8-3fa1-958f-3136bb085276 | -11.06457 | -44.68426 | 2026-09-20 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b437f416-12cb-3e46-ba8e-50e1a0aa3452 | -12.75809 | -46.12517 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dc297a0-5338-3d17-8b99-5bf393849f9e | -9.69258 | -48.31663 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55535d94-64d7-39b1-8eac-cfc14e91a595 | -12.16257 | -47.02946 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4d7c824c-3b6d-31b9-8879-2e56a78280f9 | -11.02958 | -48.30618 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d20dd0f9-64b1-310f-a702-c4230b8721bc | -9.81241 | -48.33002 | 2026-09-20 03:45:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fc8f0b0f-d84f-3cd1-971a-b589facfee9e | -11.47074 | -45.33535 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a33e866-e687-3239-9ed2-c255e5be69f1 | -11.0709 | -49.498 | 2026-09-20 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4816544a-38fb-3469-a2ed-046aabf2a17f | -7.76427 | -49.19839 | 2026-09-20 03:45:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f5e05aa3-c7bf-3166-acf1-3a2558fd749a | -12.34097 | -50.68945 | 2026-09-20 03:45:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d747c1-6c4f-3c2a-b061-a532d0e27e53 | -7.43278 | -44.74146 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d762b71f-8728-38e7-979a-b7151be1721c | -11.85487 | -46.86676 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b4369758-c3c4-39f3-a901-7f0ba3f08742 | -11.22038 | -48.36544 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89b73a10-b6aa-3027-b3c5-a58bf177458d | -11.87135 | -49.00297 | 2026-09-20 03:45:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4cff37b2-802d-3574-8361-fb99dd859006 | -9.02372 | -48.78292 | 2026-09-20 03:45:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dabe7f3a-49f0-3c5f-bfdc-0e56a59bc71b | -8.04649 | -46.25749 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3fad2a30-7e52-380d-8073-f9292b20a3a5 | -8.49962 | -47.4352 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| fcbdf2c5-1765-3df3-a64c-dd177d37f80c | -6.1702 | -47.49369 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aecefb5-310f-3add-9990-d2647efa9bca | -11.08843 | -48.30345 | 2026-09-20 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb7ebe1b-9d86-33c3-8618-e687b6d6068c | -10.46204 | -45.08338 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57d951d6-4adc-33e2-a392-6ecbeed067e0 | -11.49443 | -47.79184 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36061c45-546f-3466-a3fa-1a0f03637901 | -10.3066 | -50.23638 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 18ec19ae-9827-3b98-95bd-0eafeb1ed8bb | -11.44682 | -45.32116 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b39e4c42-d033-39a7-9cfb-59da276a76d8 | -11.86377 | -47.65843 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8dd67ac-9c65-3abe-a2f3-94ed04257911 | -11.85076 | -46.87346 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da05cb20-6830-31cf-980c-f0266d9dafb0 | -6.95393 | -43.09518 | 2026-09-20 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56c0be8a-9c3e-364b-a834-3665944ea7f2 | -7.87389 | -44.87664 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cfdb90f-072c-3e2a-bd92-8b5110e50bdf | -6.92099 | -42.91259 | 2026-09-20 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ee7043e1-9dab-3cab-a6ee-0db483f62737 | -13.03089 | -46.91212 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b429e590-df1e-353e-bcea-d29d4762afc8 | -10.31924 | -50.21002 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 521aa997-d192-367b-a946-01d4e049d6de | -11.32244 | -44.17938 | 2026-09-20 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c080d8f-343d-3e42-8604-4f114f5d68f1 | -11.45231 | -45.37726 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea2d4467-ec7d-35c2-8754-6c639d4188c0 | -9.79314 | -45.06126 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 761dcdb2-8613-3cf2-a592-2a60670e62e2 | -7.76776 | -44.83422 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6eef815b-cd82-38ac-8012-dd4f16aa6127 | -9.81013 | -48.33306 | 2026-09-20 03:45:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2de803f7-bf00-3c6a-a9f8-6b232e6a6953 | -12.16177 | -47.0335 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0b42d877-eadc-3d5c-b81b-e317e67a336d | -7.36193 | -44.87284 | 2026-09-20 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b55b4f6e-76fa-3829-870e-0fa711d19950 | -12.42375 | -45.07384 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8ff26e0-7c38-35c7-ab0f-52d86d039517 | -8.76077 | -48.65475 | 2026-09-20 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b390561c-d7db-3127-835d-eebb010a8af5 | -11.31698 | -47.28892 | 2026-09-20 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fdd4f07-f98f-3cbb-9933-8c039a9b231b | -12.12585 | -47.02353 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e21b12d-0091-33bc-95ba-e972457f1385 | -8.04342 | -46.27436 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c561bd1-ab5d-3072-adbe-03fb128784e8 | -12.76208 | -46.13276 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bcfada04-c176-3e38-a615-ddbf21ae9ddf | -9.12096 | -45.7225 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be5a4d50-4a46-39fa-b733-b5ec3c67ebeb | -11.63166 | -47.77024 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eef4fafc-ed96-3539-86e4-fcc34d37c884 | -6.61254 | -43.75256 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ed78af6-6229-35ef-a035-2b3321c597ac | -8.66203 | -45.43782 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84bc3cc8-f423-3807-a2f2-d24866da69b4 | -7.49009 | -46.70835 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72e07bfa-fe42-3208-a16a-26f7fc2e4e79 | -11.28697 | -41.99911 | 2026-09-20 03:45:00 | NOAA-21 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bbf9f457-8ecf-3d50-823f-566f1cd57992 | -7.55161 | -45.44355 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5820f6c0-085b-3c97-957b-77626dec3f5e | -11.03693 | -48.31319 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3ea9d5e-7dbb-3cea-a614-653c550b351d | -7.18081 | -47.89983 | 2026-09-20 03:45:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d52dcb6b-73f2-3df2-9bf1-71cb3a3a1085 | -13.02298 | -46.9199 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a556e7db-fe6b-31ed-adc9-9fffda179736 | -9.781 | -45.06897 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afb6e581-42ce-3eaa-938f-f32260a025d7 | -10.13104 | -45.5527 | 2026-09-20 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 08c54a5d-42cf-39da-8202-7fa4d3e18562 | -11.79299 | -49.83077 | 2026-09-20 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 667d3565-50f6-38b3-9595-da8a4bc059e1 | -8.87374 | -45.94714 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1cf8def9-2e5c-3b81-896c-fd1b438f5773 | -11.44562 | -45.32755 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e29c3c53-6339-3bc9-bd3a-5b7ec53a0069 | -13.03442 | -46.92015 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0a396b41-1066-34d3-90b7-e1f1b815e74d | -9.96495 | -46.54504 | 2026-09-20 03:45:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f1308e8-167b-3dda-a760-c061bde81517 | -13.03564 | -46.91721 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3dfa41b8-262a-3c61-87c4-844bd55e4c98 | -13.02971 | -46.91503 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2021b5a7-05fc-3f82-9d46-92ef43c3e0de | -11.15145 | -42.79422 | 2026-09-20 03:45:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 32cc494f-a20d-3d15-8a7f-87cdbea56c77 | -9.23106 | -46.23564 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a03e311f-b697-33a3-a46a-fc35434d0d5b | -12.35013 | -50.69095 | 2026-09-20 03:45:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05d54e6d-9892-3f63-9121-d76a3dba8022 | -11.39869 | -41.88655 | 2026-09-20 03:45:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 605a5e1f-c315-329a-9ff9-f4a11d77b696 | -8.43472 | -46.8418 | 2026-09-20 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3313b0dc-409f-3ee9-a260-dd9d34b049a3 | -9.12716 | -45.7196 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a45de0ef-ad3d-3f5e-ac8a-9166f3540a6c | -7.43632 | -44.75229 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6c3a053c-abc6-38f8-ac25-5eb780ed99f3 | -9.79715 | -45.06878 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 334b332d-17db-335d-a84c-2b873529b550 | -11.44839 | -45.3412 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed6ba12e-069f-30db-97e1-433fe60529da | -7.75612 | -49.20361 | 2026-09-20 03:45:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| da90fec8-6f7a-381e-9a42-dbd153a2758e | -12.75811 | -46.13027 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4df95c40-f01d-3c30-bfce-dbd0dc8a31de | -8.6681 | -45.43534 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 551774d9-e97d-39d9-b950-7f4d7a157c55 | -11.4879 | -47.76204 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84cc2a15-0840-3c13-bcfd-acde870c4de6 | -7.44107 | -44.75631 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00a835f7-32d3-3ce5-831c-d44ba1427f97 | -11.00185 | -48.31496 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73b28335-528a-3306-ae82-0937186c20b1 | -13.27653 | -46.73289 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bb77b50-ad31-35b9-9b97-86508e26b4bc | -11.03265 | -48.30186 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0cf416df-fe1b-3bce-8b25-af3c91723fdc | -11.0111 | -48.31268 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d92239a1-3e45-349e-a96a-8808a9ca194a | -10.85953 | -50.17903 | 2026-09-20 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0dfee23-34c3-3bed-bebc-b1fa6b6360e5 | -6.97244 | -42.58099 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e5a74a2e-9e26-3672-ab0f-afbe92e0683c | -9.25829 | -45.93312 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0ac00daa-df22-31e4-a326-325d7f7218c0 | -7.43514 | -44.75891 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b4ad1e75-1ee6-3907-8bb8-112a4b5aba8a | -9.1258 | -45.72708 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| cc3b86d0-4181-3c7b-8eb6-f97cea757a29 | -11.85782 | -47.65745 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69f8034a-6237-3243-b1cf-d048ab027178 | -8.75956 | -48.66103 | 2026-09-20 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0e649ec1-6256-3be3-b5f5-74df8806ba11 | -7.55354 | -45.43271 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9347d75f-1895-3fb7-861c-6ec70dbbb476 | -7.62306 | -45.42425 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b823f9d7-c0a9-3326-a0df-175031926593 | -10.31084 | -50.25178 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 88fa7800-1d1f-3c8a-a1bf-0c69bfd4b259 | -8.4396 | -43.86414 | 2026-09-20 03:45:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 351b39f6-c80c-3ee7-a4c8-1bc61a296322 | -7.39863 | -47.77578 | 2026-09-20 03:45:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efffe98e-afd2-3b13-897e-840f63ab5321 | -10.41643 | -48.33264 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
