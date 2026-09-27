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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 997f6348-d51f-3f73-9dcc-3ea2f8c25de2 | -2.51194 | -56.22507 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07d168cb-3eb2-3307-a50d-ffbc6ee883f2 | -4.57547 | -54.92524 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 304ed387-eeed-3224-ba22-726c7c1f622c | -3.09254 | -49.35309 | 2026-09-27 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 353c9c08-8551-339c-9b3d-c9dbdda1b0c3 | -0.52156 | -49.12791 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d74ef281-9ad8-3aa0-b9fc-4f9984dae7cd | -2.66783 | -56.45521 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64e52ddf-3be2-3a2a-9726-b32495ece5e2 | -2.06212 | -56.86864 | 2026-09-27 05:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9be8107-820c-35ad-86dd-882902adc4ad | -2.65765 | -56.54293 | 2026-09-27 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81ec3f22-2b02-3535-bdde-45cee9e250c2 | -5.88379 | -51.94026 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fe8ee06-263f-34da-b612-b5032e0d8e26 | -6.09657 | -57.62226 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 812ce5b3-ba30-369e-a4f9-8c169e48a367 | -4.0506 | -45.33545 | 2026-09-27 05:27:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 410451f1-778e-39d3-b586-035432c01aa6 | -1.11943 | -57.2764 | 2026-09-27 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d92edf37-a901-3ba4-b9b5-6518cda7b0c7 | -3.22639 | -54.32442 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 469f941c-d0c1-3624-a98e-8e7b8131b8af | -3.20072 | -51.03406 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3e5381b4-e67f-38c5-8101-6f6741b6f45d | -3.71601 | -54.65059 | 2026-09-27 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c52d549-1197-3383-b0e2-80562e74e266 | -4.5421 | -54.96985 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf231c66-9e6f-3473-8143-4461ef09ede8 | -3.98183 | -56.13069 | 2026-09-27 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 536821bc-c01f-3c7d-8362-d229d749241a | -3.94826 | -56.09422 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c53c001-78e0-3e80-be47-001622845909 | -1.11194 | -57.06541 | 2026-09-27 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3524785d-0de7-384d-88c6-a8e183b4b83e | -4.97733 | -56.15126 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a415b3b-17a2-3882-887a-cf2e6f79e0b8 | -3.21412 | -53.95358 | 2026-09-27 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c209d93-ecf9-33a7-991a-21d845cf60b7 | -4.29763 | -55.25465 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4dd9c49-cc33-3d07-8003-cc1a73d2732d | -5.06936 | -56.06837 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38e09616-a5bf-32ea-a02c-228657dd24cb | -2.72921 | -54.19809 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef7a3e96-1ba2-3365-b3a8-eec9366a1ef9 | -3.22331 | -54.31926 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 653df6d2-f659-3579-87e3-447c38829163 | -6.08871 | -57.62835 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3fbb801-08a2-3440-b20c-0844dd2f4a86 | -2.55121 | -56.28779 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b80dcf9-9231-336e-868c-219c3d905fee | -3.41982 | -50.41859 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2b1a08d-ae74-3a7d-9bcb-abdb3f9e1abf | -1.14244 | -54.08686 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c0831ea-6169-30e7-93ab-d4f9edd1f942 | -5.16859 | -56.01 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a01d56ca-e7c6-38cc-973d-53e6b5e72d6d | -2.93132 | -56.57719 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cc5ff90f-d150-3b8b-a0fb-6eb1e943865e | -4.54015 | -54.98272 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a732d3fc-b6e8-3455-9fc5-bd8ab815464b | -3.19999 | -51.03889 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c2751216-81f1-3a27-a52b-133d0dd6f2da | -3.97075 | -50.71327 | 2026-09-27 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 92b64ccf-e7a9-3110-aed7-a055f010452b | -2.02001 | -52.11396 | 2026-09-27 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2fcd865-ea9f-3ac9-bcab-5152963afab0 | -2.89151 | -49.48361 | 2026-09-27 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01547e93-5185-3b17-9555-2bd7f31ba1bc | -3.86599 | -55.81309 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a7130d7-2155-3720-8e12-c055e61c8796 | -3.07548 | -54.40262 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a68caaaa-0296-345d-a88e-92eb6cbdacaa | -3.42309 | -50.43031 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 988a6cbb-b673-3666-8cd9-86b9c227a1eb | -6.77608 | -48.66071 | 2026-09-27 05:27:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb248078-a016-38ce-b54d-6a50b46e5316 | -0.53813 | -49.18896 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18946f2d-7d9c-3247-9ec6-a01bb5007858 | -4.36047 | -55.28139 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffa9615d-2a40-36b0-968e-8552e420d1c0 | -3.00975 | -54.20263 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e8594a1-0c25-39fe-96c0-248915141b20 | -6.05898 | -53.61096 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80fe5cbf-b435-3833-8235-2df173635c78 | -3.83692 | -55.90845 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c86da0eb-c0e7-3779-af66-64efb97c5384 | -3.27231 | -50.14464 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93a9760e-6b32-3c46-a3b8-747738ab9f80 | -6.08048 | -57.81329 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f474148-7fa3-3024-acb3-9a366843eb55 | -4.46294 | -55.03056 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca6d7f18-c4e0-3fa7-bf9d-9fec06287c2c | -4.98146 | -56.1479 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b01691cc-fc91-3277-b4d0-ec13c16d02ac | -1.21704 | -54.55806 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9605acf5-451a-36be-ac6c-ea8629b7e236 | -6.06426 | -57.82889 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17b8772f-12ec-3e62-8a4d-12941c0a1fe3 | -3.23017 | -54.325 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a09be81f-2859-3181-9ef2-9cd30427c186 | -6.05959 | -57.7044 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2816bd45-6794-3e91-bb04-89fbb3972d0b | -3.0599 | -50.33871 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02478afa-ac94-3aa3-9161-b9b3e56de052 | -4.21768 | -56.05173 | 2026-09-27 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d743a9df-6018-36da-8ba1-45d17a68e99b | -5.73719 | -45.06301 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63301492-a8c0-3a6e-9d60-0e24d0f86cd9 | -3.86186 | -55.81646 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1e6d51b-bb9e-393b-a1ec-242ce5d83130 | -3.21337 | -53.95847 | 2026-09-27 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01c7abd6-7f81-3a84-abc0-7d40f75c25fe | -4.49046 | -54.95047 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 74c73255-7ed1-34d2-a01c-9cc555281284 | -2.73393 | -49.46275 | 2026-09-27 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89216544-dc72-3bcc-9ed0-c72f2df07e67 | -4.24144 | -55.16174 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 397ddcdc-f569-3d9d-bb9b-b66c2a4611a7 | -2.9251 | -57.66238 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11eff5d3-402b-3e30-bdac-c9fb0bfa6a4d | -3.9674 | -59.34235 | 2026-09-27 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abc6c6e6-6353-33d9-8dd5-7a25d7832455 | -4.3478 | -55.77409 | 2026-09-27 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b02ba26-a60c-3ce2-9ca6-803da1deb2ce | -3.87714 | -52.28754 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30ab04f1-0c67-3730-ac7a-6129d4e57baa | -5.86573 | -57.56148 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59feab56-8071-31b2-ab28-e1a5a808826a | -6.07043 | -57.83349 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6b03ad8-91c3-3994-9d86-0b998a5e452c | -4.14178 | -48.22035 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51a49a67-355f-392d-9866-ca0e1c7698d9 | -6.07656 | -57.81631 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93c50620-ede1-3157-b9d2-71ff3f42b262 | -2.65425 | -56.5424 | 2026-09-27 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 582403a9-945e-364b-bd2a-5b70cd254494 | -3.97075 | -59.34288 | 2026-09-27 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 274cbf76-5806-31aa-8db2-8bbb27767d90 | -4.51031 | -54.94477 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b66d4b9-627d-332c-b82a-9ea4ce705905 | -4.26144 | -51.04429 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 027fce75-e1bc-3fde-b068-85002c34ddb0 | -1.22943 | -54.12147 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 637e4a29-40e4-371a-b3a2-7bc7a28da8e7 | -3.22708 | -54.31986 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a42ab3c8-6549-384b-8dac-8a7bc77bf92b | -4.46513 | -55.42638 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62ec6197-ec2a-3ca4-9ec1-aabdb2ce5d17 | -5.73591 | -45.01986 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e5edfdf-5675-3ff5-89e7-af41298f0131 | -3.29812 | -52.08599 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 498d1c94-26c4-31a9-abc6-fba1f5908667 | -4.49113 | -54.94614 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 62c01a69-64f0-31a2-abf4-b58c420aeb36 | -6.12826 | -53.05201 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82a1ed71-2c12-3a5f-ad0f-742f2077efb0 | -4.87676 | -55.84612 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a656926-f77a-391d-9b07-2bc767190ae6 | -2.13266 | -52.35704 | 2026-09-27 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 164d1bd3-d16d-3bad-b68a-ee49e99a9b93 | -2.73161 | -54.90666 | 2026-09-27 05:27:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24f00907-c7e7-3887-8982-82c7fec447b9 | -6.62387 | -52.99266 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 444f81ac-39bc-32ac-9c47-615f1b09d78a | -6.07992 | -57.81683 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 207cca49-e37e-3083-aabb-23e13356d85f | -5.68005 | -50.09685 | 2026-09-27 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 394a1df8-d936-31f2-959c-d982249a4db7 | -4.09663 | -54.32632 | 2026-09-27 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bec4adab-d7d4-3f76-958f-5f2750a75ae3 | -4.71723 | -55.71721 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 095e40c3-5b35-3994-ad48-3e47e0afb54f | -3.85217 | -49.13274 | 2026-09-27 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e856c05-81f2-3896-aca9-150c74027021 | -1.21929 | -54.56724 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37025e3b-780b-3664-a06a-af97342da88c | -2.50001 | -56.14369 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df73598d-0169-3160-bd9a-73614d735821 | -6.07712 | -57.81276 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d837b1b-b4c3-3dd8-807d-d7b3761e68f4 | -2.9064 | -45.42548 | 2026-09-27 05:27:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c716de56-edab-3244-979f-cefc7d4811bd | -2.96415 | -49.56448 | 2026-09-27 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3924c65-1dc6-3120-82c0-8b617f19af9b | -1.7428 | -55.242 | 2026-09-27 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66e8e054-5450-3654-8ba7-210b48b40f10 | -4.50722 | -54.98883 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5b67f5f-69ae-3c6d-b05a-5af117fc2928 | -3.00906 | -54.20719 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 786df0aa-cae5-3958-8b3e-12b896037386 | -1.14781 | -54.10122 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2df9acb6-f7ed-30d2-bbd8-e5592df4a5f3 | -6.13253 | -53.05265 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 686aa9dc-deeb-30da-a739-fec1b40fc240 | -3.29742 | -54.68909 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7ac6556-95a7-3261-b377-c5cb66f64847 | -4.14705 | -48.21894 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README42.md)
