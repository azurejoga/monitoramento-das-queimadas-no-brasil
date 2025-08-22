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
| a4f25dec-df06-3036-8ae3-417527c88903 | -7.02358 | -44.63024 | 2025-08-22 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ac17b65-4ac0-3929-b91d-abc318948ab4 | -7.60731 | -44.37809 | 2025-08-22 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b7dfe40-8cea-3e77-90e3-9ccaee8ad0df | -7.6387 | -45.23954 | 2025-08-22 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0019e301-1c65-3b96-86d8-773e6f06e52e | -6.94999 | -44.55656 | 2025-08-22 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2712739a-ed8c-3ff4-93da-1bd9d232557d | -6.93829 | -44.28717 | 2025-08-22 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 020cab42-c62c-31f1-bbd9-d9febe029799 | -6.50934 | -44.58503 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0969c061-efe4-3db2-9dd9-a4eafc27b682 | -6.93732 | -44.29259 | 2025-08-22 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6bd349e0-121d-378b-b60c-9ca45e6423bb | -6.04059 | -44.36631 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4dc4fd76-4b39-3d10-ae7a-07129d5a7346 | -5.79439 | -45.07182 | 2025-08-22 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ccca796c-63fb-3139-93ec-3e84636fce1d | -3.81741 | -41.57863 | 2025-08-22 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa115f0a-9f36-3c74-9c8f-d9301f644a38 | -6.03315 | -44.37035 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c239ad9a-7073-3fc6-9f3b-890ba8aab306 | -8.49963 | -44.73858 | 2025-08-22 03:30:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5516da2b-f8fd-38dd-902b-a59dc1cb5cca | -5.14115 | -45.17253 | 2025-08-22 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2200638-88b0-3554-becd-cd004a4b7f2b | -6.94638 | -44.29117 | 2025-08-22 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b137244-82fa-3b94-b8e1-8b68d4677921 | -4.39688 | -44.09159 | 2025-08-22 03:30:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d381e859-f681-3199-9935-293b3bfacd48 | -6.04035 | -44.36659 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7e4764a6-b3c3-3a33-ba21-0ff8376ed594 | -7.09626 | -43.69054 | 2025-08-22 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 43d90a84-86ce-34a9-a237-5bfb03c29df8 | -6.29219 | -43.70166 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d9804ce-cfdf-3814-90b6-3ce9cf99ac9f | -3.81871 | -41.57091 | 2025-08-22 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 391ca7e4-0976-3f19-8db4-b7ff63765b76 | -6.48817 | -42.85819 | 2025-08-22 03:30:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dbc8e17b-6d51-3294-aace-54cac385cf58 | -7.65202 | -45.24179 | 2025-08-22 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5204a97-95ec-3546-a800-928f759c95b4 | -4.65601 | -41.41348 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a78cab9e-9e6e-3bfa-801c-f0f8df3e6d77 | -5.14081 | -45.1724 | 2025-08-22 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 44aef788-ea4f-3e64-82cc-b17a603994d4 | -3.9824 | -43.24159 | 2025-08-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d668cacc-27cf-372d-9366-2506a49040ba | -5.70223 | -43.5362 | 2025-08-22 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 674d8719-8349-32c5-a19f-0cddd1d6f209 | -4.64009 | -41.40564 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae02fbb5-57c9-3ace-b288-25752e5d0832 | -6.41965 | -44.23804 | 2025-08-22 03:30:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e275a341-2461-3fa1-bf20-727a4435edef | -6.42674 | -44.67336 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bd961c4-95ea-3168-b7b9-843adaa3cead | -5.45292 | -43.58591 | 2025-08-22 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 275b36de-d86a-36b2-9ac3-1e951d110352 | -6.41928 | -44.67723 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff0531e5-1496-3b6e-bdfd-5520eaf1c09c | -3.81806 | -41.57476 | 2025-08-22 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d27d7d4d-bc34-3b9d-b766-71bb3c6c5c6d | -6.29162 | -43.69851 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73825b23-acae-3bb3-9743-9bfda44135ed | -4.65038 | -41.41166 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b5ee2d38-0417-3757-9a05-21062625053f | -5.455 | -43.58464 | 2025-08-22 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2ec1295c-fd86-30f2-85b0-0cc66d6c4d2e | -7.0373 | -44.62842 | 2025-08-22 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9cb9bc48-0de1-34ba-86f4-b3ce5893ee90 | -5.79124 | -45.0772 | 2025-08-22 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cb6e6fbe-9b83-3f03-a715-d74089580dc8 | -3.63032 | -43.54879 | 2025-08-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d15c8d6d-09a7-3562-8300-e55327d2c9dc | -4.64093 | -41.40274 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01a59a2f-f748-3aaa-a200-b8b784e04f0e | -8.67618 | -36.23139 | 2025-08-22 03:30:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 46041d1c-a625-3d7f-b7ff-79d426a508a1 | -6.94344 | -44.55589 | 2025-08-22 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 666253a6-883a-37ed-acc3-63e95e211f6c | -5.37441 | -36.7606 | 2025-08-22 03:30:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c81f358e-1f95-3ee6-bb4e-5d436dc1f702 | -6.50834 | -44.59048 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 6fbf1884-9bb4-3a9c-a2ea-1ea805f5b6ed | -7.63413 | -45.24339 | 2025-08-22 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9f2cf162-1980-367c-b10f-f658b2af645c | -6.29128 | -43.70681 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee589bcf-caac-39da-8e03-5fb9051ac0fe | -7.27036 | -43.67049 | 2025-08-22 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f5dc99d7-eb61-32fd-895f-5f20bd3f9b9a | -7.09538 | -43.69531 | 2025-08-22 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff5e6d23-d06f-3d50-b451-8c05a9170aca | -7.17051 | -44.66813 | 2025-08-22 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ab60540-ba1e-31f6-b4a2-c9aae1d44eaa | -7.27046 | -43.67335 | 2025-08-22 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2341d824-0f58-3f62-9a12-7ecef98bda5e | -6.58346 | -44.72847 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23c07dae-1b90-355c-8281-385835d7533f | -6.30147 | -43.89029 | 2025-08-22 03:30:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c23f138a-7141-398c-b947-993021cc7711 | -7.2713 | -43.66882 | 2025-08-22 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63855d06-12f3-3bba-9d82-d0aee7d7dac3 | -7.1492 | -43.23342 | 2025-08-22 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7a13e2e-3ecc-3ec6-b53b-4400ee1bc6a4 | -3.62912 | -43.54626 | 2025-08-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| acbb9b5c-fd45-3d9e-b517-cc59cbc764bb | -6.7368 | -43.13357 | 2025-08-22 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7543506-8019-322e-9ae3-af50d08b8867 | -6.94108 | -44.2844 | 2025-08-22 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 927acea7-ae5d-3a73-afd3-5a6dc678c905 | -5.87367 | -42.41006 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a8c7ae45-c6f9-3357-88c1-3fa7db15b536 | -6.29069 | -43.70354 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f0f1f89-2d7a-3afa-9c09-16151c2d609a | -6.42575 | -44.67886 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c62b7716-8de4-3869-a8e7-00b28b24bbda | -5.87942 | -42.41103 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f5b6f0af-0bef-3a2c-b521-d035bf627da4 | -3.9863 | -43.24434 | 2025-08-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b17209f8-9b1e-3452-a125-029607c74eb0 | -7.14056 | -44.17519 | 2025-08-22 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7aef242-1ef7-3758-9b15-2db6fe6f1ce8 | -6.44036 | -44.52272 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6df0b7a0-a844-33a0-9411-7773580e69a2 | -4.72507 | -38.3963 | 2025-08-22 03:30:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 60decc5e-4f1c-37d6-a2e2-f5b963e185f9 | -6.94456 | -44.28879 | 2025-08-22 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b1268c0-b73f-3582-93e1-537bd5125465 | -7.61356 | -44.37962 | 2025-08-22 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c390136-2b43-3ffc-962f-607ac479c823 | -7.63748 | -45.2459 | 2025-08-22 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 64f85b43-ae0c-3918-a8e5-10a21f264f97 | -6.50502 | -43.43005 | 2025-08-22 03:30:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5bfa8dc7-9935-3fb4-9915-8961a2fa6979 | -6.4359 | -44.5108 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3731f31-8ea0-3db4-a97f-905fe99b505c | -6.29945 | -43.90138 | 2025-08-22 03:30:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9866a87c-5bce-329e-83fc-ed892e78314f | -7.94238 | -42.66237 | 2025-08-22 03:30:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca54588b-8ede-308d-96df-ea81a5bb4f9f | -5.24596 | -37.69671 | 2025-08-22 03:30:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 455e7fef-cb60-30e6-a881-aae894afab31 | -7.37381 | -35.11224 | 2025-08-22 03:30:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| abbf558d-2def-3df4-a930-f0239db35d95 | -3.82064 | -41.55951 | 2025-08-22 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| da36178d-a930-3337-9e45-507331edbc1d | -3.98782 | -43.24748 | 2025-08-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28a2c292-3a85-315d-b7fd-aed99267b811 | -4.72331 | -38.39547 | 2025-08-22 03:30:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3c32f0ee-7a42-3cb1-858b-54e207d05c1e | -7.07649 | -35.26881 | 2025-08-22 03:30:00 | NOAA-21 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ee44c3e-11ab-3844-934f-1ac43143d9e6 | -6.94011 | -44.28961 | 2025-08-22 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2434f3bb-76ba-306b-8ee8-62ac517feb4b | -6.49402 | -42.85923 | 2025-08-22 03:30:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fa236d7-c19f-34a6-a25d-805d0c698a60 | -7.37317 | -35.11619 | 2025-08-22 03:30:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f50e50ed-dcce-3a3f-99cb-71c651e7e7f6 | -5.87488 | -42.40929 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4e103cfc-05df-3266-8600-49a2d2bec99e | -6.30051 | -43.89557 | 2025-08-22 03:30:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8dafbb1-e197-305a-9fd4-a301d9f02a35 | -5.45379 | -43.58113 | 2025-08-22 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b213b2b-dd0a-3164-ab59-6d989fe41a64 | -6.4348 | -44.51662 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ca30cad-4f4f-3270-a538-d5dd02ee2f21 | -3.81936 | -41.56709 | 2025-08-22 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 01fc1e5a-cbb9-3fed-b61a-bc705d7acd7b | -8.67251 | -36.23079 | 2025-08-22 03:30:00 | NOAA-21 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e9ecdf07-cc6b-3c23-bec8-996c6ea6f8f2 | -3.98156 | -43.24647 | 2025-08-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dec0e691-28ba-3f09-88db-500149036afd | -5.90136 | -43.44855 | 2025-08-22 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b1f353f-6a38-3fbd-bc44-5645e2995e0b | -4.65063 | -41.41195 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8c5ae4f7-7c18-3cd1-8881-7810a8c85edb | -7.65086 | -45.24786 | 2025-08-22 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6754b134-9356-348e-bff2-f95bb46ffa88 | -6.2942 | -43.89471 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbc66331-266a-3410-8061-e95c69c5580f | -4.65633 | -41.40987 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 10d455c0-1d8d-3e8e-a3ff-74f21265bd0d | -7.14995 | -44.67076 | 2025-08-22 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3f621d6-82ce-3cfa-ab54-51b40b44aac5 | -8.67267 | -36.23259 | 2025-08-22 03:30:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 47eb258c-7679-3466-b331-baa0c1c03f7e | -6.95093 | -44.55145 | 2025-08-22 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b73a254-0ee0-3afd-80f8-ded6dd0288fb | -7.46637 | -44.45199 | 2025-08-22 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e05778cf-8f29-3d90-ba4a-99de889ab464 | -4.40492 | -44.0885 | 2025-08-22 03:30:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e262a0fb-1ccd-3636-9a85-928c3cb8830e | -6.51033 | -44.57964 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ac0abbc2-4645-39c4-b091-6b7ebcecba0e | -5.88063 | -42.41023 | 2025-08-22 03:30:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d45a810d-62ea-3db5-b048-7f5be07fd886 | -4.65578 | -41.41321 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b22e6cba-ba6f-3d43-a6bd-f4eb6f49b9c3 | -4.39842 | -44.08721 | 2025-08-22 03:30:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README7.md)
