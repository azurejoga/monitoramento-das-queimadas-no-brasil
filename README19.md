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
| ee831165-ea66-33c5-9cf3-f1b7289ea50c | -12.98 | -51.32 | 2026-10-02 02:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e803d10b-883a-395c-b5ac-52c05b8e5972 | -13.13 | -51.26 | 2026-10-02 02:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a91725ca-c39e-3dab-8dc7-bf4d6729d03e | -13.13 | -51.2 | 2026-10-02 02:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d8cc14b-7305-3e09-a1f5-612c09623f19 | -13.1 | -51.25 | 2026-10-02 02:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9b2c361-37f5-379e-b3fa-6c67a39d97c4 | -10.8005 | -53.7682 | 2026-10-02 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 73b6da12-3833-375d-a8ba-b661a9d66305 | -11.142 | -44.6261 | 2026-10-02 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 41e18600-618d-30e6-9fff-5e1266c3ca89 | -11.7545 | -43.5512 | 2026-10-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 128492d2-fd49-30c5-8b13-a21559cdd3b2 | -4.4507 | -47.9112 | 2026-10-02 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 6adde773-624c-3219-9995-9f74b5729e18 | -6.858 | -59.2636 | 2026-10-02 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0bdc6141-0924-342e-9f38-e4c2efcedcc1 | -11.3099 | -50.94 | 2026-10-02 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 3cb99eb6-39f8-3037-b74b-d978fb08d247 | -4.4693 | -47.9103 | 2026-10-02 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| b8b166ee-e054-31b7-8c57-41d991230f42 | -3.1839 | -54.0839 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 2204b042-d3b9-3fde-8172-a39424dd851a | -11.1424 | -44.6029 | 2026-10-02 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 564f50d9-ae2c-35fa-af71-7e61100b261c | -11.3292 | -50.9167 | 2026-10-02 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e9639b6c-522a-32d9-a74a-91b6350345d6 | -6.2091 | -60.0187 | 2026-10-02 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 46f0d84e-a001-3421-a982-8fa183b3918a | -11.2912 | -50.9208 | 2026-10-02 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 339ec53b-fed2-3880-a0e2-852bdad663ff | -2.0393 | -56.8789 | 2026-10-02 02:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| c8b66af1-23b3-353a-9182-dbecb44be8fe | -11.7926 | -43.5689 | 2026-10-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| dc58669e-9433-3342-b7b0-1db4cb23a9d0 | -3.2766 | -53.8602 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 07d09386-9b5d-3911-ba35-d58a6c298387 | -12.7887 | -51.3233 | 2026-10-02 02:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d72a2315-f7ca-3a49-875c-37f0de80da42 | -3.1299 | -53.7633 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 93041733-7995-3c08-b39e-c8158fb0e64e | -13.3481 | -43.8538 | 2026-10-02 02:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| a64a7b97-f228-390b-9ce1-591548314c48 | -2.0576 | -56.8786 | 2026-10-02 02:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a7638de8-3ff1-3f25-b13e-b896e308d74a | -4.4506 | -47.9329 | 2026-10-02 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| a0bbf49a-1315-3e1c-af26-52b0c6c1204b | -3.2951 | -53.8395 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 7d4ffdf3-aa8d-3acc-b9a4-ed7ecb462398 | -11.4691 | -43.4299 | 2026-10-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5a6b0ffd-e998-333a-9f13-e7835a27084a | -4.4691 | -47.932 | 2026-10-02 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| fd04bce8-d045-3a9b-8109-b7f948f8d6d6 | -11.7733 | -43.5719 | 2026-10-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 4f2dfc3a-90b6-3fc4-b413-9453cdd56fe2 | -4.2953 | -49.1021 | 2026-10-02 02:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7fb7a5c7-ea72-3aed-aa30-762140992df4 | -3.295 | -53.8597 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d1235a28-bf01-3c72-b277-2daa27242ced | -3.1838 | -54.104 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 423c1a60-8ddd-36c5-bb2d-d9c347950ce5 | -11.7541 | -43.5749 | 2026-10-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| a4e7e8b3-bf58-380d-845a-e2b1c14aa881 | -11.3102 | -50.9187 | 2026-10-02 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 01dd86a8-f96a-3526-8417-68ce1b1417b3 | -4.2677 | -50.7297 | 2026-10-02 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9da0b536-d210-3eb5-8db3-349523d86d48 | -11.1615 | -44.6002 | 2026-10-02 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| f1298e31-3102-31ff-936f-4a4fedfefa20 | -11.7738 | -43.5482 | 2026-10-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 62c68df9-a56d-3e1a-a713-6114a502a5cb | -3.1299 | -53.7431 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 290707e1-b937-397c-9787-fe69bdb322d0 | -4.2676 | -50.7506 | 2026-10-02 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| f980fc35-55aa-3922-8f63-9609289e2d3d | -2.0394 | -56.8593 | 2026-10-02 02:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 79b080ef-a5ec-3fe2-a4de-f9ae411b152a | -6.3952 | -56.4158 | 2026-10-02 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f5c4be08-fd3f-3aa4-9ea2-ff9fc3fdd2c8 | -2.0577 | -56.8591 | 2026-10-02 02:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d4a5267f-1537-362f-bf28-e4f3fec35ddf | -3.1483 | -53.7426 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ebb8fe2f-3ecf-309f-9f71-9ea62e47d31b | -6.9132 | -59.2806 | 2026-10-02 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2f3ccdec-4cab-3a42-ac17-19e6b43ef456 | -11.7729 | -43.5956 | 2026-10-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d9e16b6c-55a4-3b1a-b0e0-0685ba153647 | -6.209 | -60.0378 | 2026-10-02 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 717c44c3-f783-3ca3-a906-524cd1b045e2 | -11.1611 | -44.6234 | 2026-10-02 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| dda83929-9faf-318c-866e-6c5bb8686428 | -10.7816 | -53.7699 | 2026-10-02 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 71d3e582-0c03-3cca-92aa-e06d5e27ab5a | -3.2767 | -53.84 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d6615bd6-ce8e-3398-99bc-6e1b09c517f5 | -3.1655 | -54.0844 | 2026-10-02 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d86c6a9c-4c6e-396a-9629-4877b484cca5 | -10.8007 | -53.7476 | 2026-10-02 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 0a9edae8-cc07-30bd-88f5-7e9f50659fe9 | -10.7818 | -53.7493 | 2026-10-02 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 2d1093a3-b3a5-3173-8db5-b9d9dcc2cf0f | -10.7816 | -53.7699 | 2026-10-02 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 9f3bc860-a5cf-34a8-ace3-b72c75484210 | -3.295 | -53.8597 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 3091d17a-2783-3f13-b738-b4fcefad4a5c | -7.0478 | -55.6302 | 2026-10-02 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 44479f76-cf90-374f-9818-aa2db190bf19 | -2.0577 | -56.8591 | 2026-10-02 02:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7c775f09-68f5-3f97-868b-dc37d982af21 | -3.1839 | -54.0839 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1b6b3bc5-6c31-3e6e-8323-1a5b36395204 | -4.4506 | -47.9329 | 2026-10-02 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9d0965a2-406d-3225-9145-b31e97feff26 | -5.7563 | -45.152 | 2026-10-02 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 2e5b6bbe-da24-3a33-8b69-7eebe6ad076b | -13.3481 | -43.8538 | 2026-10-02 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 93d4c8e5-d903-30e6-b964-b2dac8b25a5d | -10.7818 | -53.7493 | 2026-10-02 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 093d155c-559c-3052-b430-6946697cad57 | -3.1299 | -53.7633 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 118105b1-5283-332e-9a57-45ad539dea94 | -10.8005 | -53.7682 | 2026-10-02 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 485ec914-46a4-3d5b-92b5-e314cf9f90be | -4.4691 | -47.932 | 2026-10-02 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 94de7f77-45fc-3739-85ce-ce346a92b84d | -11.4691 | -43.4299 | 2026-10-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 30dc92dc-69be-36ad-b78e-3968751efc59 | -11.7733 | -43.5719 | 2026-10-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 3c683c16-b956-3ea3-ae87-df6646fd8f84 | -6.209 | -60.0378 | 2026-10-02 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c8d1917f-744e-35df-86ac-90727ab6218d | -6.9316 | -59.2991 | 2026-10-02 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5e84203e-540c-3667-b3e7-a82f3c0c9ad5 | -11.6575 | -43.6136 | 2026-10-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 2d51e073-4cca-3c47-918a-94323ad2ce30 | -3.2766 | -53.8602 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0b3d8700-8aef-3286-84b0-6546efd91d7f | -11.6579 | -43.5899 | 2026-10-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 290.1 |
| a5ba8034-f68f-34b9-a814-d724d6ac93cc | -7.7551 | -49.2067 | 2026-10-02 02:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ad245cc5-5d17-3e0d-8c17-5d6fbbacf65b | -2.0576 | -56.8786 | 2026-10-02 02:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4bb2b434-1c67-355a-be34-5545a01bf2ab | -9.5335 | -45.3405 | 2026-10-02 02:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 50718afe-335b-38a7-904b-de0b08896525 | -3.2767 | -53.84 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d94e05f2-c334-3f63-9b21-ab1b41b39ff8 | -11.3099 | -50.94 | 2026-10-02 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| eeaccc7e-e322-3025-a8f1-648ac20bf6f6 | -2.0393 | -56.8789 | 2026-10-02 02:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| db82dd7c-8191-3898-a7b7-d3a9e35dc5f7 | -3.1838 | -54.104 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e0136b39-41dd-372a-b934-6603311655e3 | -6.2091 | -60.0187 | 2026-10-02 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 143bbea3-a96d-35c1-b586-2d503a446dfb | -6.0626 | -59.8897 | 2026-10-02 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| eae76c47-f853-3c07-a988-a7acf024ad88 | -3.1655 | -54.1045 | 2026-10-02 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a3b87ac1-d299-305f-bf64-568ac1bc7999 | -4.2676 | -50.7506 | 2026-10-02 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 672d257f-aa32-37ec-8094-53a9162535e1 | -3.1655 | -54.0844 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| dd79ff4d-e79a-38f5-9362-785b438c2de5 | -11.142 | -44.6261 | 2026-10-02 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| a6877506-f843-38bd-9f8d-5a6e05ac7617 | -3.0008 | -53.8874 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 7c5acf68-ce24-353d-8a0b-327884e1b9b8 | -3.1299 | -53.7431 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 1e57b853-bf0e-363f-9e59-ff924b5d47d4 | -3.2951 | -53.8395 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| a4712c32-f5be-3d36-b3a9-3395fa5af7ab | -11.3102 | -50.9187 | 2026-10-02 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7db7504e-b19c-3098-8e9c-295674a97207 | -6.9131 | -59.2999 | 2026-10-02 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| bb7c65d4-5c3b-3aa3-9bce-bf6ba9a47604 | -6.9317 | -59.2798 | 2026-10-02 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 17e8ac45-7b40-3af4-a2aa-8a1250aa1863 | -4.2953 | -49.1021 | 2026-10-02 02:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4a498ba8-4501-3f48-9d72-c5fe204d49d5 | -6.044 | -59.9286 | 2026-10-02 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d0f553ed-1a83-3661-b514-c7b268749da5 | -11.7926 | -43.5689 | 2026-10-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 81087bba-0b87-3731-86dc-9d77a6cdb967 | -4.4693 | -47.9103 | 2026-10-02 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| d802029f-d1e8-3bc1-accd-0600bdb38b88 | -3.1483 | -53.7426 | 2026-10-02 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6055758c-13f5-3fef-815c-757c84c3ccbd | -11.6767 | -43.6106 | 2026-10-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 2a5d95c2-91dc-3211-98fb-543921942260 | -11.1424 | -44.6029 | 2026-10-02 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ed44d93a-8de2-38c7-8b79-5764eccab1ed | -6.9132 | -59.2806 | 2026-10-02 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 7ab72cce-60e1-350f-bdb9-7087a7f5c831 | -4.4507 | -47.9112 | 2026-10-02 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 1d5f2889-8413-378d-9e66-e15357f005fb | -11.6771 | -43.587 | 2026-10-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| d1580445-d03f-3624-85bf-4a727ba1dcf6 | -11.1615 | -44.6002 | 2026-10-02 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |


[Clique aqui para ver as próximas entradas](README20.md)
