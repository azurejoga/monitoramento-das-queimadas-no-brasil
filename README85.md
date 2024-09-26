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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7d355f4-eb40-347f-b40c-5cb39c6c2fa1 | -22.21431 | -48.67638 | 2024-09-26 04:10:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| e829d8f1-9b88-3403-bbb4-5c9343690c9a | -22.2135 | -48.68094 | 2024-09-26 04:10:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1b1d6039-ec10-3852-9024-12e805e0c158 | -21.18631 | -49.64031 | 2024-09-26 04:10:00 | NOAA-20 | MENDONÇA | SÃO PAULO | Brasil | 3529500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 478980c8-6f03-371f-b615-ab53244533a0 | -20.92072 | -49.6777 | 2024-09-26 04:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 7f13a4e2-3976-34b7-8ed7-d340bed011ee | -20.91482 | -49.68758 | 2024-09-26 04:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| de5777b0-a0e0-34d8-a1d7-c6fa26b2e472 | -20.91192 | -49.68134 | 2024-09-26 04:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e6e7e84f-0738-31ed-be9b-ea72183bcb1b | -20.90991 | -49.69209 | 2024-09-26 04:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e5e7e62b-b60e-32a0-bd02-60e6884827b7 | -20.90802 | -49.68049 | 2024-09-26 04:10:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0f9d4f12-623b-3c8e-9690-6241a372bcde | -22.53988 | -48.8129 | 2024-09-26 04:10:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0319539d-1692-3d3c-a4f9-fd8a99a36538 | -23.16982 | -50.019 | 2024-09-26 04:10:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 573c2848-1073-3192-833b-8e4bd875383d | -23.16601 | -50.01801 | 2024-09-26 04:10:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 9c136b39-32e5-3ee2-a49a-583b39405ab1 | -23.1622 | -50.01705 | 2024-09-26 04:10:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e4782d6d-f355-388a-85f7-5b3945258182 | -23.16179 | -49.38654 | 2024-09-26 04:10:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 2052f34f-25cb-377e-849d-793c6fdd9958 | -23.15933 | -50.011 | 2024-09-26 04:10:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 56db51c0-2e53-3e15-afaf-150cffa33ef1 | -23.15838 | -50.0161 | 2024-09-26 04:10:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| af154538-39b3-31e5-992f-8505a1a3aed0 | -23.15 | -49.80699 | 2024-09-26 04:10:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 327b70e1-9274-3bce-ba90-2e957468884e | -23.14784 | -49.80415 | 2024-09-26 04:10:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fbd07f35-8994-325b-9407-e712f52daa1b | -23.14619 | -49.80626 | 2024-09-26 04:10:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d2f14810-8104-33e9-b205-de84ab470e16 | -24.02409 | -49.53145 | 2024-09-26 04:10:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f16ffd4-6f4c-38aa-ae4a-f1aa5c3e1172 | -24.7103 | -49.46451 | 2024-09-26 04:10:00 | NOAA-20 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f746bb09-ff19-3afa-895b-da7d7fa35b29 | -26.6162 | -50.6609 | 2024-09-26 04:10:00 | NOAA-20 | TIMBÓ GRANDE | SANTA CATARINA | Brasil | 4218251 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 54c3e9a4-80a3-39c0-bdcf-a2c4003821a6 | -20.33958 | -50.57857 | 2024-09-26 04:10:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b0301a01-0fec-335a-9ae5-efd69091a66a | -20.33881 | -50.58265 | 2024-09-26 04:10:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 7bdc5afd-5550-3271-ac9a-c83dce7bcb96 | -21.27575 | -51.00101 | 2024-09-26 04:10:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 67b758dd-bb0e-38c7-b07a-e3d01d65aa36 | -21.27572 | -50.99943 | 2024-09-26 04:10:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7aee580e-5676-3aa6-920b-55a78fddf70d | -21.27156 | -51.00003 | 2024-09-26 04:10:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4807582e-cf72-3eae-bad5-57c5b4dcfd6e | -21.27154 | -50.99844 | 2024-09-26 04:10:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ed4a7734-4a93-3ec6-8646-136f23772d45 | -21.27072 | -51.00261 | 2024-09-26 04:10:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9cdee6dd-9f24-341f-a245-3351ef11b8da | -23.62804 | -50.88521 | 2024-09-26 04:10:00 | NOAA-20 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| da40fb9f-17fb-34df-8da2-b492e2d9c7b9 | -23.62728 | -50.88914 | 2024-09-26 04:10:00 | NOAA-20 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0cbb46ef-79a4-3c7a-9718-62193781aade | -23.08811 | -51.20231 | 2024-09-26 04:10:00 | NOAA-20 | BELA VISTA DO PARAÍSO | PARANÁ | Brasil | 4102802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 42c62bb6-45a0-337d-91b3-a6eb356684f2 | -23.08732 | -51.20644 | 2024-09-26 04:10:00 | NOAA-20 | BELA VISTA DO PARAÍSO | PARANÁ | Brasil | 4102802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aab7c9bf-6d24-3c0d-bd54-7eed9308e7d1 | -19.78213 | -51.48375 | 2024-09-26 04:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec91a1e4-c1c9-308a-aabd-6eed8caad951 | -19.78118 | -51.48848 | 2024-09-26 04:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dd6dfc6b-60d7-3466-8b33-5ad3dc7fe452 | -19.77674 | -51.48747 | 2024-09-26 04:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d9b91c8-004c-3dde-ace9-48c0d5076c16 | -19.77205 | -51.47504 | 2024-09-26 04:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa99f030-512c-3a46-a2d6-8b0d2aa66c0e | -20.99474 | -51.79597 | 2024-09-26 04:10:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 61e7fd5e-fdfc-3f92-aebb-fe6e39517b39 | -20.61322 | -51.51573 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 469bb6fe-813d-3c72-8f62-d31852f044bf | -20.61231 | -51.52039 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7147f0a3-d112-3249-94ea-57e55fc05438 | -20.60973 | -51.51014 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 6b4009a8-0b2f-3bf0-8845-d0ce447a6ba8 | -20.60882 | -51.51482 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| 93f32612-636c-30a4-93c4-8a25d8448cab | -20.60791 | -51.51949 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| d19a0fe9-6c3c-3e21-8c63-93af6a89f5a1 | -20.60533 | -51.50924 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 57b4c15f-2390-3cfc-afc2-387d4dba52b6 | -20.60442 | -51.5139 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| 184f7b43-0f0d-39ea-b75e-7d791ef5fb72 | -20.60364 | -51.49451 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 24ba52bd-fc94-3ed3-abf3-6812a3021c37 | -20.60274 | -51.4991 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b8f2207c-16a8-378a-84f7-116c670e83c6 | -20.60184 | -51.5037 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6f21e7b9-2f2d-35c1-a829-17d903893f0e | -20.60093 | -51.50834 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fd3834e4-4e2c-3e54-87d9-b15aa0d953c8 | -20.60003 | -51.51297 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| f3aff265-551e-3adb-aba6-b8f7451291a0 | -20.59927 | -51.49347 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 55c3f513-94d5-3536-8b3f-c002451f27c5 | -20.59836 | -51.49811 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0fed3680-76fd-3cc5-a951-302e7d65327e | -20.59745 | -51.50277 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1355c1e7-8421-322a-8196-059387c95f1c | -20.5949 | -51.49243 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c631aaa0-70de-35a2-aee3-d9f6eac6040c | -20.59322 | -51.4777 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b0ac69dd-ed7f-3d5e-9706-7967aa806228 | -20.59248 | -51.45821 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 240b4765-9390-31cd-a1e6-a2b984d81031 | -20.59158 | -51.46279 | 2024-09-26 04:10:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9a0f097f-ac60-3cf3-9c9d-81d43af1b975 | -20.0785 | -55.53965 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 21f7f961-8259-3813-a19c-812331636707 | -20.07495 | -55.52857 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8a00daef-af14-3b4b-a65c-c228d801b9fe | -20.07192 | -55.5423 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c3527d0-b051-3ff6-84d6-46c7b62fcde7 | -20.06931 | -55.52703 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| afa05e6b-da42-3215-b608-0186321ec381 | -20.01288 | -55.48512 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b704f4a4-6066-3e83-ab74-9d264ec8dbae | -20.0119 | -55.4829 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a23a6ffd-37b6-3302-8346-544e028002e2 | -20.00731 | -55.48334 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85e97f14-1f93-3a32-a64e-68e8bc46ee17 | -20.00639 | -55.4874 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b02fc245-4f67-377d-8525-2d0b70dde30f | -20.00547 | -55.49147 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 312d4195-746c-338d-ac5a-ca6550c548e8 | -20.00542 | -55.48524 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4dcb524e-eba1-3f20-97af-23ba3b873f2d | -20.00454 | -55.49556 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f504e62-1d07-32aa-93d9-d39e24dadc28 | -20.00453 | -55.48929 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41a61178-0092-3d6c-aabd-eb38cee135d9 | -20.00363 | -55.49342 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48462a1b-dd91-3f9a-8e0d-59297ddc2234 | -20.00274 | -55.49747 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 575e39b8-dabb-3bf1-92fb-5708042125e4 | -19.99991 | -55.48958 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ef3302e-4ec4-3e55-86ea-72ea97fcd921 | -19.999 | -55.49361 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8585b3b2-bb89-3af6-afa4-cca26a3250bc | -19.99808 | -55.49144 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40df8b7b-e57e-398f-bd87-1e5f53b65d8f | -19.99162 | -55.49366 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54f49291-5539-3660-8439-43473cf4e69f | -19.99066 | -55.49803 | 2024-09-26 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54d41b61-0b5f-3607-933d-fe94ec5a2817 | -21.39301 | -54.66422 | 2024-09-26 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 367b183d-335b-3a17-9adf-12c29e09ea13 | -21.39227 | -54.66772 | 2024-09-26 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 406eea69-ca81-35da-94fc-a96f12ea5f68 | -21.34438 | -54.65897 | 2024-09-26 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 616dd9b8-2c05-3a0b-88e1-d027eb037017 | -20.78635 | -41.96115 | 2024-09-26 04:10:00 | NOAA-20 | FARIA LEMOS | MINAS GERAIS | Brasil | 3125309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8eda937a-3371-31aa-a6d3-e12c1f320906 | -20.78161 | -41.48434 | 2024-09-26 04:10:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 350d2453-c333-34ec-819d-2044143dbdeb | -20.63489 | -41.9098 | 2024-09-26 04:10:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4f00633-8d4f-3edf-835e-79790b6174e5 | -20.63373 | -41.91816 | 2024-09-26 04:10:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5fa3f6a3-1f6a-3a89-b86b-eed2c14dd53f | -21.93462 | -41.55415 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb98fa01-a66b-3dbe-b101-858b6b392ac2 | -21.93401 | -41.55867 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fc16b110-7cec-3098-8165-ed867f612c25 | -21.93099 | -41.55359 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3c3b47b1-0e2f-3add-9224-536bebd86e8f | -20.99962 | -41.28391 | 2024-09-26 04:10:00 | NOAA-20 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed12a473-dfb1-3933-adb4-12e0fa3635e6 | -20.99899 | -41.28849 | 2024-09-26 04:10:00 | NOAA-20 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 05d5bc9e-64ce-3085-82ea-9fd124cab4ba | -22.8851 | -42.4421 | 2024-09-26 04:10:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1cc8ccfa-f93d-3a15-8e45-be9b8623ac57 | -22.49549 | -42.0556 | 2024-09-26 04:10:00 | NOAA-20 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 321886b3-bbef-35fa-9fcd-041215ed05b2 | -22.49192 | -42.05504 | 2024-09-26 04:10:00 | NOAA-20 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3e021cd-9ec5-3429-aa0c-1dc1150529ed | -19.14463 | -57.4759 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ab48a172-e900-3598-8d96-3aaa4f874ba4 | -19.14363 | -57.48024 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ea0dbfde-c4ad-359d-b1af-e4ec4cc0afad | -19.14348 | -57.47772 | 2024-09-26 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 6f95f0d7-70de-3ca9-b582-110977a57d9c | -2.6785 | -57.531 | 2024-09-26 04:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b9270d91-16ae-3433-985e-9f36fb555c48 | -2.6968 | -57.5307 | 2024-09-26 04:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a6795473-791a-3ebe-8204-97628287cbf3 | -6.8024 | -59.3044 | 2024-09-26 04:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e2e917f2-7b04-399b-b1bc-1585884fa016 | -6.9306 | -63.1053 | 2024-09-26 04:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 28ac16fa-bdb5-3aeb-80fc-af08a834e4cb | -6.9305 | -63.1241 | 2024-09-26 04:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 5ae2f968-4813-3175-8a5d-3e7feb53baea | -7.3824 | -55.4924 | 2024-09-26 04:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 365c9bfa-1405-30d0-8b0f-9c85fee5ff00 | -7.3823 | -55.5124 | 2024-09-26 04:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 182.4 |


[Clique aqui para ver as próximas entradas](README86.md)
