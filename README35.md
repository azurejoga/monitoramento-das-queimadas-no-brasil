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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6179a626-925d-35d3-8246-691e0db66733 | -7.65781 | -42.57893 | 2025-10-11 05:01:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4cb167f1-bf6a-3e61-b745-5350bd8b3f43 | -10.53102 | -47.3355 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 769e6dcd-d79c-35d0-b9bb-b987ca0e0bfe | -9.81409 | -45.52002 | 2025-10-11 05:01:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d03034e4-5ffc-37c7-b092-15f06d7d8a5f | -13.4592 | -47.70743 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 730a8d42-7f72-32d1-b063-47b279b2418a | -7.52661 | -44.29526 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 414fb5e5-9a19-37d8-9036-38c6d798263c | -13.45689 | -48.09233 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 923f69af-50fb-3876-9b78-dc8f0b32586b | -9.16717 | -68.17565 | 2025-10-11 05:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48ec065a-3ff8-3d3d-b2ff-bb06e575ae56 | -12.90074 | -47.05643 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ab9d319-c479-396e-a8de-3c57b6533735 | -7.06825 | -45.21777 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc55aa2e-65df-3f84-aaf9-70f49dfe517b | -13.36289 | -47.62655 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 333f87fa-61a2-3b34-a889-20328ea7bb8c | -11.76831 | -45.0428 | 2025-10-11 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8ef8b61-50db-3d81-b642-0d9d7f614f1e | -13.00687 | -48.80793 | 2025-10-11 05:01:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eab41f1c-3bb8-3e43-a490-ea05bb86bee7 | -8.35882 | -48.67565 | 2025-10-11 05:01:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c72905c-ed1b-3820-a715-513b664989ca | -11.75476 | -46.35163 | 2025-10-11 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c71eb43-4556-360d-8287-8715698e519c | -7.50436 | -45.13892 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec0bb313-d7c9-3db0-99fb-5202031a0146 | -12.14767 | -48.01598 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2da25984-b861-318d-b32c-f47d51df014f | -13.30781 | -48.49721 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 110e4937-6968-3004-b66f-77df3455678f | -11.76944 | -45.04065 | 2025-10-11 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 303b72e0-8b48-3f44-ba48-6954175832a5 | -8.18864 | -43.32393 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0f9f32a7-f981-300f-87a3-a9bdffa40e67 | -8.04585 | -44.12085 | 2025-10-11 05:01:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5962dd2-9a91-36ec-af3e-71e7c815a8c0 | -13.48462 | -48.10682 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17e74c57-8457-3d48-ae2b-b09fd47ea26e | -7.74394 | -44.69542 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cce2eaa-13e9-34fa-9006-02578be78d91 | -13.30418 | -47.98423 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5c6e8ab-f10b-3b1a-a878-04904a43968a | -9.54419 | -66.46973 | 2025-10-11 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39687e59-d2c7-3b95-9ac5-e7cdbd7efbd0 | -12.99236 | -45.23006 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a1f1dcb-134e-32f3-9b12-f187c49ae15c | -12.899 | -47.05626 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 362af703-495d-37c2-9880-11e4e7210ca8 | -10.53319 | -47.33698 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20e053c7-37b8-328e-90a3-107347a6d25c | -12.17952 | -48.8098 | 2025-10-11 05:01:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9b7a6b4-66f5-3ef4-8ede-bd315e26d48c | -10.87515 | -44.18942 | 2025-10-11 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98eb5247-1ee2-3285-bee7-266f2bfcfe7b | -13.40962 | -47.26783 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6a54be7-f3c4-3d3e-8b78-f7667671aab4 | -10.38742 | -57.64459 | 2025-10-11 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1433e2cc-58ff-3351-bc65-15b1af06e17d | -13.20845 | -42.34919 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 6f49150a-9692-371d-962a-6513b7977812 | -11.53237 | -49.28112 | 2025-10-11 05:01:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4a61a79c-7e18-3876-a0cd-db22374e4db9 | -12.90197 | -47.03315 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bdbd102-6c89-31e2-964c-1f90ec259531 | -8.19653 | -43.32424 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 074e4f3f-1f34-3335-a367-7caf04ad4c7a | -8.15938 | -43.31965 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 519ac98f-88fc-342c-806c-c2970dae4d4a | -13.22307 | -42.34414 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 33.1 |
| a51a2c38-8315-301c-9eb3-dd9099fba828 | -7.35114 | -43.85651 | 2025-10-11 05:01:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04ece57e-1a13-33f7-a990-413ab3696af0 | -7.8597 | -44.49347 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53ea9999-4fc5-3e4c-8da5-27d18a76127f | -10.51075 | -47.35633 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 94b73642-2edf-3cf5-bea4-67f89d2265c7 | -7.38728 | -45.16862 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9b7be30-5d18-3b3d-8772-404c0b3bf1d8 | -12.90492 | -47.05102 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 953924ce-9ab8-3b02-ad16-a1608ec948e5 | -13.32306 | -47.12256 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5046973-6188-3f16-847c-9f3f7d517df1 | -10.51333 | -47.35547 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b5fec1ab-44e9-3b36-8122-772906fbda40 | -11.62414 | -48.79158 | 2025-10-11 05:01:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82991ccc-afd1-34a7-b431-a6e45f6678fb | -11.76337 | -43.31565 | 2025-10-11 05:01:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b38dd8bc-7ab4-3939-87b4-06556ab9d34d | -7.85613 | -44.47667 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80a6b1a8-1594-323b-b938-0174649a7fef | -7.67467 | -43.99652 | 2025-10-11 05:01:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44f506a4-a3a9-3f95-8db0-d2231186fbe7 | -9.24963 | -56.304 | 2025-10-11 05:01:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baa546fa-005e-39de-bc4c-d8d42e341489 | -13.21798 | -42.33477 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 3c26d2d2-98f8-32f1-b655-8ed62e7586f3 | -7.39991 | -45.91948 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14456ecf-6e31-3750-a25e-b16aea772fc3 | -12.24283 | -51.13975 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5295b5f-c725-3859-892a-d35d051ab766 | -8.16449 | -43.31593 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 25b75245-4ddf-3eb2-844b-f0769a08b0dd | -7.33823 | -43.86285 | 2025-10-11 05:01:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6aaf3425-af1f-3a7b-a487-da6a5c7b3c64 | -10.52759 | -47.34172 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 541105f7-b919-3793-b177-80f90f5a4202 | -12.24673 | -51.14032 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85e6e91f-cccc-3929-87d6-730148ca729a | -12.23864 | -51.14082 | 2025-10-11 05:01:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e27e0063-17a7-341e-be98-c10e300cf8ac | -11.53159 | -49.27858 | 2025-10-11 05:01:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce2cec4b-da79-359d-906b-15bf2ee4438b | -12.9067 | -47.0372 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63f94396-c0c8-39d3-918d-82800348f368 | -7.53218 | -44.60695 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79401daf-53f8-3682-8894-1e4bddb0240d | -8.1897 | -43.32819 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 180b6607-22a7-3bc1-838d-c0ca74db4186 | -13.46055 | -47.69692 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 599652db-94c6-382b-a6c6-5a8167f5da4e | -13.37963 | -47.7373 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d091965-c4b4-3c9a-84b2-d43f346ce955 | -13.29864 | -47.98899 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b04b6fd-da1f-34b8-bc50-d9c473ee86c1 | -12.95634 | -46.47801 | 2025-10-11 05:01:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f03025e4-0ffd-31d4-bb40-7fd034fe962c | -8.19543 | -43.3201 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 35b0f1d4-0140-3ded-a528-1da2684b0c14 | -11.97903 | -58.06573 | 2025-10-11 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1d21c06-e7da-36fa-9c08-b4c8f2fdd545 | -13.30381 | -48.4911 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dec7e1f-4e2f-326c-8b82-9ea02f90a73f | -13.21103 | -42.33383 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| ecf59135-6f11-3b14-898c-0a839a13973c | -13.31746 | -47.12546 | 2025-10-11 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea09c28c-67ff-34fd-a7a0-b562f2620407 | -9.10989 | -45.04493 | 2025-10-11 05:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d242ff74-be90-307c-9003-8affe7322a42 | -13.36229 | -47.63144 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f50a49cc-c5b6-3c9b-8e59-36193bf0c1df | -10.52829 | -47.3363 | 2025-10-11 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e80f841f-12ee-3b59-9c85-8e23716e9d87 | -13.29322 | -48.49901 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3c30101-1944-3f09-a5f8-9e7378b671a9 | -11.76327 | -43.32099 | 2025-10-11 05:01:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35aaa7b6-e1ab-39ed-8c5e-c0fe291df315 | -7.65637 | -42.58643 | 2025-10-11 05:01:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7a80ad2b-d3bd-342f-86a7-6aeeb43f73b9 | -10.62106 | -54.95618 | 2025-10-11 05:01:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00747962-e895-3703-87b2-5fc66f659fb8 | -8.0169 | -44.46435 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c4f3b19-e0ca-3721-827b-5ee7a4da2857 | -7.52601 | -44.61007 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a59e1e8-f328-3281-a6fc-9ebe2a3933fd | -7.06626 | -45.21824 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 629c8c5e-5168-3107-a62f-e669c0f50800 | -7.38906 | -45.16827 | 2025-10-11 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99afdd53-408f-3cd4-9f08-789f475f5629 | -9.50917 | -47.87706 | 2025-10-11 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aff13fc5-e7a0-39fb-8ced-cb6a34824b38 | -10.06529 | -67.55349 | 2025-10-11 05:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 13.7 |
| da92f54d-a6bf-365e-bff5-01172ac0222f | -8.20039 | -43.33041 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 00fa2f4a-6396-3f7f-86a9-f3e062188211 | -13.20884 | -42.35395 | 2025-10-11 05:01:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 73dbd55a-1df2-3f72-ae2d-e645c4268443 | -11.88456 | -45.48866 | 2025-10-11 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87dec813-6f68-3e50-aa6e-4d63f168bc07 | -13.2577 | -48.02057 | 2025-10-11 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e83ce32-5ee7-3831-a653-f8ba20f6cd13 | -7.40403 | -45.91991 | 2025-10-11 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b894d033-4d00-3e86-892c-881e97c6cb9e | -8.21152 | -43.34168 | 2025-10-11 05:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ea293d89-8d57-33b5-8f2f-bc4cbfb04de6 | -13.29938 | -47.98291 | 2025-10-11 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cbc8336-1a6b-3a16-acd7-5760630e8655 | -7.85508 | -44.48453 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3044ee04-4ee5-3ce1-bdb2-efffa9d93402 | -10.16542 | -44.55342 | 2025-10-11 05:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31b7e7c2-943b-352e-ba25-f2e554891f93 | -13.30315 | -48.49623 | 2025-10-11 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0af0cca-5b08-378a-bbd7-61b5beaf3d23 | -12.71546 | -44.94263 | 2025-10-11 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6eb386c-9f76-30cb-8548-61046ec3902a | -10.56124 | -57.51225 | 2025-10-11 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8baeb45-bb55-3216-8f3a-ee91d336c40d | -8.01736 | -44.46609 | 2025-10-11 05:01:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c525136c-276b-3725-a52d-54210dc3b230 | -12.90176 | -47.04799 | 2025-10-11 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5971eadf-e5f2-3c91-b4c4-ebd78597e90e | -7.62122 | -47.83178 | 2025-10-11 05:01:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e88a085c-b3fa-3e4b-a516-1109ccbc0b3b | -10.42803 | -44.99837 | 2025-10-11 05:01:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e265bc0-6e07-3da6-97f3-4edac9d55214 | -11.77472 | -45.03849 | 2025-10-11 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README36.md)
