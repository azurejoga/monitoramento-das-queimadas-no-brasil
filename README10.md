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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9041964d-3379-3886-a7c0-45096261d875 | -12.50149 | -57.76527 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb495eea-485f-34d5-bb3c-500d809d0900 | -7.25524 | -44.29861 | 2025-07-23 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8240ecb-c8b0-35f2-a108-2c3c62cfe3ff | -7.91806 | -49.64475 | 2025-07-23 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69a10f25-985f-399c-b1a1-5d29dadb3ecd | -13.70287 | -45.69205 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4d385d8-25cc-358a-b1e4-33fe3c3e2e80 | -13.70974 | -45.69785 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0db411c2-6e84-3e88-a20f-20b1ecc7c4b4 | -8.1381 | -49.50799 | 2025-07-23 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d0f6d33-eeff-3216-9ca7-bbd86ae4a411 | -11.76363 | -46.29142 | 2025-07-23 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a821372-fff1-35d4-b6e1-7b884d7497f9 | -13.7104 | -45.69319 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1e1b502-80a2-3a9c-97d4-dd7092165851 | -6.88723 | -45.24656 | 2025-07-23 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 172cafff-77f6-3a76-a8fa-8200fac6b7a8 | -10.03711 | -59.09731 | 2025-07-23 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0edc7622-a460-3752-931f-89ca2c0a6d70 | -10.71701 | -49.48404 | 2025-07-23 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3b17df2-0eaf-3e82-83bf-3af45a24ea48 | -7.47797 | -49.22805 | 2025-07-23 04:34:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a134d17e-bea5-384e-80de-4b4b7fa5be48 | -10.50526 | -44.88199 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82eb6c57-36d7-3047-9801-32fd1684abc0 | -13.71859 | -45.68966 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f6f0e9b-cc70-3100-9087-2df314dae79a | -7.52972 | -42.42006 | 2025-07-23 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 67f136a6-27c4-3bb9-a1e2-3cfd7aa68f94 | -10.64449 | -44.48227 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf115070-28c3-3348-a133-992223d49ca4 | -9.1205 | -60.75462 | 2025-07-23 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24fff0a3-c33f-3a3d-bc04-8132a13a96f1 | -7.74819 | -44.02388 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 41aef097-2366-3315-909b-25a292434335 | -8.92406 | -47.35038 | 2025-07-23 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4e580d3-feda-3c77-9aaf-639094255331 | -10.6353 | -45.23755 | 2025-07-23 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91fc1031-de47-3dbf-ae18-bb9acc31b3f4 | -9.05758 | -45.06339 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1da973b-0318-34b8-a11f-db74c29aa795 | -9.40767 | -47.95938 | 2025-07-23 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b210174-6aba-3c06-b507-cdb70bd89fcd | -13.67957 | -48.77578 | 2025-07-23 04:34:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 346ef9ab-fb56-39ff-a83f-263de1120b80 | -9.05281 | -45.06509 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1d19c63-eae4-38e8-b2a1-061a9ff2fc88 | -9.13674 | -50.77554 | 2025-07-23 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 525127c4-d686-3200-bae6-603bcdf2dc35 | -9.06322 | -45.07117 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91fa3b53-d4cb-3ac8-b0ca-bb24b7204a0f | -10.63089 | -48.09372 | 2025-07-23 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1fb07ec-8485-31dd-94ec-32de14a55907 | -13.70664 | -45.69262 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58cadd83-4b99-3070-8bcf-d8f3b8fcee87 | -13.71482 | -45.68909 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea0d368d-f8b8-3368-8677-92c005d77989 | -7.75587 | -44.02516 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fa903ae1-befa-3c4c-8005-7bf8a7af1ac6 | -9.4322 | -48.85036 | 2025-07-23 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e876f1f0-4e2c-392c-b6b3-4e7ddde3cade | -7.75343 | -44.01497 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 135cc9c6-72b6-3278-a008-ae4e08e85d41 | -8.08651 | -50.07991 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d290bb6-c619-39f4-97e7-f06192c9ddb0 | -7.94049 | -44.85207 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa4b6049-3677-3aad-a5e1-504bd5fc683d | -12.66266 | -45.03379 | 2025-07-23 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63398aea-a132-33fc-8589-d38538556115 | -12.50582 | -57.77328 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 12612e08-c981-3c91-82e9-9a01436c6380 | -7.28003 | -43.09482 | 2025-07-23 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 81d8b532-6ec3-30d8-b331-86f7dc79d87c | -14.18868 | -45.34082 | 2025-07-23 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49eaa026-1a76-31d8-874a-81aa9ab43395 | -9.06512 | -45.05792 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9f4ac243-c161-3e1c-b55f-54beba1a078f | -6.89138 | -45.24313 | 2025-07-23 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22316963-4f0c-3fb1-96a0-771bb31fee72 | -8.08595 | -50.08342 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 430eb01e-5dc5-333f-85d5-4bbf65a35d51 | -12.49941 | -57.77652 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a463628-3482-3c89-9389-4e05e9bb0e20 | -8.87261 | -49.03517 | 2025-07-23 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03fb9c57-7572-36ee-a7f1-6a10b880d5d6 | -9.05954 | -45.07064 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6572f75e-cb0f-38cd-a265-7a112abdbde5 | -7.91749 | -49.64833 | 2025-07-23 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2e3105b-0742-3f6a-a728-2281f6d3a818 | -13.71726 | -45.69899 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8bce331-7933-354b-89b5-cf368284e6d4 | -7.79712 | -44.78199 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da50981-e54b-32ed-b0a1-1a1fe3882817 | -14.49993 | -43.80934 | 2025-07-23 04:34:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93011543-cec2-368a-b015-c239f7dff098 | -7.76041 | -44.02097 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c2b734a4-4b7d-3fbe-b22c-11234ff0f092 | -7.52503 | -45.38547 | 2025-07-23 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37542571-81c0-3a6e-9a5b-9a4498bab24f | -13.71793 | -45.69432 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 42e49c89-cf10-3d9c-830c-7524fb2ab0ed | -11.73183 | -49.7142 | 2025-07-23 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08925505-f77b-3b22-8397-aebd220b2fe2 | -10.7173 | -48.85305 | 2025-07-23 04:34:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f282b1e-2d35-33d3-a108-acd340700c77 | -7.0256 | -45.84487 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 661ee888-664d-3834-af3a-d4ee9732071c | -8.09098 | -50.09539 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7860962-af36-3e35-90d6-34d24563d506 | -9.26342 | -48.55944 | 2025-07-23 04:34:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5a98f58-0ddb-306c-8a3d-8a9d6598bdd0 | -14.21257 | -43.9623 | 2025-07-23 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d7a48f8-dfc2-3a42-9e9f-0c57c7e4f6b5 | -13.45746 | -46.72308 | 2025-07-23 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a063f044-5fc1-3acd-83e0-2042704f946d | -10.88548 | -44.36714 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea3d903b-66f4-3aa2-a79d-3f3ecf0764fd | -9.05325 | -45.06721 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4cebacf5-0c9f-3dbb-a8d3-cd6030adb0d9 | -10.88227 | -44.36152 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a57dc62-8819-34b8-a25b-f87b8fec05a8 | -10.88578 | -44.36343 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48ac1587-6bb7-3a54-90c7-7bdfb51e8b62 | -9.13613 | -50.77935 | 2025-07-23 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce050dce-0443-3991-8925-62c1577047d6 | -7.02098 | -45.85197 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4494681-899b-34a6-9df6-16ab662ccaa6 | -9.76665 | -48.58281 | 2025-07-23 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78c2ad1f-3bca-35c8-bb07-6dbb82e564f4 | -12.66198 | -45.03871 | 2025-07-23 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e79c799-806e-3405-b00a-f348588beef5 | -9.43772 | -48.85838 | 2025-07-23 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 718a5808-51a1-3af6-a358-70dd3d411b4f | -8.09216 | -50.08806 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8987f608-47c9-3231-8b52-126b0c3ec955 | -13.71106 | -45.68853 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3eccd922-2528-320f-8973-5376d41c6f82 | -9.05648 | -45.06569 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5129c8d3-de9c-3eb6-937d-8c2bd00dc8f9 | -13.53951 | -43.70869 | 2025-07-23 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff82059f-5ed5-3b91-beff-c9947592a993 | -7.91258 | -49.64402 | 2025-07-23 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4023f58b-8359-3546-9a92-271f2c3bcf26 | -12.50436 | -57.77755 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7861f4ba-e622-30e1-a42b-ae29f262b1d6 | -11.26297 | -47.82155 | 2025-07-23 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00d9f678-ddc0-32b6-8460-b9afb75b32f3 | -10.04843 | -59.09934 | 2025-07-23 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d27852ae-4df2-37e1-9b5c-63e06a8d920b | -13.30521 | -44.17952 | 2025-07-23 04:34:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61a4788b-9221-3b89-a73f-00396cf96cc2 | -7.54733 | -49.67022 | 2025-07-23 04:34:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5ec9a61-2f94-369a-8f18-40f8aa33af7d | -10.63596 | -45.23302 | 2025-07-23 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9936834a-051c-3a9b-91f4-9cc2a8fcb16c | -13.69403 | -45.70027 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 476374c9-1aad-34fc-a429-c846f6eb2db6 | -12.25733 | -44.78008 | 2025-07-23 04:34:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f8497b5-d186-380d-89ad-4d31b27b9365 | -7.19972 | -45.33511 | 2025-07-23 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 147a2251-517d-336d-abd8-7968119f6c7b | -10.06614 | -59.09847 | 2025-07-23 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73b89bba-d002-3a6b-95ad-687d34a090c3 | -10.88185 | -44.36287 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e00b4273-f100-3523-8a79-a07f6800b2a2 | -13.67902 | -48.77937 | 2025-07-23 04:34:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58c4a03c-082b-34d8-8067-5e66683e4a82 | -7.89107 | -45.55284 | 2025-07-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4dbdca4-9c78-3c23-acb8-0db060f7f3ff | -7.27895 | -44.3718 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c2a9ae6-b5d9-3c60-9c51-2770924199a2 | -13.70222 | -45.69672 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10161234-94f5-3ee8-ac86-34f2e14b5d41 | -7.75273 | -44.01976 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4488fdf5-ff0d-319f-a6e7-27bdf9f4f1d6 | -12.50046 | -57.77082 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b8d8a3b8-16c2-3c3e-bbfc-2d52bfe84f18 | -13.64945 | -45.71722 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db001fdb-9a13-3fae-b0de-9246fd0e3050 | -10.88972 | -44.36399 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00e0bc9a-8b57-394d-a1cc-e432e3ea67ef | -10.64506 | -44.48478 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a81d3e3-7de2-3e09-9464-30281f44a462 | -9.7435 | -48.57915 | 2025-07-23 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f7dbb9a-223d-3431-b84d-a06ce7beeacf | -7.0464 | -45.84821 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d78d0e9e-30f1-3462-9c6e-9be4977be8c5 | -8.09494 | -50.09237 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043d79e7-93a5-30da-a2bc-2202d129f81b | -7.75727 | -44.01558 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ed20752a-4767-31b8-863e-2f4bdb2fb8f0 | -9.0608 | -45.06183 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c5b69e20-229f-3d4d-b50f-2883fcdf5da5 | -9.33624 | -49.84361 | 2025-07-23 04:34:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c454a1e-7b63-377a-bb8e-8ab8fc18c748 | -7.57045 | -44.57422 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0501ce82-2deb-3cb6-881b-a90040d03917 | -10.432 | -54.37921 | 2025-07-23 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
