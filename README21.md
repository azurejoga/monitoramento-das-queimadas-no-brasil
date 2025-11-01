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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14d5a867-5dc4-3a9f-9879-402dffadb2ab | -3.58916 | -50.8132 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9057b6ab-b17a-383a-bf51-80156f9e840e | -7.87976 | -47.55738 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72e76dea-29bc-315e-a769-7af35fa7b88e | -2.89407 | -48.06178 | 2025-11-01 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a2b1075-a6d7-35cd-a183-c838e8eb1424 | -3.15815 | -50.82845 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f77d141b-4ba1-394d-a7b4-b872f3529750 | -7.07052 | -46.99806 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5266a097-89d9-3f2a-a435-d2e9aad05b9a | -4.29586 | -46.26173 | 2025-11-01 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 70a25252-b992-3743-b9bd-d87520135735 | -5.98208 | -43.61467 | 2025-11-01 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72b74faf-629c-38d0-af7c-ed3eea54f134 | -7.07077 | -47.3647 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| de89cad7-bf91-35bb-a35f-c1e2a102ee41 | -4.75115 | -50.68581 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b89756c-8861-3e60-b0be-6db796aa5800 | -3.47469 | -53.50107 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1525ba16-e37f-30aa-883e-1904a3ff1b8a | -3.86173 | -51.17103 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebd8523b-1a9c-3652-8120-9addc7861243 | -3.07854 | -51.25631 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50f814d9-137c-3002-b578-4712107c7fec | -8.86103 | -49.87785 | 2025-11-01 04:38:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bdf55a10-2cae-36a9-93ff-1abd0694ce82 | -3.72868 | -44.10229 | 2025-11-01 04:38:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ff7c5b1-1646-390a-b581-f9fc73c68464 | -3.52125 | -50.31067 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9ae9fd0-e2d8-37db-9aa1-9f81f28acc93 | -5.59491 | -50.06451 | 2025-11-01 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c04669e-4ab9-318b-8734-096d3160a3ac | -5.88082 | -48.15047 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd0ca117-5a00-3bda-839e-92ee9fbf7a3e | -3.54481 | -46.43015 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 807b16c0-12c8-3861-b27c-89013dc08c85 | -6.73356 | -45.95515 | 2025-11-01 04:38:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0cfed423-e7a7-34d6-845e-6823e9d66872 | -7.17341 | -47.26825 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d66be753-c2f8-3535-bfdc-fb4cfcfed273 | -3.39617 | -50.32499 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8e4bd14-b834-34da-8776-8a2cfb077839 | -4.65906 | -41.9643 | 2025-11-01 04:38:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bfa63bb1-f27a-3680-a7dc-583815c9a67b | -7.06733 | -47.36424 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7804405-4d4e-3bca-8e2f-0e8a1315a8a0 | -5.54261 | -48.38047 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8c84e10-b092-3195-8094-c6356911ec4a | -5.83638 | -44.06366 | 2025-11-01 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1aa8450e-0f83-3e1d-a563-701f86204244 | -3.48409 | -46.02338 | 2025-11-01 04:38:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5df7f2f8-9f36-34a1-90e0-80ed405a4167 | -7.08094 | -48.30748 | 2025-11-01 04:38:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a78640f9-8a1d-3e8b-b99c-26a620e72dc3 | -4.67258 | -45.8099 | 2025-11-01 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84617f9e-1b4c-3cd7-840e-76a7841cfe38 | -5.17099 | -50.07668 | 2025-11-01 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a92462e-68a7-3d91-8931-9b2e9bd8b9a5 | -3.80724 | -51.80313 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36a00a3e-6004-3cbe-9d75-4c391c85bd9b | -7.45077 | -46.71015 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebfb1827-2514-3afe-a367-10e744015e24 | -6.75132 | -48.68009 | 2025-11-01 04:38:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6c8bf1a-9b8f-3511-b6ba-f0b39a4bf53c | -3.15875 | -50.82466 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5eeef866-8452-3ef7-bd32-d6b167e0d4cf | -5.59789 | -49.07568 | 2025-11-01 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a468d6b6-b869-3f2b-b5e4-1440630d6b5b | -5.54983 | -45.41027 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8ba2f1d-0710-3a63-a55c-aecf0cd96bd2 | -6.57779 | -47.53757 | 2025-11-01 04:38:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d385619-646e-3dc4-b683-e16f7610e4cc | -3.47406 | -53.12684 | 2025-11-01 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1ed3aac-03d4-3786-a4aa-42c6717ee462 | -2.89001 | -40.49083 | 2025-11-01 04:38:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 60595728-d3bf-3527-bece-a8f4ccb95b54 | -5.34535 | -45.77823 | 2025-11-01 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20cb6695-8a54-3b65-b9cc-7d4497432186 | -5.74827 | -46.65965 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd8299a8-d69b-39da-8307-9b1c7d641e41 | -4.82701 | -45.78806 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d1f3fd1-17b3-38f1-b040-f4d65b7fb81f | -5.12516 | -43.3835 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d683649-c0a7-35eb-ad32-18d48859ab46 | -7.0702 | -47.36848 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b2117f34-7d3b-3542-9232-7b430976f245 | -4.21247 | -48.09487 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4870b122-ca4d-3aed-8e61-74e73b334c7c | -5.83234 | -44.06304 | 2025-11-01 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3ee8b27e-e8a8-323d-9ccb-c51e248f6272 | -2.8576 | -43.6733 | 2025-11-01 04:38:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92423e96-31f7-357a-80b2-e7da319dc6d1 | -4.55708 | -48.4819 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d591e39-bcdc-3867-a219-dc01fdad6c35 | -5.12459 | -43.38729 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f55d6ec-87ad-3ff1-b937-2b3cb88612d2 | -4.1766 | -47.64965 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09c62fc0-42a3-381c-8480-5f5552db0004 | -5.61883 | -46.80933 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36c9a07d-e837-3ce5-bad2-fd6131f91627 | -5.14554 | -49.87167 | 2025-11-01 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2512370-740f-3b37-a14c-89ead965d031 | -4.83061 | -45.78859 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce026adf-84ee-3210-95ad-2accea68902f | -3.81816 | -51.39602 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aad8f0d8-9089-3cc3-8a52-3e52061f2fac | -3.35607 | -52.8025 | 2025-11-01 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd8c1cfa-a3c2-3b6b-8395-132f0409ac42 | -5.51528 | -48.18367 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b189230d-f9f9-334f-b854-7c2171b32d1e | -5.2198 | -43.75227 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0abe2353-80a8-3f1d-be59-f259b5097954 | -6.04768 | -47.97412 | 2025-11-01 04:38:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0963b0a7-4849-302b-b47f-71e151bf111d | -3.60103 | -50.628 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8def2369-3de3-3899-a4f8-d336e657f747 | -1.26049 | -54.09106 | 2025-11-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f36866a0-d869-3882-9c66-af8cb4170c84 | -5.26178 | -45.60798 | 2025-11-01 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 56878c44-1002-3b5a-aee3-98b5ad1e477c | -7.26021 | -47.71137 | 2025-11-01 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7f13d2a-6571-386d-967f-f2271f7dfcfc | -8.93036 | -47.68143 | 2025-11-01 04:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 02a2602c-ac66-39b5-ab3b-ed60110891e0 | -3.65966 | -50.18864 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a33b2ef2-9cd4-33cc-951b-d8c03cedb1ca | -3.22582 | -50.58122 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4708c003-97ad-3365-a7d8-cdb305d7fcc3 | -4.17993 | -47.65018 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9c0a1622-a13f-3285-9501-b9bdb0f2b70c | -4.68039 | -45.80685 | 2025-11-01 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bea8f51-ec0f-36fb-8a17-04dd48db6d3a | -4.62619 | -45.42908 | 2025-11-01 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9e2746b-a47a-3628-aceb-8bc3d844fc5c | -5.70524 | -43.20778 | 2025-11-01 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fedb28e8-74d8-3664-b172-5a4d5a57c4dc | -4.42501 | -47.60115 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0f906d3-3e1d-3dc5-be26-925b640c04c7 | -5.13353 | -43.38469 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51c26da8-466a-3039-9564-577ad6db336a | -3.67688 | -51.75415 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6cea47a-fb95-3059-b5e9-41053ccf4b6a | -4.42555 | -47.59761 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afb01aa2-7de1-3735-bdcf-b925e40918b8 | -4.82936 | -45.7969 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a23b155-1c6e-3658-8e7f-cc0228944711 | -4.91982 | -45.59119 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b8294d94-865e-35cc-b822-bf3289e5f890 | -6.88696 | -42.84992 | 2025-11-01 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b7cf0ca3-6e3d-3b40-87bd-15da24253f2c | -4.91917 | -45.5954 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9b863c7c-0e26-3e02-b23b-e9809faf17d5 | -3.01626 | -53.96688 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 796aa66f-cebc-3b8a-a754-42633587d5c7 | -6.80276 | -47.04977 | 2025-11-01 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 061f3ed2-968f-3217-965c-350583752508 | -3.80267 | -51.15005 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f35d60e-975c-3073-a303-115a19bb3b10 | -5.59546 | -50.06102 | 2025-11-01 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5adaffb6-bc01-3925-ab70-7a4437439bae | -3.07791 | -51.26023 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 261b8698-0b10-3292-aee8-08f3296b9622 | -3.22866 | -50.58547 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| c6c2368b-eb4e-3ae5-a39b-f406b1e048b4 | -3.11264 | -45.23383 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 14486f2c-9ee3-3684-990c-e19e4155bafb | -6.57992 | -48.73188 | 2025-11-01 04:38:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 505a0495-55c8-3b7c-ba37-d349f3e9ea85 | -8.15252 | -45.4329 | 2025-11-01 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f65ef41f-46e7-33be-b5bf-f2025cc42f20 | -4.65952 | -47.23331 | 2025-11-01 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5efc1617-d334-34ee-bba8-5cfe3ab081b6 | -3.53001 | -53.00097 | 2025-11-01 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2891f9bb-6f5b-3362-9598-e9d35523f590 | -3.192 | -45.7998 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75bcce64-9a0f-339b-82f3-cfc7bcb8a40b | -5.83215 | -51.64085 | 2025-11-01 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae37bf63-7025-3674-b3aa-e77f2ecf1a05 | -4.57453 | -49.41464 | 2025-11-01 04:38:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f0e6465-1310-3f53-b86b-468b2d51c5c4 | -5.3667 | -45.20913 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdc7dad4-a3e9-3786-8286-d625ec1486ac | -3.76148 | -50.37428 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2ab3f2e-e384-3447-a17e-3e450bd25917 | -5.25936 | -48.47515 | 2025-11-01 04:38:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ced80c28-3890-3827-802b-d4016cc58707 | -4.21633 | -48.0919 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fa10ba3-7ee9-3292-a987-3f7c6fd3ee90 | -4.50593 | -47.29886 | 2025-11-01 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7664c85d-1aa4-3b3c-9643-3d65e2b0cc6d | -4.56961 | -45.40718 | 2025-11-01 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b16ae651-758f-37b0-8182-9a3342384f59 | -4.75368 | -44.46854 | 2025-11-01 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9822f5ef-d43c-3a07-bff6-de9e464f1494 | -3.88888 | -47.17899 | 2025-11-01 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7a7f6c57-63c4-374a-85fb-d14f3a2e1364 | -5.95533 | -45.57629 | 2025-11-01 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a2c8873-f2f5-39c5-b029-f405bdbefd36 | -6.94034 | -49.62769 | 2025-11-01 04:38:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README22.md)
