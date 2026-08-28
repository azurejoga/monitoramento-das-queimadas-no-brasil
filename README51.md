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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c9e79d6-002e-3ce0-81b1-1cf428e0ffff | -6.51435 | -55.24595 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd604a64-de4c-3875-bd57-3dd7ed7d16dd | -9.43392 | -51.69467 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8149c3f-278b-337a-9ce2-5c7ad046eada | -5.87452 | -52.1895 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e85a0a6-df82-3755-ae49-f66a15ba7794 | -9.40471 | -51.63331 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e1d9c23-99c7-3adf-9f8c-50cfdff36f5e | -6.76043 | -55.69117 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de42d8df-fda3-3b04-8461-815bfc4fc0a2 | -6.63255 | -53.18452 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78cd37d9-f3c7-36fc-b574-2980f8340ddd | -9.43441 | -51.69121 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a61d8680-bf92-301d-b691-1be1a4eea508 | -7.2546 | -45.86195 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 73e108ee-775d-3959-94a8-08b61eba4791 | -8.59637 | -54.76103 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dec22e0d-6237-30e0-8d16-e93472dc4025 | -3.45888 | -59.51338 | 2026-08-28 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 074bbe01-0e1f-3d54-9c7c-603885b0de57 | -6.26545 | -53.36427 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f92601e8-1236-39ba-b2ab-18c43147e1a2 | -7.27852 | -49.94867 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4cc9d5ac-8131-3cce-8f75-a68970f6dab5 | -8.93817 | -50.71626 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 289aafaa-1cea-30e8-9beb-113a39c2db64 | -8.59982 | -54.71618 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3784d65-153c-3f85-9f7e-d5746351e855 | -10.55399 | -50.48422 | 2026-08-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 391e99f1-89bc-3eee-85d3-f68b9cd5e197 | -9.21363 | -51.55191 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e418fe5f-d37d-3652-aede-fea32651089f | -7.87974 | -46.09706 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 46b4e5bc-3b79-31f5-815f-11b5a0b4a3c0 | -8.08945 | -45.85618 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2c4f681-1e6c-3724-b9e7-b0c5c6d4daad | -6.67961 | -56.35218 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39894a24-80bc-3226-9810-be0581dcb633 | -6.26619 | -53.1202 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c12b0744-e79c-3612-bff0-dc4ee065fac6 | -5.89769 | -52.11055 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2b8523b9-8343-37f1-8aab-3813c0313683 | -6.54457 | -55.09626 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f23bd67-d8e9-32fc-a1ec-d740cc1dafda | -6.84018 | -56.40972 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5b7818a-15dd-3858-a04d-89390c6caae4 | -8.59584 | -54.71936 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e30e30db-3eea-3e9d-b458-79c7b3674655 | -8.6038 | -54.71299 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adae58ed-915d-31c9-8daf-8e41b773411d | -8.80264 | -50.49251 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec495279-0a04-3c42-8112-cf464d3ba998 | -9.22774 | -51.53961 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b35f933-d910-3ec1-88c2-126236351297 | -3.79691 | -50.61667 | 2026-08-28 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3927c99d-5275-3644-963a-82d34455dcf4 | -8.59189 | -54.69979 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7761cd0-6ba7-3ba7-b22f-a6ca1f9ff2e1 | -6.30771 | -53.57792 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0136444-34c3-3e64-8f89-f2003cf437d7 | -7.35212 | -55.16777 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 798f6a38-68e3-38c9-86e6-38c15aff38c7 | -6.64262 | -53.19013 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09075229-a079-3a79-b518-334b8089e4d0 | -8.77786 | -49.94901 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7779121c-d4ca-3b42-b289-49a95c04b42e | -6.26597 | -53.12502 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8698cc65-a4c3-3ab3-a73b-e32a85ec417c | -8.0779 | -45.81572 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bda4987-ac9a-3846-b646-a0e1dcafa9ad | -6.27367 | -53.35753 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e10053da-5e72-3253-9833-b4a6d450a6b5 | -5.93371 | -55.67759 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4237e7cc-690b-3f68-9474-6dbcb81bb240 | -6.26304 | -53.12047 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ee8a77b-aaa5-3462-87c2-9928c16fe533 | -6.90242 | -44.67489 | 2026-08-28 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91906ab7-2402-3ae8-b9e5-4e856899e78c | -9.96533 | -53.94079 | 2026-08-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1bfee8bb-d824-3766-9049-9cfc06a7e0ce | -10.06129 | -46.94077 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f61461b-d309-3de5-bbe7-55de5b2ab224 | -6.56308 | -56.55017 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 816b1d8c-3fe0-3e3c-97c7-226c1c2ad52d | -6.42717 | -54.93349 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 085b933b-2db2-3700-8d68-6bf744ec75ff | -7.37732 | -55.15342 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5371169f-4326-38ee-91b0-62aa56db9f54 | -6.22768 | -55.49324 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42444d24-d47d-3b1c-bc87-3ba19a7b1bdb | -8.22556 | -54.96307 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cb6ecad-5520-37ac-bea7-e38c5d1c84d6 | -11.38393 | -45.14123 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b31d03f8-3668-3948-9dac-244caee4f00e | -8.08327 | -45.8124 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb920910-c325-35f0-8071-efa2a8859e2e | -6.16588 | -57.78152 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b53773a8-53d4-3185-86ac-a8d99d497570 | -8.15471 | -64.00246 | 2026-08-28 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6599447-e66b-3c8d-9bcd-f17e7db1f15a | -9.66464 | -55.08138 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd4f0cbd-961c-333c-8146-ffeb8319589b | -8.15379 | -64.00769 | 2026-08-28 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a870e40c-f1f1-3362-bbf8-ed22d527abe7 | -6.77807 | -55.68686 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c87172c-de00-3a75-9d73-87d51f52850e | -7.88024 | -46.0934 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| eacf6b2c-bcee-3e47-8402-c8b254f236fc | -6.22518 | -55.61704 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cc4306a9-7847-3ea6-853a-ab6f042ecdb2 | -7.28266 | -49.94716 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73e9d468-5780-3733-9503-7b9c5d865a8e | -6.62601 | -43.7351 | 2026-08-28 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a433e8b7-976a-3873-8766-522982374b95 | -6.64556 | -53.19469 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b380f601-b3a6-3695-9ee7-5a37a4030e25 | -8.06457 | -45.86465 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37e6f046-72c9-384d-a5a2-98bae36b7c38 | -6.68237 | -56.35617 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a5ed2d5-c550-33e5-b0d7-40b30662238c | -6.14417 | -53.51772 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b415c204-5f25-3d53-86f9-8c2fe370013a | -7.57502 | -61.30652 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f64747b-ac84-3f25-a8fb-1bee340c80bc | -9.68215 | -55.08048 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19d5dee6-33cc-3b05-be90-45bf606a2abc | -8.08435 | -45.81219 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d97732f7-646c-39a5-bd9b-68f4630b2375 | -8.77339 | -49.94836 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ba99d93-fa58-3aff-b1a6-bc4d7c216ec2 | -6.16871 | -57.78574 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a40e985-517a-373d-a25b-f91ebc82e126 | -6.5149 | -55.24246 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b33d1a50-efdf-3689-85d2-ee6edbd0f036 | -8.95276 | -50.16816 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f9f987b-e3cc-382e-a153-7d3bc1328b2b | -6.27308 | -53.36145 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d16aa988-2047-35f1-a842-0546712ced9b | -8.60035 | -54.75785 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c42a5382-3882-3ad3-8ea0-f745676f44bd | -8.24079 | -54.97624 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b30a0224-92ff-37d4-9052-5dea916ee4eb | -11.37638 | -45.15046 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9357ee9-8f3d-33ef-b5c2-398128fdda62 | -5.87517 | -52.18516 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc80dfaa-6e1b-3584-9b17-0c65d3c197ee | -10.00945 | -46.41197 | 2026-08-28 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3df0f7ed-4731-38fe-936f-4d3a08aa8a3f | -6.11653 | -57.82672 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f16cd6d-4ddb-3914-a30e-5a35afcd7fe1 | -8.24306 | -54.98386 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d980e16-7578-3d12-9da7-4e657a6282be | -7.57844 | -61.31073 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05edda27-9ae6-35b8-bb79-d7f7ebf9be3b | -4.92668 | -55.77246 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cce11d0b-407c-3f12-b257-706623620360 | -6.12103 | -57.69108 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee48e106-3bc1-33bb-9df3-c5c15f9cb5eb | -8.04905 | -54.04108 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 024f2c1c-4f4d-312b-8209-b821eac61e9b | -6.83648 | -55.6178 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72d0b71c-516b-3746-8ca5-ef6349a013a0 | -8.69002 | -54.7227 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29020dd9-2e3a-3cc9-bc40-dcb05a7dead5 | -9.60889 | -55.12159 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fc7593e-500e-3d88-83c1-287fca46998d | -6.63967 | -53.18557 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cc97366-8105-33a7-b29c-f1409f1cb67b | -4.92999 | -55.77298 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3d3f2ee-2034-3635-b1ba-b6a0f451da06 | -8.07249 | -45.81172 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3068b4a5-5d10-3212-b4e2-4013582137e4 | -7.2715 | -45.35515 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c4f068d1-d987-30ec-9d20-a8d32be317c9 | -6.13599 | -53.52452 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffffe8c2-ad92-392d-8ea8-85c28e66fe87 | -9.66859 | -55.07823 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd4487db-8d93-366a-b5c9-9c6c0357a89b | -8.58956 | -54.7826 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9d2bbac-32f9-308c-92d2-614e866c2542 | -8.24532 | -54.99154 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb7aa99d-6a84-3028-8fb0-0d6374b738f7 | -7.38575 | -55.18733 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ca88d1b-6408-3744-9fa5-f840c7235d73 | -6.2336 | -53.47936 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e888e0b-bf98-37a8-ab20-2858eed1fec0 | -6.28243 | -53.37087 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 302c0315-1f30-3f4a-94f6-cd8c088b2c20 | -9.43636 | -51.59044 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7515c028-a4b9-32db-b063-9ca04ba3be7c | -6.73971 | -56.33686 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e80d12c2-2d70-393a-bb8d-bdba51cbe3df | -8.17262 | -46.16726 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 085f7e1a-f5e3-38b2-9b8f-dda3c6d20e1c | -6.1647 | -57.78888 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa51a04e-8910-3b8f-a9d7-db4908ec6d04 | -10.00896 | -46.41593 | 2026-08-28 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8371d71-2bdc-30be-97af-85474a152121 | -9.23387 | -51.55455 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README52.md)
