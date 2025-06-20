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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46e3dfc3-4409-3004-80b3-a14dcc756ce1 | -13.26328 | -46.8208 | 2025-06-20 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fc185c5-aa89-340c-b37b-f67f81412dd4 | -11.53512 | -56.99668 | 2025-06-20 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9ac941a-38bb-3477-941c-31794fae9a05 | -12.20183 | -49.62526 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3070a06-c483-3693-935c-d8e71da5e17d | -14.03149 | -55.13321 | 2025-06-20 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0def84ef-f367-316b-8ea7-29c5c79b1e21 | -14.17043 | -60.05541 | 2025-06-20 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3712b5d-d4db-3b6a-ad9f-2234ae42420c | -12.35055 | -49.31111 | 2025-06-20 04:53:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a4bec153-c169-34ad-9dbd-fd74fc136c4b | -16.31533 | -58.25433 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 970eaf66-cde6-3c84-be56-de59454410a4 | -16.31099 | -58.25801 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dc5e3e47-4042-3cc5-9087-0ed76c961350 | -13.9309 | -54.49842 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ae7781a-1be0-3359-9963-1fd38df2254d | -15.42842 | -47.8382 | 2025-06-20 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cdfde43-eb8a-3ea5-88f8-4b638f71675f | -9.95496 | -64.99454 | 2025-06-20 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5ce9bd1-cab1-3846-b998-dabc8b0f0edb | -14.17453 | -60.05615 | 2025-06-20 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5aec3a6-a6af-3984-9671-b67f955c48d9 | -9.58906 | -65.88831 | 2025-06-20 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11800fc2-adf6-3763-bf6f-e45fd1d55f98 | -14.04158 | -53.36345 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38bb14e5-4339-333a-9e17-e5abfd5efb56 | -12.55234 | -57.71531 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc36fdb5-2b1b-3d70-a070-bed7e9578085 | -16.31204 | -58.26412 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 596938cb-9064-3c56-ae7e-30d7583202ef | -12.20076 | -49.61676 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a406da66-fcd3-32bb-81d5-aa9329b2439a | -16.30514 | -58.27026 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9ee790f8-9925-3a52-a313-1ce3371e8ff7 | -11.07919 | -55.05173 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 142d37ee-6170-3b23-8811-72a4aea45618 | -11.87399 | -54.68113 | 2025-06-20 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87c4bd24-7e4c-31c6-9f93-4590cfd6f415 | -14.17112 | -60.05159 | 2025-06-20 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 849c1679-7fd6-3ce2-ab19-990f6c139a6e | -14.04716 | -53.37177 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46d798ec-4400-374c-9629-01f34a7da613 | -11.53367 | -56.98353 | 2025-06-20 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e6f8c5c-9ea2-372f-8797-11d42580b9af | -11.94985 | -58.74006 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8171c28c-a532-3fec-9341-d660337f4417 | -11.53009 | -56.98292 | 2025-06-20 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a00a5f0-3404-3831-8c52-194600823431 | -12.55383 | -57.70653 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a104de62-d827-3199-a705-6657b5df13c3 | -14.03325 | -53.37325 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29387bd5-407a-3bc6-94cf-0ffaafc1d0ab | -17.58058 | -47.50045 | 2025-06-20 04:53:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31725812-658b-3f71-8fd5-47853a5d7871 | -13.14317 | -56.8102 | 2025-06-20 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14c3a934-1bca-34d5-add4-ff58302dd811 | -11.94724 | -58.75528 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 39ec7e59-fe25-34dc-8fb2-b9279020604f | -14.82152 | -48.48102 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bea37e9b-12d4-3c0c-9e5f-fb72696be42a | -11.62476 | -58.29193 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d391dccf-9631-365c-9223-87f1e9461506 | -12.42599 | -54.87029 | 2025-06-20 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b6a7056-f0df-3c73-b03f-b95fcb365d0b | -12.02827 | -57.09467 | 2025-06-20 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d248a8e5-2e26-3c8e-abac-015fdcc9139d | -13.09515 | -52.29576 | 2025-06-20 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cfc7c08-ac86-377c-9287-8913ff3e4f1a | -12.64895 | -54.12617 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ee3f9a2-cba9-30c4-8f8a-f5418a0b0d7e | -13.14666 | -56.81081 | 2025-06-20 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45bfcadf-3994-33d0-bd39-764ce5f03a1f | -11.93512 | -48.41982 | 2025-06-20 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14a7f8b2-fac0-37e7-8f8e-e7a7abe5cb95 | -11.65032 | -54.54652 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 448e3622-8cf9-366a-a411-4347ad4e966c | -16.3034 | -58.2714 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2988c1c5-d320-36ca-830b-77d13e70a4e5 | -12.58221 | -56.97315 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ed6318d-3e10-35e3-8a9b-a5806e422601 | -12.50863 | -58.3607 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d8b39183-f566-3201-b746-8b79522639c4 | -14.44228 | -48.90409 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d14a1ea9-192a-309c-aec3-23dfd7ce40ef | -14.02987 | -55.12199 | 2025-06-20 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44954a1b-d6b6-31ce-ba55-d249ce88cbc7 | -14.02931 | -55.12555 | 2025-06-20 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82c59b6d-a7a6-31a9-a0b2-b06aa8407659 | -11.87731 | -54.68167 | 2025-06-20 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae6da7f8-c9b9-3c20-b1c8-a105e3a411c2 | -16.64507 | -48.4922 | 2025-06-20 04:53:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56cc4ed7-fdd7-33cb-afd2-736154196bbd | -12.55601 | -57.71593 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb95c361-b7bf-399c-8ed0-22c67befb4a1 | -11.92556 | -51.74706 | 2025-06-20 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ff7fc92-fead-3670-804c-79a2712d10d1 | -10.9382 | -55.3342 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a752f24a-3292-34f1-8ced-ee107153bc70 | -12.50947 | -58.35591 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9823f11a-d2ba-3244-befb-4ec190ca55ef | -11.93664 | -48.42356 | 2025-06-20 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5fbf503-db80-3563-b207-8ff81fd75324 | -12.55309 | -57.71091 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd3708f2-5e25-3b7d-bd78-35e17b0f38b6 | -11.37279 | -55.11489 | 2025-06-20 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f780a45-2786-3a3e-8424-2388733d54e2 | -14.04382 | -53.37123 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e003403-ea07-3e51-956e-1b8c447afc1f | -14.04492 | -53.36398 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc3841fd-ffe7-3c0f-8b58-bb936373c8bf | -12.20395 | -49.62227 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6fc1942c-3701-3b53-a944-5d63dee4a294 | -14.04048 | -53.3707 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c9c6e1e-ac13-365f-8830-9a59a5758349 | -11.0853 | -55.05643 | 2025-06-20 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 997cb4d9-52f5-3acf-a968-ebb9014b515f | -12.20253 | -49.62035 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8644604c-d304-3f32-af4e-69fbbaf9f088 | -12.51113 | -58.34632 | 2025-06-20 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c131c63e-c60e-3193-bb8c-852639bc3c7b | -12.5219 | -57.20384 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 334f2d85-9d58-35f2-bf2e-eb498980a7a3 | -16.30127 | -58.26214 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 4c16c5f7-0321-37d9-b3f4-481995d19129 | -13.14731 | -56.80686 | 2025-06-20 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 738587dd-239d-32e8-9685-68084f416dfb | -14.43551 | -48.92303 | 2025-06-20 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc585878-04f4-3e21-988e-f9714a03adf6 | -13.66082 | -53.93988 | 2025-06-20 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 24da2cee-a084-3d7f-ba0f-39e68606302f | -12.97678 | -54.68188 | 2025-06-20 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 808f0beb-b9f8-3e23-a2d9-aa9ed25cbaa6 | -11.95509 | -58.75664 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ebf71171-d51e-3617-9705-c9a34d4175c9 | -11.53225 | -56.99189 | 2025-06-20 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f291aab-d014-3147-864f-c9413e02422e | -11.94898 | -58.74511 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0db97787-81fd-3ac7-b8ef-61787f9c04d3 | -13.39461 | -48.44954 | 2025-06-20 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce7453dc-e7ba-3e9a-8f81-053ab976ab3f | -11.94593 | -58.7394 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e1d0b4cb-97b6-35e3-b7f5-b88b502ca967 | -12.02758 | -57.09885 | 2025-06-20 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7318ab34-cf2e-3cd9-8cf9-6412fd65dc6e | -14.03319 | -55.12254 | 2025-06-20 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcf9f0aa-287c-3205-a206-5e79bbfa928a | -16.30413 | -58.26711 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 30ff499f-f202-362e-8d72-33e947843f76 | -12.20009 | -49.6217 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1d26a93-258f-399d-8a45-f2741a6146a6 | -13.23825 | -49.83696 | 2025-06-20 04:53:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ee49895a-b462-36af-9123-990ba20b37db | -12.28201 | -57.26843 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f048c7e-dbfc-37e8-a7c1-8642f06ff01e | -13.37004 | -54.25845 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cd97c3e-9c1a-3411-b281-bcf38c8381e2 | -12.76665 | -44.41193 | 2025-06-20 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18531d4d-8c79-3c2d-adf3-933ecca981e7 | -11.81807 | -54.49837 | 2025-06-20 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b784bc5d-ff70-3a63-abeb-a61a4110dd63 | -12.20328 | -49.62717 | 2025-06-20 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0435eb50-ca4c-38d8-82fe-cba23ba04e69 | -12.0523 | -63.77706 | 2025-06-20 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 44ded3e1-f9fd-323f-bcf9-81db130145b1 | -12.34266 | -49.30994 | 2025-06-20 04:53:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be0d2fd7-6b31-3ce2-b8ef-195a9610facb | -14.04437 | -53.36761 | 2025-06-20 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c46f65e-3a2e-3f20-80b3-c6b4335bf164 | -12.49534 | -47.47935 | 2025-06-20 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f98b936-77dc-33f1-b944-4ad7038a573f | -11.37671 | -55.11185 | 2025-06-20 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 376ee0dc-4a8e-35f2-ae57-0272f67188a3 | -13.97466 | -58.10311 | 2025-06-20 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa775dc1-2961-3af8-8436-e7b8a7745a8e | -15.40449 | -47.80799 | 2025-06-20 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 470a019f-1814-3b8c-8f51-47d72a2db93e | -16.29908 | -58.275 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0247c893-8a74-3de2-bc27-bfb413197284 | -11.93715 | -48.41971 | 2025-06-20 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec5204aa-694e-3c34-a9d3-e556ecc9c11f | -11.95378 | -58.74071 | 2025-06-20 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16ad6c34-fc6f-3dfb-afc1-dd71aa03d370 | -14.50999 | -58.67745 | 2025-06-20 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41399c3e-0fb8-3858-8866-ac01e95ff682 | -13.24361 | -48.4174 | 2025-06-20 04:53:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca1bb144-a8c6-36f6-9480-6ffa0740f0e8 | -12.58288 | -56.96911 | 2025-06-20 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 496b56b6-60e8-369b-8785-90173baa7d3a | -15.40903 | -47.80864 | 2025-06-20 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7c0778e-85cc-3d52-812e-8ce14981e163 | -11.93614 | -48.4274 | 2025-06-20 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8fc723e-3cb9-33a9-8876-a9fc5eaf2de0 | -15.57061 | -47.85485 | 2025-06-20 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15699afa-9aec-3922-a3ea-b05a619fb3dc | -12.50012 | -55.73912 | 2025-06-20 04:53:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49865469-c6b8-385e-bde9-9a3799816756 | -16.29409 | -58.2608 | 2025-06-20 04:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |


[Clique aqui para ver as próximas entradas](README23.md)
