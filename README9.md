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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e63bd63c-dd68-354d-a1d2-1b3d0325a06b | -12.08082 | -54.61666 | 2026-06-25 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecd8f870-b2e6-3d47-b2f7-5f86eb5a20f3 | -12.55566 | -54.58501 | 2026-06-25 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 358a2241-fe4a-3c55-9e34-b0e0653dd30b | -15.06351 | -47.46023 | 2026-06-25 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 3917a2e2-2fda-3657-adb4-d65d47d5a617 | -11.88579 | -51.75595 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 077237df-9af2-3962-8359-c251b0b045a4 | -11.79957 | -56.99136 | 2026-06-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d085e54c-5978-3888-bdd8-01405f98533a | -18.15551 | -43.59278 | 2026-06-25 04:17:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62c39750-819b-302c-82f0-e927969b4f34 | -11.32204 | -43.32867 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5464f0dc-d60a-3397-b2d7-2d03f12134a0 | -12.5549 | -54.58885 | 2026-06-25 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f8b6980-d5ec-3a16-a78e-42fe67e560b6 | -12.23094 | -55.5032 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6a72d4a-108b-3812-b6fa-7c564a76237e | -15.06764 | -47.45689 | 2026-06-25 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| fcb4c750-b3ad-3e4f-b3a8-0f251f904708 | -11.89146 | -51.75161 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8a1a5142-77e4-3c77-8869-7bdcc97eee43 | -11.04243 | -47.03386 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69255142-739c-32e6-857a-2ab7243de0ff | -13.06485 | -53.35857 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9fd71e09-1a23-3315-8a9a-8e882cb141ad | -11.91295 | -43.3997 | 2026-06-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 823fc22c-30fa-35e5-becd-018ea14b6bb2 | -11.7653 | -47.33796 | 2026-06-25 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97f67688-a565-35d7-9dc1-4ce4a15fa3c5 | -14.21753 | -45.63322 | 2026-06-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 569e2574-a489-3e32-a57b-f973597f1b69 | -11.24746 | -43.3274 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7ac19679-aec8-3b2f-80af-515a15a67bff | -11.64203 | -52.85967 | 2026-06-25 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86e9bccc-db27-3f9a-8aca-17821b300db7 | -16.42661 | -48.84513 | 2026-06-25 04:17:00 | NOAA-21 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb71b4cb-92b2-3afe-885a-c27ed17771e2 | -12.7347 | -44.46234 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 099283a5-d1e2-3e4c-b271-fed459b04d98 | -10.37359 | -47.34067 | 2026-06-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 913f19f7-0cdb-3140-a7ed-fdacef7fc9ea | -10.61921 | -47.1764 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b908f20e-f587-3e79-8a13-c55463362abb | -13.8609 | -47.1372 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d895d049-6ee1-3610-9c9d-0329e41c2666 | -11.54023 | -52.7779 | 2026-06-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fd44041-6ca1-33e8-8130-07ce41c54ba8 | -11.64145 | -52.8627 | 2026-06-25 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cc3d7b2-36fc-34aa-96f9-a59561182c8b | -12.2181 | -55.50551 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c107e082-3526-39bf-85c2-4f788b6bdc78 | -11.5886 | -47.44449 | 2026-06-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03b79b87-c9c5-3b55-85fd-8194e4aecf66 | -12.749 | -44.45745 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a2511b9-4d1d-3321-be77-65c437f27c6b | -11.25463 | -43.32495 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 57d45e0e-0d2e-351a-90a8-ba6296a9e11e | -13.06605 | -53.35223 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebd14dff-7261-3651-9cd2-a0fc966177f7 | -12.7446 | -44.46394 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e5c4e1d5-bf75-3140-8066-2ee78c7f6e2b | -11.3198 | -43.32109 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55cc49c7-0a25-39d7-a6e4-da25c0460f3d | -12.83641 | -44.35674 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| df1d5eaf-57b1-36cf-99f7-30ce39a66473 | -10.61634 | -47.17145 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6d16b6c4-3c1b-35c5-ac20-5179be0d02ec | -12.13897 | -48.26488 | 2026-06-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| e1706f3a-71c2-3c60-883e-8c27e1f22a72 | -12.74845 | -44.46096 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4a524620-f027-3e75-a181-e152b74f5a2b | -11.91573 | -43.40377 | 2026-06-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9601409b-fc65-371b-91c3-7f64241b7d5d | -12.21466 | -55.50533 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4214c6d-de13-3d83-8d2a-42285463da12 | -11.04254 | -47.03855 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aab5b30-f3b9-3624-8421-9aa9aaf57fc5 | -10.35677 | -50.11268 | 2026-06-25 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 747597c0-fef8-3393-ab65-5705f65fd321 | -11.50693 | -54.4991 | 2026-06-25 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| babd6dcb-da63-3e9a-9947-3370a26870b5 | -14.28249 | -47.41606 | 2026-06-25 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74168a99-6795-3bd1-8972-a4cc8f2bf1ae | -12.74735 | -44.46798 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a9c2dda-02d5-3baa-81a1-0fbbf0048db8 | -13.068 | -53.35392 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 194f4b5c-35d3-3f11-bade-3d5700d2a057 | -11.32258 | -43.32514 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6896cca-807d-3a3a-a930-0effcb5aa2ca | -15.75662 | -43.23275 | 2026-06-25 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2d57eb04-8e22-3b29-84ca-3388962833d6 | -11.94379 | -46.74612 | 2026-06-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac8a0b89-5919-32d8-8220-c60c9c0facac | -12.22662 | -55.5075 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 63aa7e5c-d4a9-3b74-aec3-2bfb02db8b3c | -17.34219 | -42.62762 | 2026-06-25 04:17:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2285b709-9e34-3c0c-86e0-9eb2991d2064 | -11.2574 | -43.32897 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c61c1f4-8133-30b2-b4f4-2ca8742e5510 | -13.85599 | -47.13328 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b89a938-b86f-3040-b35a-799bf0fb48a9 | -12.22065 | -55.50634 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6979d1b3-21f5-3ceb-87b9-946a94fc56ba | -12.75065 | -44.46852 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ece5636-ad48-3267-bf35-2446102dba96 | -12.14015 | -48.26367 | 2026-06-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1fdc00f5-f6f3-3694-98bb-fbffbf2ae1f1 | -12.77706 | -44.43361 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af82be03-895a-331b-90ba-51c025057729 | -15.52667 | -45.92012 | 2026-06-25 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bda57cf9-5d01-3401-830b-2361b9ea9ec9 | -15.08689 | -45.49662 | 2026-06-25 04:17:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ae6df5d-6e00-3a93-a7b3-ca59a6274341 | -11.63871 | -52.86078 | 2026-06-25 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3d9ce2a-4054-3825-bef8-342bdcb661cf | -12.84026 | -44.35376 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c582296d-6932-338e-bf5a-f1285438862f | -16.08589 | -45.89332 | 2026-06-25 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13389d28-35fd-3515-9068-86ef4a172d1a | -10.12854 | -52.10867 | 2026-06-25 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec88310e-54f9-368e-bdcc-d34d65b347ab | -11.54475 | -52.78182 | 2026-06-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8a0ace8-2dc2-3e54-9e44-8ddc16ccfe1f | -12.7424 | -44.45638 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7466586a-3139-3de6-a521-fda5348ddee3 | -15.76002 | -43.2333 | 2026-06-25 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6a513da7-bdfe-3cdb-8725-a746a30562a8 | -12.50639 | -48.26031 | 2026-06-25 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb4ea6f3-71e7-375b-84b3-07b6e2ec8707 | -11.49706 | -52.92553 | 2026-06-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc437f8c-6067-3331-a531-8b77620c3fda | -11.04611 | -47.03913 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f1a42cc-56e4-37af-8084-75eedb7ced57 | -12.83971 | -44.35728 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 776044a2-92ab-304a-9984-0c8d93763065 | -13.06738 | -53.35708 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 711a3f3b-097b-3eb8-b407-c15ef1036574 | -11.91647 | -44.16811 | 2026-06-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1076854-ba10-3add-9ee3-c18742f30cd6 | -14.69576 | -46.15213 | 2026-06-25 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f723e7f-0310-31f7-b566-ba7f884602b8 | -12.22588 | -55.49741 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6a504976-8978-31ac-8784-893cdc2b2a0a | -11.62233 | -48.48972 | 2026-06-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 272da99f-e10b-3217-9f3e-0397c6ec0a9b | -11.88206 | -51.74984 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3688a099-9a85-3235-b5c8-e03e392fa93b | -11.5599 | -47.61615 | 2026-06-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15bb4961-7c63-39c9-b6fc-fbd31dae144a | -10.77183 | -54.11009 | 2026-06-25 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50fb606d-232c-3e23-8260-823ff52cb1c7 | -10.61561 | -47.17574 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d0096ef5-921d-32a5-8e85-c6f422350b3f | -10.12802 | -52.11156 | 2026-06-25 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72492195-6110-3b33-84c2-1abe77554dfe | -10.36848 | -47.34869 | 2026-06-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9c4ed3a-8f99-3031-9e53-7179ee9bb773 | -12.43243 | -43.77947 | 2026-06-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ba725e3-7d22-3072-aeee-89c1256d7de9 | -11.79179 | -56.99591 | 2026-06-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b2d090c-4165-3422-ac8b-8fae5969e020 | -11.91518 | -43.40731 | 2026-06-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a28dc553-3dcf-364a-92f3-b1458d0de025 | -11.88676 | -51.75073 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 64e5fca6-526a-32e1-a036-3fc07729f663 | -11.91241 | -43.40324 | 2026-06-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c92e64c8-d821-3354-b788-d88b9d9554e3 | -12.7457 | -44.45691 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 040c2d3e-beb9-33a3-8e11-a6b1db400eca | -11.31926 | -43.32462 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b4bc26a-850a-370b-8c28-a892ed8e7de1 | -11.04321 | -47.03442 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9a69b4b-076f-3c08-9ee0-a94c11f3fa8c | -17.12189 | -41.34264 | 2026-06-25 04:17:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| acef5b78-863a-3990-a1f2-28f63c720cb3 | -11.20562 | -43.35684 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a442ed98-a9bc-3da7-a5ea-b4c632047d89 | -11.58498 | -47.44389 | 2026-06-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d431cad2-9938-3da3-aa14-6e01bf1215b8 | -12.7479 | -44.46447 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1c3cb1f8-cb07-3f21-b09e-14e5c8220dd7 | -11.90909 | -43.40272 | 2026-06-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa2aa158-1671-357b-a28b-2f6d0434f6f8 | -10.37286 | -47.34497 | 2026-06-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6c47fd85-059d-34ea-8f4d-0ce6b72e61f3 | -11.28213 | -53.94845 | 2026-06-25 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d9d0bd2-3762-32a8-a309-484f7af722e7 | -13.8748 | -47.13949 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd6defdb-14ad-30c7-9b41-9f5fb4c65f01 | -14.31571 | -42.40659 | 2026-06-25 04:17:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| add8620d-a748-37d0-b42a-1f07bde8d52b | -13.86231 | -47.13825 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abee3bf5-092b-3fb8-9ef8-3a972bd1b2a2 | -10.7736 | -54.11242 | 2026-06-25 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea7b0333-0ae0-3e6f-800d-7bd22d13efe9 | -12.21653 | -55.49618 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 416553c1-6c62-35c8-a333-f03266a7f158 | -12.22755 | -55.5029 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README10.md)
