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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55333f0a-497e-384f-be62-454ed143d747 | -5.24933 | -55.94623 | 2024-10-08 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65728fd2-7e04-38f8-b513-3d73758123f3 | -9.36141 | -57.50076 | 2024-10-08 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cee9995e-b8bc-3b95-80d0-754734aa3c28 | -9.36076 | -57.50519 | 2024-10-08 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc6a8465-bb0a-32ab-93f2-794830a96a61 | -9.35771 | -57.50019 | 2024-10-08 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 082cb486-a468-3749-92f8-06f647eee4e5 | -9.35707 | -57.50461 | 2024-10-08 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 806f5318-31be-3a90-ad00-1561ccd9b18b | -9.34226 | -57.60619 | 2024-10-08 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb5cd876-712f-3d79-aee6-8153466064ee | -9.64916 | -56.70166 | 2024-10-08 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63159950-c4b1-3fd7-9ec9-bdb772b8fb26 | -9.64803 | -56.70417 | 2024-10-08 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bb0b973-a2df-3ddb-86a2-fcc6aa635b6c | -9.54463 | -57.90596 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbf7fa6c-32c5-3928-b4e2-0d1cf50f5bb3 | -9.54099 | -57.90543 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e8fb77f-d187-3f54-ab8b-7d37572ec85c | -9.48524 | -57.93169 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6feb518-cb75-3138-ab2c-f9e4e1dbb949 | -9.47923 | -57.92204 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6ad7862-8739-3678-a1c2-9b1f1d201dfa | -9.47812 | -57.9231 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32f4fad2-24fa-3792-bce6-165d0ca79fd0 | -10.60111 | -57.52788 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bae3d38e-4687-3092-bca6-9eae50f952c1 | -10.56155 | -57.69358 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5646ea8-4778-3e95-970a-f76f51f6549c | -10.55784 | -57.69302 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4faa346-b3fa-3384-a28c-32a562353796 | -10.33029 | -57.79419 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aaa515b-ac57-3a7d-a3e2-b75e3c3ab3a3 | -10.32661 | -57.79361 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 044687b2-181f-383f-be60-e5024b49f0f5 | -10.24164 | -57.73848 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9369cf3-1772-3eaa-a178-b09c64be8af5 | -10.22212 | -57.79417 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a54294b7-05e9-3f5e-8bf2-ed964ad8f873 | -10.22147 | -57.79857 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 304da074-d009-31ae-8c04-866758d52354 | -10.12052 | -58.20733 | 2024-10-08 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23b6a2ed-6398-3513-8d4c-c941a31a7d8a | -11.97012 | -57.59751 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 899a522f-bd65-352d-8b17-d055ebfb21bb | -11.96944 | -57.60225 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6fb3935-fd78-3749-a21c-361e459cbdc2 | -11.96632 | -57.59692 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 775464da-8b90-303d-8e40-96605321c0c1 | -11.96251 | -57.59633 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1084d4e2-f8ce-3e20-96fa-1256dbe06d91 | -11.97772 | -57.59871 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ee4a3d8-3984-3aec-ae24-e8c4ab8ba9e8 | -11.97703 | -57.60346 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a0b6ea-9f4a-30d4-8496-351f6bfc0b84 | -11.97392 | -57.59811 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e2e908b-40f8-3f85-81f0-dd94a940916f | -11.97324 | -57.60285 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b828395-204b-38ea-9692-3510dc7f4323 | -11.96564 | -57.60165 | 2024-10-08 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de3fd192-983a-3c98-831c-f6b93f5efef8 | -12.47388 | -57.66245 | 2024-10-08 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f105627-995f-348c-adc5-c31d653033b3 | -12.47321 | -57.66724 | 2024-10-08 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca77d1ab-a6b3-3d5c-b739-90622d4307fe | -15.33955 | -58.13315 | 2024-10-08 05:23:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f798b9de-e141-3d9e-8a98-42ab7a3e5e6d | -15.33885 | -58.13821 | 2024-10-08 05:23:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1d42c6a-20c6-3b86-93b8-75138993fa73 | -15.22471 | -59.35774 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d0c96a6-932b-329c-8e3d-46152d7f92af | -15.22304 | -59.35906 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa5e2082-bddf-352f-a5a4-c50ecbfeafda | -15.12594 | -59.02421 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7389a37-df0d-3534-88e1-4dadff97a68f | -15.70714 | -59.42176 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 316cd404-3248-356b-b68e-cc87621bd13f | -15.70653 | -59.42607 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17b9695c-0009-337c-9d5e-5d4e82ade3f9 | -15.70531 | -59.43464 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5da4b38-d897-33c2-9a5f-4060734248f7 | -15.7047 | -59.43888 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3faae2b7-ce65-3d26-8d9e-da910415afad | -15.70293 | -59.42547 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f20d1d85-3424-3761-8642-b3f21a4396c7 | -15.7011 | -59.43832 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a42f7028-4c32-335d-b79a-6867280b8336 | -15.70051 | -59.44247 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4d8048e5-9e01-3eb8-921c-7ef59960783c | -15.69872 | -59.42921 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27babc3f-1250-3530-833a-0002214feef3 | -15.69691 | -59.44193 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 197ee413-cd49-3652-8dc4-cb796eece1ca | -15.69512 | -59.42863 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1115358e-750c-3917-bb67-90b6e4720e3e | -15.69451 | -59.43295 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de9b0c16-d5b2-3757-ad36-c228fcaea975 | -15.69272 | -59.44554 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15cf6cd6-fb61-3285-a066-3c8c3a74d89b | -15.69091 | -59.43241 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60ae25d9-6ef1-30d6-9cb6-272a933a8232 | -15.6903 | -59.4367 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9dd02fd-4bc4-3998-ac30-0fc46132567d | -15.68912 | -59.445 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2769169-93be-315c-9347-afa51cd13496 | -15.68679 | -59.40953 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39edf27b-9ae3-3b7e-a206-1cab4adb3942 | -15.68492 | -59.44872 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41b1bf67-84b9-3641-819d-24e178ef222b | -15.68378 | -59.40472 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d4bf8cd-e52a-3903-93ce-76cb0faa2d49 | -15.68317 | -59.40906 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8317df5e-0a5a-3242-a459-6efd65d4b3be | -15.68132 | -59.44816 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 306434a3-dc90-3551-b62b-1c5b074a6653 | -15.67956 | -59.40857 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 842f7c63-63b1-35d1-b2d4-21c898e3affe | -15.67894 | -59.41293 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f95c831-451d-38bd-808d-78897e13631b | -15.67833 | -59.41726 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cd747a2-d30e-3f3b-a822-9dbad1a856f1 | -15.67713 | -59.45178 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 364e41d8-cc4f-3b81-9753-f0692820b5c6 | -15.67474 | -59.41663 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e32114c3-d7c4-3c64-ad99-93ad7ab93c17 | -15.67413 | -59.42095 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8292a3df-010b-3803-b328-108c1203825d | -15.67352 | -59.42527 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a57f44e-5372-3606-8ce7-389a648712ba | -15.67295 | -59.45535 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7f71fa0-3bfd-3a14-9f5b-7a4ff3d8c1de | -15.66992 | -59.4247 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bdb8480-2db8-31e5-9f74-bbf6676ac483 | -15.66936 | -59.45475 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fffe9e9d-fe9c-3330-8f4a-f723b83fbc8d | -15.66636 | -59.44998 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0aa15afb-c986-3bca-8693-9edac9ae8def | -15.66577 | -59.45417 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ee1cc5b-86d0-3d24-b784-9ee2f725b689 | -15.66571 | -59.42851 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5021e361-09c2-3690-a43a-a8fdcd185032 | -15.66511 | -59.43277 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16d651ea-aa54-314f-af1e-6040f6eaa52d | -15.66451 | -59.43699 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2a2e10d-c869-314a-a000-4dd513abcb38 | -15.66276 | -59.44941 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 637b1f10-97bd-3a10-aff0-b5d262d89996 | -15.66033 | -59.44056 | 2024-10-08 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a8fc694-296c-38a9-bd66-740cc49f0eaf | -5.78687 | -57.73256 | 2024-10-08 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa24a3ae-96d3-3ebf-b776-9de025f64421 | -9.51748 | -59.50597 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61ee4ec8-9a3a-311f-b686-60f56d4d0944 | -9.51692 | -59.50965 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9b3cf46-32be-35f7-baa5-4ac273189d6e | -9.43684 | -59.04302 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ed2060-7b90-3492-96ba-5cce5199b880 | -9.43626 | -59.04683 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 666299f3-c53b-3d60-8bc1-e0c6a0bbe5e0 | -9.99286 | -59.53559 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2ea6f5b-112b-3117-9d8c-ebb74d32a414 | -9.99223 | -59.53661 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38086fb0-7f8a-3850-a17a-a9b2e11f4bc4 | -9.88491 | -59.15954 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afb09e09-8b3e-321e-9705-a7877e09a338 | -10.70807 | -58.58274 | 2024-10-08 05:23:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fd7f4db-51d9-3ef8-a1d0-ee5f393adbf2 | -10.23735 | -59.14503 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93501b33-e438-3b45-bfa3-9b82b2b8786c | -10.21934 | -59.40265 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34f17ee0-46f6-323c-b321-7f6e520304fb | -10.21878 | -59.40638 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd2c7d4f-233b-3cf8-be3a-f2662ab0e9e9 | -12.31356 | -59.18074 | 2024-10-08 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6b42cff-ff01-3a9c-aeb6-37aad08a2931 | -12.31005 | -59.18018 | 2024-10-08 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4e6dfa9-03d8-30a7-91c0-f09110eb5c8e | -12.29479 | -59.18602 | 2024-10-08 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee10da99-7017-39c0-ae86-24ccc097ba42 | -11.70917 | -59.14302 | 2024-10-08 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c88972c-1dcb-37b5-a3fc-92f827cad954 | -11.48809 | -59.09962 | 2024-10-08 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e2a05a52-66ea-3474-830b-37d18713857d | -11.48459 | -59.09909 | 2024-10-08 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe81b8f4-70d0-37c6-9b65-4f6da6bdae57 | -11.03687 | -58.97095 | 2024-10-08 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d76b47e7-c118-3143-95d5-cac4e9bbd60c | -11.48868 | -59.09565 | 2024-10-08 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d803bac-b1d6-38b9-93b6-1541cffb6f8e | -5.09626 | -60.23207 | 2024-10-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a33560-37d0-3e20-93a7-67164a74bb5c | -5.09572 | -60.23551 | 2024-10-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a5b40ea-18be-3e4d-a88f-f32a4dec63c6 | -5.09295 | -60.23155 | 2024-10-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dadfc837-e103-34a5-b1b4-d2e6ee2c4c4b | -5.09241 | -60.235 | 2024-10-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d6c87de-19d2-3790-b0c0-59b10a9d1958 | -7.19996 | -59.61343 | 2024-10-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README121.md)
