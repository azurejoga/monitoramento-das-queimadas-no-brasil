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
| 1de5f4b9-c43d-3292-8f9a-55512f52a2e1 | -10.8413 | -49.2322 | 2024-10-15 00:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| aca2e02d-0e95-39c9-ac11-c2ae64b19d8e | -11.884 | -43.8142 | 2024-10-15 00:16:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d2e58845-810b-3714-bd22-3c31ca52faf9 | -11.7271 | -46.850601 | 2024-10-15 00:16:12 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1706ba4-4ad5-3686-815e-58713fd89986 | -11.7302 | -46.865898 | 2024-10-15 00:16:12 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93a78ee2-66b6-306e-9ed7-63a6a3e0b30a | -11.7205 | -46.867901 | 2024-10-15 00:16:12 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bba5836-887c-38f3-97bb-74ebabec50ef | -11.6915 | -65.2432 | 2024-10-15 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6315d53e-aa3b-3555-83ab-ed4044acd096 | -11.6917 | -65.2243 | 2024-10-15 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 301f4fe9-0b99-3dcd-9993-df9635e2253d | -11.1246 | -44.181099 | 2024-10-15 00:16:13 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00c3d2a1-ac9a-38aa-bead-5c08ad089072 | -11.1344 | -44.179001 | 2024-10-15 00:16:13 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20e13c99-dbd7-323f-81b1-27854c0d7e8e | -11.0621 | -43.886299 | 2024-10-15 00:16:13 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62c0fafe-acbe-39d7-a18c-1fb755eaf500 | -11.1268 | -44.191101 | 2024-10-15 00:16:13 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91df28be-8d1f-3f1e-817d-5780a0d29435 | -11.0718 | -43.884201 | 2024-10-15 00:16:13 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ecd98f79-b8a9-39c1-9a56-8da7d173f846 | -12.0796 | -50.2966 | 2024-10-15 00:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 39e88775-d7be-308d-857e-cd7bceaa1ea2 | -12.0799 | -50.275 | 2024-10-15 00:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 4468a3b8-ceb8-3c5d-89f0-5d7b05d4b927 | -12.0987 | -50.2943 | 2024-10-15 00:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 504888ce-5361-33fa-bbfd-4357c4fd2aff | -12.099 | -50.2728 | 2024-10-15 00:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| dafd70db-a35c-3ba8-bf7b-c68fd4f44941 | -10.9116 | -43.612701 | 2024-10-15 00:16:14 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8113255-f923-3d1d-9604-9871a3f535e9 | -10.9395 | -43.743301 | 2024-10-15 00:16:14 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3815f0c2-6cbd-3239-91be-33f1d1f0537f | -10.9415 | -43.752701 | 2024-10-15 00:16:14 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c0c2257-628a-3bbd-af9e-462d36476b22 | -10.9297 | -43.745399 | 2024-10-15 00:16:14 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e645b5a4-f465-3888-85c8-8a534cc42044 | -12.3793 | -63.7294 | 2024-10-15 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 182c4aef-3fd6-3b0d-a776-1bce7e6a7732 | -12.3795 | -63.7103 | 2024-10-15 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8170e67c-bd6b-37ae-a7c9-31e330d20588 | -12.3982 | -63.7284 | 2024-10-15 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 9b0a723a-1cb0-34c2-8f8b-431ad735d766 | -12.3983 | -63.7093 | 2024-10-15 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 04fe037e-f188-35b9-81bc-030df136fc17 | -12.4603 | -63.0169 | 2024-10-15 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 21478a1b-46a1-3758-98f6-1792592dd9cd | -12.4961 | -63.2641 | 2024-10-15 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| ddaf352c-29d1-30b5-ad53-2b6b9baf5ccd | -12.5149 | -63.2822 | 2024-10-15 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 03a5a73a-4738-3616-b13f-447adcf4a18f | -12.515 | -63.263 | 2024-10-15 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 126.3 |
| b4a3cb88-c21c-37b3-a067-e77c47de7953 | -10.4821 | -42.432899 | 2024-10-15 00:16:17 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 75f6bf56-1615-3e40-aada-42a83018ac77 | -10.4838 | -42.440899 | 2024-10-15 00:16:17 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ded57875-b768-38bf-a93b-b723ce622db9 | -10.4856 | -42.448898 | 2024-10-15 00:16:17 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 99f33ef1-d512-36b4-bd88-a3b8947262dd | -10.4723 | -42.435001 | 2024-10-15 00:16:17 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d495fe53-3a90-3ac2-98ba-a5590af6d275 | -10.474 | -42.443001 | 2024-10-15 00:16:17 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 11181c3f-cf6e-3ce5-9997-8f4de90a0a27 | -12.0793 | -50.250099 | 2024-10-15 00:16:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad257410-c27e-33c0-9cf4-2470f2c6d4cb | -12.0843 | -50.276699 | 2024-10-15 00:16:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1de09c9-8cdc-3994-8c4f-5b5e7f97f57d | -12.0696 | -50.2519 | 2024-10-15 00:16:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08734a4f-925c-322d-9cdc-9483627dfade | -12.0746 | -50.2785 | 2024-10-15 00:16:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3c53f1d-6457-3346-95e4-449dd368865f | -12.0599 | -50.253799 | 2024-10-15 00:16:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76dce0d1-4fd7-3a4e-8028-ca9afc8a519d | -12.0649 | -50.280399 | 2024-10-15 00:16:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62f80d63-4855-3c7e-88c5-ec0543c1cffc | -10.8329 | -44.444801 | 2024-10-15 00:16:18 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4869e91f-e86d-3e32-94c4-ac6f9b3fbabc | -11.6191 | -48.492802 | 2024-10-15 00:16:19 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be23e82f-2e7d-323e-8612-d76fc2c01279 | -12.9538 | -62.7962 | 2024-10-15 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 04eb206e-8eb2-33d9-aded-6d3a24f86ac2 | -12.9728 | -62.7951 | 2024-10-15 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 205bbc0e-407b-3919-8fe1-5cd3f47bb08a | -11.5745 | -48.419998 | 2024-10-15 00:16:20 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 826299ba-4226-3a63-b0f8-b21004dd1ec2 | -11.5783 | -48.439499 | 2024-10-15 00:16:20 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b00b014-0dfc-3dbd-ac32-be7c36c518cf | -13.1285 | -62.3227 | 2024-10-15 00:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 120.5 |
| ca21def3-9a30-358b-84bd-6704c437b7bf | -13.1287 | -62.3034 | 2024-10-15 00:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 104.3 |
| f6b578bf-3526-3a73-a01e-db5b6c67e415 | -13.1473 | -62.3408 | 2024-10-15 00:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 680254a6-203f-33b0-b7d2-ad505c2a95da | -13.1475 | -62.3215 | 2024-10-15 00:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 0c8b7ba7-cca9-32b7-aa97-e60cc0b9c274 | -10.6754 | -44.328999 | 2024-10-15 00:16:21 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| abbc4fe2-4d34-30a7-9821-04640799ef6a | -10.7598 | -44.8246 | 2024-10-15 00:16:21 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a1bfb971-9d0b-38f4-9ab5-26b8eeb594dc | -10.7501 | -44.826698 | 2024-10-15 00:16:21 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4f9ac98-0eb9-3cb2-9c9f-ff18f7d0b0e6 | -10.7524 | -44.837601 | 2024-10-15 00:16:21 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4f07fb0-a088-38a1-9882-cb2f6c4cb0cd | -13.3594 | -61.9789 | 2024-10-15 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| bb925905-eff3-3b38-928a-481f381e1414 | -13.3596 | -61.9595 | 2024-10-15 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 60898937-d3ff-3ec5-ba74-90bcfd4cd6ee | -13.3653 | -61.357 | 2024-10-15 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 54407706-c7be-38bf-95d3-59ee36e8946b | -13.3655 | -61.3376 | 2024-10-15 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 5486fa52-50e2-3e19-b186-e7612054c170 | -13.3786 | -61.9582 | 2024-10-15 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 13ff7f45-2c50-3dd4-93e2-5767d36539da | -10.5716 | -44.225601 | 2024-10-15 00:16:22 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6d87b35e-5038-3e32-8450-4f7de632d614 | -10.4656 | -44.063999 | 2024-10-15 00:16:23 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae15b7e3-3fd2-3cbc-b607-17e9f5423279 | -10.5122 | -44.186699 | 2024-10-15 00:16:23 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afc275a5-82fa-342c-b731-0673cff3b97e | -10.5143 | -44.196499 | 2024-10-15 00:16:23 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ccfa97f-fedb-35bf-9d2c-477708467911 | -10.5024 | -44.188801 | 2024-10-15 00:16:23 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f077b3ae-889b-3a16-8571-0b114a9ed2f6 | -10.5045 | -44.198601 | 2024-10-15 00:16:23 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67445c9a-07ea-3b57-a716-c76a6b1d5af3 | -8.3308 | -42.7388 | 2024-10-15 00:16:24 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 238fcc1b-d89c-3a50-b61e-9174884b3a74 | -8.3326 | -42.746601 | 2024-10-15 00:16:24 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f4f6bdfc-a568-3ba0-bec6-d5c08d5f1361 | -8.3193 | -42.733101 | 2024-10-15 00:16:24 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99200b58-9fe9-3db9-93b6-0815abdfeff1 | -10.5327 | -44.861198 | 2024-10-15 00:16:25 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c713faa-0212-3b6e-a734-f71b225b57c9 | -10.2607 | -43.967602 | 2024-10-15 00:16:26 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 50b7a9b3-03ad-3467-b9e8-8fb5f7c70ef3 | -10.2509 | -43.9697 | 2024-10-15 00:16:26 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67b7c577-d93a-3a77-b2e6-3834cf961e05 | -10.2529 | -43.979198 | 2024-10-15 00:16:26 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b70c8a3-8f2c-324d-a7c3-1a0165768e72 | -10.4906 | -44.904099 | 2024-10-15 00:16:26 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff772937-1e18-38b2-a8d2-1cb528c4c824 | -10.3874 | -44.801998 | 2024-10-15 00:16:27 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 85859297-d46a-38c7-8196-4e1ae0d8d6ae | -10.3896 | -44.812698 | 2024-10-15 00:16:27 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 938373c3-5c92-3d42-90fb-8ffa501d3361 | -10.3919 | -44.823399 | 2024-10-15 00:16:27 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4b3056b6-37af-3c9d-99d3-23a15fabbdf4 | -10.3799 | -44.8148 | 2024-10-15 00:16:27 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 062a3aa2-299d-3ff8-beae-13be31c15973 | -10.3821 | -44.8255 | 2024-10-15 00:16:27 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ba08906-a739-330b-a9fd-d79f4513d243 | -10.0432 | -44.194698 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 12aee983-9e9b-3572-9ff1-ce19f45861cd | -10.0557 | -44.253201 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46005623-9cb5-3870-8dcd-3e719afd30ac | -10.0578 | -44.263 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| edb70e99-5c29-3dff-9137-b9e2265dca8e | -10.0845 | -44.196098 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0288e06-064a-3103-bfa5-c1903045ef70 | -10.0866 | -44.205799 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2813aec2-c709-3428-a04a-d26521546d60 | -10.0887 | -44.215599 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a1b6dd6f-1502-30f3-902b-91400eff0e28 | -10.0726 | -44.188499 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51c83fd8-6dcf-351c-8537-e0cba19c57f7 | -10.0747 | -44.1982 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13fa8d5c-24e2-3241-b0bd-c74f589d9127 | -10.0768 | -44.207901 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 070fb95e-aa76-3346-ba23-a520a202fa64 | -10.0789 | -44.217701 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3330cb0c-01dd-3f41-a5c6-9a6d2ece1ff4 | -10.081 | -44.227402 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a278ac7-b44f-375a-9af8-979e15d714ef | -10.0831 | -44.237202 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a56c7c8-f148-3f4a-b43b-eb9583865f7f | -10.0733 | -44.239201 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70ad799c-5db7-38df-978d-42a6157aaeea | -10.0489 | -44.173199 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe0176cb-c347-3fe9-a443-c6d0e47b7fad | -10.0411 | -44.185001 | 2024-10-15 00:16:30 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 668041a7-26fe-3b2d-98d6-cda17534980b | -10.0334 | -44.1968 | 2024-10-15 00:16:31 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78f8f050-cd45-392e-aec5-d2ead77aef31 | -10.0355 | -44.206501 | 2024-10-15 00:16:31 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8908b021-02d7-348f-89d0-a72adc4a265a | -10.6097 | -47.691898 | 2024-10-15 00:16:33 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ddb3221-8b2c-34cb-b388-8e4defd0989e | -10.6131 | -47.708698 | 2024-10-15 00:16:33 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3070754-268e-3697-8fe0-7ca320023f41 | -10.6033 | -47.710701 | 2024-10-15 00:16:33 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70386a6a-f67c-3ee1-93bd-f4252a9bcf63 | -9.7133 | -43.8508 | 2024-10-15 00:16:35 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 322aed6c-43f5-36b3-bedd-4656a6b5d55e | -9.7152 | -43.860001 | 2024-10-15 00:16:35 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cdace851-dd61-3e80-bfbb-e0d2de102385 | -10.8262 | -49.2271 | 2024-10-15 00:16:35 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
