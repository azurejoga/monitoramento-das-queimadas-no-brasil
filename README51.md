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
| 86aa57f3-65aa-3fb3-af7b-cda10c8b2365 | -2.72811 | -48.34435 | 2025-10-25 05:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc52e3a3-8ae8-3555-8a2f-9254b9eca6ec | -3.14407 | -50.15991 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5da12511-34ca-3a86-8c67-de629f72a6d7 | -3.08636 | -49.47293 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f1c401f-ba52-3d6c-b2a3-05be1365863d | -3.16695 | -48.60714 | 2025-10-25 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 150ab853-0454-34cd-a705-cb2e21ed7e30 | 0.36047 | -50.92154 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84406d46-6765-37a6-87ab-bae9e7595e4c | -3.08709 | -49.46812 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8bdd1d8-54a6-3985-8605-b698f198d554 | 0.274 | -51.39319 | 2025-10-25 05:08:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc0765c3-b3e4-3202-ad19-a603d380ce20 | -1.20466 | -54.01522 | 2025-10-25 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 774f998c-4e90-3d34-9546-e1340c1f0866 | -2.58351 | -51.34665 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bccea572-44d8-39dd-94aa-290d1d52dfa4 | 1.64005 | -55.72621 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 968b5d2d-23e9-34e7-aa47-954a34ee840c | -2.7964 | -49.136 | 2025-10-25 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a39358ff-0f81-33b8-87ab-25f4a5ee943e | 1.6386 | -55.7455 | 2025-10-25 05:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| fbf28d37-3683-372d-abc4-b602de2d3e34 | -2.8149 | -49.1354 | 2025-10-25 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d92cdd9f-5a1f-363d-b8e9-4d036517bc23 | -9.26376 | -59.49115 | 2025-10-25 05:10:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bd26de6-6c1b-3274-9340-c16295c3262c | -4.87606 | -47.53145 | 2025-10-25 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ef14db4-a394-372f-9373-c73b4b9b64b0 | -6.89588 | -46.36648 | 2025-10-25 05:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32cf6f1c-f7c2-3e0b-a258-35f05e7b2a12 | -4.80965 | -45.581 | 2025-10-25 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1572f1f-c6ea-3644-8406-90ad1bb29223 | -4.24599 | -48.55293 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0161e05-2bb2-3b4c-afe5-69877c8bb60e | -6.89529 | -46.37097 | 2025-10-25 05:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62cb7d15-96ca-3a45-b56e-58e0bc27c0d8 | -9.29237 | -57.54537 | 2025-10-25 05:10:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7f8818c-14e7-30b0-838d-7fb9f2aa3144 | -11.06423 | -49.62675 | 2025-10-25 05:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ce494889-9cb5-3d5e-a18c-518edd34ad8e | -6.24693 | -46.39606 | 2025-10-25 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce4bf9a-ef3e-3a24-bbbe-7af01bd06567 | -5.65336 | -49.06652 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ed59bd4-938c-3122-b3bb-24ecde990947 | -5.00264 | -47.76198 | 2025-10-25 05:10:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2a36bd0-fa35-3bb6-b25a-71d0b764d1f1 | -5.72432 | -49.09998 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6e8073a9-96e5-363d-9abb-5245cc071e36 | -8.54867 | -50.04731 | 2025-10-25 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e6caa53-837a-388e-9be8-0304fa0ba40d | -4.90199 | -48.97042 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b16139b6-10fa-3afd-9bcd-8a203c67db5b | -10.87049 | -48.05233 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b096c863-f648-3f0c-8f22-16af22ed5c04 | -9.57355 | -49.67791 | 2025-10-25 05:10:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 462d3bb5-6682-3c14-a294-6bdbd0a566d7 | -6.91165 | -45.1713 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91bf6ff1-b049-3a20-95d0-b83777d42c52 | -3.39286 | -51.53772 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eb353a4-eee6-3938-9a00-c9a2ca700bd7 | -9.4539 | -56.64934 | 2025-10-25 05:10:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbab385b-8283-351e-aab0-2405eaa7e5ea | -6.2438 | -46.39473 | 2025-10-25 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1060203-4df5-30d8-9e5f-916ec88b6820 | -3.33889 | -51.65145 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94d45aff-f297-3f49-9b6d-b41fc842b964 | -9.95131 | -54.74278 | 2025-10-25 05:10:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a27cb79a-65a9-34d3-af93-0e3479fce2b8 | -10.58949 | -49.64296 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae0664be-6636-3b0b-b0a6-6c036f01de25 | -10.84685 | -48.96973 | 2025-10-25 05:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3b67758-2230-39ee-968e-429de95d1559 | -10.83888 | -48.81225 | 2025-10-25 05:10:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0198de91-f5ed-3b00-b68e-10256480efe1 | -9.28853 | -57.54832 | 2025-10-25 05:10:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b28df07-98f5-33fb-b5f0-f0637bf10b5c | -5.70757 | -49.3066 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1691fd1-d32e-3dc1-baf9-641587078cee | -4.90976 | -47.65912 | 2025-10-25 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d941d116-1106-355d-a9e7-12eade011aa3 | -5.70682 | -49.31207 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53df362c-2c4c-336a-ba86-c16e6f0ba92e | -10.64484 | -48.06018 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0213d7b1-f95b-3868-a960-a724588f6dd9 | -10.6254 | -52.18605 | 2025-10-25 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f9da1f6-269b-3991-8398-6f53296e9e60 | -3.86894 | -51.89376 | 2025-10-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf66d294-4ace-3abb-88af-6120dc0d3f54 | -5.70794 | -49.31685 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 214cddef-fde1-3c52-b7be-a81f9694c5db | -6.91948 | -45.16226 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a26b0a3-3cb5-31f6-bb8c-79c46fc0b646 | -9.92901 | -48.00224 | 2025-10-25 05:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc12d333-b13d-30fe-b93a-2f127025f67b | -6.11261 | -49.03756 | 2025-10-25 05:10:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf08fb1a-833a-3c26-adf7-498c35d335eb | -8.61026 | -54.95929 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 552a7be3-1d86-33c9-bf8f-85e85a0bc1cf | -10.66671 | -48.0702 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fee90ecd-b0d2-3f49-9924-fc896096b863 | -11.05618 | -48.32162 | 2025-10-25 05:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6be81aa-561f-3f24-91ed-f3df1e549eac | -10.82493 | -47.99733 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18c2e8c5-dd56-3519-b7f8-f30400da1996 | -3.69157 | -49.94077 | 2025-10-25 05:10:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a76655c-8879-3820-8d02-28171ab5190e | -3.82767 | -50.19793 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4731d37-757b-3195-b9ec-c584078b2b80 | -8.63853 | -54.55693 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 178dd9be-0277-3f5a-9238-093f42f95acb | -9.28961 | -57.54137 | 2025-10-25 05:10:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2c6d826-4073-3c78-af0d-6f822a67a2f0 | -4.96225 | -47.59993 | 2025-10-25 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dd5de6a-0d96-3403-9f1b-4754920a806b | -3.9181 | -47.69291 | 2025-10-25 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fdd3a159-898e-35e3-8597-372a711fb261 | -4.21843 | -48.35727 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a38334e0-d1c6-30be-92d5-e982fd490ce9 | -9.95706 | -48.26418 | 2025-10-25 05:10:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 275b6619-b982-3fdb-aca0-c0749e34d224 | -10.89556 | -48.0373 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 732f9a4c-00a5-3bf3-bae1-24af988205b3 | -8.54938 | -50.04199 | 2025-10-25 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c875ad2f-507f-3296-ab52-83e3413b9b2b | -4.83504 | -50.92973 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d2dd5d3b-0b68-3fb8-9bab-a7b65b1de2dd | -4.55243 | -46.68436 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 08752963-712c-305e-a050-740e301ace99 | -9.17805 | -48.84956 | 2025-10-25 05:10:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ba4a615-351b-3788-96a4-ecbe4f8d7f2e | -5.47923 | -50.17333 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7803e2ab-40e3-3309-9064-da23ca156584 | -3.79496 | -51.35951 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c7fbec3-a2bf-3d1f-8cac-3186eab81bf5 | -3.29689 | -51.59099 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0794aaed-b4b8-3cfb-b73d-192159a063f6 | -3.99089 | -50.5227 | 2025-10-25 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ad5f04e-a730-3418-be4f-f2673c3d28e0 | -6.23723 | -46.39823 | 2025-10-25 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c778f3f5-ee96-394b-b1af-6a2df0b978a6 | -5.59392 | -52.17186 | 2025-10-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8d2c772-5fdc-3b15-bcb6-cf0c0b759985 | -9.4578 | -56.64627 | 2025-10-25 05:10:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc43a826-21e7-3fac-b795-8dd1118c11d5 | -10.95344 | -50.29144 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b45240b-d672-3f8a-a221-6a5a4871f664 | -9.74841 | -47.8364 | 2025-10-25 05:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 307db904-3305-357f-8045-68df3c111a20 | -3.31037 | -50.78946 | 2025-10-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a02e8a1-a77b-3914-855f-cc4ece8c596c | -7.43925 | -46.60646 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ebcb879-3839-31be-85bd-243845cf0bfa | -9.59713 | -46.86593 | 2025-10-25 05:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d1527a4-20c8-3fc2-a71c-25797ad5868e | -7.7062 | -55.50002 | 2025-10-25 05:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b8a5c81-876a-3ae5-9159-558678ea73e7 | -10.95551 | -50.29215 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2538c71b-2741-3c8d-9c73-63b85f9bd84a | -10.80291 | -49.64981 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 129499e0-61b5-3684-be0d-8dff130e16c7 | -10.80252 | -49.65287 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ce5657e-547b-3080-86df-71ab5fccc613 | -4.84302 | -50.93501 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2db9a8a-138a-370d-865f-0cf29c2849bd | -10.64313 | -52.18446 | 2025-10-25 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d9deaa7-f7c4-3228-b28a-ccc3d1ab0218 | -3.83257 | -50.97271 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5148275b-43a3-3513-9aa1-f1881b54eabb | -11.06462 | -49.62365 | 2025-10-25 05:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0abfbcde-4ba6-379a-b217-8b9320118b32 | -5.8136 | -50.19838 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 985c2ac6-381c-386b-ac27-8e04cddee0e0 | -3.69039 | -51.3348 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9d04395-794b-37d3-a19c-f0dd00519a82 | -2.69188 | -54.76945 | 2025-10-25 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec173d5c-ef57-372f-9af9-67296cbeeedf | -9.32328 | -45.19149 | 2025-10-25 05:10:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b0be3f6-20bf-3c2c-ab63-ccf0fcbfe643 | -6.91818 | -45.17199 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 99a2c4fd-8bed-3dcd-89da-6419694863e7 | -5.81742 | -52.09795 | 2025-10-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 835925b8-b4a0-3d8f-9c06-668aaa2abce1 | -4.21428 | -55.72147 | 2025-10-25 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df170334-e03d-35fe-b8e5-f4d0031e5cc7 | -3.10028 | -53.17159 | 2025-10-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2391da7e-a4b0-3e44-93ac-bb251ec8dd95 | -6.88763 | -43.61947 | 2025-10-25 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 45ba039d-283b-3450-9a80-c720b923b265 | -10.70795 | -51.87037 | 2025-10-25 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 593b0e94-23d2-3df0-a935-24b57951dc30 | -10.63876 | -48.06261 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 166cdd80-b756-39b9-a539-913d3014116f | -8.55934 | -49.85557 | 2025-10-25 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a18e1baf-87ef-3f96-b173-04fadaf88354 | -4.83134 | -50.92514 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2da75271-5064-3eb0-902e-66eb4a4916fc | -4.8158 | -45.58195 | 2025-10-25 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README52.md)
