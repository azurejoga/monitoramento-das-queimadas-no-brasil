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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b91187c-7d76-362e-ab7b-6f31390ffa60 | -2.96709 | -51.11224 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d7bcc3c-8a68-39b9-b096-8453de93665c | -2.89815 | -50.707 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b2e3b16-8c1a-361c-a27a-0e6eeb27f345 | -2.89742 | -50.71173 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6daec0d1-7667-3352-8005-812f315f1eb1 | -2.89669 | -50.71646 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b215e5f5-851d-33a4-8740-85a1480d7d9b | -2.89286 | -50.71588 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00bee6ce-e1ca-3a86-8ab8-9555d2e9d666 | -2.87895 | -51.67694 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95c130c1-f25b-3ba1-a2f2-635e830fe861 | -2.86149 | -51.01917 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8291d29-1d1d-3d93-8b8c-1b478276cc04 | -2.86077 | -51.02379 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ed46bdc-ad52-3b68-acb3-edc20c71aba6 | -2.85773 | -51.01859 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85439fcb-d5e7-3245-9e9b-9a4af8fcffb8 | -2.32216 | -50.52047 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b74f4dc-208c-35ed-9e44-5ed8514010b4 | -2.31963 | -50.52314 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 655ec58c-d619-3694-a3ef-6b7a00971646 | -2.58334 | -51.92167 | 2024-10-09 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15dc1aae-8dfe-3f8f-8daa-b7f536b6f80d | -2.58271 | -51.92571 | 2024-10-09 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1871f08b-332d-3cd1-b757-d835d22c0583 | -2.22703 | -51.81187 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 871a194d-0e89-342e-b25e-78a6521eae41 | -4.62838 | -50.98544 | 2024-10-09 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed6def22-77e7-3b71-9827-dedd24d32051 | -4.50145 | -50.8751 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bb88e46-1db8-3292-bb2a-969baa7bfe18 | -4.15798 | -51.04686 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c606aad-0f67-3847-8da9-1983430df22a | -4.15726 | -51.05159 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2a09c4a-6841-3af3-b8f7-5923abd3aacb | -4.15413 | -51.04644 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe2e85e2-5267-3937-812c-2eb4d6087f3f | -4.15342 | -51.05112 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2242e7c5-b291-3893-860a-156de5026b60 | -4.15032 | -51.04583 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b56653cc-4ac9-30d3-84e6-db547cfe133e | -4.0892 | -51.03647 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c39520fb-b1ef-34da-8754-982b09cb8cfd | -4.06238 | -51.11632 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d77d14a1-1a87-3e60-b99e-9541070b2f2a | -4.06163 | -51.12112 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3918d6da-4434-36b2-a97b-7656a5bd4899 | -4.0614 | -51.11861 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01501434-772a-3abd-823b-555acf41842c | -4.05782 | -51.12061 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b5c2aa5-2bfc-377f-a45d-7d11faa14ff2 | -4.05759 | -51.11808 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f007c59-b816-39bb-893f-9f44a156904c | -4.05021 | -51.11953 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7672b59b-4837-3443-9ef6-42f7c5f941f9 | -4.04714 | -51.11428 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cf6c955-7696-3861-a47b-54e27cca364c | -3.91044 | -51.01874 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f337dfc2-e5a6-3f4f-ac73-11ddb5cd22fd | -3.87313 | -51.18829 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 897800d0-212a-311b-8620-ab40b847aa1f | -3.86935 | -51.18772 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e94f53ee-1858-3333-b70f-1abfc6cbec66 | -3.79671 | -52.21332 | 2024-10-09 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dda94df4-e736-31f2-9ad4-e82aef5c70b1 | -3.78641 | -52.25728 | 2024-10-09 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8926264b-bba1-3075-befd-b66887dbbace | -3.7858 | -52.26133 | 2024-10-09 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 306c4e38-dcc6-3525-9d15-46fbf30e5c16 | -3.78466 | -51.98997 | 2024-10-09 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0bc8af7-cd8b-3e2a-abc9-441a3c25837f | -6.40983 | -51.70764 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e563698-0172-32ca-8187-728e03b65aa1 | -6.40847 | -51.71681 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 500883b0-7362-3eb8-b8fb-ebba72a101ff | -6.40606 | -51.70697 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54b18897-db7c-3079-a9b8-e3ae62713819 | -6.40536 | -51.7117 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3823904c-c8c1-39be-a1e7-de868bc1262b | -6.40469 | -51.71624 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c2afb37-3510-3b7e-afda-1cf4c441d9ff | -6.24705 | -51.73486 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2abcfb7d-cf78-378c-b564-1d0b7a6fb1fa | -6.21016 | -51.51587 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d135763-e628-3fd5-b72a-0298c3f345df | -5.83205 | -51.64211 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b5edab8-7efa-3d2e-8b0f-d6ea870184bf | -5.83195 | -51.63999 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32548d9f-de3b-3c70-927d-48e7a2dbc93c | -5.83124 | -51.6446 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a5bcc0a-4eda-3ffd-8bf8-96f66378203d | -5.63874 | -51.58964 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 118c246d-2141-37e5-9123-d178539f46f0 | -5.60246 | -51.69776 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd352caf-0f41-3307-ac75-dd7984ac9932 | -5.60071 | -51.69107 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9509c45-a106-34dd-b71f-b4d11b5702d4 | -5.60004 | -51.69561 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9032f3db-20fb-3be3-82ac-4e62a21c49f9 | -5.5994 | -51.6927 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6674f754-ff91-3826-b267-bbb6e4bf61ec | -6.08261 | -52.46964 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18976b41-5f64-354d-930a-253199157001 | -6.079 | -52.4691 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06039214-f0df-3d39-a5f3-23f226087035 | -5.90739 | -52.53476 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3e8ec0d-735b-3d73-b5db-add97e63582a | -5.90676 | -52.53887 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcea01bd-4235-3537-ae79-61b3c6f1e1eb | -5.90515 | -52.53769 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9c4bb82-ae39-3027-944e-7dca45f282aa | -6.89782 | -52.19415 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ea14049b-b666-3188-b53c-43204f540e57 | -6.51149 | -52.55006 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf243b1e-b1f8-38bd-8c8e-e421a1f9341b | -6.78454 | -51.66071 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee20637-7ef4-3382-bd74-c0dae2c67afe | -2.20173 | -51.95784 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54e36b6e-8a64-3798-82ce-552dd0d956bf | -2.20131 | -51.9567 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcb54dce-4480-31a1-a487-7f54a7fa6b6e | -2.19818 | -51.95729 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fbf6051-d099-390a-8c9b-cab765805807 | -2.19776 | -51.95615 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c090a617-66c2-36de-bac8-7bf4988ff314 | -2.10532 | -52.27354 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fddb214-59f2-3db8-975a-e9c890999170 | -2.10183 | -52.27301 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efa96e20-a2d2-3072-8151-5273592cd5e6 | -2.07832 | -52.0287 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d66762d-872f-3822-96cc-1814fc83cbe2 | -2.07799 | -52.02997 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d7d66ef-23f0-3c0a-9c3c-f40998853c18 | -2.07508 | -52.02547 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e1d92aa-f31d-3017-84c9-25f03fec337f | -2.07446 | -52.02943 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e104d11-64c4-3090-af63-fbe5f0ce9d8c | -2.07155 | -52.02493 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08b31d16-0de4-37f4-866f-5458269ac37c | -1.66636 | -52.14188 | 2024-10-09 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93426e42-5f12-3edc-a2ce-cba359418792 | -1.2253 | -53.05934 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3dcb928-8bf6-32fb-ac13-b55414a0ba9c | -0.94383 | -52.41666 | 2024-10-09 05:01:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e445c85e-9a6b-39da-8651-e36a7765717a | -3.64649 | -52.30011 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a60185ca-8618-3cd9-87f1-05de02bd0e9c | -3.53971 | -53.0079 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c387fa38-f252-352f-adb5-ffaae992cf09 | -3.41209 | -52.8342 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae47c3b0-211c-3f09-9749-213815ce03ea | -3.37479 | -53.30038 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1bc06b0-4d5a-3f19-ae65-3c38b9384207 | -3.37139 | -53.29985 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68cdd62d-8ea0-3b19-b66b-2f480dbf2c3b | -3.33235 | -53.3944 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 767dfb90-d593-30dc-a895-bb2720b0ce76 | -3.32896 | -53.39387 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38ee258e-dd6f-3b28-9082-4f1203ea3110 | -3.32827 | -53.2184 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb3bad56-8f7a-353b-a890-bc41b9734ccb | -3.32614 | -53.38971 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 427588f5-769c-37ec-b442-92fa011817c1 | -3.32558 | -53.39333 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c53d6fd3-5c73-321c-90ff-0a68993ec9cc | -3.22053 | -53.00914 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0cbc693-d680-308c-a448-40e05df7166c | -3.21709 | -53.00863 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a46cb9b4-32e2-3e53-94d6-460067458a58 | -3.0481 | -53.03659 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd60fb5d-9084-3916-bc58-256a4a4f41f7 | -3.04753 | -53.0403 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e7f404a-8755-3ce3-acb2-a35f2ddfe9d8 | -3.04411 | -53.03979 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 694ba4ff-26a5-3684-acd0-358ab3c2825d | -3.04353 | -53.04349 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76915c70-0acc-3816-949e-3dd68d343b64 | -3.04296 | -53.04717 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6693a4f7-dba2-3c87-8c66-e62f84e713e7 | -3.04011 | -53.04296 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f255ded-63a5-33c0-abe6-6f8ca46a0fad | -3.03954 | -53.04666 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 004d662b-94eb-3528-84ae-9489a38c2295 | -3.03727 | -53.03873 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8048d46c-904f-3f34-bcd3-993d94dad9b8 | -3.03669 | -53.04243 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f38cc573-881e-3a24-815d-7d66d191e969 | -3.03506 | -52.53268 | 2024-10-09 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9d5f9cc-445d-31d2-a49b-0da52f3572e7 | -3.03446 | -52.53654 | 2024-10-09 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a638fa22-f77c-3163-9d92-db2e0f43401a | -3.03328 | -53.0419 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0ad8663-8af0-325e-9612-36e5269cbdd7 | -3.03271 | -53.0456 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 977e2d8a-dd82-32aa-a992-9ac7bd08518f | -3.03156 | -52.53221 | 2024-10-09 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d705acf-a1ab-3441-9b87-6f8ace1a64d8 | -2.88972 | -52.40012 | 2024-10-09 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README165.md)
