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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0306055-e94a-3dd3-94e5-f76a558ad920 | -5.88915 | -52.08681 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a07c042d-fee3-3033-9837-35026f345614 | -7.66219 | -46.10064 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f43749b1-990e-39bc-a340-43afef043c22 | -4.57474 | -42.95052 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e7c23da1-d98b-3718-b2ca-1927fd597a96 | -7.67441 | -46.08816 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df5adb1e-4e5f-3537-bdfc-451b79d26a5f | -7.94226 | -44.81271 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a86f52c-2933-3582-8698-d813e10181c7 | -6.94956 | -43.10739 | 2026-09-18 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b38c692-affc-3684-951d-78c1347b0399 | -4.5433 | -54.93149 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db8ce691-71be-32d7-b36c-f62fafaf41f1 | -6.33209 | -45.66924 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5022b45d-6bad-324b-877c-e92c0d73b208 | -7.37564 | -44.52119 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27c5e5dd-80c9-350f-a6ac-eb003fce192f | -5.51542 | -43.66591 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8fbc2686-a715-3acd-91cc-7b78c0ca13cd | -6.03499 | -51.80499 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6bd453d-ea1a-3999-acab-af53cace0474 | -3.37349 | -50.44407 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 074b5a5b-4255-3faa-8758-b36fc726cc2f | -7.14528 | -42.14213 | 2026-09-18 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e0489f1-fd1f-31d4-90d0-9b907582dd23 | -6.99441 | -42.15696 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cdba5d3f-7078-3da6-b725-f1107f2224df | -4.81234 | -42.88694 | 2026-09-18 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a9023922-0b13-3eee-ad0d-a19758e587f7 | -7.80059 | -44.89352 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7ac4335-ebfd-3a61-9290-676210664cc0 | -5.04687 | -42.61499 | 2026-09-18 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9754471-aedb-3f44-a52b-d1eb6b7f2868 | -6.95265 | -42.55437 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1d7d0ffa-be00-3754-8341-937058ff2995 | -6.65234 | -51.49063 | 2026-09-18 04:19:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f760e42-ba73-3d27-8ca6-815bd93edf12 | -4.56972 | -42.9608 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1edd7ee5-3784-3cfc-8569-319927ec599f | -3.17548 | -48.58114 | 2026-09-18 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cffe019-4aca-3a43-aaa1-391cdb27a767 | -3.21312 | -53.94981 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32ba7a2e-ffe1-379a-8e81-967fdc7cb95e | -6.4676 | -48.00673 | 2026-09-18 04:19:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28168df0-a429-3c3d-8f0f-998c16266d4e | -7.9898 | -44.04056 | 2026-09-18 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e09d1dc3-fb94-3cbb-a81d-1bf5dccf6b6d | -1.49077 | -54.97263 | 2026-09-18 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3238981-38fb-39ec-a02f-edd9b60f8183 | -4.55004 | -42.95412 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 384237d8-03f6-3a59-b41f-bcee8bd49bbd | -3.37211 | -50.45243 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5beeba1f-dcd5-32ed-bef4-74fb6fa5432a | -7.93408 | -44.84349 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fff16319-329d-386c-916e-901e9d0483d5 | -2.64498 | -54.69179 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e96df56-a149-37c6-baae-bdeaa08bece8 | -5.16056 | -45.24417 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84e9f9fa-606b-3a90-b97a-f50472745595 | -3.96688 | -48.12696 | 2026-09-18 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dc2c11b-85f3-3b88-85fd-96bb79d6c6c6 | -5.6346 | -44.80229 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0f21d2d2-b1c0-3f71-a012-daae8c0345e5 | -3.69104 | -44.15476 | 2026-09-18 04:19:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c626cf1-e70d-38f2-99e2-2ff4d0b2d514 | -4.5905 | -42.9603 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0edc97a2-a854-3018-9f20-3a9cc44d31f1 | -5.40545 | -45.847 | 2026-09-18 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| becce69a-5cb6-3c07-bdd3-fe21f6f5ade3 | -5.62968 | -40.86418 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 530038ac-b4d2-3fa7-b672-b4ad89e58422 | -7.00149 | -42.15815 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a56f0ef-7c73-3a1b-b744-212829f31d16 | -6.43821 | -44.95083 | 2026-09-18 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fba3b1e3-453a-3985-aff9-09e783232460 | -7.79898 | -44.90391 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 496d47b7-9f4b-3bc9-aa29-91425f448e51 | -5.77411 | -45.1073 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0d68866-7aa1-3ead-93a3-2426a333b29f | -7.00691 | -43.87098 | 2026-09-18 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d5ecff3-7b38-3375-9669-e2519cc5be55 | -5.62132 | -40.8596 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3c17aa6a-91f5-3583-ac57-94383275ffe7 | -7.67828 | -46.10682 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b02d987b-7d70-3547-aa02-1e474ee4d1c9 | -3.10693 | -51.26397 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2f92f5c-79f5-34fa-969e-98ce1903734b | -2.96881 | -52.13589 | 2026-09-18 04:19:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e8f1f657-1f04-3836-bb5a-f8aa4e79e4fc | -3.35743 | -50.45578 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17190097-ee88-32f5-b0aa-6cc4a111a525 | -5.61998 | -40.86838 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1c969bc4-ae95-3040-99ea-19827b1c8bdf | -7.93516 | -44.83655 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c9559e2-0f30-3306-840e-a0123f413db4 | -2.2425 | -48.75373 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e9b8baf-8700-3d93-b08e-3c040a39ea89 | -5.22711 | -49.30844 | 2026-09-18 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 178abe0e-b57a-32a8-a2fe-986fd7cd8a27 | -4.5669 | -42.9567 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9e369ba-a09d-3537-8d97-c457c84ab05e | -5.58068 | -48.10214 | 2026-09-18 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7f8c27a-701e-3df6-8c62-b76396b6a3f1 | -2.8146 | -50.46272 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b927ed7-c384-3137-b784-21b605362236 | -5.89336 | -49.78348 | 2026-09-18 04:19:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4e3e63a-30f9-3f90-9dfe-3ac695611d2f | -5.51597 | -43.66238 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3aa9ea2f-9034-360a-b173-5409f76a0300 | -2.60942 | -54.76052 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 854f90ab-d702-3ad0-8f10-ea346582e808 | -2.05329 | -52.16496 | 2026-09-18 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c95300d9-74e0-3ef9-a1f4-5fc4d44a477e | -2.96284 | -50.33133 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a182b127-2bee-3b73-bdbe-1e5047981479 | -7.79952 | -44.90045 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 194b7895-6493-3b9a-964e-4e40876fea7d | -3.26254 | -54.27078 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e9192b68-f2c9-39d2-9e84-629a5380192d | -5.92148 | -42.99452 | 2026-09-18 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56d83a81-4964-3a16-aebe-1c8b4ce9af13 | -7.45631 | -46.83685 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02345b4c-0bc9-3a01-8e46-69219b33d54d | -7.66442 | -46.08659 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 45088824-dc20-38d4-9e22-8e5bb0905c0e | -3.26463 | -54.30678 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48f1ce1e-8c27-375a-8596-1979b6f4ac80 | -3.92734 | -55.92454 | 2026-09-18 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 596f8aaa-73b6-383a-aa63-e962a8fa9089 | -5.6577 | -43.38398 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 36dce8c1-9587-321d-acfc-2609691e00fd | -4.4988 | -45.90545 | 2026-09-18 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d6625ea-5db5-334c-8635-a0509192a2b9 | -7.68051 | -46.09272 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6cfa7e04-e05a-3814-bc84-704a476e0aad | -6.65474 | -43.63847 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be015126-ae8a-37c8-a9a6-6f91b41d861d | -4.3739 | -55.42101 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b31c6f3-c73f-3e96-a747-4d613ddcbea8 | -6.41332 | -43.46621 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e143adbf-19b4-3747-a756-e6dbbc8e788b | -4.88565 | -56.06195 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2ff0edd-60de-3ca2-b615-0235f6fabec1 | -6.51994 | -49.88813 | 2026-09-18 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3cb97fc7-3f7b-3420-91db-5172ecd59ba8 | -2.05832 | -52.16579 | 2026-09-18 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f9caec0-15c5-37b1-bdaa-8f04a02b3eda | -7.96803 | -44.82436 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6354bfd0-ef24-3ebd-ab71-6e86464167b0 | -3.70227 | -54.1762 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3bbe238-0272-3c36-9fab-2c8bfd2c49b9 | -7.08334 | -47.47765 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dd64ad2-173b-328c-a18f-da00c6165c1b | -3.74549 | -51.12561 | 2026-09-18 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abdef0c2-b55f-38cf-b0a0-6d76db72629e | -3.36405 | -50.44688 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 49cdcdf2-a180-3236-ab74-08d3c4caeaeb | -2.82272 | -50.46843 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 4d154799-486d-3a2b-bd8d-90e69d81c969 | -4.49768 | -45.91262 | 2026-09-18 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58268d56-7a3a-3313-a091-10ef0d3cc89c | -2.29789 | -48.58504 | 2026-09-18 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e991965-4ba7-393f-9135-2aa22b3fe7cb | -5.83123 | -49.95614 | 2026-09-18 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9881b849-7d5a-3636-a81d-98ebc0ee370c | -4.43065 | -55.52319 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 836b32f4-4eb7-3f93-841a-1c06a687abf9 | -5.14682 | -55.94452 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a5ba9f6-89f3-30f6-978b-8497a60e3c35 | -3.38086 | -50.45383 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd9e7824-15b3-3020-a868-55cb73c33a53 | -6.59355 | -45.8868 | 2026-09-18 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b51ed87-8274-3ace-a341-af26f8387eb9 | -7.00518 | -43.63721 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2b8ae692-b78a-3617-8c11-1d4a02faf3cd | -4.77211 | -55.70631 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0999ab0-1fc9-3705-a0f6-9c7377850f02 | -1.161 | -47.62959 | 2026-09-18 04:19:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25ff17f4-d07f-37eb-b84a-e454b8a2d6e3 | -6.65529 | -43.6349 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d637de9-d3a0-30fd-8f3c-33b30b0e84d3 | -7.01636 | -43.63161 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b5ccbeb-e8a4-38b0-a03f-95c13b38c8c6 | -4.00486 | -41.26862 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05ddc590-8bc2-35a5-ab08-c2b5ccdadfe2 | -5.65676 | -43.21149 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 23d76641-a3e5-3c0b-88a4-85a90509e89e | -6.2878 | -41.80092 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0052a51c-aaab-3104-b83e-718e25f69655 | -7.46251 | -46.8416 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a66830a-751b-388e-8e3d-07596a4ab980 | -4.4936 | -55.49302 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e93fe7be-bb22-3070-b153-73401df18133 | -4.56635 | -42.96029 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9d574f0-c198-3e23-bb56-44bc5646a84e | -5.73789 | -43.27873 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e65616f8-196b-3049-b886-4af3ba61be93 | -5.64067 | -44.80676 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
