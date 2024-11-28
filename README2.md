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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 279eb09b-decf-3ca1-8cc3-813095f913a1 | -6.5593 | -39.200901 | 2024-11-28 00:03:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 46e84371-b2f3-339c-9d70-26794a3fcd08 | -2.2809 | -46.175201 | 2024-11-28 00:03:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 83bea143-d65b-334c-99b7-c393b269c38e | -6.1177 | -42.613201 | 2024-11-28 00:03:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4798843b-950d-3767-823a-0c72e51ed05f | -6.5578 | -39.193802 | 2024-11-28 00:03:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d0e8f73f-87a1-3aed-b1d2-dcb7fe4b0fe0 | -5.1673 | -44.903999 | 2024-11-28 00:03:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3313a929-1685-3f89-8eaa-f8f5e30ab7f9 | -5.0298 | -44.836102 | 2024-11-28 00:03:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9bbcf2bc-011a-39c6-9f0c-e843c6c863db | -5.527 | -43.1427 | 2024-11-28 00:03:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26649772-e843-301b-9340-4c53ddaa6184 | -4.7196 | -44.449799 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cec9ed4-0dd8-3cc5-a833-762729fc48e7 | -6.0489 | -41.930698 | 2024-11-28 00:03:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18ba02c8-8e41-327f-af66-c57fe5bd1fb7 | -2.2245 | -47.1035 | 2024-11-28 00:03:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| badeb29a-1a78-372b-987f-dcbd02bb3c27 | -6.3663 | -38.622398 | 2024-11-28 00:03:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6bd729a5-27bb-3fd8-a461-fd5504f83c16 | -6.3151 | -45.678398 | 2024-11-28 00:03:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b353f68-d893-3a9f-80a6-133d64178f0e | -3.6195 | -45.7617 | 2024-11-28 00:03:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc2857cc-3d43-35b0-8c72-b1445a36a404 | -8.9763 | -36.145901 | 2024-11-28 00:03:00 | METOP-C | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 86647264-9ca4-3238-895a-df36abcea4e2 | -4.0934 | -43.844002 | 2024-11-28 00:03:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fcf03ec-ae6f-3e53-af21-da206abc53de | -6.3248 | -45.6763 | 2024-11-28 00:03:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a06698d1-5d3f-359a-b1d1-2d481f1e7199 | -9.6797 | -36.4659 | 2024-11-28 00:03:00 | METOP-C | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 582e02d7-b73f-373b-b535-f8378726d3b7 | -2.0919 | -46.063499 | 2024-11-28 00:03:00 | METOP-C | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04d6a185-1f99-3c5f-ab5c-b93248b08857 | -3.9078 | -48.0774 | 2024-11-28 00:03:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd960618-8d25-3c6e-ae25-b4c064f5cdc0 | -3.3377 | -50.084702 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2d2d938-4351-3800-bf3c-b58b53b014de | -6.0444 | -48.0201 | 2024-11-28 00:03:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08935f46-53e0-30a9-986d-8040cd6e801e | -6.0299 | -47.999298 | 2024-11-28 00:03:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7a313ba-7110-384d-b793-b95196f5d6a0 | -4.0983 | -43.82 | 2024-11-28 00:03:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23ac89c6-ca1f-39de-8f0c-63590d9338e7 | -3.3281 | -50.0868 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc79012-4611-3b08-8b26-8e0db089b2c5 | -6.8561 | -38.101299 | 2024-11-28 00:03:00 | METOP-C | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 02f98ce8-cc44-3f49-8f3a-7f5ac6b56fb6 | -3.0415 | -41.135201 | 2024-11-28 00:03:00 | METOP-C | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 09dfa934-4937-3926-b21d-c5cfd3896cc1 | -3.9032 | -48.056198 | 2024-11-28 00:03:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ae2929-addc-3831-b855-2c739d374b98 | -6.1155 | -42.603401 | 2024-11-28 00:03:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83a4257c-8101-3960-afd7-038bffde3b67 | -4.7283 | -44.396599 | 2024-11-28 00:03:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd40296d-034c-39d8-971a-f6bb65911a9c | -4.7337 | -44.421101 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba9f9ec-138c-3517-ac71-106561d34755 | -10.4456 | -36.882 | 2024-11-28 00:03:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae5fcf2d-92e1-3adc-8a28-0ce995f34910 | -6.1422 | -44.408199 | 2024-11-28 00:03:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c683354-76f9-3da9-a742-397e82584390 | -9.7897 | -36.181702 | 2024-11-28 00:03:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4bb7a4d9-95bb-3228-ade8-1161982ff0be | -5.3435 | -40.659801 | 2024-11-28 00:03:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ec82aa73-3a3d-3161-bde9-66b50b6b6821 | -7.6398 | -42.967701 | 2024-11-28 00:03:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8411c90c-c1ed-396c-885a-3b62fa3eda54 | -4.7142 | -44.425301 | 2024-11-28 00:03:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f44ef500-9602-3abb-b378-7fef53380c5f | -5.9304 | -45.3601 | 2024-11-28 00:03:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f5df341-b5b9-3c1c-b2c5-5af2f83be580 | -4.6298 | -44.5989 | 2024-11-28 00:03:00 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42918057-24cf-3833-8362-d65a0115634b | -2.869 | -45.789001 | 2024-11-28 00:03:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1b1a477-d1c0-3907-8d4f-74cb89d1f2af | -4.7435 | -44.4189 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ec705cd-de7d-3215-a88f-058cee2d57be | -4.4805 | -44.618 | 2024-11-28 00:03:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef259d12-7967-319a-9f64-44941196b4f8 | -6.6883 | -35.014 | 2024-11-28 00:03:00 | METOP-C | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0e34b41c-8a36-33a0-8339-cc062128c6ac | -3.3215 | -44.198101 | 2024-11-28 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27cd3812-90d4-3292-9495-36ac5672e342 | -4.878 | -45.400799 | 2024-11-28 00:03:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc44b3c0-8841-3508-b27f-5d437fbe0679 | -7.4763 | -35.115898 | 2024-11-28 00:03:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0742756-3414-3d71-a7a8-dbd056f46b59 | -3.3121 | -50.0602 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3bc91f5-8474-3c6e-9a30-a68c56e77301 | -5.924 | -45.330502 | 2024-11-28 00:03:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24fcfa17-436e-33cf-8cc9-7eabd98bffaf | -2.8034 | -46.8181 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea736837-04a3-303c-8ef9-b2bd849f4529 | -2.8244 | -46.866199 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36037fa9-bc4b-3a38-b977-fc2f6efd7d29 | -5.1771 | -44.901901 | 2024-11-28 00:03:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc9b7d72-0c1f-33f6-883a-104f092c92cd | -1.9774 | -45.693199 | 2024-11-28 00:03:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4510cb5b-01e2-30cb-bfe8-f1d3dc8b80f6 | -2.4212 | -47.024799 | 2024-11-28 00:03:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 199693e6-f5f1-3e0c-b3fc-df123c9149ee | -5.9351 | -39.038399 | 2024-11-28 00:03:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 867794c4-6bdc-3721-a88d-1d29e342fe83 | -4.7418 | -44.457901 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c38949c-ee5b-3be2-bec4-dce8c75b7fde | -4.4777 | -44.605499 | 2024-11-28 00:03:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53a9e79b-df5f-3ab2-b6bb-933af6288aae | -3.0432 | -41.142799 | 2024-11-28 00:03:00 | METOP-C | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4b149435-0d11-3616-8075-02e2ecc7f810 | -7.2086 | -39.752399 | 2024-11-28 00:03:00 | METOP-C | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 73a1e228-fef2-3993-b594-222d92682c06 | -5.6399 | -39.508999 | 2024-11-28 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e6041f61-74fa-36e2-98a7-2af658b66487 | -1.9134 | -46.540798 | 2024-11-28 00:03:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dace7db6-00af-3b3e-94e0-d517c7c65f29 | -2.8132 | -46.816002 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d018180-5bab-387e-9aba-75fb1da7d8f0 | -4.7212 | -44.4109 | 2024-11-28 00:03:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80326e43-6561-3f0f-b554-428ad81e8730 | -4.0799 | -46.087299 | 2024-11-28 00:03:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12ed815b-a977-3e67-8048-31d901d50134 | -8.5005 | -35.211498 | 2024-11-28 00:03:00 | METOP-C | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fadb1134-b792-38b0-a13e-6d2fc0eced42 | -2.8109 | -46.851501 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce632b57-1e2a-3bf6-b82a-86848593a225 | -3.9515 | -44.265099 | 2024-11-28 00:03:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56f7ec3f-a0fc-37b0-a5ae-7ecbe93f4449 | -2.1815 | -48.494202 | 2024-11-28 00:03:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 490dcba6-b441-37d2-b295-3da3ffd8cff7 | -4.759 | -43.2869 | 2024-11-28 00:03:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d573ef12-7c26-3bd8-b9ce-a79778addde1 | -9.5251 | -36.153599 | 2024-11-28 00:03:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9977e1bc-1218-37d0-8235-b999edc6b6e0 | -6.0251 | -48.024101 | 2024-11-28 00:03:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5b1ba8-bcd7-3077-8cd1-c69a96abdd5b | -8.3978 | -35.081501 | 2024-11-28 00:03:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7658256b-5bd7-35f0-bc31-bf04335649fd | -2.8146 | -46.868301 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28453456-40ca-362f-b4a2-ae95c33fcfc1 | -3.2628 | -46.361599 | 2024-11-28 00:03:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 879319d7-816e-361e-a731-63849466c10f | -4.7637 | -43.307701 | 2024-11-28 00:03:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10406a44-759c-36dd-8498-a91f0b804eaa | -9.9784 | -36.4632 | 2024-11-28 00:03:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a050b1a4-bb21-3ec1-9cb3-e5a029ff7a2e | -3.3602 | -50.140598 | 2024-11-28 00:03:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3538b635-e110-3403-97c3-4971c9081f4e | -6.0411 | -41.941799 | 2024-11-28 00:03:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bc0007f6-c2c8-3975-8117-ba94d745813a | -4.7185 | -44.398701 | 2024-11-28 00:03:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c50b7e7-1ccf-3dd5-9a7f-d74764907012 | -6.1296 | -42.620899 | 2024-11-28 00:03:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 190b9685-98dd-3875-8581-c637acd70bfd | -7.6519 | -42.976601 | 2024-11-28 00:03:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f3494d44-ef3d-3cbe-9692-7a1a952ead6c | -3.2792 | -44.055599 | 2024-11-28 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcbea9c0-1eb6-3aee-b03f-197185f905ea | -5.7801 | -44.107498 | 2024-11-28 00:03:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d2e783d-3a29-3614-a2e1-79f70ad4212a | -2.4852 | -45.992699 | 2024-11-28 00:03:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 203a53d2-f69a-36b1-834b-82782af033de | -4.6787 | -46.539001 | 2024-11-28 00:03:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f25758ad-0073-30ac-aebc-c1e8788c35e7 | -2.4819 | -45.978199 | 2024-11-28 00:03:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c70b8f2a-ebc9-3e1b-a1e9-eeda9bc6a144 | -2.8207 | -46.8494 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a283267d-8a06-3f7d-bcae-c9164b9dbb79 | -2.7877 | -46.839001 | 2024-11-28 00:03:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d47a71b8-ad42-3c45-8709-5475decbe4a4 | -2.433 | -45.397701 | 2024-11-28 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a17f1869-2378-3e99-a235-ecdb79ed102f | -7.6512 | -37.518398 | 2024-11-28 00:03:00 | METOP-C | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 73dd3e78-8d93-30ed-bbb4-c798dffecef2 | -3.4392 | -44.586601 | 2024-11-28 00:03:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb65397-79a0-3f66-af9e-d79dfd6e9316 | -5.5788 | -39.694302 | 2024-11-28 00:03:00 | METOP-C | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8991443e-1341-36ef-ad9a-2319482f165c | -9.8207 | -36.226601 | 2024-11-28 00:03:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d12326d-6b34-3b0f-b78f-8c6c41e13947 | -4.6074 | -42.376801 | 2024-11-28 00:03:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a71d95e8-2027-344e-9e77-55265b2f2fc6 | -10.5402 | -37.0714 | 2024-11-28 00:03:00 | METOP-C | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1089b81e-dc79-31d1-8071-f703aa17d643 | -9.8239 | -36.240601 | 2024-11-28 00:03:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfee59e4-40e5-3dcb-83cf-0c6d90921555 | -4.7408 | -44.4067 | 2024-11-28 00:03:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13ab6601-921e-3023-a966-8b6e9012c798 | -3.025 | -49.176701 | 2024-11-28 00:03:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 231c6994-3571-347a-913c-df2a5408c8f3 | -3.1688 | -45.620602 | 2024-11-28 00:03:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 65bad5c6-6fbb-3a10-a3c4-df3f990a5239 | -4.8811 | -45.415199 | 2024-11-28 00:03:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7b8a783-da3e-3dd5-9332-218177370222 | -6.055 | -43.9608 | 2024-11-28 00:03:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99c87d0e-9316-3ad3-add3-38ee315b86d7 | -4.7266 | -44.435398 | 2024-11-28 00:03:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
