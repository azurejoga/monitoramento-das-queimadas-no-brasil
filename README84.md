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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcfa9ef9-4e3c-3678-854b-ef3f860e94f6 | -5.80229 | -43.2366 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79412cfb-e499-37e8-a0ce-c4393e737e75 | -5.9103 | -57.7223 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31c5dfb1-af7b-3542-8dbf-8a42cd162b8b | -8.20989 | -44.80755 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5032633-930c-3687-a017-cfe6d97a906e | -5.91862 | -57.71289 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab040305-3d93-35a2-82ed-8240add36de9 | -7.47707 | -44.83276 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69ee8699-96d9-35f5-ad2d-9727c0633461 | -2.94097 | -54.80367 | 2025-09-03 05:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ece72a10-8686-365d-ba1d-407caf5d1ae6 | -6.33999 | -58.18566 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd0e27be-d313-3394-9561-a7fe419acd72 | -6.22895 | -55.93752 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2378ab1-3317-39b0-8229-b26d69f3477d | -6.85797 | -52.79211 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2d8397c-7a13-38f2-9648-2ff71106139b | -5.89866 | -57.7526 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46a85b8f-c6af-32b0-946b-5941ad544e20 | -7.90846 | -46.44265 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b4a020f-626e-3422-82fe-d54d08e11467 | -5.82105 | -43.22138 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8ceea9e-6481-3da0-8d99-6413f24f3b72 | -6.80492 | -52.82485 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd863236-2b78-3328-85f8-90a3d47ce864 | -6.3446 | -45.66841 | 2025-09-03 05:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8e8ef29-0833-3012-b90c-a1c0810b4f6e | -6.46736 | -53.4017 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 430e54dd-f72a-3a14-910c-a63eca8ec882 | -7.4928 | -44.81755 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ece4c55d-6e2c-3bcb-823e-4116216668a4 | -5.55552 | -43.76065 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4eca8106-1c92-3bdf-a7a0-654d7308347f | -7.72072 | -48.74391 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39c3d323-cf27-36db-b03a-1cc3c833a892 | -6.81039 | -52.81883 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad0965cd-c873-3502-805a-3ab6b17054c9 | -5.90698 | -57.74319 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6cc84a5b-2759-3254-bbbc-607eff922ba2 | -3.20047 | -49.11241 | 2025-09-03 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed85b887-7372-3408-a858-191714af606e | -6.26166 | -57.89271 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61296ad6-57f7-3e63-babb-72dd3e8c012e | -6.89895 | -45.56318 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 092f7cdc-6a17-39cc-89f9-615f00b80152 | -7.53111 | -47.44206 | 2025-09-03 05:12:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8857dbd-f377-3c31-b7db-3a24493593aa | -3.79178 | -49.43024 | 2025-09-03 05:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b0146b5b-496b-337c-9902-a42834068303 | -6.27799 | -44.51368 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b392d36-ae9c-36f5-b4dc-29b620fbf07c | -7.93774 | -46.55322 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d28ffeb-65cf-313d-a894-b2f83448009d | -5.91196 | -57.71184 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83caae07-b0ba-3080-9c1f-85ea656eca6b | -6.81704 | -45.6801 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59ddf267-f13c-3fda-b9cd-0c082fb3e05f | -5.31685 | -55.88178 | 2025-09-03 05:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ac5c7fc-c90f-37bf-aff0-470bcfde6465 | -3.23044 | -47.11994 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67ebee27-9b17-3ac5-930a-6224b8c97c67 | -7.92675 | -46.54235 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32976026-35f8-3ce8-8e29-7f7df74914d5 | -6.70104 | -48.39979 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 526c2ebb-5d28-355c-b306-ab7c791a9380 | -6.02574 | -46.00407 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94cc1964-c935-3409-a6a1-534a448f569c | -4.16306 | -46.79023 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5ae99918-8976-3eaf-b242-073fc8b5dfd1 | -5.87255 | -57.76637 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 40a6d8db-e5ad-3d55-adae-1d7f33e4d0f6 | -6.80495 | -52.82824 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4986d99f-bf7d-384f-8359-251a409b91ab | -5.89814 | -46.163 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 167df6b9-95f9-38d6-af6e-4142c1c89946 | -5.92529 | -57.71394 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f68609d6-e5c5-3064-ac4b-006ad4bf9477 | -6.54584 | -44.56505 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46acd865-c722-379f-b8af-7372bbed0a64 | -6.47172 | -45.40466 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6da6c5c7-0ae1-3d6f-b453-84b99153d650 | -7.70056 | -48.73478 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 554b4a0e-300a-350d-a842-078262648d5c | -7.47629 | -44.83862 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68c14835-b4cb-33b8-b741-5097687ff4c1 | -6.80957 | -52.82046 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6c2e7d2-2489-3996-940c-6d8873b7141b | -3.48237 | -59.2555 | 2025-09-03 05:12:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ab3814-6c24-3beb-a5af-15b2f4ee4401 | -7.90953 | -46.4808 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01b5fd29-acc1-32d7-8809-5e33047f40ff | -7.91044 | -46.47602 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df090648-7f6f-3792-a0d6-12d4b881af24 | -6.231 | -43.38153 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5863ceba-10ec-3e46-a5fe-f67104ceefaa | -4.58014 | -48.02057 | 2025-09-03 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d11b8030-b7b1-329e-9546-ea5f32025be8 | -6.33499 | -58.17401 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8b717fd-d214-3e35-9665-032f42c5c7d7 | -3.44444 | -54.63747 | 2025-09-03 05:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5bf24d6-905c-30af-87c8-2987c45f05d1 | -5.86977 | -57.76234 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c368b4ae-292a-34a4-88d2-ab7360d6e397 | -8.05853 | -45.36617 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0d7679ef-cada-306c-839e-bf341628d2e9 | -7.69278 | -48.75209 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d567189a-4564-35de-9ab7-f8a4ddb7d764 | -7.62704 | -46.54647 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3904952-a405-3891-b85b-63abc39e48bd | -6.845 | -52.82564 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be47add8-e079-36f1-8ef2-bd507677c2e2 | -7.69235 | -48.75517 | 2025-09-03 05:12:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ef97541c-1433-3f90-b174-d37179f9b466 | -6.22951 | -55.93393 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30a68115-7c81-3bcd-a43f-02315fbcbf20 | -6.85898 | -52.81256 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9635e649-3697-39f6-bf4c-a0308361e8d7 | -6.14976 | -57.9353 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44ecdda6-e557-357d-a99d-d647272c62bb | -4.15739 | -46.78925 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 27557b32-9f17-3b0e-8a60-6173f8a592af | -3.48801 | -48.44206 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d9e559b-33da-3db4-8b19-f2c483481e52 | -7.70099 | -48.73167 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b16eb076-8b43-3579-a908-74c885ea8d7b | -5.55467 | -43.75613 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7e91abc-b4e5-362c-9796-902705f83150 | -6.20149 | -43.34511 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0790b2d-d197-3a1a-8eb8-4b1cd9824827 | -6.46734 | -55.88837 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8956842-7070-34da-8076-880807f0eb5e | -5.90752 | -57.71828 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 184b2206-681c-38fe-a79e-8b6c8798cc1a | -8.07024 | -45.36989 | 2025-09-03 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 775739e1-613e-3f6a-8b00-614a31118002 | -7.70625 | -48.7324 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 423e01b1-ed54-34af-a330-a6315d12679d | -5.91641 | -57.72683 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d68255d6-c547-3036-b664-c32cedfd1baf | -5.86699 | -57.77979 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8547129c-9aae-30a2-97ef-5aad05178b82 | -5.79734 | -43.23357 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e119c1eb-7b96-35bd-bf5b-7dcb0c30804d | -5.81057 | -43.23001 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16f7a14e-61e6-3213-937c-a0b60cc8cde5 | -2.1999 | -47.99564 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d48c2498-fb69-3b15-a26e-415be3acad10 | -5.91032 | -57.74373 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68041c17-601f-31ae-a48f-f9042a17fa31 | -7.94443 | -46.54949 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18a45910-38ff-3e40-8884-4c51e94d4150 | -6.33107 | -58.17701 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b18559b-bb44-32d8-bf2b-2266517f40b2 | -3.41273 | -51.56402 | 2025-09-03 05:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8ee4911-76c2-318c-9e89-852a908dcb2b | -5.86755 | -57.75483 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bc0bdc7e-a7ef-3f15-af2d-5af34b608f33 | -5.69122 | -45.94732 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e240588e-bf97-3536-9333-605ffd9e1d99 | -8.06518 | -45.36642 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28d556c7-a913-32d2-b7c3-da5826f566d7 | -5.48286 | -51.22571 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09cb8e68-773d-3ee0-a6e6-67a4a9fc1a94 | -4.90161 | -43.2074 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 475b6e3e-2910-33c6-ae18-5847d3ce7f66 | -7.6993 | -48.74376 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ee66e257-f870-33a7-92e0-7a748c1082a5 | -5.92251 | -57.70993 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7d406141-f09c-3421-a357-a2bf64af05ea | -7.71421 | -48.75209 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 543fd175-8f8d-3fd7-ae99-e59b657d08be | -4.24413 | -55.53463 | 2025-09-03 05:12:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ce5b9ab-42ae-3bf4-bf17-e38e1c612de2 | -4.4289 | -56.13397 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2a7fd37-2548-3bec-9a3c-5f7ac6acf697 | -8.07183 | -45.36661 | 2025-09-03 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 877a6eca-5424-34cc-808f-47752b17cc1d | -7.11733 | -44.75581 | 2025-09-03 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ee2410a-cbb3-3377-b364-af3a6a73021a | -4.90067 | -43.21423 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed0d082d-a732-3627-bdd6-4ded332edb09 | -7.7072 | -48.72565 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7fe6d64c-1697-3191-8984-5efc29a5da9d | -5.91529 | -57.71236 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2be8b5e-d9a4-35d3-b04c-b2073641d7f5 | -3.22938 | -47.12702 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b34ef11c-0cbb-3e8f-a492-0048ba0e90d9 | -6.70063 | -48.40282 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4d19829-b33a-3f28-ac2b-4793befbfd5c | -5.90087 | -57.73865 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6dbfc187-489b-3634-960e-5f3dc7535418 | -6.80646 | -52.81823 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a238b24-8e96-3a1e-9a18-94de3c747a17 | -7.90116 | -46.45102 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30427a8f-2f02-35a4-a812-c7e9064b8df8 | -8.0519 | -45.36578 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 671f864e-45f2-3f42-886b-f3a5d2bc2393 | -5.90809 | -57.73623 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |


[Clique aqui para ver as próximas entradas](README85.md)
