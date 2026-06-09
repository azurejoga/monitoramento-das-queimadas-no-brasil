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
| 9331e824-b3ce-3a1a-b0a7-ad8d27fffa2d | -12.77216 | -46.81872 | 2026-06-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0712698f-2e2b-31d2-899d-d3a7e5fb4a11 | -10.90196 | -49.35367 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cd75b56-96fc-3fe4-8b9d-b456d39c44b7 | -15.59397 | -41.79437 | 2026-06-09 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f610f7fd-0b77-3672-b248-bf14535bab13 | -10.86083 | -53.73586 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 654a2dd1-694d-3392-9933-afe77708eee5 | -11.26647 | -53.97245 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d430ad73-2024-3571-931c-8b6e0f7df88c | -11.33578 | -51.39117 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e895e60e-4267-3b67-9461-e1da2618018f | -15.59035 | -41.79388 | 2026-06-09 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f8a32641-3442-33fb-80a2-423cb5e7fb66 | -11.95525 | -43.40273 | 2026-06-09 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fa4bc96-da1e-3030-b870-1f9298188fbe | -11.26754 | -53.96694 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46cfa635-836a-3057-ad15-f97615abf884 | -12.10127 | -45.82745 | 2026-06-09 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c16632-1acb-34b4-b555-10bf8861b1df | -11.27418 | -44.52695 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af5a649e-90f1-353e-95b4-97b4425be79d | -12.46916 | -55.13385 | 2026-06-09 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9269b95a-51ad-359d-aedd-f2d71beef440 | -12.05762 | -49.75988 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 69d82887-f2df-33db-a7d0-26cbfe8a0180 | -11.55289 | -52.78466 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a57a013f-7f17-30ff-871a-a620bfd025ed | -9.34026 | -47.91133 | 2026-06-09 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73132b27-4bbd-3097-a6d4-8bfebf5cf70f | -19.91146 | -47.97503 | 2026-06-09 04:17:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67934d6b-ea8b-3ed9-ae85-ab9eeace2150 | -22.80427 | -49.3489 | 2026-06-09 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b67d60fd-d243-3f68-b519-02cf60a58f75 | -9.22466 | -48.56612 | 2026-06-09 04:17:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e05526c5-f869-360b-9eef-7b294743debb | -9.08616 | -50.60448 | 2026-06-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fa6e4fe-3729-32da-b2e0-e8dc6c00b717 | -21.54908 | -47.04144 | 2026-06-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f7aadb9-325d-397f-b81d-00630a0dbb18 | -10.42548 | -49.44672 | 2026-06-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ae906cc6-bc5e-37d5-a29d-1824023f4530 | -20.14487 | -48.9333 | 2026-06-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9a1db4a-3e9c-343e-9815-99d42d614781 | -12.48598 | -46.27212 | 2026-06-09 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78072152-48f4-3e87-b771-38df4bbc7388 | -12.85357 | -44.37009 | 2026-06-09 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1b6a6514-8474-3ea8-9004-5fc0c7bf45f4 | -12.36146 | -47.89173 | 2026-06-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbd30296-bc70-3852-b32a-75a53acc39fa | -15.79718 | -42.0235 | 2026-06-09 04:17:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c4831656-b589-38b5-9c0e-def0966c47b8 | -10.90666 | -49.35072 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf03eb20-ce16-3d55-8922-1d02016f1f41 | -11.26794 | -53.96492 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1fea024-af0d-3ce1-89aa-5fb5b88700f6 | -11.33488 | -51.39607 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eb0b3fc-37b8-38f7-8bf8-e1f2e52f691f | -10.42614 | -49.44293 | 2026-06-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fba6975a-4b68-38d5-8f4d-7215d62cb935 | -11.64683 | -52.86335 | 2026-06-09 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65722ad9-8bd9-3e34-8c40-6e940c72f113 | -10.86089 | -53.74009 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da591412-61a9-3c58-a1c6-0bb2e39828de | -11.57397 | -54.58419 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c7201b8-ce72-3193-a492-b4678a24110b | -17.5329 | -45.31569 | 2026-06-09 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59c93396-47fb-354c-b17f-693d6e90b011 | -10.88082 | -49.54226 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03123a43-6ca6-3d87-981c-25c789e02706 | -11.95892 | -48.52851 | 2026-06-09 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcf2a635-a978-362d-a3b6-b5a9c422793d | -12.46833 | -55.13798 | 2026-06-09 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ce48bb1-d5d8-382f-9753-0c1ff18223b3 | -10.64886 | -49.38907 | 2026-06-09 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59a4ad10-70bd-34ab-bb78-639070b3d92e | -13.03977 | -46.79853 | 2026-06-09 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e32dc746-4811-39c9-bca0-4dbd00458fa3 | -10.64475 | -49.38835 | 2026-06-09 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 490a457e-1108-37b9-a0d1-a1aeb7329cb6 | -9.75138 | -48.22 | 2026-06-09 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 500557d1-f57e-3429-9822-508ec8500661 | -15.63035 | -42.48881 | 2026-06-09 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bd28162-1b4b-3b7a-98eb-f7040c55ca43 | -11.66481 | -47.94505 | 2026-06-09 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36eb172f-65ea-3d41-8c67-5376a01adc1a | -10.64606 | -49.38081 | 2026-06-09 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| b77ee26c-7107-3537-a3d6-55b0dda859e2 | -13.96351 | -46.1855 | 2026-06-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe6439de-1d35-3baa-a54f-1d09eb55eb4a | -10.90586 | -49.3539 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e253f2cc-965d-3dd4-acca-b6cdf7427b1b | -14.40311 | -43.80005 | 2026-06-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f75c222-d5ee-3409-9dd4-c15050642390 | -20.45492 | -42.34107 | 2026-06-09 04:17:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 62ce888f-617b-36d7-8d20-110bb16384ee | -15.17967 | -43.85653 | 2026-06-09 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f51bd266-077c-3624-bbc2-962dcb4d3f80 | -21.54571 | -47.04067 | 2026-06-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a718df45-eaad-3bc7-b963-3ba4921d0987 | -12.05284 | -49.76293 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6059e667-20ce-38ec-8860-58829a0df427 | -11.54783 | -52.7837 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 485a37d4-f360-3f7f-ae6f-369b556e0b9b | -10.4088 | -44.93904 | 2026-06-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ec127a6-c950-3c8e-b240-ae06bc156dfb | -10.89381 | -49.35226 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 675e44d2-3d6d-3621-9727-88cfb104e5ba | -12.43707 | -58.47162 | 2026-06-09 04:17:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2e52b74-1e0b-3c33-aec6-5ff1c4ada0b2 | -21.09606 | -43.82487 | 2026-06-09 04:17:00 | NOAA-21 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7a6f61c5-6309-3073-89cd-e3290656ab1a | -12.04444 | -45.29063 | 2026-06-09 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c88f2b2-7782-3e27-912e-e3ff0fda97f8 | -12.36067 | -47.89511 | 2026-06-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 771a152a-a787-3dc8-a367-5795c03f7d3e | -12.77151 | -46.82263 | 2026-06-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 255b96aa-5651-38a3-8ffb-9bd7b926f092 | -19.03083 | -52.80505 | 2026-06-09 04:17:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 469e8365-3e57-3aa9-a870-82b8880b540c | -15.63093 | -42.48475 | 2026-06-09 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9e5a285-f586-3de5-8bdb-6bb7cbcad7b6 | -9.07619 | -50.60758 | 2026-06-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 317a08d7-eb6a-3259-8534-75cb4d829c40 | -11.54275 | -52.78281 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a797ddee-3dee-3a66-8061-0733419dbc76 | -12.22418 | -43.99506 | 2026-06-09 04:17:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4289a384-7edb-3ccc-94ed-941f735d1799 | -12.04387 | -45.2942 | 2026-06-09 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52462f25-230e-3167-b70e-28207e8220a1 | -11.5484 | -52.78067 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 034f7cf7-d417-3148-aed3-4ae7b813eb86 | -11.57233 | -54.5825 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3801277f-4334-3f49-9d2f-36e61ab1d458 | -9.62335 | -49.0231 | 2026-06-09 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 087d8739-e770-3d17-9f00-f804e0e7c08c | -10.58318 | -49.64463 | 2026-06-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9891aa0c-d3e9-33cd-9d6f-6caae1877d5d | -15.18301 | -43.85706 | 2026-06-09 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d3ee5cac-7272-3ba5-8a15-15487bfb922b | -11.54218 | -52.78586 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1c411597-4703-314b-9e19-a3baa9027ed4 | -9.69587 | -47.69591 | 2026-06-09 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1beb18df-611f-372d-99bd-24d337b3440b | -15.17354 | -43.85181 | 2026-06-09 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f22512c0-733c-3628-8268-c390ce096e18 | -13.96015 | -46.18491 | 2026-06-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7a3c3bf-0898-32ba-83e9-170e20e6eed0 | -10.86017 | -53.7394 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e907c85-a165-3b19-8003-fbcb6152cb72 | -13.25739 | -44.39941 | 2026-06-09 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 676dec46-95e8-3a62-9aad-97d3b40e958d | -13.25409 | -44.39887 | 2026-06-09 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bdde6964-4b7e-3cb3-be9c-d55f087dfaeb | -13.95955 | -46.18858 | 2026-06-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b5331fcd-5142-3e87-8d14-d593505cd2af | -12.36507 | -47.89141 | 2026-06-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 169d465d-d9c0-3ee0-8d42-cebbd45190ea | -10.90603 | -49.35441 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 960d38cc-e391-3ad8-8b09-25acf7aa0f3a | -12.43565 | -58.47821 | 2026-06-09 04:17:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79ca580b-f823-3303-9749-e8e671eac38c | -16.70536 | -48.87838 | 2026-06-09 04:17:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98bbf762-d04c-3703-8d6f-9b7ff102cb80 | -14.36724 | -45.54056 | 2026-06-09 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b5cf739-a80a-3926-acb5-0aed8de21a6c | -22.80082 | -49.34818 | 2026-06-09 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09d509ba-a2d8-325e-b09c-f503c9c9071a | -14.30426 | -49.24489 | 2026-06-09 04:17:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03cd3899-c98e-3322-a921-f2aa56f3764f | -21.43182 | -48.64544 | 2026-06-09 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dc02eba-010e-33d2-966d-dfd973dc558f | -21.20703 | -48.51738 | 2026-06-09 04:17:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94c33ffa-dd26-3611-ae2f-64c8a4b4fc39 | -10.92147 | -54.11257 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9b97b88-5788-33e2-b04d-be03a0ad19f3 | -16.73185 | -43.37095 | 2026-06-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecc75f57-dcdb-34f3-9340-e87917087f84 | -10.17494 | -51.66389 | 2026-06-09 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bffdfae-d5cc-3f9b-8309-3951b535bf60 | -11.554 | -52.80687 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e74930e6-aeba-3806-9c8b-0333c02dfaab | -11.02434 | -44.31778 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 077bbd08-1baf-39d6-a068-2dc59b696e78 | -15.18022 | -43.85289 | 2026-06-09 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3a3315a-2dfb-320e-b85f-fa389d91be66 | -11.26653 | -44.52879 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7da6a10-1182-33a9-ae8d-e0b660c79581 | -10.85952 | -53.74291 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcccd614-118b-3d7c-ba9b-70e22aa2df19 | -11.54727 | -52.78672 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f4749a34-59d7-3691-9033-690dfcac0698 | -12.77564 | -46.81922 | 2026-06-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e009f331-3638-33c7-8a24-1180a5489186 | -11.03094 | -44.31884 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e62daeaa-492e-3b0d-a22f-045da8f9f164 | -11.55795 | -52.78564 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cf15ccfe-78b2-31a0-8a04-95c327a9b9ca | -10.85406 | -53.74189 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
