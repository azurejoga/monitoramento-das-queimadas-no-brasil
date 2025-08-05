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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daf02664-494b-3da1-816d-76160c46b8ef | -11.7539 | -45.01615 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fb3ba83-c6bd-3cc4-9ce4-9b9f174875b1 | -6.73895 | -45.30847 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34af2cd2-dcc5-3aea-ba6e-8ff759e83fe9 | -11.79031 | -44.99616 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b6bc118-e0b7-332c-a2f1-4e600ebd70db | -7.99635 | -43.14449 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| ade9fc84-4cbc-3194-ae13-ac0d123d1610 | -6.50017 | -45.54024 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 666403f5-de20-33da-9074-992b90e4b2f4 | -11.91705 | -44.96577 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e874c5e-b85f-352d-9a78-6ed7eafdaac6 | -9.77347 | -49.75397 | 2025-08-05 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ef5f364-eb11-3a3f-9957-c2ca0e58e078 | -15.83027 | -44.03346 | 2025-08-05 04:17:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 836f1d8e-2860-371f-856a-0750907efa7c | -8.71708 | -46.43819 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c73e289d-0498-383b-8b69-ebcf0197c46a | -7.21749 | -44.48326 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6f85497-5817-3904-82df-5ce42f369002 | -12.35415 | -46.06175 | 2025-08-05 04:17:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb77b1a4-7fb2-31c8-9df4-f2546c00c24b | -9.32835 | -44.85159 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db1916d3-be16-3221-9562-e0d6874612eb | -17.68884 | -46.64065 | 2025-08-05 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f194cc58-f8ab-3d35-9f41-ce58e476520e | -8.96007 | -46.74463 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa55745-4160-3dde-a4e7-83071fcb30a4 | -8.34499 | -46.91523 | 2025-08-05 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a65acd24-de54-334f-aeab-c806ec32fdcb | -5.80183 | -43.62696 | 2025-08-05 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9822185-4387-35d0-9599-92969052b8fb | -14.30006 | -52.014 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eba8d388-6034-39aa-92dd-6a511c59b62f | -9.18204 | -48.84198 | 2025-08-05 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4cdc3f9-de56-37da-b96f-76e5990a91dd | -17.37705 | -44.99114 | 2025-08-05 04:17:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c07f6b2b-c421-3cf0-a759-d9d79676e3ba | -7.368 | -43.71466 | 2025-08-05 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a54c2712-c275-3cf4-a257-e30595eb6f6b | -10.46171 | -44.37727 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13bb9abf-e3f3-3bdb-bb63-8213b0ea4b1a | -13.29414 | -39.8678 | 2025-08-05 04:17:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f3048b7f-a16b-3bf5-9528-fbfd029e813c | -6.46717 | -43.03408 | 2025-08-05 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f5d1692-762f-3867-878e-42da53596318 | -7.98975 | -43.16482 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 187b79f4-1d75-33b3-982a-c8d17a1e4775 | -6.96736 | -42.86801 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 8d9c1adc-f9d6-34a9-aac6-c840e899ed0a | -5.88444 | -43.74412 | 2025-08-05 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 833817f3-e15a-31c1-a2de-ffea7f5a0ef3 | -5.71972 | -49.10349 | 2025-08-05 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faa4a7dd-1ea8-37c1-bc02-d12affb8e4ef | -8.24231 | -45.05998 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c19cb009-e245-399a-be39-da99fa69c00d | -11.81591 | -44.26157 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d62d74f-1006-32a2-a6b6-5b25c0503e01 | -7.60464 | -45.30483 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e93fd4bf-6d22-31b4-bc3a-df6f6faa9f21 | -8.94631 | -46.73796 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 48f03eed-a981-3b8e-91e0-eb69da032d24 | -11.59633 | -44.83385 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 78b6d8df-3c6d-3118-9948-a61af8af1b8a | -6.72202 | -47.21104 | 2025-08-05 04:17:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e18e10a2-165c-3dd9-8bf0-2cf87fae0b8f | -8.38627 | -45.79279 | 2025-08-05 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fedd427b-17b6-385a-9ccf-6e9fd48dfe50 | -7.94916 | -47.59295 | 2025-08-05 04:17:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52ff79af-b3f1-3d2b-8be3-b7362722b4f1 | -8.71333 | -46.42592 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3fd1d50-0c87-38f6-ae83-815925b1fc81 | -7.75571 | -45.23661 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4eec68b-5a11-3544-bb37-835e3c4c9b54 | -5.78404 | -43.60978 | 2025-08-05 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6471d83f-a005-3801-b5d3-51eb95f81550 | -8.91663 | -48.93593 | 2025-08-05 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5fe8cc2-5821-3e79-93f5-e82cf794423b | -5.78459 | -43.6063 | 2025-08-05 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2af0173e-a67b-3844-b450-bad28ad56dc2 | -10.91687 | -48.37628 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d53895f4-f78c-3983-9d0b-d5ff2bf3b02b | -7.90511 | -45.53923 | 2025-08-05 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a1d65e8-8f69-37d3-9ee1-ebb6e2e973ac | -8.25191 | -45.06532 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 187895d8-96aa-3221-a60e-e31cec6925d0 | -8.00353 | -43.14206 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 7a14581b-f897-32cd-bf3e-e3a439ef326b | -7.94449 | -43.89658 | 2025-08-05 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dd8ae6f-bcb1-32a3-9b80-c022b3f76ec1 | -10.78785 | -46.52061 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b09946e4-a3a7-341f-be0e-c45eae9eb758 | -17.72207 | -42.95839 | 2025-08-05 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 996f3385-b9f0-3648-86a1-48f3243f05d4 | -7.85534 | -46.73958 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78c838f1-cc2c-3371-b3ad-cca74ec9a67c | -9.39619 | -45.51072 | 2025-08-05 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e0303492-f716-3233-a56d-e28101651357 | -17.20982 | -44.82908 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e209ebe5-496e-3587-bb3f-53dd7e46263c | -7.99541 | -43.23695 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c80206cc-ddd2-34a3-ac6f-b731aee0d160 | -7.06033 | -44.39227 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6d4bf51-c927-3f47-a614-233d3cd59796 | -11.75838 | -45.00955 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d362e9f8-c7eb-3161-8fbb-d33c2e8a3582 | -10.5322 | -42.5499 | 2025-08-05 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 78e81a42-40fb-3b0f-a3f4-4a53fca6c006 | -6.01022 | -52.15235 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d7db512-e5b0-3ab1-9bc7-f9392b71bd03 | -9.69569 | -51.94472 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d952693-9801-39b3-a720-4e7b9d5596df | -7.41101 | -45.99459 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a694f24-c86b-3cdc-959d-98235709c420 | -6.93 | -43.34216 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e09ccc9d-f327-3f1f-9425-aec8a8466cdc | -5.78016 | -51.66433 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc04aff5-ea5a-314b-9dac-398783c8cff6 | -6.73784 | -45.3042 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1adfbc74-2169-3d92-9720-728aa2273412 | -8.37894 | -46.57945 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dad1af9-9880-3cd4-a55d-dfe616727d59 | -10.47347 | -44.3825 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bebd680d-7bb6-3d37-a041-c4d302a03617 | -8.9427 | -46.73734 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 00b54d2f-0ab9-3098-95cc-655c58f9a321 | -8.95216 | -46.74752 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 92fd4b38-3798-3d2e-944a-b4a7f4536b4b | -7.38737 | -44.64016 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00feecbf-4c19-3ba0-ac94-04d5e84e07fe | -17.2115 | -44.83262 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46530b3a-e896-318d-9402-bd1914a150eb | -7.56561 | -44.8802 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2217ea8d-cd47-3b59-9770-d1cbb67c7247 | -7.37375 | -44.16555 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 423b2e8c-c8a2-3658-b504-9489d8ad3e25 | -6.68174 | -49.79122 | 2025-08-05 04:17:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1362a6af-50fd-3bc3-86fd-4c596d8d76a8 | -8.13048 | -49.58624 | 2025-08-05 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87581ee6-80c3-3062-b7f7-1f804c194c2b | -8.84745 | -47.61028 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 86574699-0207-395a-8513-49ee6b79fbac | -7.21646 | -41.85317 | 2025-08-05 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a2a8dea5-35f7-3e6c-afe7-0f8b43d6f982 | -11.91865 | -44.97712 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aad842ee-8b80-3c2c-a08e-64d923e99194 | -9.31885 | -44.84636 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91b6ab93-adfc-3602-98fe-a71d3d9ef7c9 | -17.20761 | -44.82124 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff94456e-cda3-3afc-ab49-48b7fcb84cba | -8.25472 | -45.06954 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84c20c21-9cb5-309d-a623-aef131862b61 | -17.21206 | -44.82898 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f79e13c5-6d80-33cc-9e8d-ab8c6e1bd834 | -7.94532 | -47.59225 | 2025-08-05 04:17:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aaf04bb-2914-3005-9b2b-a5f99b572c67 | -10.33015 | -47.82689 | 2025-08-05 04:17:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 977ce56a-d616-3d3b-b085-fc26f5f7d5c0 | -7.20971 | -41.85213 | 2025-08-05 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07012c4f-421d-3ae0-b072-1a5b1309a65a | -14.2927 | -52.00248 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcf8e4e9-b370-3f25-a453-20af4b50174b | -9.32163 | -44.85049 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24c535db-fe43-39be-b3a1-a14b5cf33408 | -8.84821 | -47.60566 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8064a28c-03d6-3d0b-bbf7-7fab270c252e | -9.05265 | -45.06596 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc52c59f-4803-326f-a343-540659b46b36 | -7.37823 | -44.15901 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 047b9bd4-dd42-3eef-895f-6b9a5e7a9b33 | -7.60213 | -45.30494 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56fb0d44-533c-32ff-9974-64892a64e65d | -6.73957 | -45.30459 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe8aa8a5-a98a-3c91-9d48-f16f2a4e78bc | -8.25812 | -45.07009 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40443fe0-1225-3978-b168-f5ee7f50dff4 | -9.40021 | -45.50756 | 2025-08-05 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d78b0d78-8ceb-3361-82c9-db6447c34286 | -6.0075 | -52.15337 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4b6b5b5-a21d-39fd-a673-9a9579008b00 | -8.74058 | -46.42933 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93c6b738-5aba-30f5-a16e-7a86e417cab9 | -6.00963 | -52.15564 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec167562-4e00-340f-b3ae-772c4eabcee6 | -7.9092 | -45.536 | 2025-08-05 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 263bbfb9-aa7d-31c9-a580-ed09fc30adcb | -16.4642 | -45.01097 | 2025-08-05 04:17:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46eb1f9d-d644-3b4b-a85a-9658ea165166 | -11.91543 | -44.95455 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 394a92c8-c081-3813-8915-cf598bbd7446 | -6.37904 | -43.71819 | 2025-08-05 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e2e9963-581c-39b5-af3f-0479ba6ffcd1 | -10.45338 | -44.38678 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d6373ff-9a3e-324c-b3f2-ef2f974771d1 | -7.08564 | -44.36344 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ef2f850-b3c0-3455-a382-6e5c6a5f342f | -10.81085 | -46.51236 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 535718eb-a085-3a71-a8c6-ccf5a06c6262 | -11.78698 | -44.99561 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README17.md)
