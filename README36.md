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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08e52b4c-0f33-3d18-9417-f677b6725492 | -10.28419 | -45.21352 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6861ed23-36e8-3842-9ed2-adf80dbdaeed | -12.10552 | -44.19396 | 2025-09-27 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c7c0ac8-255d-3772-bbcb-c2ff6fc3c4ac | -10.88512 | -45.12838 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 55f57db8-c453-3dac-8750-8082b647e850 | -11.94332 | -47.86814 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 016bdbd9-e4c8-3bdf-bfd5-21d1b4b4df93 | -10.12232 | -45.33918 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b7828900-8205-3437-8ce4-6639fe9f945e | -11.4331 | -43.51793 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 690fae69-b6a9-33b2-b1f3-525016458da8 | -11.43386 | -44.98928 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb992931-c671-3b30-8739-658f2f85f0e8 | -11.43217 | -44.97791 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b83fb57a-f426-36a6-90e4-6c269227a399 | -13.06886 | -48.71798 | 2025-09-27 04:23:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 267c1c57-6380-31f5-b4a5-ce98d3629809 | -12.84716 | -47.62354 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e53e444a-7b61-3691-ae78-2f9be3d32c39 | -9.11572 | -45.88204 | 2025-09-27 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf54fcc4-98ca-38f4-a9bd-b385687c81e5 | -10.60496 | -49.64083 | 2025-09-27 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a09a08d-45f4-332e-956a-d8e021a58b92 | -7.87718 | -44.02545 | 2025-09-27 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae96efc9-0025-3334-9b35-bcf2fc732790 | -11.78703 | -44.86788 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eece19cd-f133-312d-96e4-1510b47aa713 | -12.83198 | -44.69028 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e709dd81-56b1-3d77-8a76-82fd52268b70 | -8.69311 | -47.02535 | 2025-09-27 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dbf97933-fa2d-35a0-8802-cf5f80ceb240 | -11.70839 | -44.42266 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56002920-4d29-3e99-9bf1-911aeb4475fc | -9.99936 | -44.17604 | 2025-09-27 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7f30dea-9f2e-3475-9899-bd11e15599b7 | -11.97615 | -46.61549 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d03400f-33d7-3cce-88d7-54becf7ce978 | -9.99259 | -44.17498 | 2025-09-27 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d476cf28-27b0-3006-ae3f-46448d0fb2e7 | -10.17906 | -46.92953 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b26b1eda-35a0-3ec0-ace7-fe537c752eae | -8.83716 | -46.21457 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bff816b-553a-331b-9304-1b594aa28df4 | -9.85712 | -48.80721 | 2025-09-27 04:23:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f01d4175-7812-3231-b98a-84c48ce756cc | -8.86052 | -46.61562 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72db1216-705d-337f-bace-2fdae4eba818 | -10.87814 | -49.39846 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 424099f8-1498-3547-b9bb-08499177cd70 | -11.67445 | -44.46255 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe2da40a-1784-37a5-a446-7799fc22c1a4 | -10.57343 | -44.07312 | 2025-09-27 04:23:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8531cb2-b85f-3bb0-ace5-38f04618fee9 | -13.17971 | -47.42326 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93056588-13ca-34b8-a70b-9e64fb02473f | -12.85732 | -47.62528 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eedf8b2-a75d-30b4-a66d-c5cc790c89f0 | -11.43109 | -45.00719 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aefe5b9-dc1d-3c7d-9e9e-347704dd59cc | -10.95403 | -44.27387 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01538724-d685-37d3-a26b-0d79e28a9c0a | -12.83537 | -44.69081 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6262430c-13a1-31e8-940d-12486c22ca68 | -11.61417 | -48.58224 | 2025-09-27 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 077cbca2-12ad-3cfd-bbfb-91a5db37c937 | -10.23573 | -50.25648 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3ad8f8b-43e8-3529-99db-9ba86680b7c8 | -8.82921 | -46.26436 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 917ea39e-f4ba-3639-aa8b-cc5ec31f1329 | -11.97203 | -47.90804 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de3eaa58-3778-3a59-8797-84784fbaa57f | -10.02933 | -45.41423 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45f72238-2cc0-3f40-915c-c6e44e8379cf | -12.06568 | -46.62654 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 864ff0d2-7e96-3171-a721-603923ab932d | -11.97328 | -47.90046 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5443d09f-bb32-36fa-8a17-2d9569eeb451 | -7.67624 | -47.42237 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5267e5b-56c2-3ce2-b5e8-e51f29140d44 | -9.11629 | -45.87851 | 2025-09-27 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65607d45-6b49-342b-b3a9-5ad18b0dc923 | -12.82802 | -44.69344 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b617925-feae-390e-b76a-90e19b341c6c | -9.55002 | -47.77081 | 2025-09-27 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43dc86e7-c4aa-3cdd-bbae-46ae5722a260 | -10.2399 | -43.95004 | 2025-09-27 04:23:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29be722c-7518-3465-a3f3-e2ad730f9981 | -11.96297 | -47.89874 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cc0d915-fa68-3a63-a6c2-ce09258e838a | -10.93934 | -44.30162 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9991e877-1d70-3f6d-bea1-db4eb1ae9aa9 | -12.3111 | -44.35565 | 2025-09-27 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4dec413e-81c1-3908-8e43-3a849aca1013 | -8.72394 | -46.68296 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf1c15be-8d05-3950-a4c2-5745b4cdc86d | -11.96234 | -47.90253 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 206d0695-6148-321e-929f-dbe9f2d0c921 | -11.43328 | -44.9707 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2213c48b-c728-32ad-a9ec-9d739c0c0535 | -11.50333 | -46.92675 | 2025-09-27 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a0fe9c9-c722-3456-bf44-f6a7921d33bf | -8.50174 | -44.61505 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efd52aab-5d94-33fd-b731-f56b7a6a7887 | -12.27364 | -44.05284 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f129abb-0dbc-35be-8646-07e7a4621f12 | -12.95275 | -48.91233 | 2025-09-27 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2ef1744-7206-332c-a5f8-cf00d46b9d78 | -7.37518 | -47.03118 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bd4a4605-796b-30c7-b1e5-911ff405f71d | -9.11393 | -45.87842 | 2025-09-27 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59dbcab8-d40d-3ca0-a086-c417b080dfd1 | -8.69654 | -47.02591 | 2025-09-27 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20e5d42b-6b57-3c91-ac45-2f91c5b8643a | -11.43936 | -44.93122 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b0380b3-135e-368d-ac7d-f369363db879 | -8.82307 | -46.25969 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baed660c-315e-33d6-b468-eee0aa8f369b | -10.47065 | -46.5296 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d60e5f4f-5b30-3067-85de-f376068f670d | -12.36407 | -44.14433 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 402366ea-96b4-3f1a-85fa-851390e7cc6b | -9.99992 | -44.1724 | 2025-09-27 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4d07cb1-6c8f-33f7-828a-98fc3ca5e35a | -8.82586 | -46.26381 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a18e59cd-2df9-38c6-b3b0-913d3eef88c6 | -11.49895 | -43.53199 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc3faf3f-1627-3582-9aca-8b3e60cb5601 | -9.05196 | -45.50195 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f0a9d9f-bdb8-3970-b007-350b414d0013 | -12.04739 | -47.06105 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d6fcc0e-941c-3c1a-9558-a1748d6cc7fb | -11.98422 | -47.89836 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f4b6aa6-8817-3758-96a9-76e0172db76c | -9.76418 | -48.58506 | 2025-09-27 04:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7fa4035-b16b-3c8a-ab74-b6320286fa58 | -11.68631 | -44.43051 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68473e4e-498a-3200-ae47-7b0938d77e71 | -10.12009 | -45.33163 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e366ffc5-73e7-37aa-aca1-71d7539cf321 | -11.14222 | -43.36723 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e3e8deb-c881-3792-a614-0dd922c36715 | -11.791 | -44.90926 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85337cbf-bbae-3c68-80c9-01d5f1e5b0b5 | -8.65482 | -43.99118 | 2025-09-27 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d0e6fa8-b266-3e62-bf68-fec00d825ab2 | -13.34022 | -47.30061 | 2025-09-27 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c99e21a4-95b7-3846-ba91-9f4a5297c786 | -11.94676 | -47.86872 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c898ed83-8df4-3db5-876d-667f5ae40783 | -8.32433 | -48.00867 | 2025-09-27 04:23:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a542ac25-eb7f-3f9c-a812-f1363bc5a4f2 | -9.89333 | -49.1213 | 2025-09-27 04:23:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9bdcfd4c-3858-30da-b4b7-918c838dde8a | -11.36774 | -45.0047 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6ae614d-2202-3179-8cdd-51e8bcdc15ee | -7.78118 | -46.93705 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9998eb4c-c411-399e-9845-29a99e4d1853 | -11.98359 | -47.90216 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7654307a-3b72-3995-b5a4-3d6ec5bd7fcc | -7.81252 | -46.89621 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 94a41a0a-5b03-35aa-8610-e425c4a9f5ad | -11.41967 | -44.9578 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 330cf04c-a06d-306f-8d2e-bc7cfec5f95a | -10.5706 | -44.0689 | 2025-09-27 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58127286-132e-37fd-b40d-0f468055b32b | -9.86944 | -45.9063 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95a32c5b-f836-3edc-9b94-0768a8addf1d | -12.00796 | -47.88277 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 799c8f8f-fde0-3830-a03f-f816fe336ffc | -11.44161 | -44.9389 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df98c1fc-2eee-3400-8299-45a8d9cad41f | -10.19342 | -44.84116 | 2025-09-27 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88ebcaaa-6432-3fd4-b2fa-bf5033df74c4 | -11.96842 | -46.5996 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad0fe806-fba2-3565-8329-01378a7ebb61 | -9.94659 | -46.27316 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 169c4bf6-dbbc-3184-9e24-42b6859684bb | -7.78623 | -46.94938 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afcbbfc6-3e55-3701-a851-f7f25b589d13 | -7.83223 | -45.14638 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b541a055-1f6a-3673-a794-a05b52defba7 | -12.95394 | -48.90981 | 2025-09-27 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29d652c4-39ed-36ec-82b7-4c76b6000a16 | -8.18256 | -42.3752 | 2025-09-27 04:23:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 261813c5-244c-3990-a1ec-1a3a524144c9 | -12.27649 | -47.84211 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 242f3d90-8af6-36be-9ec9-e118f8fa0d99 | -13.43351 | -46.51533 | 2025-09-27 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d429be5e-ffb9-3950-ba90-c59d0c64d01d | -11.29833 | -47.81656 | 2025-09-27 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 082c0799-c23a-32ff-bfda-dadb52995bdc | -12.06234 | -46.62599 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ebab007-451c-3d78-92f5-3c337d5c5733 | -10.12684 | -46.47773 | 2025-09-27 04:23:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79f83ae8-c029-37f6-a164-86bb41ced4aa | -11.49545 | -43.53144 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f27f3a34-668e-3f88-9a44-8855859cdd71 | -12.26503 | -44.06316 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README37.md)
