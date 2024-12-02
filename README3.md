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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf2621ad-1a09-38b7-84e1-141b140bc7ea | -10.653 | -44.495499 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 916f6509-56ce-377d-8a7b-51623198371a | -4.8075 | -48.6115 | 2024-12-02 00:14:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 611144d3-daee-35fe-88ce-265e81d990ec | -5.3233 | -40.430599 | 2024-12-02 00:14:00 | METOP-C | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3f45757d-93cb-3a1e-9eb2-675f118a4e33 | -4.573 | -43.354301 | 2024-12-02 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a8d9ea3-5349-377d-9b6c-7b259dc4d966 | -5.6114 | -43.477901 | 2024-12-02 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d3e85aa-6922-3e6f-b697-2c3fa7b34456 | -4.5654 | -45.456699 | 2024-12-02 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfbb9ff1-c91a-3033-ace9-a39da6258bb5 | -4.9045 | -41.3391 | 2024-12-02 00:14:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8cdf8abf-a5b7-31a0-9a6c-304f60650777 | -4.6396 | -46.8871 | 2024-12-02 00:14:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7092136-209f-3ac5-87b1-88feb8f44ca0 | -7.3551 | -35.201698 | 2024-12-02 00:14:00 | METOP-C | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42547d7a-4a65-36c5-9e59-2f0db8079af6 | -10.6512 | -44.487202 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dde36267-8011-3903-85c0-883b2846e1db | -4.5746 | -43.361198 | 2024-12-02 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc972b5-9367-30c6-92bc-1ce00519cc85 | -5.365 | -44.8936 | 2024-12-02 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13890f40-e51a-395c-af2a-a5ded6116ff1 | -3.8475 | -46.5172 | 2024-12-02 00:14:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c5b4e90-4a84-3728-ae18-2c90661466f6 | -5.1304 | -45.177601 | 2024-12-02 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c70223c-7c2c-30bd-9df0-5382794358c2 | -3.1401 | -44.349899 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 568375a9-57de-3a3f-ae73-9b2a5012d5ab | -6.0825 | -48.0327 | 2024-12-02 00:14:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8794d6d-c6ed-340c-b89a-0db5a9c48010 | -4.1353 | -44.828999 | 2024-12-02 00:14:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29fd3a81-bc3f-33fd-8a89-273d12ab8306 | -3.141 | -45.985802 | 2024-12-02 00:14:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7f4848f-abbc-3e42-a26a-2aa1e5e12c11 | -4.3981 | -49.768398 | 2024-12-02 00:14:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22beed1b-9c97-3509-bbd4-4d10b27ccb19 | -15.6108 | -39.334599 | 2024-12-02 00:14:00 | METOP-C | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e5544bc-1f10-3533-877a-1c7bf918b6ce | -4.6589 | -45.643398 | 2024-12-02 00:14:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 790b6e6d-dfb5-347d-87b1-f78e2d1a3551 | -6.0777 | -48.057701 | 2024-12-02 00:14:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f396e7e-4c08-3439-ad01-b52bd31efaf1 | -4.7241 | -43.248501 | 2024-12-02 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13392087-96cc-355c-9bf3-261a825b804a | -6.463 | -44.191502 | 2024-12-02 00:14:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4415773-3877-3dbe-83b4-1840138fac6d | -6.1792 | -42.6208 | 2024-12-02 00:14:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e61b124d-52db-361c-a9ed-1234115a037f | -9.9094 | -44.334999 | 2024-12-02 00:14:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e4bd8017-9a0b-34a3-9531-93586dbd7e21 | -4.4241 | -46.291901 | 2024-12-02 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8275730-cb02-3edb-bbb9-adef6cf338d5 | -6.3644 | -47.3563 | 2024-12-02 00:14:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca138e07-ef38-3752-ac78-6a1dcdc51f6f | -2.9195 | -41.188099 | 2024-12-02 00:14:00 | METOP-C | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ae45969e-7a66-32c1-b22c-181d28e049ec | -1.9888 | -46.4431 | 2024-12-02 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34ef7155-9ec6-30db-87d6-bd78ca0e892e | -4.7704 | -46.415501 | 2024-12-02 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3d3cd3f-be76-302b-bd4b-ab3aaa77b17d | -6.1776 | -42.613899 | 2024-12-02 00:14:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08a6764d-0de3-3926-a61e-b61916e0c92d | -4.5828 | -43.3521 | 2024-12-02 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 517aa53d-e3a2-3a19-93f9-bf61cecc37bd | -4.9029 | -41.332001 | 2024-12-02 00:14:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d18843b-3a17-33f7-a3ea-a1c6d32f5382 | -10.6932 | -44.966099 | 2024-12-02 00:14:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a8ca3f1-86b3-37a7-97cd-374d42f6573a | -6.6741 | -39.321301 | 2024-12-02 00:14:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f679e88-ec74-3f8c-b8f0-a6b954ace5c0 | -4.0534 | -48.951099 | 2024-12-02 00:14:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc12e76e-bbda-35d1-977a-2a4fb2451dec | -3.9495 | -46.011101 | 2024-12-02 00:14:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5194ea65-ce58-3772-aab4-3c0961072daa | -6.8088 | -46.765099 | 2024-12-02 00:14:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 340a9ae8-96fc-3186-a086-ded9e9aa83bd | -3.987 | -47.2756 | 2024-12-02 00:14:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34491576-6b58-34f7-a7f8-835520a36702 | -10.661 | -44.485001 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 126e922d-cae4-3619-ad1f-d484ffd287cc | -3.1385 | -44.342899 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cfaa6813-21e7-3028-a115-53629d4194e2 | -5.6098 | -43.470901 | 2024-12-02 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbde5986-9826-3f6d-ad55-b54e6be670c3 | -11.0559 | -45.367001 | 2024-12-02 00:14:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 881d2ea2-fd18-308e-8e99-8b3ea962f7b0 | -3.9849 | -47.266102 | 2024-12-02 00:14:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0888f30-e366-36c1-bbb1-08ef55675758 | -3.2387 | -53.593601 | 2024-12-02 00:18:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc915cd-b07e-3e56-9050-d7dcc6705ff9 | -3.5353 | -50.163601 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75e44ad4-f2e1-386f-8a50-49f73b982e0e | -3.2236 | -45.760502 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 846cb8ab-c2d3-3f12-b6b4-bf1fd092a4b7 | -3.2219 | -45.752701 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac349e3-be5b-3937-aaca-4ae6e66a3dbc | -5.129 | -43.215801 | 2024-12-02 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18ce4b0a-a50d-366f-b733-6c4f5780e40a | -5.2027 | -42.861301 | 2024-12-02 00:18:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62aa5cec-7452-3a3f-b027-00372f6e8b0a | -3.3614 | -53.187199 | 2024-12-02 00:18:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799faca3-1527-392b-9d24-8debc78379d8 | -1.909 | -46.409698 | 2024-12-02 00:18:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30f7b641-ced8-360a-843e-1273302248a1 | -2.4822 | -46.576698 | 2024-12-02 00:18:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08d3d6c2-400e-3d7c-8798-009e1dd0d5ec | -2.9866 | -52.505501 | 2024-12-02 00:18:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c87012ab-3d32-3627-a5e1-542cef187366 | -5.1175 | -43.211102 | 2024-12-02 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d3ea79c-ea23-342d-8bfa-5ca329ccdfc7 | -4.9608 | -42.031101 | 2024-12-02 00:18:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5179658d-6b87-318b-9715-adbb86f96866 | -3.3654 | -49.859901 | 2024-12-02 00:18:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0a06c0-d71b-3b9b-b7bc-6a0566438fe8 | -3.1537 | -51.108799 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70e755f4-5cdf-3faf-83d0-3179266a8357 | -3.4638 | -50.255501 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdc0aac9-88b2-37ce-af5a-4eb3ecf4218f | -3.3371 | -50.237 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06dbf591-ca51-3393-9395-40d123292e5b | -1.5326 | -45.843601 | 2024-12-02 00:18:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad9a4aea-8599-38c8-92a1-044b50ed4b7b | -3.191 | -46.571301 | 2024-12-02 00:18:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0e34d0f-c4a0-3516-896e-0733b6da570e | -2.6561 | -46.117901 | 2024-12-02 00:18:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8d715e1-ae50-3127-94a2-bc7fd856da0a | -2.0984 | -46.608898 | 2024-12-02 00:18:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4728cfdf-3f29-3509-a144-add4d3a012b9 | -3.3518 | -53.189201 | 2024-12-02 00:18:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca8388d8-7a88-39a4-80ad-d6198a770db3 | -4.7518 | -41.125599 | 2024-12-02 00:18:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1d297585-c62d-3718-a9a1-94948e834d97 | -2.5491 | -53.411598 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31e4d4e2-8274-3bc5-b7da-51a1c3315022 | -2.9196 | -45.827499 | 2024-12-02 00:18:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3f61fb-a10e-37f6-9310-07bbce50687f | -1.5309 | -45.836102 | 2024-12-02 00:18:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 649d5499-2509-3d53-a3fb-a29b1c8f702f | -2.5342 | -53.390099 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 033bcdba-929e-34ec-91cc-ecb77ec8a657 | -2.5289 | -53.3666 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 870e8905-e5b7-3b14-bef4-03298489c46f | -2.672 | -46.5966 | 2024-12-02 00:18:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eafdc569-3a25-3271-a99a-a4ea40e17aac | -2.094 | -46.317799 | 2024-12-02 00:18:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3338c85b-cdbd-36b8-8ffa-8673b0f0452e | -3.08 | -53.198601 | 2024-12-02 00:18:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44bcb1ab-f30c-35c5-a70b-192da257a5f2 | -2.912 | -45.3405 | 2024-12-02 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc00f4a2-d715-34f5-a3f9-a723e03d8606 | -3.1929 | -46.579899 | 2024-12-02 00:18:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16fe2b20-bdb1-3181-8f70-1cdf14a6c8f6 | -2.0072 | -54.292702 | 2024-12-02 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebce7a5-583e-30fb-80ef-4c80ea9a80c9 | -3.2103 | -45.747002 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63019417-840e-362e-b045-fd001304ddb3 | -4.9592 | -42.0243 | 2024-12-02 00:18:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e0233985-f31f-3b72-b81f-95e4e1cf7fda | -1.7998 | -45.162998 | 2024-12-02 00:18:00 | METOP-C | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef61846-1ff5-3c5a-98bb-d0e968d01d73 | -2.2803 | -45.733898 | 2024-12-02 00:18:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 635c9e3a-e5b0-3e63-a8ce-8ed992d0300b | -2.0169 | -54.2906 | 2024-12-02 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eacecd1b-02f0-3934-ad43-b22c318d98c8 | -3.3923 | -50.209702 | 2024-12-02 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 581d8c1b-a80e-3ac2-9c56-244e8b7e45d2 | -2.0011 | -54.265999 | 2024-12-02 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 224c09e0-b499-37e4-b56a-4a2c3fc2a0d7 | -3.372 | -49.844101 | 2024-12-02 00:18:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea08681-d0d5-3df5-8fbe-29cb9abd9261 | -3.2429 | -53.566601 | 2024-12-02 00:18:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c182b4f-c5ee-31a4-b628-787b5536391e | -1.6288 | -45.407299 | 2024-12-02 00:18:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87dd3f69-cf5d-3bf3-82c5-c4943f4c735e | -3.1194 | -45.982201 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e868648-02ec-341e-9a1b-9990d92a9900 | -3.2808 | -46.149601 | 2024-12-02 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7e829d-f5a3-3ce7-8dd8-95a439071ad9 | -2.5395 | -53.4137 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 569a279e-c214-38ef-8dc2-9707eeec5a86 | -1.9053 | -46.393501 | 2024-12-02 00:18:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7103be96-807c-3df5-aee4-0448ff497270 | -2.2838 | -45.749199 | 2024-12-02 00:18:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f30c451-ed92-37d1-8f6f-e5e975908877 | -5.903 | -46.2425 | 2024-12-02 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6618b28d-689c-3c8a-bd2a-4d5cb3b5ce30 | -2.1985 | -45.6007 | 2024-12-02 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5030842-2918-362b-a9a5-3c80e44c567a | -2.1483 | -45.651501 | 2024-12-02 00:18:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f776843-ac84-3847-b7ef-d9d671804cb9 | -2.6758 | -46.613499 | 2024-12-02 00:18:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f069261-ccf2-345c-8de5-20a8f331128a | -2.5579 | -53.360401 | 2024-12-02 00:18:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83103ee-41da-3cb9-9039-ba2e7a73cd05 | -1.559 | -46.7719 | 2024-12-02 00:18:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc40d417-7b1c-3347-be9d-1dfbd8418cc1 | -2.378 | -48.612801 | 2024-12-02 00:18:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
