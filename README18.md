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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c4982e2-c3e2-340b-a65d-15a9af7a82f9 | -12.82024 | -45.43495 | 2025-08-02 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69a42c3a-a557-372d-8bb8-8e39eff8fc93 | -13.65681 | -47.31215 | 2025-08-02 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c088e3ed-c9eb-341f-a569-9a532ffa9e7c | -11.91086 | -55.486 | 2025-08-02 04:49:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc916ea1-91b4-37d1-bc12-48d9d6552882 | -12.67766 | -44.48152 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc88e701-2709-36e3-92c1-06dd9c650264 | -15.10156 | -55.229 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03a2ff27-3c7d-3e9c-a272-5b54ee61d8ec | -18.23886 | -45.17394 | 2025-08-02 04:49:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70fde12-7b36-3367-abc8-1128fb0f75ea | -13.89868 | -42.13153 | 2025-08-02 04:49:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 059f09de-825d-3a25-897c-ccbe4967afb1 | -15.11132 | -55.21096 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dff7d109-15c2-3089-8385-ed21dd7d81b5 | -13.99887 | -53.94489 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11c74728-b704-3f06-bcad-e80c1132c597 | -12.65658 | -44.53043 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a61b6f77-838b-3973-a5c6-7c3758489014 | -15.12026 | -55.22062 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5fd618a-9db0-3002-8f92-7977d0d3bf4f | -13.9945 | -53.92937 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad042bdb-bc89-3e2f-bdf2-a94be5b70e2d | -12.66497 | -44.5029 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 46e3d77d-6bff-355e-87ce-436f5f033e28 | -12.66142 | -44.49089 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5ce30e6c-d666-3a34-9109-5c42abe3e3ec | -15.40722 | -55.77951 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79e16c65-d680-3f5b-95e0-841d07d98fba | -16.24785 | -48.95775 | 2025-08-02 04:49:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| aba0b537-2b59-3f24-9e41-03dd10d72c33 | -13.52903 | -51.90527 | 2025-08-02 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01ceac59-7374-355d-8496-00c8957d5c58 | -14.91039 | -51.05842 | 2025-08-02 04:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab9ca63f-c038-3c72-9eba-a9e87734e98f | -12.65371 | -44.51289 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6a71e5b2-e561-320b-8d2d-f9429cd53832 | -13.05715 | -47.44748 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2eb51c0-4faa-3998-a4db-95cfd1df6a58 | -12.67378 | -48.08839 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ca758ce-5545-32cf-982a-d112362d8c6c | -12.67629 | -44.53323 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 91b4cbc5-118f-35de-8114-54a1d2dc3726 | -13.21927 | -42.2533 | 2025-08-02 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| faf2eda5-8a31-3fdf-9100-c3d544ba69fd | -13.9816 | -53.94578 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e315673c-edbc-3fe2-97f7-2df4c4e5876c | -12.65934 | -44.50791 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 905441e5-9b05-3a72-ac72-717a71447cc6 | -14.79555 | -42.72086 | 2025-08-02 04:49:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 664ea503-c585-3e4e-b933-664cc136a797 | -12.44644 | -47.0507 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 883bdefd-2ad7-3c5c-b84d-c275c9bef54b | -12.66003 | -44.50224 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0ef92d55-dd8e-3085-886f-21b90b5398b8 | -16.77428 | -49.33698 | 2025-08-02 04:49:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c479d93-d6bd-3635-a598-d4adafa7f4be | -12.65647 | -44.49022 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7921bf45-f285-3e1b-a051-b9d59da560ff | -12.67131 | -44.49224 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7d7f1892-6e30-3b1b-832d-227534f946ad | -13.05406 | -47.43953 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33bcd97f-af43-3d5b-b491-537f1f754e6d | -12.71114 | -47.7907 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 359e4311-12ca-3698-bbfd-1290effa391b | -13.17424 | -42.23264 | 2025-08-02 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| d9e63bfb-8805-351a-9f1a-88646b677d09 | -12.45058 | -47.0513 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdc0d934-9608-37ae-a228-807537fb835c | -14.02522 | -53.50074 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 062d2be6-e60a-3b41-b99b-adbd827633d3 | -12.67626 | -44.49289 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0f1eaf40-2da8-3976-8c93-9c23f43f355d | -16.58882 | -48.34133 | 2025-08-02 04:49:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a28fa0ae-ca9e-3dc0-90e2-3d15b111dee1 | -14.27783 | -48.85289 | 2025-08-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e1b7228-b6b4-3492-907a-1e3dcca97788 | -13.89985 | -42.13247 | 2025-08-02 04:49:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c6baca2-a7bf-374d-b6e6-655fc862f2c3 | -18.21299 | -44.71296 | 2025-08-02 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dabd392-f876-32e9-9cba-f428824ef200 | -12.4646 | -47.07272 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb317acf-e523-35ac-a72f-3f20a11723c4 | -12.46195 | -47.02956 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05b0c412-77de-3199-bf2e-fe99f3affb3d | -16.70128 | -49.3932 | 2025-08-02 04:49:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1127f951-b1c4-37b5-815e-018bb384047d | -12.54555 | -44.72232 | 2025-08-02 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 500ef0b3-7cad-308c-b455-e40eda209e9e | -12.44229 | -47.0501 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a4fb23d-2520-33e6-a156-482bd13ade18 | -12.65435 | -44.49413 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2e5a0499-8af9-376d-a4ec-93d3efd90c84 | -12.4618 | -57.87527 | 2025-08-02 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625e8311-0797-35a4-bd24-dc2a977787b6 | -12.4708 | -47.05808 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a68daedf-185a-3591-b94f-2971f946bd48 | -11.63904 | -51.68968 | 2025-08-02 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 312d57e5-50dd-33f0-8107-73ec840de410 | -13.23241 | -47.22858 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd1639a0-9882-320d-a5bc-176dc1c36501 | -16.70062 | -49.39809 | 2025-08-02 04:49:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f410fb36-b8c2-37a3-9eaa-04ac6077316e | -12.47029 | -47.06189 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28842a46-2420-37ff-814d-ccd5b2d584f4 | -12.67559 | -44.53888 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3e6f956f-fe7b-39fb-bddf-d31d7c243df9 | -12.67486 | -44.50424 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f9188ca2-d514-3a8f-8d34-09ca45e16a43 | -13.06123 | -47.44803 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9fc76bba-c0c4-3c26-a375-4bdf6220cf99 | -17.4938 | -47.99623 | 2025-08-02 04:49:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e6ddb2e-1e5e-31d6-bfc9-192b96c814f8 | -13.22634 | -47.2422 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b7966a7-239f-37c2-91af-82d3d7b65a3a | -15.56896 | -58.70869 | 2025-08-02 04:49:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3fb0bff-d042-3ef8-937d-695f6c01d656 | -16.69096 | -41.01492 | 2025-08-02 04:49:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| af63c3eb-3ba9-35b6-a2df-7f40c45f106e | -12.67312 | -48.09308 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 41fd7eb9-03b7-3326-bb85-bb1c426a907f | -12.44694 | -47.0469 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 915f8fdc-dd69-3f07-a595-1888f1a05bd1 | -12.67067 | -44.53817 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 22184a70-0384-365a-93ba-70eb9f4e1902 | -12.44593 | -47.0545 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b2a7962-3589-314d-b135-9e6981895750 | -18.21376 | -44.70568 | 2025-08-02 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3f5f0f4-2bd6-3090-bad2-1137d5ff4d85 | -15.06289 | -43.87228 | 2025-08-02 04:49:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff6135c8-fb7a-3dae-8c0f-9f453048be3f | -12.67346 | -44.51559 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5ec75f11-745b-3b90-a406-7e3572ba28a3 | -14.87602 | -57.51741 | 2025-08-02 04:49:00 | NOAA-21 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d48d1e9-91a7-337b-b137-ba5379f4c456 | -14.02466 | -53.50431 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d4ac2d0-acec-3dec-8531-f2492d4bef6c | -12.66072 | -44.49657 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 64e6961f-2c77-30a0-9c23-1135269c89f4 | -11.91067 | -54.78366 | 2025-08-02 04:49:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9a06328-8305-32e5-853e-968016fdfce8 | -15.12415 | -55.19739 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 481badaa-3c1e-349c-b9f2-dbde5c56e0ef | -13.23143 | -47.23577 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7031a199-b0c3-30a2-b169-522642c8e0d7 | -12.65509 | -44.48845 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b038c617-f2ca-3318-81c2-a2d8623aeed9 | -12.45262 | -47.03601 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ba9d37f-fd15-3a9e-9f77-e709389c72a1 | -13.99174 | -53.92521 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4ac67033-1f8b-32a9-9a67-969d22f21111 | -18.21262 | -44.71652 | 2025-08-02 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09c93cc0-bf44-3cd8-9c53-eac166a76b61 | -13.23096 | -47.23926 | 2025-08-02 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4402068c-5008-3c5b-894a-cd372a87bf1d | -12.67206 | -44.52689 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a350d598-5da3-37af-bf09-e08a967728dd | -15.11409 | -55.21546 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c054f7b9-bd30-38d6-89cc-8f103e718a83 | -13.69462 | -51.95367 | 2025-08-02 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e7cffd7-5321-308c-83cc-ac209310d991 | -12.65929 | -44.49479 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 746fb4a9-1661-30c9-8337-c1734e16b906 | -13.98218 | -53.94216 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6a565cb-e502-3984-958f-4ff9f5c90c1b | -12.66082 | -44.53676 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1e89753-31af-3643-a303-9b24359b4af3 | -13.99116 | -53.92881 | 2025-08-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e65d89b-dbf9-3d0e-9056-6d2a34f4b98d | -12.44178 | -47.05391 | 2025-08-02 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f687312c-90c9-3850-aeda-4cb0fb3a15b9 | -13.21913 | -42.25036 | 2025-08-02 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 0214dadb-d72c-34b8-94f7-655467beae58 | -12.65578 | -44.49591 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3fb1bff7-6efd-39cf-a996-109b1103ef90 | -12.66922 | -44.50924 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d81cf237-6773-31dc-8722-d6a7d5d66041 | -12.66852 | -44.51491 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 38686a50-b6d2-3017-aac4-d28798d12a24 | -13.04949 | -47.44266 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a980c00-69fe-3239-8153-b7356673be8a | -13.06173 | -47.44433 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cfd08b1e-ee29-333b-bfc1-0f69de8c18fc | -12.53584 | -44.72091 | 2025-08-02 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9795bee-f296-3f40-af0f-b727ae99cdb0 | -12.71042 | -47.79587 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfaa3c32-d1e0-366a-a920-c81d7c574520 | -15.70708 | -56.39084 | 2025-08-02 04:49:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 094f26f9-dab9-3ada-9eb4-dfcfafe30870 | -12.66003 | -44.48912 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fff8d7a2-2adb-3398-8c45-9cc7ebc3c93a | -12.66859 | -48.09708 | 2025-08-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d8d6fa1-7a90-308b-bbd4-dfcb53dc8791 | -15.11086 | -55.23475 | 2025-08-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e3b7d84-8e7b-33a3-a0fd-754b4082c6dd | -12.66358 | -44.51423 | 2025-08-02 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ea78ec13-95d0-399d-90da-5b4fd172c9cc | -13.03919 | -49.17117 | 2025-08-02 04:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README19.md)
