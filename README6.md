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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7089529d-b3ec-3154-9040-ce82f11ab006 | -10.91118 | -56.85356 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03df0b26-35d7-3b85-862f-fcfa0a301ecc | -9.33268 | -58.01468 | 2026-06-30 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95aa28cc-52c1-3587-a19c-7d7d53edfbc2 | -12.45187 | -58.49509 | 2026-06-30 04:21:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b8cdb3da-30aa-3cb5-9916-8cce62172608 | -13.25584 | -56.79711 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 40869dbb-8f02-33f3-b19e-37c225809b7b | -9.60152 | -56.92766 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 46e2d140-2701-35d4-b930-829d99a566b7 | -13.71511 | -47.87074 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e27bcb4-7814-337d-b0ee-d1dad5a4c085 | -10.12816 | -52.40882 | 2026-06-30 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af858cbb-267c-3365-b7d6-983afef4f2c7 | -11.05312 | -55.76117 | 2026-06-30 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9189b9f-36fb-3903-91a3-a30cd1be4d74 | -11.22083 | -53.835 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be7a30ad-c8de-3385-9481-39ab112d0be3 | -11.31588 | -54.46489 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1234d570-a56c-3ac0-b267-c2b6268ccf00 | -15.07557 | -55.8096 | 2026-06-30 04:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e86727d-466e-3d4d-80cc-c9dcc6fccf9e | -12.86134 | -44.34673 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d87c755b-e76a-394b-94a5-2983adfb205f | -10.69552 | -49.60624 | 2026-06-30 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3c590ee6-a6b8-3677-a19b-d8828f9f981b | -11.91464 | -43.39614 | 2026-06-30 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b40851b3-496a-3d90-bd60-0fa880da6d3a | -13.71173 | -47.8702 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fce5a6fc-1361-3d80-a7b7-466432fb31f7 | -12.85796 | -44.34621 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fbf59494-4595-3737-8df6-92a7643dcaf1 | -10.80458 | -48.5704 | 2026-06-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a06df488-de93-3b99-ac92-cd558424a8ae | -10.7771 | -54.11374 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50d83ac5-64f6-3d6e-8616-072d45f08749 | -11.57927 | -47.45249 | 2026-06-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d78abc5c-55f6-3c2f-8eda-811419684f2a | -9.60268 | -56.91771 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d65b615b-1e26-3517-870e-d11a71f309c4 | -8.70528 | -50.71224 | 2026-06-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 430e0497-cc99-329c-9ca7-85721830893c | -11.92216 | -57.38946 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f396568-d58f-38a3-be21-ebafb7e46123 | -12.50703 | -48.27393 | 2026-06-30 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e4c88750-a8f2-3188-b527-8851a3af008f | -12.85653 | -44.34677 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84e3a6bb-a0e8-327f-9d92-812bb4e9766f | -10.53196 | -48.15741 | 2026-06-30 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18c21690-afca-3e8a-9486-397cf5c6a9b6 | -11.92217 | -43.39328 | 2026-06-30 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e1ac673-4442-3579-b77c-e860539c6f91 | -9.60767 | -56.92889 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 79ddf81e-4628-3ab9-a3bf-5a9d9c7ecb2d | -10.13812 | -52.40569 | 2026-06-30 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c1c98d3-0424-3abe-bfc4-c051437c401c | -12.50767 | -48.27006 | 2026-06-30 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ed33b244-ae8c-35ab-a5a3-57502f35696e | -12.22095 | -56.55494 | 2026-06-30 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e5cd21bf-7fad-3eea-b864-2387eedcae7b | -11.9355 | -57.70711 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5e4d24f-cf26-3f5c-8659-48382a29dfec | -12.85029 | -44.39809 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d362c590-1039-34b7-8a3b-c4abb5219bf9 | -11.47265 | -47.41602 | 2026-06-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87d6d0a5-9999-3401-a3e2-8e7a7e46e2cd | -14.19821 | -57.43434 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 55089266-5c5d-3368-9ec6-9f6ada40a1f9 | -11.89872 | -57.38013 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80f21196-1b47-3381-96c4-c65fcb77105a | -9.60076 | -56.9275 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a59e4630-0346-31cb-8c3f-06d15d9956e5 | -11.7971 | -56.99675 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e5238bf9-652a-34c3-a454-24ad41a6930a | -10.14268 | -52.40645 | 2026-06-30 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab31c6de-8e04-3a55-91e7-ed5fa1b2f41d | -11.77287 | -46.40987 | 2026-06-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acb49774-bf5f-3e10-abff-a493156129ad | -11.9212 | -57.39427 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e501cd8b-f9c4-3e87-928f-eb79c991a494 | -11.2303 | -54.31448 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e84ca0de-cdc7-3752-905c-324dc3268c10 | -9.33155 | -58.02044 | 2026-06-30 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a93483fa-19ba-329a-8523-f84c0a2373d7 | -11.87353 | -57.0928 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4427f562-aa7f-3440-adef-a392763b6447 | -10.93446 | -43.04229 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| da299acf-9c9b-387f-9e20-b5bee25498c7 | -11.89865 | -57.37807 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 549b02b2-62ff-3f0c-a423-397f37e51dd1 | -9.75693 | -49.03672 | 2026-06-30 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5f080fd-a7d4-3574-8f09-8f42148ca3cc | -10.93912 | -43.03492 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a6e007ff-20a2-3cce-9bd1-4f5b5f0e3d26 | -11.89533 | -57.13976 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2409525b-c6b9-3848-a152-896d5e8b7995 | -10.58742 | -55.42588 | 2026-06-30 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c54ebfae-2e19-37f5-a910-1e8228604088 | -10.94087 | -43.04729 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| cfe08a1d-eece-3c41-9e98-bae3d47ab4e7 | -16.44775 | -43.14632 | 2026-06-30 04:21:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b30a658c-32ff-3226-9ea8-75a426f1981f | -10.77612 | -54.11331 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c75f1285-6391-350d-a6b2-f9a84d7d53e2 | -10.93795 | -43.04282 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 68133c65-2ade-3c65-8b08-69046851c29f | -13.26076 | -56.80235 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 235942dc-f730-34b1-9bd3-83e3c30690bc | -11.22973 | -54.31752 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e80809a-2b50-3c32-9535-764ccccd18bf | -11.47663 | -47.41286 | 2026-06-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cf501b7-059e-3dd4-b391-1c8b65527501 | -10.45877 | -45.08702 | 2026-06-30 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f737052-9889-3538-85bf-a79dd969173e | -12.20512 | -52.86896 | 2026-06-30 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d6e9541-e415-34e6-bd29-5e38aa343c4e | -11.78117 | -47.57328 | 2026-06-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac75fac8-d469-3da3-9f17-2a3ead91e689 | -13.72329 | -47.87191 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b835102a-7be2-359a-9ab5-c908e16e1df0 | -9.59461 | -56.92628 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 55b88486-99a4-3dd2-9754-60e1d936d6e6 | -14.20306 | -57.44048 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3f55a3b-ef17-3af8-b4c8-10f249257200 | -13.23905 | -51.56062 | 2026-06-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7797517d-558e-3398-8749-1c042082f2ca | -9.74734 | -49.02598 | 2026-06-30 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d65b4a3d-685b-370e-a54d-e869793803f4 | -11.76353 | -47.33929 | 2026-06-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7b9a343-3504-338d-b2f7-9f3f156d9624 | -10.71994 | -51.66191 | 2026-06-30 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 501c4525-8695-3e20-9154-3b34e1956347 | -13.27847 | -49.77076 | 2026-06-30 04:21:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea5886fd-fc84-374d-bd74-8bac05aefd95 | -10.77668 | -54.11032 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59b53cf8-3710-35b9-8c85-62675e4767ae | -9.75323 | -49.0361 | 2026-06-30 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b842f96e-7a1f-3c0e-aa82-ad6757185130 | -11.22523 | -54.31352 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6085002-b7af-35c6-8742-48d80257c290 | -10.29656 | -57.13088 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4221e84-a65f-31e3-8cfd-757b565acb01 | -12.45122 | -44.75557 | 2026-06-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09d4ac8a-d69e-3284-a4bc-ccc6e3d515a3 | -10.77205 | -54.11283 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce5c14d1-650a-3fbd-b41c-9e5557f2f69a | -9.21578 | -47.91885 | 2026-06-30 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 342e2e4d-4ce4-3e71-937e-adc687d9084a | -13.72186 | -47.87187 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7112544-26a3-32ad-b1b0-04a56f9a2c19 | -13.26646 | -56.80369 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 36958d2f-b559-39a4-b4f4-614da944b970 | -11.22917 | -54.32057 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b9c5aaa-517e-3344-a084-733e7aa70d2d | -9.60787 | -56.92386 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6235034-ed4e-3057-a986-ecc2604d24ef | -11.94028 | -57.70575 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7c8c8cc-2899-3181-a678-6972c0eb1332 | -11.93204 | -57.71449 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e669c1fd-dbfe-3351-9a17-23ef2ae6a0de | -13.26158 | -56.79827 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 45b34eed-2cc3-3599-93fd-4d33124ad9ec | -14.19909 | -57.43006 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2398d99c-4e88-3b85-a594-0dbda25d47ff | -11.90132 | -57.141 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 045dcf31-d3bd-3189-b351-93c50b803077 | -12.85741 | -44.34992 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5a8a72d5-ed5c-3c0a-af85-61b28d0d8c5b | -9.60244 | -56.92275 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8897f65d-169f-30fc-bb61-e2a861b3e77c | -14.04737 | -46.3352 | 2026-06-30 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ac189a4-89b0-3bc1-8f11-737419afe911 | -13.24247 | -51.56507 | 2026-06-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77c7c3f5-f51c-3e66-9b6b-15ea8d6ab8d4 | -9.59966 | -49.32365 | 2026-06-30 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4611365-4a2a-3435-9a5b-685074cf226d | -14.95557 | -52.85994 | 2026-06-30 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3039f800-9fdf-3c61-bcc1-b1e3c088d24a | -10.78843 | -54.1034 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0888a7a-fbeb-3150-a77e-f02bad25499f | -10.78376 | -54.10577 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a411ceff-03c2-33ed-961e-ce1cc26c67f7 | -10.93154 | -43.03782 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24a7da75-941b-3397-be43-3f0af0fe4e5c | -10.29753 | -57.12607 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29c50f2e-f6dd-3131-9ed9-69d7c490df99 | -9.75473 | -49.0272 | 2026-06-30 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2681d8ba-0d7e-3676-90d6-caf1cf8e23b7 | -11.89805 | -57.12606 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 943df8f4-15b5-35ff-bc28-f0b642898365 | -9.60173 | -56.9226 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f3b1de37-67b6-3219-b2a1-ec5d66bf20bf | -10.76808 | -54.10597 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0aae76f-c5fd-3104-aa44-8b0d051b620b | -13.26563 | -56.80788 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7b351d3-4bfb-3783-8540-5273fbd37d1d | -13.4419 | -43.85367 | 2026-06-30 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f031e960-b17a-32bb-9c46-3449843c194a | -12.20595 | -52.86431 | 2026-06-30 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README7.md)
