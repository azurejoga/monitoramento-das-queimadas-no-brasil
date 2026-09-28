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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5abdacb-0ccf-342c-95bb-86501ae2f88a | -7.37829 | -42.11803 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fa8f60e6-39a8-333d-a464-dd6978a2b5e5 | -6.02015 | -57.67612 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d951f8ac-7144-3a72-8a9a-e80cd1b0e911 | -8.66072 | -45.42469 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf67cdca-a099-3f13-9082-cd56b8120dfb | -3.04648 | -51.33442 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 087274d4-6885-3fc5-885b-11056cfcdc1c | -6.07287 | -47.29914 | 2026-09-28 05:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 083b46be-952b-38bb-8826-f55f2291557d | -10.21328 | -49.99207 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e249d65a-342b-3b84-aab6-f7e00ddfd461 | -2.05763 | -56.86758 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1ea4b3c-0f1d-3e96-b78c-f59e34c852eb | -3.50946 | -50.31416 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d44b1562-42e7-3739-a416-198577cbe47b | -6.74015 | -55.08611 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5afd12aa-64fd-3207-a89e-a40c759e1a81 | -8.24154 | -45.40346 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 150eaee4-4bc5-301a-800b-cd16d41d8cc0 | -2.66132 | -51.73681 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca194c78-43b8-3c07-8c41-1005f5665007 | -2.79803 | -57.70164 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a37cff6-d338-3a51-bef9-599d68a649d6 | -9.98193 | -50.16333 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| aa7dc8ea-cc90-36f6-9f9b-197bc4b2534e | -8.01958 | -43.73893 | 2026-09-28 05:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 60fb0156-5a15-3cc0-aa86-ed2386c34612 | -2.99734 | -50.47279 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a15a65c-0e02-33ad-a938-40359d2877c6 | -2.94676 | -54.08876 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 49f8b9b8-b46d-32e3-9d45-90bf6669ee1b | -10.21532 | -49.97778 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b9d86d4-33c8-35c8-894b-b0b59afd9c48 | -3.12627 | -51.7326 | 2026-09-28 05:10:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0c82807-290a-3044-8ab8-e1c8fe57d1e8 | -9.97869 | -50.15755 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f4fe94cd-5c6b-3798-9bff-19efa094aa87 | -8.10353 | -44.0049 | 2026-09-28 05:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b525654e-ff8e-339e-b1bc-1e70a6fee6ce | -6.71069 | -45.59133 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4cf6d9d-1015-3cbd-a930-4279bae420f7 | -10.38002 | -44.97512 | 2026-09-28 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6496dc1e-27e9-3c74-9915-88dc991e1938 | -9.14185 | -49.96739 | 2026-09-28 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e4960d5-184b-309e-90cf-039de842f7a2 | -6.72623 | -45.59666 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 080635ff-5192-32da-bcdd-ccafc8cb1fdb | -3.27346 | -54.26937 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f66df4e-b3d5-339f-bb41-7abe98fa3a06 | -3.97056 | -59.348 | 2026-09-28 05:10:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01936bd2-8766-33dd-be6d-2cd942c8edac | -8.59918 | -54.64836 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f271f43-0d5d-35aa-b96c-5ee8bcf17c3e | -3.41938 | -48.33042 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e7b07df-d627-367a-a0cb-2384e5042feb | -8.23777 | -45.40582 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89c13cd0-7560-33f9-9179-6556aa4eb33f | -10.2143 | -49.98492 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2b962ce-9529-34df-a33a-7cb13e8ae19e | -8.66733 | -48.96358 | 2026-09-28 05:10:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00cf7071-0373-3ef6-8f2d-8535df89581c | -5.30296 | -55.8318 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a6d6a2d-094d-371a-b958-37b26672816e | -6.94322 | -41.61221 | 2026-09-28 05:10:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fa841405-1e24-3224-b654-c6996c51a377 | -8.96854 | -44.14489 | 2026-09-28 05:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 25e1ec33-de14-3edc-8a07-9fd412afee5b | -8.23745 | -45.43263 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c0423a4-3e84-39d8-843d-4aa630b7bbab | -3.0727 | -54.40675 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 82cae35d-daff-3ac1-a65d-a711f9bcce22 | -6.71589 | -45.59204 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68970c76-7b0e-3d72-8aeb-a8d1595b3db6 | -7.82812 | -55.13772 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c21f193a-aede-3d9c-9edf-3c3f2759ee7f | -10.22343 | -49.97898 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79220130-0deb-3dd3-9751-1465fd8a82f2 | -6.08612 | -57.79513 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6379b6ad-f2cd-3998-8249-5bca0883bd19 | -9.15442 | -46.75253 | 2026-09-28 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ffbc378-17de-3bcf-abb5-864236bfc918 | -2.93995 | -54.09487 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59b7a5f9-6a8c-364a-89c9-3b12c8abea4d | -9.98968 | -50.13793 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 82d02bbe-1661-3464-9fb2-ffc71f47f0b2 | -6.6971 | -45.64873 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a83140c-ef6f-3dce-9f81-9b025add0784 | -6.08239 | -57.79448 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 534f5beb-01fc-33fe-a200-0f2eb5363308 | -2.94191 | -51.97233 | 2026-09-28 05:10:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74ec2831-1bde-3121-839c-57631786d538 | -5.89691 | -42.43923 | 2026-09-28 05:10:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0af6d5d8-ea34-3c3e-997b-93527eea2f50 | -8.2379 | -45.42939 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 312d1b69-d680-32ae-9e69-fcbaf7752b06 | -7.37903 | -42.11258 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6e4cbb92-7c24-3808-bab5-4f9fc7f64887 | -7.89389 | -45.44455 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c29c542-4f14-3282-bd90-8beba498d00e | -3.29052 | -50.30864 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93a6d3e2-3f01-375e-b3ae-e851aa7ab335 | -6.16318 | -57.70565 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| add3a043-7b56-3a0b-be03-ed1be9d9062d | -3.41832 | -48.33749 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4a4149a-b799-38df-af19-679cbdc14945 | -6.78612 | -59.38092 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09e2e6f4-6043-35fc-b336-dddd3e413194 | -10.74973 | -48.91211 | 2026-09-28 05:10:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50192677-2b37-3c79-b8e0-a648a8dad949 | -8.02643 | -54.88971 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fafa7f84-86b5-3c38-81e9-90af3e84c953 | -6.76809 | -45.37112 | 2026-09-28 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a557de4e-b99e-3e91-ab1c-debf37e725be | -2.92332 | -54.19976 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b01015ff-6d5a-3bcc-b3b0-aa5c5f6f7b35 | -6.70004 | -59.96467 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1176a452-5f9c-3176-b322-e32e30edb00e | -2.89766 | -54.167 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5527133-40e5-3fe3-848d-cac0381cabb5 | -3.20918 | -51.03765 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3b4330dc-3198-3d63-b087-c3efd6d4cb23 | -10.25005 | -44.61441 | 2026-09-28 05:10:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7da392a2-80fc-399a-8931-39b18be43d61 | -6.71109 | -45.59136 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da515fe7-e77c-3013-bf06-b56abf7687fd | -7.71994 | -54.7724 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94c4a44b-ef13-3946-b3a1-ad35ee679bf5 | -9.99919 | -50.12868 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 096cc854-27e3-3445-9434-fdee70d06e7b | -2.78686 | -57.69271 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 231c8b83-17ee-378f-be60-9825ac619fe8 | -3.41885 | -48.33395 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca7dcfb5-b621-3fcf-8e01-8cda28f94f14 | -2.94621 | -54.09225 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5a2bc05e-dea0-35a5-a16a-5192af8552fe | -3.68219 | -47.49419 | 2026-09-28 05:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35fe1c13-19b7-3423-bf64-bb991a97087d | -11.18848 | -44.81573 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 8989e246-dae7-3864-b185-81e6919da5b9 | -8.36096 | -45.44634 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 620fea84-d9a3-3d72-86cc-8f5b78b64d0d | -3.10254 | -50.32385 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3abc5875-a542-3339-a3f8-fcfc5f4cb7e1 | -2.6738 | -56.46042 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c774931b-4489-36e8-928f-8a53f6095cf6 | -3.27124 | -54.26184 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c475c48-715c-370a-a433-339cc85fbc6a | -4.26714 | -48.55964 | 2026-09-28 05:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59d6d3be-a872-3a84-8e2d-2bb20abd6c22 | -10.70658 | -44.42793 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef0df781-19aa-3a78-b607-c1261bff6fd5 | -10.21227 | -49.9992 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e59adee7-fdba-3b5c-b557-5eb953921297 | -3.2078 | -51.04232 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c087a149-5b40-3572-aa8d-1128ec23099a | -3.20841 | -51.03846 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| de24d2e3-4e6d-352c-9add-cbf26b8ffdb6 | -5.13107 | -56.02456 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e632cf5e-3507-345a-b2d7-596735b6a553 | -3.20491 | -51.03792 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 367697f4-93e5-3949-91a5-3e3b4b498491 | -8.22741 | -45.48379 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb773472-0e06-3113-8d59-5f22916baadc | -6.76328 | -45.367 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e8bfaf8-39ba-3128-94dc-900b975c72d6 | -6.59428 | -47.16962 | 2026-09-28 05:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa6f0f09-aee6-3dd9-be60-d224b348c276 | -9.97943 | -50.15236 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 31cfec08-a107-3e4a-88a9-e3555ed647bb | -6.69393 | -45.97826 | 2026-09-28 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d013b8b-bcd3-34e6-a604-3946c5f6de66 | -8.03309 | -54.89077 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f1f6b3a-ecb4-3593-b777-9787b5887e6a | -2.99376 | -50.4722 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21c1f78-a263-38bc-acdf-00738874720c | -11.17211 | -45.13778 | 2026-09-28 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ba39afc-fcf2-361e-8be1-b1c4f2baac98 | -10.21682 | -49.99623 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 676192b6-a32d-3116-972e-7b586182ae77 | -6.77921 | -59.37227 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da36d514-dc1e-39c9-aadb-ed74011fc789 | -2.94329 | -54.0954 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95763c67-facc-3c5f-9475-54207997f82e | -10.21277 | -49.99563 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a16c381b-d779-3991-9687-c880916d0d7a | -3.26793 | -50.1415 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6bea69d-524b-3a03-880f-ae599636464c | -7.68112 | -54.85234 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62ad96b6-bf43-3d3c-83ed-ad565512ea6f | -10.88413 | -43.6898 | 2026-09-28 05:10:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d465a1e-d8bf-39e3-a73c-f54d8bc4d692 | -10.22948 | -49.99445 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28490aa6-0bf2-3e09-9294-53a6d16c1b3f | -7.0001 | -62.96968 | 2026-09-28 05:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf13d419-22cc-3bd8-b223-4d94bfdbd853 | -10.7959 | -48.73392 | 2026-09-28 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 293e2ddf-f7a7-3bba-9a75-491bcf5075d9 | -3.01415 | -54.20325 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README49.md)
