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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06e9a731-1f27-3898-ac0a-447560a2fad7 | -12.40168 | -58.04691 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b10e794-58f6-377b-8b1c-461f2a3811d6 | -14.19679 | -57.25098 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6683574-30bd-3ad1-963f-38b4251d1734 | -15.48207 | -48.95143 | 2026-01-10 05:20:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef60c899-d245-3143-bed0-770f5ae52371 | -16.59471 | -58.21238 | 2026-01-10 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f38830e8-80dc-370e-99bb-61c1987f201d | -12.40982 | -58.04013 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 339c011b-7ca8-3143-bed5-e1c27567aee9 | -12.40575 | -58.04351 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40d24ed8-b366-324e-8e13-ad607db2d49d | -12.39528 | -58.0419 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0fafd631-0c44-3318-b6fa-6b41efdb8b37 | -14.19068 | -57.24098 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c8fa22e-6d8c-3d37-a23f-d60b99cef1c0 | -12.38132 | -58.0397 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec5b31d8-7a6f-3a44-9044-1e5bb8cb997e | -15.97144 | -56.27803 | 2026-01-10 05:20:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 824015e4-8e61-3739-8897-b1e7b77d11a0 | -12.40342 | -58.03512 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4203634a-dd33-336a-9b41-087741e0d913 | -16.09606 | -56.75188 | 2026-01-10 05:20:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b6de3d0-181c-30c5-8fe7-e364ae06ed09 | -14.19373 | -57.24601 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42b80b68-afc9-38f5-99ed-78e7b192ae5d | -12.39469 | -58.04583 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4cab4605-4711-3893-8063-da15cfc5526e | -12.29621 | -57.3654 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c3e4ec2-b9cc-3b50-afc9-333b69d18ae6 | -15.26702 | -59.86037 | 2026-01-10 05:20:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99f276ff-209b-3fc0-a255-a16a34635d68 | -12.39644 | -58.03404 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 342e9e1e-b537-3e13-ba12-a02fee14d907 | -14.31584 | -57.58855 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2425dea6-d783-36f3-be36-f266af4510dc | -12.38539 | -58.03633 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 873b3aa3-1dac-3646-933d-93c4c517c033 | -12.39993 | -58.03458 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 81df343a-e0e3-31c4-ae7a-c7434c85cb69 | -11.83642 | -48.6475 | 2026-01-10 05:20:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77c26819-c25b-39df-8986-a044140a3d4e | -12.39586 | -58.03797 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d50d423b-c2d0-3600-ae35-bd076c8f1e7d | -16.37104 | -57.20884 | 2026-01-10 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cb32af63-e36f-3951-91ff-0ebf8a4eba13 | -14.18633 | -57.24492 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09d2bbf6-32e3-3255-b514-272a0611a922 | -16.09996 | -56.75244 | 2026-01-10 05:20:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0fa8dbb5-1ad2-3f51-b731-7fd3e077b85e | -12.39935 | -58.03851 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| edda6a26-3c78-3172-b611-6d121c4a5894 | -12.40691 | -58.03566 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe6bddc2-dcae-3bfe-a526-434074ae7c55 | -11.15045 | -55.17403 | 2026-01-10 05:20:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fa91297-c95f-332b-b400-e463d29606d9 | -13.48559 | -52.94485 | 2026-01-10 05:20:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa445906-932b-3bbd-a348-62dd917f7f79 | -12.30217 | -57.37487 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d3d1b15-2025-3701-a22e-3dd8bdfbcce5 | -12.3883 | -58.04079 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 137d42fe-1658-33aa-8b53-fb16b48b35cd | -12.39121 | -58.04528 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0fb0c333-6102-3f6a-b735-8358a9b7e677 | -12.30339 | -57.36652 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a17fbc88-f261-3ba3-8735-d289d146644a | -11.80838 | -58.17801 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b6c6a90-c1b8-3f8b-858e-2e721fdb00be | -12.39295 | -58.03349 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e710ccef-7cd0-31a9-b723-d833acba0aea | -12.38945 | -58.03296 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 16407743-54f0-33a0-816d-74c9de3784ed | -11.00015 | -56.90934 | 2026-01-10 05:20:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a6d42d4-a505-34ac-8144-4e364c5b13a9 | -12.39179 | -58.04135 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9416eafd-2b91-395d-acfa-2541c9dc279b | -12.38481 | -58.04025 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e5e0b317-7cf9-36b0-b7e4-08c8d3ef7890 | -12.38888 | -58.03688 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f3b10bdf-d264-315d-b997-2a701ff3656f | -12.38772 | -58.04472 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b74038a8-7787-3f38-9c50-d6af0582b978 | -12.39412 | -58.04976 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dbc6a1d-7b6d-3491-b059-1db7de3962d7 | -14.19309 | -57.25045 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44513980-0516-309c-9615-c62657f1be8a | -15.26758 | -59.85669 | 2026-01-10 05:20:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9ce8aa5-9e3d-3f62-b7f0-4e3f0612cfb3 | -12.38423 | -58.04418 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 23dba7be-bb87-3a5a-9f3d-d2085cbc8497 | -12.40633 | -58.03959 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14566ed2-6ea7-3de7-b1c6-6f8371b7df9e | -12.41041 | -58.0362 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56486fb5-9f22-3a99-be19-0b6a228b5391 | -12.29918 | -57.37017 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7222925-6d86-3fff-baec-748fef9d8eaa | -14.3116 | -57.59227 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 119f743a-1440-3438-bae3-f5d4bf7f1623 | -12.29559 | -57.36961 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72166717-884e-3108-9555-385ac6771385 | -12.39063 | -58.04921 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 687e7b4a-fcbc-39bb-b59b-b10cda003d21 | -16.09926 | -56.75745 | 2026-01-10 05:20:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ae6f7ea-7fd3-3b94-b873-b38e718a3e00 | -12.39818 | -58.04637 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b7f1ac03-3445-30d9-8c72-faf72c4b5797 | -12.39877 | -58.04244 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8ab91d4-16ff-37af-a3da-2ae9a1dc79b8 | -16.36831 | -57.20599 | 2026-01-10 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1430376c-21f8-3bf6-9129-abd20717d042 | -14.31523 | -57.59284 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f31ff80-df08-3780-98d4-e7b378c92005 | -12.29192 | -57.39473 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e9cdeb40-d2f2-3b3b-a1b1-14887ea32ef9 | -16.10316 | -56.75801 | 2026-01-10 05:20:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8252ce96-3618-3e93-87d7-24e266ac4839 | -16.59048 | -58.21617 | 2026-01-10 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bd90312d-b82a-3b90-945b-675b6bbf7f56 | -12.2998 | -57.36596 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bf56524-3263-3428-8eb7-b6b60812f613 | -12.40226 | -58.04298 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17e2848f-2ae5-3714-9d7a-6af1fb3438fb | -16.10386 | -56.75299 | 2026-01-10 05:20:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55b1c663-cb1f-3904-877b-b6e285c44b3a | -16.36762 | -57.21085 | 2026-01-10 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6cd2d9a9-5ea8-371f-8cce-b1cb8a753e5b | -14.19003 | -57.24546 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61ab2bf8-77cd-30f4-9b14-f046148fdf0e | -14.31221 | -57.58799 | 2026-01-10 05:20:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aba39b83-1702-3cec-b381-14763003d0ae | -19.79542 | -57.38256 | 2026-01-10 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 237022e3-68aa-3573-bd42-dba330073f72 | -19.79457 | -57.38444 | 2026-01-10 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| aaded87e-6462-387c-a22f-bcee6c4a79e7 | -21.04498 | -49.59564 | 2026-01-10 05:22:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 039f6ea2-6803-3224-8290-b08d3d84c7d6 | -19.79219 | -57.37671 | 2026-01-10 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2fb442e7-a45f-33af-b8d9-2a149d787980 | -21.0454 | -49.59024 | 2026-01-10 05:22:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e408e06f-f1b2-3b72-a5e0-c91d33dc2682 | -19.79613 | -57.37727 | 2026-01-10 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a793426b-b293-3acc-a277-1641810c23b1 | -19.79523 | -57.37915 | 2026-01-10 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 80821cd6-6f58-3888-bb9e-a427e40f6429 | -20.54635 | -57.94944 | 2026-01-10 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 34769dc1-3324-3ed8-a9b0-081394ed8d8e | -21.04582 | -49.5941 | 2026-01-10 05:22:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9bd2abda-bc57-37da-ba2a-6d5dbdc165b3 | -22.81986 | -49.29646 | 2026-01-10 05:22:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebeec564-b063-3f5b-a84b-07b72f4e42cb | -18.52033 | -55.10714 | 2026-01-10 05:22:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 960f012e-f094-38fc-9e56-f0aab0d849bf | -22.82033 | -49.29007 | 2026-01-10 05:22:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c17cc5b-1d54-3684-b531-9d8ac4725b33 | -20.54568 | -57.95448 | 2026-01-10 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c46176e4-e1cf-31bb-8a93-8efe08e74a79 | -18.52424 | -55.11238 | 2026-01-10 05:22:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5071ca0b-66dc-3c50-b842-8640d9b9794d | -22.97673 | -48.65106 | 2026-01-10 05:22:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b79e40b-e39e-3e74-9626-0a8c572d3571 | -21.03928 | -49.59341 | 2026-01-10 05:22:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b9855753-d93f-32b7-b4fe-1421e9027690 | -12.4135 | -58.0292 | 2026-01-10 05:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| a7cee94f-3ce2-3efc-95b3-7303a9a0401e | -12.3946 | -58.0307 | 2026-01-10 05:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 6330dcfd-dae8-3e0f-bc2f-2166faa610e5 | -12.4133 | -58.049 | 2026-01-10 05:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 27a6a518-ae1f-3da9-92da-e0f937671d2a | -12.3943 | -58.0506 | 2026-01-10 05:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 56ed34d3-118e-37bc-aa57-d9ca1958bb30 | -12.4135 | -58.0292 | 2026-01-10 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 831542cc-6cb4-3ae2-a5ab-1a124d45e55e | -12.3946 | -58.0307 | 2026-01-10 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 7ff988c4-1db3-311b-8ab4-fec61b9952a9 | -12.4133 | -58.049 | 2026-01-10 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 005c7e65-1af5-38bd-acd6-8f6ef0eb565a | -12.3943 | -58.0506 | 2026-01-10 05:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 11224038-1c6b-38ee-a9dc-b9bdf864dd84 | -12.3946 | -58.0307 | 2026-01-10 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| dbb15426-20b2-324f-9e76-5961c0717858 | -12.4133 | -58.049 | 2026-01-10 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 39a8e6c3-d808-34db-84e5-6174dd068860 | -12.4135 | -58.0292 | 2026-01-10 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3c70ad6c-d813-3668-a120-ee7e37c28a24 | -12.3943 | -58.0506 | 2026-01-10 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 072e6fc6-c2c1-3ec6-a54f-4e478dece170 | -12.3946 | -58.0307 | 2026-01-10 06:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 2eb5a486-0822-32c4-8a28-21bfce5db005 | -12.3943 | -58.0506 | 2026-01-10 06:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f6b56b04-6538-3fbf-bbde-ad2d2c6959c7 | -12.4135 | -58.0292 | 2026-01-10 06:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 140a8680-df84-3390-b0f5-9dd8eea9b9f8 | -0.14891 | -60.74113 | 2026-01-10 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db277f37-0c5f-396f-8526-1e0d8e59bd0d | -0.14398 | -60.73651 | 2026-01-10 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ade4072-57bd-390e-8b86-27d3fb849c48 | -0.14947 | -60.73759 | 2026-01-10 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbba6760-403f-3ac3-b5fc-278c9c989692 | -10.38653 | -48.89711 | 2026-01-10 06:09:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README13.md)
