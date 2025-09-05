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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7fbe7c0-9146-3930-af8a-5bb9834828fc | -5.49821 | -60.12469 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd28caa7-7bac-38d7-9433-b6f59deeba90 | -7.69487 | -50.28901 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58254fd2-8623-3f0a-a7cf-2492a4b066a1 | -10.75854 | -48.2943 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72084279-44ef-3b8a-ac04-700c512e1c9c | -10.97779 | -45.94791 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee70f0df-32f0-3a9d-a483-bd3e179bd594 | -5.90979 | -57.73349 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dabfffd-5e60-354a-b980-11a81ca9dae3 | -10.23464 | -50.54532 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c00e4aeb-eaf3-389f-ad68-5cad173735f1 | -7.72597 | -61.52485 | 2025-09-05 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b95593b-220e-323f-b8e8-79d3b80e2941 | -6.82525 | -52.80985 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d8ecbf9-6065-3672-b0e1-5e8547ed437b | -9.98439 | -51.62908 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6453f52d-070b-3c23-b3f1-f0072c7f47e2 | -11.0879 | -52.01846 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eeeb4d1-8158-3fcb-ae58-02daaeb57eba | -12.2661 | -50.15881 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c58958d-167e-3931-9d5b-5beadf798a12 | -10.5081 | -57.77938 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 421801a3-f9de-38b1-bb1e-129b959a6377 | -8.3433 | -48.30984 | 2025-09-05 04:57:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5263b8b2-88dc-3743-964e-5e58d500c4ae | -12.7205 | -45.08199 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 66cce857-2d25-36a3-b723-5a6dd3214d98 | -14.03591 | -49.69222 | 2025-09-05 04:57:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ecfe3c7-3909-382d-9e06-26740f7e4c7b | -12.97579 | -48.05738 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63d8d45a-31a1-3262-a7a9-2b7f36430221 | -7.59262 | -46.21398 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fbb325f-2274-390a-95ab-f764f7787961 | -12.96686 | -54.78755 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51999b2c-26a3-3630-bfaa-1c1f96ac609d | -14.04081 | -49.68853 | 2025-09-05 04:57:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65cd26c9-6d62-3282-82f1-55dcc43c0978 | -10.44604 | -53.61035 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3aa87822-4048-397b-88c1-91dd57d61cb9 | -6.27493 | -53.44492 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cce0050b-cdd0-34ad-a787-375e4c3fec14 | -7.0744 | -46.19516 | 2025-09-05 04:57:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c00940ed-67ec-3a91-9121-1a6c2ee61771 | -6.33049 | -58.17031 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebe78212-4027-3b9b-a30e-5c02c22ba21b | -6.62908 | -53.15377 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9227f48e-58e8-3033-ac4a-e2f9372402bd | -12.29399 | -50.0157 | 2025-09-05 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dcd1d85-0e21-3044-b878-f03c2a16b4c7 | -13.66551 | -47.91446 | 2025-09-05 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbed5f1b-0f6b-3ee7-90a7-45d72b82bb21 | -9.51401 | -57.78505 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a40b030-f04c-3ed4-ab57-704fbbe3e05a | -8.09783 | -45.34453 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff0a8848-eda8-335d-8ea6-bd0e0887e486 | -12.95118 | -48.05925 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a4578de-2b33-37d6-bb39-8b725ee9bc85 | -11.594 | -52.18269 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0b16b0a7-d2fe-3bc2-bd5f-fecc8ee34f8b | -10.13609 | -55.00169 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 301842f7-69e0-3afa-b405-1ae1c87e9b83 | -8.01072 | -45.44151 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7df20ba-867c-3c72-93b1-2f0e9791f0a4 | -6.74156 | -58.73304 | 2025-09-05 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 152d8ed7-d46e-316c-90e9-269f418b6ec3 | -5.8639 | -57.76794 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb5aaf36-324d-3b2d-bdbc-00449387077e | -12.52133 | -48.07229 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dc7045b-6c7e-3f60-be2b-4290dee5808e | -12.97542 | -54.81439 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81c391c0-29bd-36f2-8855-98ca4fcde9da | -11.64444 | -52.22329 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5196626-3fcd-32c4-a89b-44b2ccac3fde | -8.01622 | -44.7746 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 018c0e07-148e-36da-8a2f-9fb11c13e678 | -7.76242 | -48.7877 | 2025-09-05 04:57:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a6418bce-0587-32d8-bd3e-6abbdcd61230 | -8.02506 | -45.4164 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 888d98fe-47fc-3abf-8569-c2ebc1284630 | -8.08875 | -45.33044 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 832f774b-4d8d-3343-8ffb-bc36f9853352 | -10.98826 | -45.92843 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dcb58c6-8047-3472-a204-5f55bc64848e | -12.90112 | -48.03164 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 191c1502-0e74-3838-80d5-334c8e8da68e | -12.91801 | -57.00552 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4946a5c1-080f-34d2-913b-494a221f6342 | -6.32472 | -58.18111 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2d70382-2560-38e2-986a-4efc647cb2c6 | -11.00532 | -47.15718 | 2025-09-05 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11f5a8f1-068c-3325-994c-f45d87bb2dc5 | -12.90663 | -48.02673 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 75e52689-fad4-3610-b1de-df1c079793fb | -8.65868 | -68.76786 | 2025-09-05 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9245444-488a-323b-8bf4-4af2a351d9ab | -5.86552 | -57.77123 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca29831f-201c-3b77-a849-7ce87c344988 | -12.9563 | -48.05754 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 277dacfa-f740-358b-b19a-1bed215d0ff0 | -12.29451 | -50.01186 | 2025-09-05 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41b4213a-ae35-3403-8745-f904411a8fe7 | -7.61109 | -43.85162 | 2025-09-05 04:57:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5f1b116-f357-38c3-ba42-e3fbd173be8e | -9.79759 | -48.30785 | 2025-09-05 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bac4df69-1549-3db9-8de8-6be65c2c6011 | -10.87965 | -55.39071 | 2025-09-05 04:57:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3d6ce9a0-9489-3349-91df-a9a16cbba291 | -7.23132 | -56.85578 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f173781a-d49b-3c6c-969b-d780f29da2d2 | -11.72511 | -47.74911 | 2025-09-05 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 244394c4-8f69-340e-8f2a-3e2f946708c1 | -12.86057 | -48.00491 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed4e4d88-dd29-306b-829a-ea9645d392a5 | -14.28806 | -45.22491 | 2025-09-05 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c07edfa-1cd7-3f06-975c-572b66ad1f9f | -11.58077 | -52.17197 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a226c99-d856-319d-b484-ab33c36ed28d | -11.59462 | -52.17847 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 307dcbd9-b871-3894-8951-65e653f4ab09 | -7.336 | -59.64847 | 2025-09-05 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fa6c0f6-77c7-3c3d-b42a-a9dfe4e9e619 | -9.32591 | -55.22906 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79512ef6-6bc5-3733-9192-5cbe6a42da24 | -10.52983 | -57.78136 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f302a6fc-a94f-3449-942b-164a19057b99 | -8.02459 | -45.41986 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65d38897-cb78-3700-a1cd-6dffd9c05aef | -7.61167 | -43.84739 | 2025-09-05 04:57:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d93d0f43-cb5b-30fc-a6d8-85b4f43bf557 | -9.63883 | -47.1043 | 2025-09-05 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f29f8977-693b-3cbb-8311-a2c6c761acbc | -9.33199 | -55.21215 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2e82c70-2078-384c-a861-d913fb993414 | -5.86403 | -57.78014 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d482fffc-04d7-3208-8842-ce249c61b848 | -12.63817 | -56.98539 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f93e89ba-178e-3092-a597-4e0b05c117ab | -6.26937 | -53.43689 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e3a863c-c87b-38be-bfca-7a449fe5f03c | -9.33641 | -55.20571 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78375f91-2150-3acc-b646-2223cafd98f6 | -6.27161 | -53.44441 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 989b43c3-a3f2-3758-8db4-ec3dc4165128 | -12.8927 | -56.94893 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db0e6cb0-3d78-3a12-9f7f-6b578659065b | -5.48887 | -60.12736 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 369b6917-6708-30bf-9e72-7b8a7ef7b75c | -12.48817 | -53.84829 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c8bee71-89bc-3cc5-b0e0-308b9bafad4b | -7.86015 | -52.12921 | 2025-09-05 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ea2c02e-c01d-3b0a-a8c8-fe80eb316585 | -8.02058 | -45.40934 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a80c8a7f-9dfd-34a7-816f-fee16ed9f5e4 | -11.82999 | -51.43932 | 2025-09-05 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee91ecd6-aa97-32b5-b2c7-40caed930e15 | -7.30243 | -44.07516 | 2025-09-05 04:57:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e072eb1-b9d2-33db-ac2f-a00d38d90c80 | -5.8565 | -57.76661 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c113629c-4dfd-3232-aac3-4bdf5c1822e6 | -7.33477 | -59.65576 | 2025-09-05 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 972b7f0d-bab5-3edb-8988-13edff575333 | -12.5319 | -53.81285 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 35150cfc-c9ce-31db-871c-26720f5d3e24 | -10.14282 | -46.24063 | 2025-09-05 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6c81f60-e2ab-38d0-b65d-07f591c7a225 | -10.09066 | -54.77249 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d97e751e-4827-3df7-a9b8-9b8db6a641de | -10.14167 | -55.16013 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5900cd94-a730-3dbd-9c13-09088080e545 | -10.50875 | -57.77542 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 438c895d-0c1f-397b-980d-e7ce3be524f7 | -13.46753 | -46.83913 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bac12aa8-84a2-332c-ae99-95bf5af324b3 | -12.9676 | -54.79845 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a49b07cc-f41e-3199-9ad1-7ed03cb41b2e | -9.96886 | -51.65943 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 067648e1-e5b3-3712-8993-8f9e35d82e84 | -12.4983 | -44.75822 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e90af546-1622-3e2d-911c-fccbae573abe | -6.33271 | -58.18012 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58e6faea-da2f-39b9-88ff-7e798d41d1c0 | -7.72909 | -50.32264 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7a54999-d34c-3ad0-a2bb-31630e9463c8 | -8.89542 | -45.77289 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f4c7c13-f822-3df2-a922-8909e24b8eac | -8.00534 | -45.44112 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82ab60d1-9c33-370d-a84a-2dc54dc2e490 | -7.95942 | -44.95144 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f5205c2-6503-347e-b675-5c854432324c | -8.05418 | -52.37511 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f76f5d0-ccc6-36c7-99e5-aeacbc56703e | -10.97883 | -46.0041 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b96abdae-70ff-3b3b-911b-94ed814ba37d | -13.30103 | -46.85212 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2d0723e-d2b4-392d-9158-1e027f2dd076 | -8.64886 | -54.84932 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8086945b-86b9-3cb0-983f-7db06fb6d540 | -11.00614 | -45.91694 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
