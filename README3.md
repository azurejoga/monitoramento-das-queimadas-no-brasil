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
| e5c927f5-5559-3ecf-8d89-634f3edf706d | -11.1186 | -44.656502 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6cf662f9-5d7a-3682-8432-70844c070c3b | -7.4954 | -45.355499 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b7fa808-d998-3d88-9355-73cdc958d9b9 | -5.5056 | -42.6311 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 876cdca0-9010-3fef-8236-892153048ac5 | -7.8932 | -46.435398 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6347a88-06ec-3eb5-acb3-bd70b620a20b | -5.7773 | -46.4585 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ca89bc4-6978-3691-9517-6a49ce48c5af | -3.7803 | -49.421799 | 2025-09-03 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ad06b7d-18c8-3d3e-93b0-5170fa59c34a | -11.3798 | -43.623001 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e489889a-77dc-3c6d-b22f-4c0ca416a1dd | -6.9596 | -44.363602 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de605b50-25da-3f03-896e-7e50906b6e8d | -7.7088 | -48.7589 | 2025-09-03 00:24:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e9327e51-a481-396c-88ef-500432612549 | -12.8421 | -48.062099 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd885fb4-e677-33b3-a91c-1a52b2836898 | -3.9705 | -44.464199 | 2025-09-03 00:24:00 | METOP-C | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e00ff217-8fb3-3497-9c0c-7fb2bb2a40f8 | -9.7584 | -50.011002 | 2025-09-03 00:24:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 972fcee6-35bd-3458-b337-4128898ef39e | -20.407499 | -45.705002 | 2025-09-03 00:24:00 | METOP-C | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1696a470-dc7a-3725-8a73-b966da72dfa1 | -5.8827 | -43.008701 | 2025-09-03 00:24:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef139962-6b34-3de6-8231-51d01b24a522 | -5.8098 | -43.227798 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9e44f66-8669-359f-93b9-4b6678be8951 | -6.237 | -42.625099 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48bac2e4-0fb5-39d2-b4a0-3e7a43dafb79 | -5.8365 | -42.9879 | 2025-09-03 00:24:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 26fc16ec-0348-3f6e-b34b-24026f31fc9d | -3.1944 | -40.735901 | 2025-09-03 00:24:00 | METOP-C | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 286f2ff3-e3b6-34da-8f92-3d8d0237747a | -8.0563 | -45.3755 | 2025-09-03 00:24:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8bb37413-c481-351b-a7a3-71fe4bff5ab3 | -8.2066 | -44.811298 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f7ffb79d-f36c-3623-b4f2-752e607bd4b8 | -10.4762 | -50.322399 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6063280-ab1b-3909-afa3-d82de1a5f0a5 | -13.3189 | -46.827301 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5cdbab-84f5-3f75-97fe-a3a9975bbaa3 | -9.7003 | -48.300999 | 2025-09-03 00:24:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df7e7f09-cbec-3d40-aeb1-466169ac9b4f | -7.695 | -48.742401 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3ffb79-fb7c-3d49-9b64-e00ca6b3e8e2 | -6.9619 | -43.300499 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3acfb2a1-b2ec-3834-8a6b-a21b9451c343 | -11.1187 | -45.117401 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98213d0f-553c-336e-8b9f-4cc77fb402b8 | -10.5269 | -50.419102 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a0bd963-bf7c-3eb9-9025-6ba69933325d | -7.6285 | -46.540199 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d79ab25-50c1-323c-a0dc-cb22b3f14501 | -20.728901 | -46.837399 | 2025-09-03 00:24:00 | METOP-C | PRATÁPOLIS | MINAS GERAIS | Brasil | 3152907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71e8bbfe-e0a5-37a9-af65-da1b446a22d6 | -12.889 | -48.041698 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8adec039-57f4-31ca-99ef-c5442172c542 | -6.7413 | -44.042 | 2025-09-03 00:24:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb054dc5-8476-3689-8478-8e5405233dd6 | -12.7988 | -48.050499 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7616d86-ce56-3f15-9ba6-f91e765d2e96 | -7.2824 | -45.2799 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe44bd68-77ed-3b9b-b4cf-6b1c3b24d723 | -11.8815 | -46.673599 | 2025-09-03 00:24:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00998e64-d2d3-3f8d-84e2-04b41c41e883 | -5.8064 | -43.2132 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8727e546-9d6e-3fc6-b0a4-5aa330d40169 | -11.6296 | -52.046501 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdcef5be-8843-3232-82a4-4ceb12c6a752 | -6.2513 | -42.597599 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6eef26ed-ade7-3b77-9ce1-dbe910ba33e8 | -7.6302 | -46.547501 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd57c5e-6dcc-3468-a29e-48824443195f | -15.5422 | -48.348 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 41be0b40-d933-34c2-9539-871b0f0befdf | -12.8401 | -48.052101 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f81ae555-fd66-33cc-918d-3f54846d2706 | -6.5746 | -44.5737 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07b49ee6-f876-35af-99b7-b26d9d1c2a27 | -7.9046 | -46.440601 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce0cb02b-dd20-3cc2-97bb-b24221464936 | -8.0124 | -44.051701 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c08d451-e793-30de-8f46-679d6d057cdb | -13.6926 | -46.9482 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f545fbde-25c6-3be3-9b50-0e041c0ea5cd | -6.4483 | -42.3811 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f8e9a72-0ca2-3e47-8c56-dcee416eca77 | -5.6924 | -45.9478 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b5f7bba-6cde-3cf4-9e13-558c796bbcc1 | -7.697 | -48.751701 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 57e24f26-ad20-3f0c-a81d-04cc3fc9b19b | -6.7933 | -44.0886 | 2025-09-03 00:24:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 381a7d4c-b2f6-37b4-bab6-d7957f104f21 | -10.2524 | -51.1581 | 2025-09-03 00:24:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5dce6b33-1379-3c84-a4f7-7e8f5255b247 | -12.4828 | -47.472301 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72f4e15e-b22b-3e24-9b23-f446908dae2d | -6.8381 | -44.238701 | 2025-09-03 00:24:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1b82105-be24-3269-9067-83c375b15456 | -8.8826 | -45.797798 | 2025-09-03 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0a8b108-9bb1-3545-9f23-7675fd172f5a | -9.1832 | -45.210602 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e48d7cf0-8aa7-33e3-90b7-41ab4590daa0 | -7.9112 | -46.469898 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 463503e0-da7d-35a7-80f0-89be6945334c | -6.4056 | -43.75 | 2025-09-03 00:24:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73bef6f3-a11b-3c24-ba63-0180fc37fe9d | -12.8554 | -48.028099 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f349232c-cc4e-39a8-8de1-8e736376982d | -3.2186 | -47.123501 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b178a74-7fb0-3865-9f72-2a03342558af | -9.6126 | -47.848202 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97d6d731-3ae9-32f8-ad29-0d73124dc346 | -6.3656 | -42.999599 | 2025-09-03 00:24:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edc3d6ca-b334-37e9-842f-677d048886f2 | -7.3761 | -49.394001 | 2025-09-03 00:24:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18b22ce4-51b8-3056-b36d-1d5d08a40b8c | -9.1605 | -45.201099 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ab462a2-cfc4-3c10-8149-e7879493a84f | -5.5093 | -42.646599 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2b498804-0d25-300a-b4a0-15ee3f204064 | -11.6199 | -52.0485 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc389f1-7d51-38a5-b85a-9bbc333cd5f4 | -6.542 | -42.959 | 2025-09-03 00:24:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2324f3b2-18ce-34b2-bf52-bd9f4bc92e1f | -11.0362 | -46.892399 | 2025-09-03 00:24:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47d2f4c0-278d-389f-9899-971e9a7a7b23 | -5.6147 | -45.020599 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14f1ac13-1731-35aa-b364-0d910509395f | -12.789 | -48.052502 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1ded21-e938-34d6-9723-8800d074edc8 | -7.7126 | -48.729 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 873c2ae2-331d-33b7-85d0-22f0729f9a2b | -7.89 | -46.4669 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 226b9996-0067-3c01-b231-f8b364a4dae6 | -6.9389 | -43.2906 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 377f8f94-8482-3b3b-afab-f7bfbfa4a742 | -8.8678 | -45.823601 | 2025-09-03 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bab837d3-63fa-31bb-b1f1-c36895f4d718 | -2.1312 | -48.003899 | 2025-09-03 00:24:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccd7dfce-550a-3d29-8d7b-aa433b2e3670 | -3.6965 | -44.170898 | 2025-09-03 00:24:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca52bdf8-8a5b-3f80-9076-67f05736e901 | -2.9333 | -49.449501 | 2025-09-03 00:24:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13ab16b5-3dec-300c-a53a-11305a6d8894 | -7.4599 | -44.792 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| abacdca0-39ba-35f0-98fb-bd16a140c305 | -6.8177 | -52.816101 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da5a98f-4a5d-3209-83c3-ca4b5d8e88e0 | -3.7823 | -49.430801 | 2025-09-03 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78f04888-ce9d-3348-8e17-5d158f09da82 | -5.6018 | -45.009102 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b384377a-e388-3653-901d-922e146eaee0 | -13.7006 | -46.937199 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0356643-160b-38b3-9442-c61e3f464bdd | -10.4815 | -50.348 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aad49c48-2767-3581-a6e2-8a70e8254376 | -6.4657 | -45.4053 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfc78314-496a-3bcd-a519-35d0fb11121e | -6.6006 | -44.103199 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e46b781-4167-3497-8545-2779dc61bc9c | -7.9194 | -46.4604 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a085b84b-f6fb-3a89-8574-1f5b2b220a12 | -6.6859 | -48.401299 | 2025-09-03 00:24:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 467c4eff-acde-3a1e-94f7-2912ff597f3e | -11.0244 | -45.063702 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35b5b4c3-ca8f-3276-b70d-889b34dbb6b5 | -15.5467 | -48.3708 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25873026-27ee-377f-90b5-aa3078fe1af1 | -9.45 | -40.404202 | 2025-09-03 00:24:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6ae02e5e-4336-3555-a393-555d823ebf93 | -6.1133 | -47.217701 | 2025-09-03 00:24:00 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d41a8021-469c-3209-9640-ca9ceeac9d11 | -6.9927 | -43.255501 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3c39d62f-cf54-337c-975d-dd9294a53a1b | -13.6614 | -46.945702 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c79890a0-e074-3755-b4be-9f358735d1a9 | -8.876 | -45.814301 | 2025-09-03 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f1fce0fa-237b-3adf-bb1f-02608a847d5f | -11.6082 | -52.141899 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d62cca81-c609-34f7-a163-1510afe919e7 | -3.7921 | -49.4286 | 2025-09-03 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd9280b6-3637-3f46-a389-fa42ad558518 | -15.5536 | -48.405102 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b3f79f02-3e11-3b4d-af65-e306d03f8a61 | -13.7104 | -46.935101 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 115d21db-71dc-363a-9437-068ea581aa56 | -13.6964 | -46.966 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e32aa26a-4063-3267-8081-5bc725c87c23 | -5.7902 | -43.2323 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 314bd49e-6779-33d9-a26d-d59eba741142 | -11.0358 | -45.0686 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81b9fe86-dce2-344f-9572-605a53682c53 | -15.0159 | -50.0588 | 2025-09-03 00:24:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 69608708-cb3b-3c5f-a854-43d4e512fd0c | -15.1237 | -48.191101 | 2025-09-03 00:24:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
