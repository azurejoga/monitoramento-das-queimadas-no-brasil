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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fa9f9e1-c00c-3d72-ba33-61eb5f847098 | -12.62526 | -47.26429 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d3e5f7a-3419-3ef5-9461-c8a26ea188f0 | -11.95534 | -50.94164 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd818070-2b86-307c-8db3-731369f45ac6 | -8.28899 | -54.70711 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 410bccbe-adeb-34bb-afee-76a807168579 | -12.39436 | -50.21963 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 951410e5-969b-3435-993e-c20b8d056d9c | -14.51632 | -48.29492 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f8418bc-392f-3bb0-b222-4784207208b1 | -12.73029 | -47.27365 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d1314c8-f9a3-3e9c-855c-55b8c711419c | -10.79306 | -48.74857 | 2026-09-29 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7c892b66-c8e1-315e-aef8-b8c528dfc85f | -10.38934 | -61.24997 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 7c5a6cc0-a5eb-3c81-ae4f-ac9f90fa39ca | -7.46714 | -55.00703 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76d83f93-71cd-380e-b0a9-d89f7f7b5231 | -12.55991 | -47.16458 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4159c3df-4ce2-3896-8664-07ef8d052e39 | -11.42975 | -43.44579 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6021e279-7439-3e8f-84d6-ed5af55288b5 | -7.50499 | -55.04196 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d67035e-a2f2-3ff0-922a-8afa270a1886 | -10.27905 | -44.6344 | 2026-09-29 05:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 881fab8e-db08-3b83-9ca8-5dd843d54550 | -13.43816 | -48.61848 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bb184ef-2e8f-340f-8caf-47b626b5b785 | -11.14848 | -48.31985 | 2026-09-29 05:12:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5759fd1-2e72-3790-ae37-bcc31c086b8f | -13.21461 | -48.5675 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79011855-2e07-371b-9e92-be79cefe3e9e | -13.46877 | -48.58493 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f13635a-cd5b-38bc-bea3-d55ff27b5e76 | -7.18378 | -69.89487 | 2026-09-29 05:12:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aade2747-4acb-3205-8d96-99b1133c9f82 | -7.49659 | -55.02969 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec4bbdd1-2e9b-3482-a541-8a0eb96e3fb2 | -12.94196 | -46.65115 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f4fba11b-8dee-319a-9c35-9155709edb71 | -11.99206 | -50.93369 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1676c53c-6ef2-3986-b2b9-b21d6ac36c04 | -11.33719 | -54.11327 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff08ec53-23d4-3fe6-a542-7b88df89811e | -14.08432 | -46.32078 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6686ddbb-6193-3e35-8beb-cc454bc79e6a | -7.50834 | -55.04249 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 382f9190-cd92-3820-94b7-256453442f66 | -11.95522 | -50.93911 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aff2b154-eeea-3d8d-bfac-a4c34c74cce0 | -12.69216 | -47.25594 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b895a45-b42d-33ac-8229-95a070dcaf09 | -13.1102 | -47.41119 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bea8173-7549-300f-bf1a-8fc282fa0d54 | -9.16969 | -61.40779 | 2026-09-29 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 00ddcf87-4eb7-3b38-a343-cd7e79f9e7d6 | -13.53907 | -49.17891 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7de1e72-a6ab-332b-8036-2d66023f48d8 | -12.47449 | -47.4851 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea136023-512b-3e45-b58b-ad40ceda7cd7 | -11.3841 | -54.04404 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d518f814-b588-3d83-b1e5-a407fcf2cf34 | -12.94014 | -46.64877 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f9ec093-8945-3c72-9cdd-dafcda0a5fdf | -12.75427 | -47.29015 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52b80e1d-0c15-36d1-9466-8cf1eeb37b9d | -7.5128 | -55.03589 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ccc0dae0-6cce-3086-8c77-bc47abc36a33 | -11.50409 | -47.4036 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e5f1575-be04-3782-8fdc-b3abb4a7fbe9 | -9.9518 | -50.15225 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9ffb8d6-6d88-31dc-b40b-5a0f8f19f46e | -11.43525 | -43.46041 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8a982a82-c064-32fe-be78-f86eb7fd86f3 | -12.02126 | -50.98144 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45a64c02-2a46-37bf-aa35-c5d0e24c906a | -11.17613 | -44.80397 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 78f43576-1432-31c0-964e-989c6ca6d66e | -7.49604 | -55.03327 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c41821f7-8305-38fe-b655-3e137c6e3743 | -9.95813 | -50.13938 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b223148-319a-3f57-9528-072460baccb7 | -11.34496 | -54.11024 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 600753f9-6045-3065-8e77-ebffcba3c1ea | -11.98596 | -50.94596 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 458c141a-cb47-3050-b6d2-d0d079e2d66c | -12.73589 | -47.27485 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 97a51202-ad24-386c-913d-58597d85d1c0 | -12.7486 | -47.28952 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1c1ae07-b614-32ee-a899-b023c7906f6d | -12.38911 | -50.22386 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b0488d1-1617-3951-ade5-18b72895f659 | -13.43738 | -48.62051 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1857b26f-3bd2-3ffb-8e6c-e799c75e40da | -8.66032 | -48.88489 | 2026-09-29 05:12:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f42be7d-42b8-3f65-9c0f-39c70bd6b14d | -13.14243 | -48.54903 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea3f7c4a-7897-30bf-9ec0-02a78af34ce6 | -12.02592 | -50.94719 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4fbcaf4b-5aa7-3f7f-9561-adcd6378fa62 | -10.38851 | -61.25472 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ffc33a15-f324-334a-99d8-bb338b3f9485 | -10.41942 | -53.77869 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9efee2d6-68df-3362-9aa5-2e491d135578 | -8.29182 | -54.71132 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab3f440c-bc70-3ad8-8db2-f0bd1401a0f4 | -12.75624 | -47.29622 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba3ef5c4-81eb-31be-9d73-7c38be2d0a80 | -9.78968 | -48.20115 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f9600ca-e448-367f-912b-d4168bcb5f3f | -11.33659 | -54.11738 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e19ef06-69fa-332a-8610-f3922e467800 | -13.06188 | -47.4524 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b26ab94-e23e-3884-a001-7e9874381b5a | -11.42821 | -43.45958 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a9edf831-58a5-3e38-bfdb-9fd35b5c4955 | -11.36255 | -54.04077 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1a1d5c1-d240-3432-977f-65ec2ef0b7de | -7.49994 | -55.03022 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00824b2d-f4a5-3f71-b67e-2f1dd0bb08cf | -11.42039 | -43.46571 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dd6bfef-0d1f-34ef-9617-74eebee2812e | -11.34819 | -54.03854 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 726119a9-4c98-3299-b1d3-5b6e801d206a | -11.98159 | -50.94535 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22f5213c-7c80-30c8-accf-17953e3dfb2d | -11.38707 | -54.04877 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 997abbe9-09c9-3c40-86a6-13ff12eb5c2f | -12.73854 | -47.27719 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4cd19a4-5e12-3c54-ab93-7ce1d0a9b6f0 | -10.69944 | -48.7634 | 2026-09-29 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d2d1a94-c6ee-3dcd-9aff-284d1eec50d6 | -9.67715 | -45.5596 | 2026-09-29 05:12:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0706e72-5ef2-3e6e-bd12-8a507ac58609 | -11.344 | -54.04214 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeb18b22-920a-3974-b790-0f03d2c11220 | -11.99299 | -50.96004 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0133eb97-797b-38b0-997d-9c22f22b99fa | -12.48005 | -47.48587 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 707a052c-1873-3890-9bcb-5f1c463ed93f | -11.16893 | -48.32452 | 2026-09-29 05:12:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55f28488-cee5-3144-8eda-ea3d5373e118 | -11.18423 | -45.13733 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f69b45ce-965e-3bfa-82b6-4d0a91ae3269 | -10.42004 | -53.77451 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39c1eaf0-5f8a-39b5-a792-d8e4b7c431db | -12.69415 | -47.38208 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ff99443-b572-3146-9453-056e0b417015 | -12.04899 | -50.94166 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 22de59f3-275d-3f9d-83c9-a92872219318 | -10.38774 | -61.25917 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2385476a-9d7e-32e9-a3b5-182e47543e94 | -11.40308 | -43.45029 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e9356f6-3694-3720-a723-f2f082c21838 | -11.34854 | -54.11078 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a7caede-4842-3848-baf5-59301cecff5c | -11.41559 | -43.46545 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aa57309b-13f6-3369-8bfe-e565ee5ee344 | -7.56474 | -55.0331 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25f5c00a-d8c4-38d2-961e-3916acbe0ae5 | -9.95875 | -50.13488 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed09613f-99f2-3f20-a920-64f8e201c9c8 | -12.31415 | -46.40638 | 2026-09-29 05:12:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9440c873-fca6-36f1-b897-b2ee0f70eb5c | -10.38551 | -61.24921 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d5c24823-1da8-3e02-a068-f313491192d4 | -9.76752 | -44.82798 | 2026-09-29 05:12:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d5eefa2-c8b8-3e19-b6f2-bbcda4237902 | -9.92831 | -60.72641 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ccab7174-fb2c-38ce-999c-0a4308e19128 | -9.95242 | -50.14774 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 722dacda-c98b-31a2-bbd6-fd71dbfae229 | -12.17249 | -50.69368 | 2026-09-29 05:12:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6bc8446-ae47-3348-b625-433addcf6e29 | -10.38387 | -61.25862 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d6e90184-6fd4-320f-8246-824770148eb0 | -12.94141 | -46.6557 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a0c8018-477a-37ec-92fe-de5610c17559 | -11.41096 | -43.44405 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9eac6cd4-5be6-3777-85f4-1af67caef848 | -11.35835 | -54.04438 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93a3ee8c-1a36-3482-af4d-e94d2b9f4203 | -11.03472 | -54.1347 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 212b0fec-82a1-33e6-bf22-215822efba20 | -9.95504 | -50.16193 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 805baaff-928f-39ae-b121-e7d561c49573 | -9.08988 | -49.88432 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97a65c39-fe5d-3764-97fe-96ac64aff69d | -14.11918 | -46.28838 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b784bbc-b859-3bed-849e-e04cbfdb1856 | -7.50609 | -55.03484 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1f63aca-0f47-32d6-af24-d6716bb3fb49 | -11.35537 | -54.03968 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd37bb6e-6e4f-39a1-b55a-4868b7a82ea7 | -13.18847 | -48.56388 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4614cfd-3db4-3d2b-a380-b777cdbc7461 | -13.1937 | -48.56456 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7aecadf0-bcfe-3b80-9393-4d578d0fa065 | -9.92988 | -60.71728 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README63.md)
