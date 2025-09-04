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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 348953f2-75eb-3cde-bac7-5effa18148e0 | -7.6491 | -63.1197 | 2025-09-04 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c9d36494-bbc0-32cf-a414-e9c83e8a2030 | -17.1694 | -46.2417 | 2025-09-04 01:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4f1dacbe-85ef-35e4-82c4-11dafa25730b | -13.1079 | -57.1109 | 2025-09-04 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 1c68961b-cd5b-36ff-a8c6-fe90e3864224 | -5.9081 | -57.7116 | 2025-09-04 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a7b2dfc9-d154-3079-953b-2734ae9347cc | -6.7832 | -63.1474 | 2025-09-04 01:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| eef35532-23a7-360e-bf87-e4dd3b93c0ff | -6.797 | -44.0859 | 2025-09-04 01:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 22af7928-1b7d-36aa-9734-0a56a6d32176 | -8.0799 | -45.339 | 2025-09-04 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 76290980-6444-3f49-a5ba-3f0a18bb5f12 | -6.7465 | -63.1297 | 2025-09-04 01:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 2d41f0e6-bab6-37d6-aa70-937efdfae6b7 | -11.0568 | -45.146 | 2025-09-04 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 5751f19f-ca8a-30ee-a6a0-65b67627d8c1 | -2.9619 | -49.365 | 2025-09-04 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 088e6e5d-6927-3a95-8a7f-2cbad1b42727 | -5.908 | -57.7311 | 2025-09-04 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 06bd5d4a-90fe-39ae-8862-3242391f5d9c | -11.0565 | -45.1691 | 2025-09-04 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 8c153d19-7bba-3cda-98aa-b70bb844b11e | -17.1688 | -46.2651 | 2025-09-04 01:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| f7e82e05-b9aa-3006-b4ef-fe7b6debb4c9 | -5.7002 | -45.156 | 2025-09-04 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| f2e90da6-022a-333a-983c-3f838bf58ce4 | -12.9009 | -56.9287 | 2025-09-04 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a7b187db-a5ed-3619-81c8-8e3c92f56312 | -4.9951 | -56.256 | 2025-09-04 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| f2973408-870b-3a1c-9432-00e72c7b2398 | -12.4981 | -48.061 | 2025-09-04 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 0d5729bd-24f6-3a25-a52b-8abfc4ccd81b | -8.0799 | -45.339 | 2025-09-04 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 925e1094-b670-3837-9337-0f95c31391f7 | -4.9951 | -56.256 | 2025-09-04 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7b7477f4-6934-36c7-94e7-26a875bfd526 | -13.1079 | -57.1109 | 2025-09-04 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 8ceca8a2-a804-3c36-93fd-ddd1d5220086 | -5.8896 | -57.7318 | 2025-09-04 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 3fe07b9c-c02a-3184-9ece-cd54607e96ce | -5.7187 | -45.1773 | 2025-09-04 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 164.4 |
| ee09162c-8210-3127-b8e8-69003d3aa73f | -17.1694 | -46.2417 | 2025-09-04 01:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9cc4f327-1d9a-33d1-8df0-3c0d773f32c3 | -7.6491 | -63.1197 | 2025-09-04 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 8d59b04b-6256-3b6a-80dc-583405efe9c0 | -11.0572 | -45.123 | 2025-09-04 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 64d3c65a-09bc-35b9-b47c-4d7e41c7b36e | -6.7465 | -63.1297 | 2025-09-04 01:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 66fc21f1-2350-3651-9126-a2a5d19ece92 | -12.9197 | -56.9471 | 2025-09-04 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| d62e259a-962e-3607-be25-f5e5b742b7b6 | -12.9006 | -56.9488 | 2025-09-04 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 68e1166b-f7c7-3cba-b3c0-fbcc563bf6fc | -9.5601 | -62.5337 | 2025-09-04 01:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| a1616e10-00fd-3b68-b76e-9c6d0063ed7a | -6.7648 | -63.1479 | 2025-09-04 01:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| cc0786a9-1860-359d-8638-fe6f890e008b | -5.7002 | -45.156 | 2025-09-04 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 279.8 |
| 57baef5a-874c-3c14-82ea-97c2125b3e96 | -12.9009 | -56.9287 | 2025-09-04 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1012b7c4-627f-3f90-a037-c74c49f972d6 | -14.6 | -48.0142 | 2025-09-04 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0ca74bd4-86ee-32c4-bcab-94fbcacb245e | -11.5779 | -52.115 | 2025-09-04 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 067152ee-2595-37c3-8fa8-e1a328e77f3d | -12.4785 | -48.0859 | 2025-09-04 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 89550c27-8024-3143-9193-05129a0d3e07 | -11.6838 | -57.3319 | 2025-09-04 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 352ed3c5-4b2c-3b16-bfba-1d90848c79e7 | -12.8816 | -56.9505 | 2025-09-04 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 14e21b06-1bdf-3f93-af30-9870f1bf507e | -11.0568 | -45.146 | 2025-09-04 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 70611b18-2f97-3f96-9a77-8e7c90b6c135 | -17.1688 | -46.2651 | 2025-09-04 01:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 141f7989-991e-3c01-a53f-4a515278fb59 | -6.797 | -44.0859 | 2025-09-04 01:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 51f1ed51-013f-3144-9eb8-b256bbbceaa1 | -5.7189 | -45.1547 | 2025-09-04 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 228.3 |
| 9375fcc0-67d1-353b-b169-3b1cf56d2547 | -11.6599 | -54.5297 | 2025-09-04 01:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6d562044-d814-3610-a3be-c1553c3f46a9 | -10.4283 | -50.3732 | 2025-09-04 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 4c7f3638-2c0b-31b4-8a78-fa7b52a9860c | -6.7649 | -63.1292 | 2025-09-04 01:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 180.4 |
| 7ce3366a-de97-3ed3-a147-f98d81b59020 | -6.7782 | -44.0876 | 2025-09-04 01:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| bad7df5d-d582-3a40-b288-9eab0eacd079 | -11.6409 | -54.5315 | 2025-09-04 01:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 48d08c32-5ded-381c-8561-a6d2ecbab10a | -10.4472 | -50.3713 | 2025-09-04 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c1926b46-fecc-31a9-8e74-5225ef0927ff | -5.7 | -45.1786 | 2025-09-04 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 65cdd804-4a19-3dba-9986-4f1c1e272b57 | -2.9619 | -49.365 | 2025-09-04 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f80c223d-4447-3b14-9489-f78f42170ce9 | -11.6836 | -57.3518 | 2025-09-04 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 88bf671d-2e06-3d82-9e64-fb245e135eca | -11.0377 | -45.1487 | 2025-09-04 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 367e4352-8e6d-366f-8702-3ca3faa28ef5 | -6.7833 | -63.1286 | 2025-09-04 01:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| d9d37d4d-4092-3535-994b-243dc745bef5 | -11.6647 | -57.3533 | 2025-09-04 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5d927e14-8db5-3032-ba0e-9193d0571732 | -5.908 | -57.7311 | 2025-09-04 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fa769270-e80e-32c1-ab1e-0aad99109cf4 | -5.6079 | -45.0265 | 2025-09-04 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 913a5e5b-4a7a-39f6-ba44-6f64fdda4af3 | -2.9619 | -49.365 | 2025-09-04 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e25ec08a-4356-3252-a45a-2116e8f0ee5a | -5.908 | -57.7311 | 2025-09-04 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e776ce98-d75c-390c-b975-3d4e48753e95 | -11.0377 | -45.1487 | 2025-09-04 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f74aa83a-5d72-3adc-8027-11558779a856 | -11.6599 | -54.5297 | 2025-09-04 02:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ac51376a-5ca3-390c-8e7f-6b4c6fc3666a | -5.7189 | -45.1547 | 2025-09-04 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ef0afcc7-2965-391f-8754-574349bda3c8 | -6.797 | -44.0859 | 2025-09-04 02:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 62768370-f919-3a45-b1a1-88e1eeb28355 | -6.7649 | -63.1292 | 2025-09-04 02:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 152.0 |
| fc5f005e-306c-3d9b-a4ed-4c00c3785d73 | -6.7504 | -58.7268 | 2025-09-04 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| be9a74b2-f9fa-3e27-bb31-56f1debf1747 | -11.6649 | -57.3334 | 2025-09-04 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 55046ab7-86c2-3cab-8dc4-acf89aa0a2ca | -6.7782 | -44.0876 | 2025-09-04 02:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cfd1c70d-27f6-375c-a21b-e1f1979d0c4b | -17.1888 | -46.261 | 2025-09-04 02:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e267013f-4858-38d0-9537-d50d6c024cf0 | -11.0565 | -45.1691 | 2025-09-04 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e5f4d664-6a08-37b8-a808-8ce65b2f7c8a | -5.7002 | -45.156 | 2025-09-04 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 268.0 |
| d5877b1d-6614-35dc-bf49-38795f5fece6 | -2.962 | -49.3437 | 2025-09-04 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| d0eb2c1c-ed1b-35a7-b956-0044eea19043 | -12.9009 | -56.9287 | 2025-09-04 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c2760f28-a375-3089-9472-5d9d5644a24e | -13.1079 | -57.1109 | 2025-09-04 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| c63bd0ba-ccef-3a46-a2c9-6a5649a6cfdf | -17.1694 | -46.2417 | 2025-09-04 02:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7aa25a06-e4eb-355f-9ddd-8f4c9ca4ef4b | -6.7465 | -63.1297 | 2025-09-04 02:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 44f4ae6c-51dd-3476-b233-2701402615e2 | -4.9951 | -56.256 | 2025-09-04 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ae8fb417-4e9b-3146-9e75-1eb7d60f7153 | -12.9197 | -56.9471 | 2025-09-04 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 7ef18c63-4539-3e25-8fe3-c52cddee2a70 | -11.6647 | -57.3533 | 2025-09-04 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 65426b0f-ad29-3cc9-a1d2-89541d5ececb | -11.6836 | -57.3518 | 2025-09-04 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 56e63736-23b1-34f0-b4af-327351b08720 | -12.9199 | -56.927 | 2025-09-04 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 377ab2af-d7c0-3a11-b3c7-7d0bd309d2ba | -12.9006 | -56.9488 | 2025-09-04 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 8243f530-c861-3489-87c7-0be01f634893 | -10.4472 | -50.3713 | 2025-09-04 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 495e0299-c024-33dd-b613-6fae8a825b8d | -6.7832 | -63.1474 | 2025-09-04 02:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 979e2ecf-5ae7-325c-b1c8-484a002f0a31 | -6.7648 | -63.1479 | 2025-09-04 02:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b22f038c-1e42-3c86-aa71-a1ccdcd5ea5c | -5.6079 | -45.0265 | 2025-09-04 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 8eee5ee5-a361-365a-8ae8-1cb8cb36d783 | -6.7319 | -58.7276 | 2025-09-04 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 7f9bcbbf-f1d0-3770-ad83-ffaaeb032ede | -12.8816 | -56.9505 | 2025-09-04 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 128e3514-8798-3b4f-b057-2b39a80356db | -11.0568 | -45.146 | 2025-09-04 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| b7ec8e5f-ef14-3682-8427-bc76d5c96eaf | -17.1688 | -46.2651 | 2025-09-04 02:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 2e8529b2-0fa1-3352-837a-03cddc0d78e7 | -6.7833 | -63.1286 | 2025-09-04 02:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 18941095-ae27-3d59-aebf-e8c0b3569458 | -11.0572 | -45.123 | 2025-09-04 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f4ac143b-88e6-3aa8-aeec-cc3deeffecf3 | -5.7 | -45.1786 | 2025-09-04 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 9ed1670b-c410-323e-ae56-7e380c32e0ab | -6.7649 | -63.1292 | 2025-09-04 02:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4c9e7ed6-c541-305e-aa4c-ce422a58f28f | -10.4472 | -50.3713 | 2025-09-04 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4c8a479e-87e9-3a9f-8bc4-34d4789779ba | -6.7465 | -63.1297 | 2025-09-04 02:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3766f973-f44c-3492-b13d-1f19ce2e4d5e | -10.5746 | -55.4161 | 2025-09-04 02:10:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| fd70cbf2-d1dc-3352-b064-1ffab6b68336 | -6.7648 | -63.1479 | 2025-09-04 02:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b915b288-85c7-3df3-a63a-39791c159454 | -11.0568 | -45.146 | 2025-09-04 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 979b36ad-1807-37aa-b3b6-c95792c218e2 | -12.9009 | -56.9287 | 2025-09-04 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 55650d18-ed1d-3024-926d-09317f8e9c9b | -10.4283 | -50.3732 | 2025-09-04 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 0baac106-104a-3948-9ee8-10c2a8afc84f | -10.4475 | -50.3499 | 2025-09-04 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5f83d35f-cb49-38d4-bcc2-daf35605ac2f | -11.5779 | -52.115 | 2025-09-04 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |


[Clique aqui para ver as próximas entradas](README12.md)
