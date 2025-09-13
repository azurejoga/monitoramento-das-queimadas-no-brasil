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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dcde7a4-b4f9-399c-88f5-54ff70bebf07 | -9.50095 | -50.88781 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ec17dc2-d663-3382-8be3-2de7d936a628 | -12.69737 | -43.46244 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73c8d52c-2c8e-3ae8-b2bf-1bb6820741e8 | -14.43596 | -47.32355 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6679b0bd-42f0-3720-bf93-5c521bb527f2 | -15.32231 | -42.0533 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 45165547-3b04-37c2-adbb-1eabc8521afd | -12.79745 | -47.98816 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebf06b12-3aa0-36a7-b65c-fb549abce72d | -11.70787 | -46.55386 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e5d40ad-c084-3c4a-a9c6-bd7429018e9b | -9.73955 | -46.8902 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78a608f8-7238-3dd0-8539-c6084c296edd | -14.18692 | -46.2737 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| f2a72e74-130c-36a8-9696-2102c003ebcb | -10.74433 | -50.54354 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02a3318a-d204-3373-b1ad-12aa80ff68f9 | -8.50386 | -47.31861 | 2025-09-13 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab1c22d4-ee18-3fd1-b7dc-6b676eb4de33 | -14.25568 | -45.07598 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55735d6c-51d2-38e5-ada8-57ff495baa6e | -14.43541 | -48.44078 | 2025-09-13 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e51bd0ca-2b13-3bef-a4af-a33b6612a8cd | -13.58489 | -44.88654 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fcb3a8ff-ea48-37ec-9393-0c08e52dca70 | -14.2559 | -45.07275 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 283dee96-6d12-3c24-b5e2-8ebdf30ceb40 | -10.59264 | -43.02732 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 712fb71b-5790-340a-b26d-0418c503b9c2 | -10.1302 | -47.19251 | 2025-09-13 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ef08d79-db53-3c05-b904-39d6211547ac | -11.71681 | -46.5691 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 96d86185-900e-396f-86fe-09821feee7b0 | -14.21245 | -46.27455 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6eebda9e-ce17-3ba8-ba11-06b6238b63b8 | -11.56996 | -50.57895 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 40779a9c-fa80-3d23-a7d8-a2d59ad6e239 | -8.09925 | -50.17844 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4908e2f0-6e23-3990-ad95-5556bd94860e | -11.40741 | -50.74864 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 45223fa7-5938-3cb8-8bf6-4f6487465609 | -10.6564 | -46.27352 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1551587a-4038-3639-9cfc-7209a6cb72bf | -12.11365 | -44.85114 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a836519-1266-3072-b655-d1674500b288 | -14.21593 | -46.25411 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c9595f5-d9a9-3582-8abe-d00d676a67e6 | -11.49197 | -43.69079 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5794d4a-6a8d-3fe9-b547-eece3b974ca8 | -9.02953 | -47.0588 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d77e9f8-1cf0-39ab-8187-e579a08f2020 | -10.90293 | -45.58134 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f80506b9-1ed1-3426-884d-f7a5fb22435d | -12.3987 | -43.81874 | 2025-09-13 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17511e96-f714-3608-8c4a-e7098a5e921b | -13.00241 | -46.74007 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3daa3354-2cfe-3eb0-be2e-5781931c8e0d | -11.73067 | -46.60769 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9666223e-eec9-3f5f-b532-9e84cc2dc18b | -11.36243 | -43.5017 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9a1f7f1-20c3-307a-af2b-9d9729ac497f | -12.12939 | -44.83741 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c557de5a-9d3c-3283-8c21-8aa40577ae28 | -9.85518 | -43.13559 | 2025-09-13 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7724dc1-7740-38c6-8b69-9d1fec66e2fa | -14.00055 | -44.77248 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 140d8586-87da-3315-ad54-276a69864ec4 | -8.0997 | -50.17593 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f16e22f4-fa62-34e9-8311-f755d78c79c2 | -12.12252 | -44.83633 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e047cab9-edd1-32a1-b04e-d64db03bf5a5 | -14.21387 | -46.28777 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5cc027c1-175c-3dc5-9014-418f1556ef23 | -12.12125 | -44.84396 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 194b3eaa-3f65-3b19-af36-dea225b24c63 | -9.23974 | -51.22398 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 411416dd-45c8-3593-b1c0-bda4033673e0 | -12.95184 | -47.9857 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46740738-56b0-3998-9651-ebf1ecae3b02 | -12.82818 | -47.95422 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9549e511-5367-3968-bb83-b85bbfb3168d | -11.7344 | -46.60837 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 449d880f-a6b4-3977-8f7d-defbbfbf734b | -12.93794 | -47.99463 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0529c86a-c942-3655-9d36-69b14b9c1184 | -12.9065 | -47.96355 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f19fe206-bedf-3447-a1ab-d567d4e078a5 | -11.77637 | -50.5561 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ae27cc5c-9197-3d1a-b2e6-c5f82e6f4fbe | -11.41999 | -45.6085 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd8202ce-4809-3289-bc99-7f450692f83f | -10.75917 | -50.51777 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea301b34-e5da-39f0-8c41-aa1c28212e6b | -14.19255 | -46.24088 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88333035-eb04-3d2e-9b9a-29d4ccae6a16 | -13.24932 | -43.75041 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85ad1245-37ed-30b5-898e-dbe1bcd6d615 | -10.64801 | -48.97788 | 2025-09-13 04:08:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 102fcc27-19d6-3e03-bd40-e8e3700256e8 | -14.43732 | -47.33773 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bbf278d-4aee-337e-bd0f-48f1e3eb63ac | -12.99395 | -46.75471 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 483ebe2a-51f8-3d84-96c7-d5485110098f | -12.90737 | -47.95871 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 65e939b5-eb30-39fb-94d1-2d3a76e69fdb | -14.20678 | -46.26477 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b504478-7dfb-3680-a743-cb61b29bf27b | -11.73651 | -46.61842 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 3b59e350-90ea-33f8-bfe4-c3623855aa3e | -11.73237 | -46.59788 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9886f6b-509a-3ab8-bbdd-468f2f5dd1cc | -12.85462 | -47.94398 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa397ad2-ad5d-33d5-9ef5-a959db5a6067 | -11.69468 | -46.90474 | 2025-09-13 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d09ca4e-1b4d-3c96-ba6b-5a5573bd7878 | -11.49023 | -43.70153 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e67ee94-82a8-3a10-ae67-3a3e6b25a8a5 | -14.29176 | -46.08574 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5a3dcc6-6a07-35ec-912e-5e8c9c706a54 | -14.44046 | -47.31993 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6c4b4e1-a021-3667-a009-56bfb448ab81 | -12.93043 | -54.74907 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c995a34-efa8-30a7-97e4-308ea0dee568 | -9.25179 | -51.24303 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd587406-3d9e-30d2-86aa-b78cad715efd | -10.78374 | -50.53457 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7efef4b7-e125-376a-905a-da02b3bbea06 | -16.24989 | -39.02475 | 2025-09-13 04:08:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3591857e-3dd7-3e87-a83e-dd2c2acddfcc | -9.52454 | -54.62317 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 575b11a2-81a6-3f44-a3ec-ef00dbdda13c | -12.81486 | -47.93674 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0f58a160-f450-30af-8c77-d8f54dd0f456 | -10.7886 | -44.779 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb46a9d9-070d-352d-98a2-ef9857914c05 | -12.89312 | -47.9466 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e38cc567-0c82-3a90-9a63-a6524acbc193 | -10.77474 | -44.77677 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f8e9d10-9496-3155-a70a-bc7daba4be9b | -10.6436 | -48.97712 | 2025-09-13 04:08:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8505af8b-9b5b-3851-8ec4-b20a5a980c19 | -11.30875 | -50.78731 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07fafe16-7966-39ee-a501-e4eb9e57c1c2 | -11.8656 | -50.58467 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2b4b7b6d-d425-307f-b89c-ccd1b7b276f2 | -8.23996 | -44.36304 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdbe7588-2aa8-3072-a689-553679483927 | -11.47186 | -43.60302 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70a3d40a-a946-355f-9c45-b51571376a28 | -14.2945 | -46.06934 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 639eeec5-514a-31aa-bcab-170f30e9ae64 | -13.15047 | -47.13717 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d416796-6df6-39cc-938e-e308db891346 | -14.21743 | -46.28841 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f20760d9-e7b2-37a7-9847-0b18487bf12e | -11.83495 | -50.56203 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 965dd9a4-06f1-38eb-bfcf-fd579f950338 | -12.09147 | -44.87893 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c3bdf64-ec3d-35c7-ae47-9d427674429e | -14.85439 | -42.27811 | 2025-09-13 04:08:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 07800746-5789-3a0c-ad1a-fc62d08774eb | -12.12724 | -44.82919 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 63f5d8ce-22af-3f6f-b8a4-8bd24428b83b | -11.76501 | -51.51813 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c06bce50-f8d4-31e0-9f84-ae9ab9b44714 | -10.229 | -48.63839 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| babb9697-7ed2-3915-ae81-427b02b4bcb0 | -11.15814 | -45.24213 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6064d051-da16-3ae7-86a3-f93437c80319 | -10.75899 | -50.54638 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b6c48a2-1eee-393c-91a9-c5cbbf74c6ef | -10.78643 | -50.53448 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 25390b7b-a07f-3c25-ace5-07787c130a13 | -10.01354 | -50.39356 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abcf21ab-113f-3ba7-8138-0c2e42a8f2be | -11.49081 | -43.69795 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1e0d458-b218-33dd-aa1f-600953079c44 | -11.78588 | -44.28294 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 95089d4d-c00d-3816-89fd-4b3e4ae6a359 | -9.41396 | -43.41105 | 2025-09-13 04:08:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d961bbb0-5fa6-3559-8493-ae424f128105 | -9.06056 | -45.81681 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c492a050-ee4e-39d9-b3d4-1bd8ddb85e4f | -11.40944 | -50.73748 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3fd103c2-3de1-30ef-b5f7-8461b59ed183 | -14.43293 | -47.3188 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a853bba6-549f-30c3-91b6-bdcdd2276292 | -13.0045 | -46.74988 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5ca4fe2-e961-3380-8aa6-526af069a408 | -10.32919 | -54.3246 | 2025-09-13 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0381af29-5f31-3d0e-b5f7-0263e96b48cc | -9.02814 | -47.04321 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8a8a924c-3cec-3ffa-a6fe-b01aabe2c4f4 | -14.19476 | -46.27079 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5064894a-2f37-3762-99a1-a8a0509c6c07 | -14.42757 | -47.3273 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddfb43c6-1e59-3786-b6bc-3c5d38ea4063 | -14.28608 | -46.07632 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README60.md)
