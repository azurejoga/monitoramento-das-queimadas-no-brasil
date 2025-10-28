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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13023f04-f8ee-3ca0-8e59-49e2299cff04 | -10.85484 | -47.91472 | 2025-10-28 00:52:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 737a01c5-f190-3fe4-9fee-952cf0b0797a | -10.93324 | -50.27121 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 1dabf552-2ad6-3f7b-99f5-1a929952a8fc | -7.96017 | -45.55471 | 2025-10-28 00:52:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 717d816f-28a9-3df7-9db0-5138cf2b5d80 | -13.63345 | -46.47775 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2902b18d-87d4-3fa3-8d24-5264436186cd | -12.08838 | -45.65129 | 2025-10-28 00:52:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 5bebe4ac-fdc1-3cd0-ad7a-97e3956cb977 | -10.30259 | -47.24646 | 2025-10-28 00:52:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8a2f4771-50b4-3b98-a117-9f766b217be2 | -12.53586 | -47.54087 | 2025-10-28 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 346406ef-ca11-3a97-a9a4-a0a2e01f422a | -11.03685 | -52.30975 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 200e2649-a0e5-3d26-afcd-6214847dd31c | -9.91248 | -47.67712 | 2025-10-28 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| bfe566f9-8564-360e-b5ed-6ff00be502ce | -12.53289 | -47.54703 | 2025-10-28 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| fcc7ee3d-d779-3163-aea5-d0a12d2350a6 | -12.63573 | -45.08744 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| de6a53d4-7490-38c1-9d9a-5503f7bc2f53 | -10.9343 | -50.26435 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ae6100f5-ad48-3b47-806d-b51392e1f1f2 | -13.04777 | -48.40861 | 2025-10-28 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f64d45f6-1b20-3c04-91bf-337874de6da8 | -15.14782 | -46.63323 | 2025-10-28 00:52:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 25.2 |
| f6bfd800-42ae-3de0-9d53-8a1f68a85468 | -13.3143 | -48.3443 | 2025-10-28 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 78690f5b-6a2d-32c0-9869-1c06bf03e3ec | -9.33869 | -50.35189 | 2025-10-28 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ac7a93b7-fe61-3883-844d-d3c4f38bc319 | -11.63948 | -48.53436 | 2025-10-28 00:52:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bf6a5ec0-51d5-31a3-909c-c82ca1507cb5 | -9.13165 | -51.30629 | 2025-10-28 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f288f994-7ba7-3abb-baff-3b6bcc085a88 | -9.22064 | -46.347 | 2025-10-28 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6fbbab0d-7501-35d1-84de-422fb5a5b86c | -13.91378 | -48.48514 | 2025-10-28 00:52:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8f308360-10a8-3ea2-9b5a-70c5ea03c209 | -14.08191 | -44.1552 | 2025-10-28 00:52:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0d6b3844-87c3-3bf4-baae-a837c6cc8776 | -10.92407 | -50.26598 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 0968672c-4eac-3566-94fa-8bf90975d7c1 | -9.10688 | -48.9066 | 2025-10-28 00:52:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9ebb675c-16cd-30fc-a5ab-8413da6e6a43 | -13.63714 | -46.97066 | 2025-10-28 00:52:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e8d9cc21-b1ef-33bf-a0d8-85cc970a3f23 | -9.04076 | -46.92632 | 2025-10-28 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 5b27e517-1ab5-31bd-a1f5-83d90c740d12 | -14.76258 | -44.96335 | 2025-10-28 00:52:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 53026d45-2b19-38c2-99a9-55b56d602ac6 | -10.52907 | -49.547 | 2025-10-28 00:52:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eae9195c-333b-3d75-b891-68b416e6729f | -13.54372 | -44.13539 | 2025-10-28 00:52:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0a32314f-1383-3817-bdd7-4b694d9e7d1e | -11.28461 | -45.51367 | 2025-10-28 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| d5cf6092-2da4-3f0d-8c57-2f6a42cbf934 | -9.56365 | -46.97223 | 2025-10-28 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ffdfcf6f-b182-33c0-b3b9-a9bc2beeadc6 | -9.04458 | -46.94962 | 2025-10-28 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f5b07e10-c23e-3e95-90c8-b8c223ba41cc | -14.0245 | -48.74036 | 2025-10-28 00:52:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9558cc35-5691-3b76-89e4-e832d99b8aeb | -13.65949 | -47.64009 | 2025-10-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0d057e37-c83d-3cf0-958d-d98db9e330a0 | -9.2183 | -46.35294 | 2025-10-28 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e5d820a8-7744-3dab-bd8f-329f1e9b50cd | -10.92589 | -50.27822 | 2025-10-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 9b071ebd-75f6-3a3b-b209-a56b50ddf958 | -9.45946 | -47.72213 | 2025-10-28 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 18cd2ccd-4cbb-300d-8240-a53ca5889794 | -11.28462 | -45.51905 | 2025-10-28 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9534d06e-e858-34a3-92fe-538b26cb88e8 | -13.84212 | -49.05662 | 2025-10-28 00:52:00 | TERRA_M-M | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| eb2d5615-9a88-37ee-93bb-d9ed22f6e87c | -14.6629 | -48.41307 | 2025-10-28 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4d3b3f24-7e06-3832-8e90-2fe31aed416c | -9.41485 | -49.33445 | 2025-10-28 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| a7db6987-cbe9-39a4-9a23-71d84738e22e | -11.73159 | -49.33728 | 2025-10-28 00:52:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a211ba31-67f1-3d80-88a4-bd677b200bbf | -13.88261 | -48.51291 | 2025-10-28 00:52:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e6639221-fddc-3d4b-afb4-834cdb9ed58a | -12.18624 | -43.57407 | 2025-10-28 00:52:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 7e7857a0-8151-3558-a5a6-ecad7b145d14 | -12.52363 | -47.54298 | 2025-10-28 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| c155cba3-1d1c-33d0-847f-fd63acac9967 | -13.55453 | -49.58126 | 2025-10-28 00:52:00 | TERRA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 8296ec30-001f-3de1-8aa3-14872c336382 | -11.84981 | -47.92766 | 2025-10-28 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4e13bbcb-fb45-3351-8606-b48ab9853a35 | -15.14457 | -46.6135 | 2025-10-28 00:52:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 7c227987-27a3-35a6-8c98-04921ef4e15e | -11.60498 | -48.54016 | 2025-10-28 00:52:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| df3095f8-9dda-36b9-b8df-390d2621295a | -5.6975 | -49.19755 | 2025-10-28 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| c52fe312-d94b-32fd-a649-4a6fe109be66 | -5.84408 | -46.45375 | 2025-10-28 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 087e33d6-becc-376c-a606-480085f9d33d | -2.75949 | -47.74606 | 2025-10-28 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2abe6a4e-f755-337d-bbaf-6a685f022ce9 | -3.70127 | -49.56782 | 2025-10-28 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5e3c6917-590d-3ca1-b430-4995fc921fec | -3.48041 | -55.45989 | 2025-10-28 00:54:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4bd8d56d-6c3d-3aaf-a792-b24e1dce2d31 | -7.24726 | -46.81136 | 2025-10-28 00:54:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 12f0b45d-365d-30a3-97bf-9ededd659999 | -2.82692 | -49.41317 | 2025-10-28 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| fc42b805-9ac4-3ae3-8219-e665411a2474 | -1.55738 | -55.4192 | 2025-10-28 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ef6bae90-ad4d-36a4-9f20-b46bf0b072af | -7.32019 | -47.20794 | 2025-10-28 00:54:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 66585940-87f6-3369-8117-743f8545e7fb | -3.86984 | -55.69187 | 2025-10-28 00:54:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 16753b35-25e8-369d-97be-d598b042aafa | 0.96837 | -51.11726 | 2025-10-28 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 57eee175-86b3-31e7-bad5-380410b3c481 | -3.23772 | -50.64573 | 2025-10-28 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ff114b99-15b8-3319-82b0-4b30be51316d | -3.70664 | -47.64185 | 2025-10-28 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c99fc5f7-ead9-3877-a307-abbf6a52f9cc | -3.64848 | -49.91743 | 2025-10-28 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 27daa89b-98de-3f6e-a636-cad56f73fc94 | -6.8506 | -50.1155 | 2025-10-28 00:54:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 149f7e9b-6366-327b-a293-3a050c52eb90 | -5.20574 | -50.57677 | 2025-10-28 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c0e36df8-c586-378d-96a5-bfa5f7720206 | 0.40504 | -50.81203 | 2025-10-28 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 862f5a45-4809-3d5a-8c1a-f060ad4e880c | -7.92431 | -49.75031 | 2025-10-28 00:54:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 1eeb82e4-5be6-3030-aedf-21921cfb96ef | -3.53165 | -51.57257 | 2025-10-28 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aed11666-e949-339b-afd8-2ec52c4cce65 | -1.69361 | -55.67165 | 2025-10-28 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c310f3c2-1e94-36ce-8d49-2fbcf85a751d | 0.41327 | -50.80176 | 2025-10-28 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 89a95b47-913b-368a-be08-927e75c711f6 | -1.70414 | -53.69731 | 2025-10-28 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| de7424ec-6907-3000-a3ad-16dd15c536ce | -4.37226 | -49.67378 | 2025-10-28 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e09628cf-abca-3ebd-9b5e-dd6ac0271cda | -5.4772 | -47.74989 | 2025-10-28 00:54:00 | TERRA_M-M | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 58bcda9c-edeb-3c3e-b53c-654e244561aa | -1.50339 | -53.1338 | 2025-10-28 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2d520287-ef2a-39b6-8ca3-45a3ae788add | -7.46941 | -47.17116 | 2025-10-28 00:54:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 30f4bd36-f764-3019-84ae-0dbe9edc97e8 | -7.93324 | -49.73387 | 2025-10-28 00:54:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| fba1aa6e-32fb-3688-aac1-4bdf4db39a8f | 0.98235 | -51.10273 | 2025-10-28 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f6474824-805e-32a8-9072-e512747dde36 | -2.20498 | -56.97656 | 2025-10-28 00:54:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4ac83cb4-c31c-36a5-ba51-2711108d71c9 | -7.45971 | -49.41444 | 2025-10-28 00:54:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| a48312c7-2ead-3eb8-86ea-4d24a430f7ce | -5.48342 | -47.74257 | 2025-10-28 00:54:00 | TERRA_M-M | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 6d4019dc-d192-30d2-9621-19852171534d | 1.04476 | -51.3126 | 2025-10-28 00:54:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f88abb34-3e60-3c47-8670-b10c943be441 | -2.75503 | -45.3975 | 2025-10-28 00:54:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.3 |
| f9693848-7b57-3c47-b5b9-c862f52600ad | -7.97838 | -46.72381 | 2025-10-28 00:54:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 6c2b7634-d604-3a00-9717-222b83855aa7 | -3.80005 | -51.10816 | 2025-10-28 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 046234ae-1609-3ed6-b924-700077711ab4 | -4.3833 | -56.27043 | 2025-10-28 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 482f374f-b243-3648-a1ae-ea643038612c | -1.48987 | -53.13129 | 2025-10-28 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b8a28e4a-c878-3496-a4e9-e9cdd1cac482 | -7.06904 | -47.36567 | 2025-10-28 00:54:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d48195c4-3769-31e4-8700-1eee34da5fdf | -3.40088 | -50.2731 | 2025-10-28 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 769dfe78-535f-3808-8149-04498ac3aa40 | -7.97128 | -46.74519 | 2025-10-28 00:54:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 10bd6921-1a96-3174-b28e-3eea882db826 | -6.9986 | -47.00306 | 2025-10-28 00:54:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 09721c19-1b21-3d8a-9910-960b859997c0 | -7.67668 | -47.41109 | 2025-10-28 00:54:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ca133fca-3ffa-30ba-bbe8-7e5cbd56212a | -3.13406 | -53.00638 | 2025-10-28 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d392b7ae-b061-3ae7-8437-3471b0cb6fd2 | -5.64988 | -47.63329 | 2025-10-28 00:54:00 | TERRA_M-M | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 4a5befba-a0ba-30b1-b887-b78a697bfee2 | 0.96613 | -51.13332 | 2025-10-28 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5dc9a0b1-91b7-365a-b9e2-cfe9f3a5221a | -2.19724 | -56.98695 | 2025-10-28 00:54:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cdf4d18b-f919-3aa2-936f-1967519b4e2c | -4.71054 | -46.43289 | 2025-10-28 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5bd5aa09-1609-3e36-8ad7-9eb287266052 | -7.27414 | -49.86422 | 2025-10-28 00:54:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7f7b2e92-5d2e-3be7-94df-28a575874b5b | -4.35784 | -50.52273 | 2025-10-28 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 65d4e0a7-b02c-3fb3-9781-66eefb00db53 | -3.83905 | -55.79504 | 2025-10-28 00:54:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9f397105-c8d1-35af-8d77-52974e9d2656 | -4.85303 | -50.68239 | 2025-10-28 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 63c1905a-c3df-3b36-aa45-e50d78e27bc8 | -7.9355 | -49.74868 | 2025-10-28 00:54:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |


[Clique aqui para ver as próximas entradas](README5.md)
