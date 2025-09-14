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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4a1ab3c-08af-3dc0-8316-4a528f0ff3a4 | -12.78786 | -47.98753 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dc84262-9bff-3ff7-a470-75f10ab8d3d8 | -5.76661 | -52.35814 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0e6d04e-1954-383a-82e7-0861d421e985 | -11.86072 | -50.49 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b7b85ca-c9a4-3d6c-81bf-6f240e1d2a63 | -12.78549 | -47.97873 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14f15b6a-6138-3cb9-b6c4-933f6f696641 | -10.89213 | -48.18601 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34f339b0-9785-3a70-bd53-4d22d82236df | -13.18059 | -47.27927 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 271436bc-da26-3a2a-b4b7-cffc36d767e9 | -13.93922 | -44.84521 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 4612d521-e59f-3080-8442-734f71e94cd3 | -11.45186 | -50.77946 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe5cb1b6-72ca-3ecc-9e20-b4c07f6fe6dd | -11.38031 | -47.71938 | 2025-09-14 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06f07271-431d-3254-b3a1-3ce6666c5583 | -11.48378 | -50.79176 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ebe5321-a041-31c8-8a9a-e6d89cd19d9a | -8.10137 | -50.16498 | 2025-09-14 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eb2ea87-3a4a-3bb9-8246-5bd834f198b4 | -11.23565 | -47.62471 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 94d102c2-1f25-3fdd-8c37-4ff24f37bf8a | -6.11536 | -47.8311 | 2025-09-14 04:40:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a46348b1-d72f-3785-82cd-705354613939 | -10.35359 | -50.49092 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e394bfcd-bd44-318e-a2f5-058ec31f3c09 | -11.84255 | -50.49789 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c2225e3-3b28-3c1c-b7aa-c7edcda0d296 | -10.08871 | -47.18473 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e0ebeae-1926-3ad9-a190-ed88521c97d8 | -9.02484 | -47.06523 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57664c03-8a49-34ad-bb93-c080e9aaf113 | -11.48103 | -50.78773 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d71b3f03-cf1f-3510-92bb-5ca77196b247 | -10.35853 | -50.481 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97984ade-ce3a-3c2c-8455-f2b7e97bbebd | -11.47219 | -50.73611 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 655c638b-f2ab-32c0-9ca3-10d87ec3bf05 | -12.98024 | -48.00515 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad4c9079-958c-3c77-a5f8-e581fbf35f45 | -11.72229 | -46.89897 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db05fb37-a077-3d3e-8e60-8464f74180a7 | -7.27572 | -48.67318 | 2025-09-14 04:40:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 594d9f4b-3fb7-327c-b911-674e1b564ff9 | -10.76545 | -46.47453 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b12d1674-d884-3201-8be3-99c772eb30ec | -12.80169 | -47.13865 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b017c744-0aa0-325e-81da-a5c3508cfac1 | -11.46673 | -50.79261 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4fc5dea-ced7-314c-8689-530a3b99c7b0 | -12.06958 | -45.62983 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7c590c68-8c94-3c7c-9884-8d63b18e3f89 | -11.47773 | -50.7872 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc82cce2-dcd8-3ccc-9122-00cd901c423e | -10.90913 | -47.20342 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20811a4e-c211-3959-863d-8c4607ff54c6 | -10.90335 | -45.46542 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba7b7b31-a862-3ca8-b613-9001bad306b9 | -10.35084 | -50.48692 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d555d2d1-d4cf-3aed-86cb-14a19a30fbbd | -11.48214 | -50.80225 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fef1e0d-e99a-3b61-bedd-b0ec86d05452 | -11.4959 | -50.80088 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81aab9b6-9b58-3321-9c46-d42263d985e3 | -9.73942 | -46.04616 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60c60556-1a87-3a47-bf26-7b5b547cf3c2 | -11.79704 | -44.69176 | 2025-09-14 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11e5d37b-ad5d-360b-a41c-8e03098e4f0a | -11.49754 | -50.79039 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eba921c-7b9a-3240-a1a5-b63a7c401988 | -13.948 | -44.84651 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 7b04e0cd-16a7-32bb-adf5-7b40d2c116d9 | -10.35138 | -50.48343 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0f5ae2f7-ada2-3d91-8369-d0c1c815a4b0 | -10.08808 | -47.18895 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa27516-0112-36e3-a83a-bd4659444bbd | -8.19559 | -46.99091 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd0ac670-305b-3032-b482-6f647f0c053b | -11.49369 | -50.79335 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 916b94e0-5fdd-3622-9fd3-36fd0be16bc4 | -11.49588 | -50.77936 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc6c2217-ac77-3fc2-91cc-afac6f8ac680 | -11.35852 | -47.32618 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b556912c-e437-39ac-bbac-51358cb94e9c | -13.93316 | -44.85761 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85de3896-f1ef-335a-be52-64a205513b7f | -8.93829 | -46.1591 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78977f29-3799-375b-8aa2-b3909102380c | -9.12091 | -46.94989 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b7859ee-5fa6-3005-91c1-04652df87539 | -12.9296 | -47.94937 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca8bcdf0-14e7-325e-93e8-cf0a32aa11c9 | -11.21768 | -47.67217 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79ae4768-e607-31d7-8523-81c4c8e92836 | -12.77906 | -48.02282 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a7bbb152-e50e-303e-9f5d-c6f3a6a9af10 | -13.00578 | -47.98045 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed85d2e9-39fa-3e43-92f5-16a17a45fc57 | -13.02914 | -47.99599 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9668658c-4d81-3663-8522-a27f639e6d3a | -10.90061 | -47.21098 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 208fd3ff-ad22-3f7b-a0f4-0c41976c19e9 | -11.46011 | -50.77003 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b724ed40-4d6b-3cde-8e0e-e397948b8317 | -10.71421 | -48.69727 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0e70dc3-6054-3a4e-bb7b-c4a11ed04452 | -11.45956 | -50.77353 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a60131c-3da6-3616-9555-2d37025f6035 | -8.94881 | -44.44228 | 2025-09-14 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c04a5d2-0cf6-3d8b-bbf0-3a1bf181ebd0 | -11.13487 | -45.32617 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3504d318-b22f-30f4-a1c2-acd7ae60f12d | -11.44526 | -50.77841 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a734385-1019-3970-b29a-6e6250c0f6e6 | -11.38091 | -47.71526 | 2025-09-14 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fea841a7-3cb0-34dd-b5bd-6b7103ad0acc | -11.49205 | -50.80384 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df858030-4549-3cb2-8ef2-8f17a7cc69e8 | -7.47656 | -46.12559 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9d27ac6-6e3c-3dbb-80ac-a95d852a2f29 | -7.03278 | -49.8638 | 2025-09-14 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b9c9f62-691c-3b55-958c-cf99aa39c9cd | -11.50463 | -43.63925 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79f07dd6-86c0-31f3-85df-605992d5bb6e | -12.78735 | -48.041 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45c4a6b3-988e-33e7-89fd-f005ed524f67 | -10.35577 | -50.47699 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5c957f70-0708-368a-be94-d40c9738db0a | -10.07252 | -47.16924 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21f72082-87d4-3838-ba12-b7bcc677f376 | -10.21499 | -48.47313 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b540fd97-26fe-3dd9-ac09-95e89e90e5ab | -7.24518 | -48.33624 | 2025-09-14 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ce69c11-2e37-372b-9254-fc170757474e | -8.35438 | -44.7345 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97757b6a-5e75-353b-8fbe-886f4f8ac5af | -11.46563 | -50.7996 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 511124b8-e58b-39fd-a77d-33b8b2a50a27 | -6.35653 | -46.51295 | 2025-09-14 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 829a46e5-e07a-384c-8af3-23065f6ac8e4 | -12.09159 | -51.38375 | 2025-09-14 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 018fc7b1-4e8f-38d1-9b5d-f9e5dc61b154 | -8.95721 | -44.44351 | 2025-09-14 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c6eec56-4e7d-351a-b7c4-12264c5a6768 | -10.75994 | -44.7707 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05b52cce-4d3b-3636-8625-209e46f80829 | -12.97134 | -48.04145 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f7d654b0-f7c5-392e-9802-14b0ec85c098 | -13.93648 | -44.83168 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| eefda6f8-748f-3a8d-9ad8-3ac12e8d357e | -11.3782 | -43.50356 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7df58195-896e-3d33-ae2a-8e59a21f0e76 | -10.2213 | -48.6158 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab7bc573-976a-38dc-9ab0-1d6ec35d35b4 | -9.73413 | -46.87489 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3a6d42f-85ee-3f16-840b-320ce46de2f9 | -7.70687 | -44.86757 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a65b201-953f-3334-891a-8a32b41860e0 | -10.88981 | -48.17769 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d28b982-5404-3315-8aa8-e0e52b34235e | -13.93593 | -44.83596 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 26605a58-0fd3-3f36-87ba-39e4c8dd8d7a | -12.24517 | -46.78305 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc5896ab-bb23-3f7c-94c8-beb9b8d551cd | -9.02063 | -47.06886 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94811541-a6ba-3132-a192-6a99e7b63cb6 | -13.0065 | -48.00066 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c38a79c-7a5c-3aa7-9d04-80dd40384d97 | -12.92358 | -47.95053 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5a778ce2-f02c-37df-89e9-644c6126aae7 | -11.48983 | -50.77481 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec7cad2e-25d8-3e0e-ad62-b0f321767888 | -8.1985 | -43.76447 | 2025-09-14 04:40:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea236474-c080-3db4-8e35-04d974f12301 | -10.73674 | -46.43232 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a060daaa-1bbe-3746-863c-cbda90d463b3 | -12.16931 | -48.7167 | 2025-09-14 04:40:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fea45b7-577c-307b-83de-bb356566643e | -10.74299 | -46.44273 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a87607e-ac3b-3baa-b9ef-ebfd58ef0095 | -7.37769 | -44.35715 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92a09418-ac55-31fb-b38b-b06d2df6fca8 | -12.8214 | -47.94768 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ed8a96f-78cb-3460-b393-70344a6017fd | -9.09933 | -44.81728 | 2025-09-14 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3add2f9-f418-3103-baba-582da7d93095 | -11.36449 | -47.33625 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9baf1a0d-1ebf-39ec-8002-02ca3a848bb4 | -8.94939 | -44.43814 | 2025-09-14 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20f70d8d-519b-3a55-993e-9250c8766079 | -10.90024 | -48.17933 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4a3d943-2af3-32ae-a975-9c6c6ff9a605 | -8.93637 | -46.72956 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f6b0e4db-cf12-3ec5-aa0d-7213db137a67 | -11.48709 | -50.79229 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e900cfd6-2128-3533-87ff-7a2f0ae2dfb2 | -9.4876 | -46.40527 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README35.md)
